<template>
  <gov-list>
    <li
      v-for="taxonomy in taxonomies"
      v-if="showListItem(taxonomy)"
      :key="taxonomy.id"
    >
      {{ taxonomy.name }}
      <gov-hint :for="taxonomy.id" v-if="taxonomyCollections[taxonomy.id]"
        >Found in {{ taxonomyCollections[taxonomy.id].join(", ") }}</gov-hint
      >
      <ck-taxonomy-list
        v-if="taxonomy.children.length"
        :key="taxonomy.children[0].id"
        :taxonomies="taxonomy.children"
        :filteredTaxonomyIds="filteredTaxonomyIds"
        :taxonomyCollections="taxonomyCollections"
        :checkbox="false"
      />
    </li>
  </gov-list>
</template>

<script>
export default {
  name: "CkTaxonomyList",
  props: {
    taxonomies: {
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
    }
  },

  methods: {
    showListItem(taxonomy) {
      return Array.isArray(this.filteredTaxonomyIds)
        ? this.filteredTaxonomyIds.includes(taxonomy.id)
        : this.filteredTaxonomyIds;
    }
  }
};
</script>

<style lang="scss" scoped></style>
