<template>
  <gov-form-group>
    <slot />
    <ck-taxonomy-tree
      :taxonomies="serviceEligibilities"
      :checked="value"
      :error="errors"
      :filteredTaxonomyIds="true"
      @update="onUpdate"
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
      serviceEligibilities: {
        required: true,
        type: Array,
      },
      value: {
        required: true,
        type: Array,
      },
      errors: {
        required: true,
      },
    },

    data() {
      return {
        enabledserviceEligibilities: [],
      };
    },

    methods: {
      onUpdate({ taxonomy, enabled }) {
        if (enabled) {
          this.onChecked(taxonomy);
        } else {
          this.onUnchecked(taxonomy);
        }

        this.$emit('input', this.enabledserviceEligibilities);
        this.$emit('clear');
      },
      onChecked(taxonomy) {
        if (!this.enabledserviceEligibilities.includes(taxonomy.id)) {
          this.enabledserviceEligibilities.push(taxonomy.id);
        }
      },
      onUnchecked(taxonomy) {
        if (this.enabledserviceEligibilities.includes(taxonomy.id)) {
          const index = this.enabledserviceEligibilities.indexOf(taxonomy.id);
          this.enabledserviceEligibilities.splice(index, 1);
        }
      },
    },
    created() {
      this.enabledserviceEligibilities = this.value;
    },
  };
</script>

<style lang="scss" scoped></style>
