<template>
  <div>
    <gov-grid-row>
      <gov-grid-column width="two-thirds">
        <gov-heading size="l">Taxonomy: Service Eligibilities</gov-heading>

        <gov-body>
          Taxonomies are the 'tags' that we assign to services, in order for
          them to appear within search results and categories. They are pulled
          from the
          <gov-link href="https://about.auntbertha.com/openeligibility"
            >Aunt Bertha Open Eligibility Standard</gov-link
          >.
        </gov-body>

        <gov-body>
          From this page, you can edit the taxonomies available to be applied to
          a service, as well as add new ones.
        </gov-body>
      </gov-grid-column>

      <gov-grid-column v-if="auth.isSuperAdmin" width="one-third">
        <gov-button
          :to="{ name: 'taxonomies-service-eligibilities-create' }"
          success
          expand
          >Add a new service eligibility</gov-button
        >
      </gov-grid-column>
    </gov-grid-row>

    <gov-section-break size="l" />

    <gov-grid-row
      v-for="rootTaxonomy in serviceEligibilities"
      :key="rootTaxonomy.id"
    >
      <gov-grid-column width="two-thirds">
        <gov-heading size="m">{{ rootTaxonomy.name }}</gov-heading>
        <ck-taxonomy-list
          :taxonomies="rootTaxonomy.children"
          :filteredTaxonomyIds="true"
          edit="taxonomies-service-eligibilities-edit"
          :bullet="true"
          @move-up="onMoveUp"
          @move-down="onMoveDown"
        />
      </gov-grid-column>
    </gov-grid-row>
  </div>
</template>

<script>
import http from "@/http";
import CkTaxonomyList from "@/components/Ck/CkTaxonomyList";

export default {
  name: "ListTaxonomyServiceEligibilitied",

  components: {
    CkTaxonomyList
  },

  data() {
    return {
      loading: false,
      serviceEligibilities: []
    };
  },

  methods: {
    async fetchServiceEligibilities() {
      this.loading = true;

      const { data } = await http.get("/taxonomies/service-eligibilities");
      this.serviceEligibilities = data.data;

      this.loading = false;
    },
    async onMoveUp(taxonomy) {
      taxonomy.order--;
      await http.put(`/taxonomies/service-eligibilities/${taxonomy.id}`, {
        ...taxonomy
      });
      this.fetchServiceEligibilities();
    },
    async onMoveDown(taxonomy) {
      taxonomy.order++;
      await http.put(`/taxonomies/service-eligibilities/${taxonomy.id}`, {
        ...taxonomy
      });
      this.fetchServiceEligibilities();
    }
  },
  created() {
    this.fetchServiceEligibilities();
  }
};
</script>

<style lang="scss" scoped></style>
