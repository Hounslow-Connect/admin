<template>
  <div>
    <gov-heading size="l">Eligibility</gov-heading>
    <gov-grid-row
      v-for="rootTaxonomy in eligibilityTypes"
      :key="rootTaxonomy.id"
    >
      <gov-grid-column width="two-thirds">
        <gov-heading size="m">{{ rootTaxonomy.name }}</gov-heading>
        <ck-taxonomy-list
          :taxonomies="rootTaxonomy.children"
          :filteredTaxonomyIds="service.eligibility_types.taxonomies"
        />
        <gov-body
          v-if="
            service.eligibility_types.hasOwnProperty('custom') &&
              null !==
                service.eligibility_types.custom[slugify(rootTaxonomy.name)]
          "
          >Custom Value:
          {{
            service.eligibility_types.custom[slugify(rootTaxonomy.name)]
          }}</gov-body
        >
      </gov-grid-column>
    </gov-grid-row>
  </div>
</template>

<script>
import http from "@/http";
import CkTaxonomyList from "@/components/Ck/CkTaxonomyList.vue";

export default {
  name: "EligibilityTab",

  components: {
    CkTaxonomyList
  },

  props: {
    service: {
      type: Object,
      required: true
    }
  },

  data() {
    return {
      loading: false,
      eligibilityTypes: []
    };
  },

  methods: {
    async fetchServiceEligibilites() {
      this.loading = true;
      const { data: eligibilityTypes } = await http.get(
        "/taxonomies/service-eligibilities"
      );
      this.eligibilityTypes = eligibilityTypes.data;
      this.loading = false;
    },
    slugify(name) {
      return name.toLowerCase().replaceAll(" ", "_");
    }
  },

  created() {
    this.fetchServiceEligibilites();
  }
};
</script>
