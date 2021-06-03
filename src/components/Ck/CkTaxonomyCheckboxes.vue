<template>
  <div>
    <gov-checkbox
      v-for="taxonomy in taxonomies"
      v-if="showCheckBox(taxonomy)"
      :class="{ 'govuk-checkboxes__item--nested': nested }"
      :key="taxonomy.id"
      :value="checked.includes(taxonomy.id)"
      @input="onTaxonomyUpdate({ taxonomy, enabled: $event })"
      :id="taxonomy.id"
      :name="taxonomy.id"
      :label="taxonomy.name"
      :disabled="disabled"
    >
      <gov-hint :for="taxonomy.id" v-if="taxonomyCollections[taxonomy.id]"
        >Found in {{ taxonomyCollections[taxonomy.id].join(", ") }}</gov-hint
      >

      <ck-taxonomy-checkboxes
        v-if="taxonomy.children.length"
        :key="taxonomy.children[0].id"
        :taxonomies="taxonomy.children"
        :checked="checked"
        :filteredTaxonomyIds="filteredTaxonomyIds"
        :taxonomyCollections="taxonomyCollections"
        :disabled="disabled"
        :nested="true"
        @update="onChildUpdate"
      />
    </gov-checkbox>
  </div>
</template>

<script>
export default {
  name: "CkTaxonomyCheckboxes",
  props: {
    taxonomies: {
      required: true,
      type: Array
    },
    checked: {
      required: true,
      type: Array
    },
    filteredTaxonomyIds: {
      type: [Array, Boolean],
      default() {
        return [];
      }
    },
    taxonomyCollections: {
      type: Object,
      default() {
        return {};
      }
    },
    disabled: {
      type: Boolean,
      default: false
    },
    nested: {
      type: Boolean,
      default: false
    }
  },

  methods: {
    showCheckBox(taxonomy) {
      return Array.isArray(this.filteredTaxonomyIds)
        ? this.filteredTaxonomyIds.includes(taxonomy.id)
        : this.filteredTaxonomyIds;
    },
    onTaxonomyUpdate({ taxonomy, enabled }) {
      this.$emit("update", { taxonomy, enabled });
    },
    onChildUpdate({ taxonomy, enabled }) {
      this.onTaxonomyUpdate({ taxonomy, enabled });
      if (taxonomy.parent_id) {
        const parent = this.taxonomies.find(
          tax => tax.id === taxonomy.parent_id
        );
        if (parent) {
          this.onTaxonomyUpdate({ taxonomy: parent, enabled });
        }
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>
