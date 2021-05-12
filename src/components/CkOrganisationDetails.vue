<template>
  <gov-table>
    <template slot="body">
      <gov-table-row>
        <gov-table-header top scope="row">Organisation name</gov-table-header>
        <gov-table-cell>{{ organisation.name }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header top scope="row">Description</gov-table-header>
        <gov-table-cell v-html="toHtml(organisation.description)" />
      </gov-table-row>
      <gov-table-row>
        <gov-table-header top scope="row">Website Address</gov-table-header>
        <gov-table-cell break>{{ organisation.url }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header top scope="row">Phone number</gov-table-header>
        <gov-table-cell>{{ organisation.phone || "-" }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header top scope="row">Email</gov-table-header>
        <gov-table-cell>{{ organisation.email || "-" }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header top scope="row">Logo</gov-table-header>
        <gov-table-cell>
          <img
            :src="
              apiUrl(
                `/organisations/${organisation.id}/logo.png?v=${organisation.updated_at}`
              )
            "
            alt="Organisation logo"
            class="ck-logo"
          />
        </gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Social links</gov-table-header>
        <gov-table-cell break>
          <gov-list>
            <li
              v-for="(socialMedia, index) in organisation.social_medias"
              :key="index"
            >
              ({{ humanReadableSocialMedia(socialMedia.type) }})
              {{ socialMedia.url }}
            </li>
            <li v-if="organisation.social_medias.length === 0">-</li>
          </gov-list>
        </gov-table-cell>
      </gov-table-row>
    </template>
  </gov-table>
</template>

<script>
export default {
  name: "CkOrganisationDetails",
  props: {
    organisation: {
      type: Object,
      required: true
    }
  },
  methods: {
    humanReadableSocialMedia(type) {
      switch (type) {
        case "twitter":
          return "Twitter";
        case "facebook":
          return "Facebook";
        case "instagram":
          return "Instagram";
        case "youtube":
          return "YouTube";
        case "other":
          return "Other";
      }
    }
  }
};
</script>
