<template>
  <gov-checkboxes v-if="checkbox" :invalid="error">
    <ck-taxonomy-checkboxes
      :key="taxonomies[0].id"
      :taxonomies="taxonomies"
      :checked="checked"
      :disabled="disabled"
      :filteredTaxonomyIds="filteredTaxonomyIds"
      :taxonomyCollections="taxonomyCollections"
      @update="$emit('update', $event)"
    />
  </gov-checkboxes>
  <ck-taxonomy-list
    v-else
    :key="taxonomies[0].id"
    :taxonomies="taxonomies"
    :checked="checked"
    :filteredTaxonomyIds="filteredTaxonomyIds"
    :taxonomyCollections="taxonomyCollections"
  />
</template>

<script>
  import CkTaxonomyCheckboxes from './CkTaxonomyCheckboxes';
  import CkTaxonomyList from './CkTaxonomyList.vue';
  export default {
    components: {
      CkTaxonomyCheckboxes,
      CkTaxonomyList,
    },

    props: {
      taxonomies: {
        required: true,
        type: Array,
      },
      checked: {
        type: Array,
        default() {
          return [];
        },
      },
      errors: {
        type: Array,
        default() {
          return [];
        },
      },
      filteredTaxonomyIds: {
        type: [Array, Boolean],
        default() {
          return [];
        },
      },
      taxonomyCollections: {
        type: Object,
        default() {
          return {};
        },
      },
      disabled: {
        type: Boolean,
        default: false,
      },
      checkbox: {
        type: Boolean,
        default: true,
      },
    },
  };
</script>

<style lang="scss" scoped></style>
