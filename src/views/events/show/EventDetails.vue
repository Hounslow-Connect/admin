<template>
  <gov-table>
    <template slot="body">
      <gov-table-row>
        <gov-table-header scope="row" top>Title</gov-table-header>
        <gov-table-cell>{{ event.title }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Start</gov-table-header>
        <gov-table-cell
          >{{ event.start_date }} {{ event.start_time }}</gov-table-cell
        >
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>End</gov-table-header>
        <gov-table-cell
          >{{ event.end_date }} {{ event.end_time }}</gov-table-cell
        >
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Summary</gov-table-header>
        <gov-table-cell>{{ event.intro }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Description</gov-table-header>
        <gov-table-cell v-html="toHtml(event.description)" />
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Is this event free?</gov-table-header>
        <gov-table-cell>{{ isFree }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Fees text</gov-table-header>
        <gov-table-cell>{{
          event.is_free ? '-' : event.fees_text
        }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Fees web address</gov-table-header>
        <gov-table-cell>{{
          event.is_free ? '-' : event.fees_url
        }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Organiser name</gov-table-header>
        <gov-table-cell>{{ event.organiser_name || '-' }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Organiser phone</gov-table-header>
        <gov-table-cell>{{ event.organiser_phone || '-' }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Organiser email</gov-table-header>
        <gov-table-cell>{{ event.organiser_email || '-' }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top
          >Organiser web address</gov-table-header
        >
        <gov-table-cell>{{ event.organiser_url || '-' }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Booking title</gov-table-header>
        <gov-table-cell>{{ event.booking_title || '-' }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Booking summary</gov-table-header>
        <gov-table-cell>{{ event.booking_summary || '-' }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Booking url</gov-table-header>
        <gov-table-cell>{{ event.booking_url || '-' }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Booking button text</gov-table-header>
        <gov-table-cell>{{ event.booking_cta || '-' }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header top scope="row">Image</gov-table-header>
        <gov-table-cell>
          <img
            :src="
              apiUrl(
                `/organisation-events/${event.id}/image.png?v=${event.created_at}`
              )
            "
            alt="Event image"
            class="ck-logo"
          />
        </gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top
          >Is this event virtual?</gov-table-header
        >
        <gov-table-cell>{{ isVirtual }}</gov-table-cell>
      </gov-table-row>
      <gov-table-row>
        <gov-table-header scope="row" top>Map</gov-table-header>
        <gov-table-cell v-if="event.is_virtual">-</gov-table-cell>
        <gov-table-cell v-else>
          <gmap-map
            :center="{ lat: event.location.lat, lng: event.location.lon }"
            :zoom="13"
            map-type-id="roadmap"
            style="width: 100%; height: 20rem"
          >
            <GmapMarker
              :position="{ lat: event.location.lat, lng: event.location.lon }"
              :clickable="false"
              :draggable="false"
            />
          </gmap-map>
        </gov-table-cell>
      </gov-table-row>
    </template>
  </gov-table>
</template>

<script>
  export default {
    name: 'OrganisationEventDetails',

    props: {
      event: {
        required: true,
        type: Object,
      },
    },

    computed: {
      isFree() {
        return this.event.is_free ? 'Yes' : 'No';
      },
      isVirtual() {
        return this.event.is_virtual ? 'Yes' : 'No';
      },
    },
  };
</script>

<style lang="scss" scoped></style>
