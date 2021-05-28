<template>
  <div>
    <gov-heading size="l">Who is eligible for your {{ type }}?</gov-heading>
    <gov-grid-row>
      <gov-grid-column width="one-half">
        <gov-body>
          Use this section to help indicate who should be using your {{ type }}.
          If any of these criteria do not apply, please leave them blank.
        </gov-body>
        <gov-section-break size="l" />

        <service-eligibility-input
          v-for="parent in serviceEligibilities"
          :key="parent.id"
          :serviceEligibilities="parent.children"
          :value="eligibility_types"
          :errors="errors"
        >
          <gov-heading size="m" tag="h3">{{ parent.name }}</gov-heading>
        </service-eligibility-input>

        <gov-error-message
          v-if="errors.has('eligibility_types')"
          v-text="errors.get('eligibility_types')"
          for="eligibility_types"
        />
      </gov-grid-column>
    </gov-grid-row>
  </div>
</template>

<script>
  import http from '@/http';
  import ServiceEligibilityInput from '../inputs/ServiceEligibilityInput';

  export default {
    name: 'EligibilityTab',
    components: { ServiceEligibilityInput },

    props: {
      eligibility_types: {
        required: true,
        type: Array,
      },
      type: {
        required: true,
        type: String,
      },
      errors: {
        required: true,
      },
    },

    data() {
      return {
        loading: false,
        serviceEligibilities: [],
      };
    },

    methods: {
      async fetchServiceEligibilites() {
        this.loading = true;
        const { data: serviceEligibilities } = await http.get(
          '/taxonomies/service-eligibilities'
        );
        this.serviceEligibilities = serviceEligibilities.data;
        this.loading = false;
      },
    },

    created() {
      this.fetchServiceEligibilites();
    },
  };
</script>
