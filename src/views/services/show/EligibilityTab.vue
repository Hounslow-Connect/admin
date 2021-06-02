<template>
  <div>
    <gov-heading size="l">Eligibility</gov-heading>
    <gov-grid-row
      v-for="rootTaxonomy in eligibilityTypes"
      :key="rootTaxonomy.id"
    >
      <gov-grid-column width="two-thirds">
        <gov-heading size="l"
          >{{ service.type | ucfirst }} locations</gov-heading
        >
        <ck-taxonomy-tree
          :taxonomies="rootTaxonomy.children"
          :filteredTaxonomyIds="service.eligibility_types.taxonomies"
        />
      </gov-grid-column>
    </gov-grid-row>
  </div>
</template>

<script>
  import http from '@/http';

  export default {
    name: 'EligibilityTab',
    props: {
      service: {
        type: Object,
        required: true,
      },
    },

    data() {
      return {
        loading: false,
        eligibilityTypes: [],
      };
    },

    methods: {
      async fetchServiceEligibilites() {
        this.loading = true;
        const { data: eligibilityTypes } = await http.get(
          '/taxonomies/service-eligibilities'
        );
        this.eligibilityTypes = eligibilityTypes.data;
        this.loading = false;
      },
    },
  };
</script>
