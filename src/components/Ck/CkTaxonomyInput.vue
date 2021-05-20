<template>
  <ck-loader v-if="loading" />
  <div v-else>
    <gov-form-group>
      <gov-label for="filter[name]">Search by taxonomy name</gov-label>
      <gov-input
        v-model="filters.name"
        id="filter[name]"
        name="filter[name]"
        type="search"
      />
    </gov-form-group>

    <!-- Level: 1 -->
    <gov-form-group v-if="filteredTaxonomyIds.length">
      <gov-checkboxes :invalid="error">
        <gov-checkbox
          v-for="taxonomy in taxonomies"
          v-if="filteredTaxonomyIds.includes(taxonomy.id)"
          :key="taxonomy.id"
          :value="value.includes(taxonomy.id)"
          @input="onInput({ taxonomy, enabled: $event })"
          :id="taxonomy.id"
          :name="taxonomy.id"
          :label="taxonomy.name"
          :disabled="disabled"
        >
          <!-- Level: 2 -->
          <gov-checkbox
            class="govuk-checkboxes__item--nested"
            v-for="taxonomy in taxonomy.children"
            v-if="filteredTaxonomyIds.includes(taxonomy.id)"
            :key="taxonomy.id"
            :value="value.includes(taxonomy.id)"
            @input="onInput({ taxonomy, enabled: $event })"
            :id="taxonomy.id"
            :name="taxonomy.id"
            :label="taxonomy.name"
            :disabled="disabled"
          >
            <!-- Level: 3 -->
            <gov-checkbox
              class="govuk-checkboxes__item--nested"
              v-for="taxonomy in taxonomy.children"
              v-if="filteredTaxonomyIds.includes(taxonomy.id)"
              :key="taxonomy.id"
              :value="value.includes(taxonomy.id)"
              @input="onInput({ taxonomy, enabled: $event })"
              :id="taxonomy.id"
              :name="taxonomy.id"
              :label="taxonomy.name"
              :disabled="disabled"
            >
              <!-- Level: 4 -->
              <gov-checkbox
                class="govuk-checkboxes__item--nested"
                v-for="taxonomy in taxonomy.children"
                v-if="filteredTaxonomyIds.includes(taxonomy.id)"
                :key="taxonomy.id"
                :value="value.includes(taxonomy.id)"
                @input="onInput({ taxonomy, enabled: $event })"
                :id="taxonomy.id"
                :name="taxonomy.id"
                :label="taxonomy.name"
                :disabled="disabled"
              >
                <!-- Level: 5 -->
                <gov-checkbox
                  class="govuk-checkboxes__item--nested"
                  v-for="taxonomy in taxonomy.children"
                  v-if="filteredTaxonomyIds.includes(taxonomy.id)"
                  :key="taxonomy.id"
                  :value="value.includes(taxonomy.id)"
                  @input="onInput({ taxonomy, enabled: $event })"
                  :id="taxonomy.id"
                  :name="taxonomy.id"
                  :label="taxonomy.name"
                  :disabled="disabled"
                >
                  <!-- Level: 6 -->
                  <gov-checkbox
                    class="govuk-checkboxes__item--nested"
                    v-for="taxonomy in taxonomy.children"
                    v-if="filteredTaxonomyIds.includes(taxonomy.id)"
                    :key="taxonomy.id"
                    :value="value.includes(taxonomy.id)"
                    @input="onInput({ taxonomy, enabled: $event })"
                    :id="taxonomy.id"
                    :name="taxonomy.id"
                    :label="taxonomy.name"
                    :disabled="disabled"
                  />
                  <!-- /Level: 6 -->
                </gov-checkbox>
                <!-- /Level: 5 -->
              </gov-checkbox>
              <!-- /Level: 4 -->
            </gov-checkbox>
            <!-- /Level: 3 -->
          </gov-checkbox>
          <!-- /Level: 2 -->
        </gov-checkbox>
      </gov-checkboxes>

      <gov-error-message
        v-if="error"
        v-text="error"
        for="category_taxonomies"
      />
    </gov-form-group>
    <!-- /Level: 1 -->
    <gov-inset-text v-else>
      No matching taxonomies found
    </gov-inset-text>
  </div>
