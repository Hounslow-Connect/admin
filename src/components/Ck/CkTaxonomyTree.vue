<template>
  <gov-checkboxes :invalid="error">
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
</template>

<script>
import CkTaxonomyCheckboxes from "./CkTaxonomyCheckboxes";
export default {
  components: {
    CkTaxonomyCheckboxes
  },

  props: {
    taxonomies: {
      required: true,
      type: Array
    },
    checked: {
      required: true,
      type: Array
    },
    error: {
      required: true
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
    }
  }
};
</script>

<style lang="scss" scoped></style>
