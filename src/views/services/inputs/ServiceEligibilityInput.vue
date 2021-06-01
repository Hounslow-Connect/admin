<template>
  <gov-form-group>
    <slot />
    <ck-taxonomy-tree
      :taxonomies="eligibilityTaxonomy.children"
      :checked="serviceEligibilityTypes.taxonomies"
      :error="errors"
      :filteredTaxonomyIds="true"
      @update="onUpdateTaxonomies"
    />
    <ck-text-input
      :value="serviceEligibilityTypes.custom[customEligibilitySlug] || ''"
      @input="onUpdateCustom"
      id="custom"
      label="Custom value"
      :hint="
        `If the service eligibility does not fit into the ${eligibilityTaxonomy.name} taxonomies, enter a custom value here`
      "
      :error="errors.get('custom')"
    />
  </gov-form-group>
</template>

<script>
  import CkTaxonomyTree from '@/components/Ck/CkTaxonomyTree';

  export default {
    components: {
      CkTaxonomyTree,
    },

    props: {
      eligibilityTaxonomy: {
        required: true,
        type: Object,
      },
      serviceEligibilityTypes: {
        required: true,
        type: Object,
      },
      customEligibility: {
        type: String,
        default: '',
      },
      errors: {
        required: true,
      },
    },

    computed: {
      customEligibilitySlug() {
        // @todo This should not be guessed, it should be supplied by the API
        return this.eligibilityTaxonomy.name.toLowerCase().replaceAll(' ', '_');
      },
    },

    methods: {
      onUpdateTaxonomies({ taxonomy, enabled }) {
        let updatedServiceEligibilityTaxonomies;
        if (enabled) {
          updatedServiceEligibilityTaxonomies = this.onChecked(taxonomy);
        } else {
          updatedServiceEligibilityTaxonomies = this.onUnchecked(taxonomy);
        }

        this.$emit('update:taxonomies', updatedServiceEligibilityTaxonomies);
        this.$emit('clear');
      },
      onChecked(taxonomy) {
        const serviceEligibilityTaxonomies = this.serviceEligibilityTypes.taxonomies.slice();
        if (!serviceEligibilityTaxonomies.includes(taxonomy.id)) {
          serviceEligibilityTaxonomies.push(taxonomy.id);
        }
        return serviceEligibilityTaxonomies;
      },
      onUnchecked(taxonomy) {
        const serviceEligibilityTaxonomies = this.serviceEligibilityTypes.taxonomies.slice();
        if (serviceEligibilityTaxonomies.includes(taxonomy.id)) {
          const index = serviceEligibilityTaxonomies.indexOf(taxonomy.id);
          serviceEligibilityTaxonomies.splice(index, 1);
        }
        return serviceEligibilityTaxonomies;
      },
      onUpdateCustom(customEligibity) {
        this.$emit('update:custom', {
          customTaxonomy: this.customEligibilitySlug,
          customValue: customEligibity,
        });
        this.$emit('clear');
      },
    },
    created() {
      this.serviceEligibilityTaxonomies = this.serviceEligibilityTypes.taxonomies.slice();
    },
  };
</script>

<style lang="scss" scoped></style>