</template>

<script>
import http from "@/http";

export default {
  name: "TaxonomyInput",
  props: {
    value: {
      required: true,
      type: Array
    },
    error: {
      required: true
    },
    root: {
      required: true,
      type: String,
      validator: function(value) {
        return ["categories", "organisations"].indexOf(value) !== -1;
      }
    },
    disabled: {
      required: false,
      type: Boolean,
      default: false
    },
    hierarchy: {
      required: false,
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      taxonomies: [],
      flattenedTaxonomies: [],
      loading: false,
      enabledTaxonomies: [],
      filters: {
        name: ""
      }
    };
  },
  computed: {
    filteredTaxonomyIds() {
      if (this.filters.name.length > 2) {
        const filteredTaxonomyIds = this.flattenedTaxonomies.reduce(
          (filteredTaxonomies, taxonomy) => {
            if (
              taxonomy.name
                .toLowerCase()
                .includes(this.filters.name.toLowerCase())
            ) {
              filteredTaxonomies = filteredTaxonomies.concat(
                this.getTaxonomyAndAncestorsIds(taxonomy)
              );
            }
            return filteredTaxonomies;
          },
          []
        );
        return [...new Set(filteredTaxonomyIds)];
      } else {
        return this.flattenedTaxonomies.map(taxonomy => taxonomy.id);
      }
    }
  },
  methods: {
    async fetchTaxonomies() {
      this.loading = true;
      const { data } = await http.get(`/taxonomies/${this.root}`);
      this.taxonomies = data.data;
      this.setFlattenedTaxonomies();
      this.loading = false;
    },
    setFlattenedTaxonomies(taxonomies = null) {
      if (taxonomies === null) {
        this.flattenedTaxonomies = [];
        taxonomies = this.taxonomies;
      }

      taxonomies.forEach(taxonomy => {
        this.flattenedTaxonomies.push(taxonomy);

        if (taxonomy.children.length > 0) {
          this.setFlattenedTaxonomies(taxonomy.children);
        }
      });
    },
    onInput({ taxonomy, enabled }) {
      if (enabled) {
        this.onChecked(taxonomy);
      } else {
        this.onUnchecked(taxonomy);
      }

      this.$emit("input", this.enabledTaxonomies);
      this.$emit("clear");
    },
    onChecked(taxonomy) {
      if (!this.enabledTaxonomies.includes(taxonomy.id)) {
        this.enabledTaxonomies.push(taxonomy.id);

        if (this.hierarchy) {
          if (taxonomy.parent_id !== null) {
            const parent = this.flattenedTaxonomies.find(flattenedTaxonomy => {
              return flattenedTaxonomy.id === taxonomy.parent_id;
            });
            this.onInput({ taxonomy: parent, enabled: true });
          }
        }
      }
    },
    onUnchecked(taxonomy) {
      if (this.enabledTaxonomies.includes(taxonomy.id)) {
        const index = this.enabledTaxonomies.indexOf(taxonomy.id);
        this.enabledTaxonomies.splice(index, 1);

        if (this.hierarchy) {
          if (taxonomy.children.length > 0) {
            taxonomy.children.forEach(taxonomy =>
              this.onInput({ taxonomy, enabled: false })
            );
          }
        }
      }
    },
    getTaxonomyAndAncestorsIds(taxonomy) {
      let ids = [taxonomy.id];
      if (taxonomy.parent_id) {
        const parent = this.flattenedTaxonomies.find(
          tax => tax.id === taxonomy.parent_id
        );
        ids = ids.concat(this.getTaxonomyAndAncestorsIds(parent));
      }
      return ids;
    },
    filteredTaxonomies(taxonomies) {
      return taxonomies.filter(taxonomy =>
        this.filteredTaxonomyIds.includes(taxonomy.id)
      );
    }
  },
  created() {
    this.fetchTaxonomies();
    this.enabledTaxonomies = this.value;
  }
};
</script>
