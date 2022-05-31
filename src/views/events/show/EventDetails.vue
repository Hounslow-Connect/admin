<template>
  <div>
    <gov-heading size="l">Details</gov-heading>
    <gov-table>
      <template slot="body">
        <gov-table-row>
          <gov-table-header scope="row" top>Organisation</gov-table-header>
          <gov-table-cell>{{ event.organisation.name }}</gov-table-cell>
        </gov-table-row>
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
          <gov-table-header scope="row" top
            >Is this event free?</gov-table-header
          >
          <gov-table-cell>{{ isFree }}</gov-table-cell>
        </gov-table-row>
        <gov-table-row>
          <gov-table-header scope="row" top>Fees text</gov-table-header>
          <gov-table-cell>{{
            event.is_free ? "-" : event.fees_text
          }}</gov-table-cell>
        </gov-table-row>
        <gov-table-row>
          <gov-table-header scope="row" top>Fees web address</gov-table-header>
          <gov-table-cell>{{
            event.is_free ? "-" : event.fees_url
          }}</gov-table-cell>
        </gov-table-row>
        <gov-table-row>
          <gov-table-header scope="row" top>Organiser name</gov-table-header>
          <gov-table-cell>{{ event.organiser_name || "-" }}</gov-table-cell>
        </gov-table-row>
        <gov-table-row>
          <gov-table-header scope="row" top>Organiser phone</gov-table-header>
          <gov-table-cell>{{ event.organiser_phone || "-" }}</gov-table-cell>
        </gov-table-row>
        <gov-table-row>
          <gov-table-header scope="row" top>Organiser email</gov-table-header>
          <gov-table-cell>{{ event.organiser_email || "-" }}</gov-table-cell>
        </gov-table-row>
        <gov-table-row>
          <gov-table-header scope="row" top
            >Organiser web address</gov-table-header
          >
          <gov-table-cell>{{ event.organiser_url || "-" }}</gov-table-cell>
        </gov-table-row>
        <gov-table-row>
          <gov-table-header scope="row" top>Booking title</gov-table-header>
          <gov-table-cell>{{ event.booking_title || "-" }}</gov-table-cell>
        </gov-table-row>
        <gov-table-row>
          <gov-table-header scope="row" top>Booking summary</gov-table-header>
          <gov-table-cell>{{ event.booking_summary || "-" }}</gov-table-cell>
        </gov-table-row>
        <gov-table-row>
          <gov-table-header scope="row" top>Booking url</gov-table-header>
          <gov-table-cell>{{ event.booking_url || "-" }}</gov-table-cell>
        </gov-table-row>
        <gov-table-row>
          <gov-table-header scope="row" top
            >Booking button text</gov-table-header
          >
          <gov-table-cell>{{ event.booking_cta || "-" }}</gov-table-cell>
        </gov-table-row>
        <gov-table-row>
          <gov-table-header scope="row" top>Show on home page</gov-table-header>
          <gov-table-cell>{{ onHomepage }}</gov-table-cell>
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
          <gov-table-header scope="row" top>Location</gov-table-header>
          <gov-table-cell v-if="event.is_virtual">-</gov-table-cell>
          <gov-table-cell v-else>
            <gov-table>
              <template slot="body">
                <gov-table-row>
                  <gov-table-header scope="row" top
                    >Address line 1</gov-table-header
                  >
                  <gov-table-cell>{{
                    event.location.address_line_1
                  }}</gov-table-cell>
                </gov-table-row>
                <gov-table-row>
                  <gov-table-header scope="row" top
                    >Address line 2</gov-table-header
                  >
                  <gov-table-cell>{{
                    event.location.address_line_2 || "-"
                  }}</gov-table-cell>
                </gov-table-row>
                <gov-table-row>
                  <gov-table-header scope="row" top
                    >Address line 3</gov-table-header
                  >
                  <gov-table-cell>{{
                    event.location.address_line_3 || "-"
                  }}</gov-table-cell>
                </gov-table-row>
                <gov-table-row>
                  <gov-table-header scope="row" top>City</gov-table-header>
                  <gov-table-cell>{{ event.location.city }}</gov-table-cell>
                </gov-table-row>
                <gov-table-row>
                  <gov-table-header scope="row" top>County</gov-table-header>
                  <gov-table-cell>{{ event.location.county }}</gov-table-cell>
                </gov-table-row>
                <gov-table-row>
                  <gov-table-header scope="row" top>Postcode</gov-table-header>
                  <gov-table-cell>{{ event.location.postcode }}</gov-table-cell>
                </gov-table-row>
                <gov-table-row>
                  <gov-table-header scope="row" top>Country</gov-table-header>
                  <gov-table-cell>{{ event.location.country }}</gov-table-cell>
                </gov-table-row>
                <gov-table-row>
                  <gov-table-header scope="row" top
                    >Accessibility</gov-table-header
                  >
                  <gov-table-cell>
                    <gov-list>
                      <li>
                        Wheelchair access:
                        {{
                          event.location.has_wheelchair_access ? "Yes" : "No"
                        }}
                      </li>
                      <li>
                        Induction loop system:
                        {{ event.location.has_induction_loop ? "Yes" : "No" }}
                      </li>
                    </gov-list>
                  </gov-table-cell>
                </gov-table-row>
                <gov-table-row>
                  <gov-table-header top scope="row">Image</gov-table-header>
                  <gov-table-cell>
                    <img
                      :src="
                        apiUrl(
                          `/locations/${event.location.id}/image.png?v=${event.location.created_at}`
                        )
                      "
                      alt="Location image"
                      class="ck-logo"
                    />
                  </gov-table-cell>
                </gov-table-row>
              </template>
            </gov-table>
          </gov-table-cell>
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
  </div>
</template>

<script>
export default {
  name: "OrganisationEventDetails",

  props: {
    event: {
      required: true,
      type: Object
    }
  },

  computed: {
    isFree() {
      return this.event.is_free ? "Yes" : "No";
    },
    isVirtual() {
      return this.event.is_virtual ? "Yes" : "No";
    },
    onHomepage() {
      return this.event.homepage ? "Yes" : "No";
    }
  }
};
</script>

<style lang="scss" scoped></style>
