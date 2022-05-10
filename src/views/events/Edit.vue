<template>
  <gov-width-container>
    <ck-loader v-if="loading" />
    <template v-else>
      <vue-headful title="Hounslow Connect - Add Event" />

      <gov-back-link :to="{ name: 'events-index' }"
        >Back to events</gov-back-link
      >
      <gov-main-wrapper>
        <gov-grid-row>
          <gov-grid-column width="one-half">
            <gov-heading size="xl">Events</gov-heading>
            <gov-heading size="m">Edit event</gov-heading>
            <gov-body
              >The events will appear on their own page, and will be featured on
              the home page</gov-body
            >
            <event-form
              :errors="form.$errors"
              :id="event.id"
              :title.sync="form.title"
              :start_date.sync="form.start_date"
              :end_date.sync="form.end_date"
              :start_time.sync="form.start_time"
              :end_time.sync="form.end_time"
              :intro.sync="form.intro"
              :description.sync="form.description"
              :is_free.sync="form.is_free"
              :fees_text.sync="form.fees_text"
              :fees_url.sync="form.fees_url"
              :organiser_name.sync="form.organiser_name"
              :organiser_phone.sync="form.organiser_phone"
              :organiser_email.sync="form.organiser_email"
              :organiser_url.sync="form.organiser_url"
              :booking_title.sync="form.booking_title"
              :booking_summary.sync="form.booking_summary"
              :booking_url.sync="form.booking_url"
              :booking_cta.sync="form.booking_cta"
              :homepage.sync="form.homepage"
              :is_virtual.sync="form.is_virtual"
              :location_id.sync="form.location_id"
              :image_file_id.sync="form.image_file_id"
              @clear="form.$errors.clear($event)"
            />
            <gov-warning-text>
              Please be aware, by submitting these changes, any pending updates
              may be overwritten.
            </gov-warning-text>

            <gov-button v-if="form.$submitting" disabled type="submit"
              >Requesting...</gov-button
            >
            <gov-button v-else @click="onSubmit" type="submit">{{
              updateButtonText
            }}</gov-button>
            <ck-submit-error v-if="form.$errors.any()" />
          </gov-grid-column>
        </gov-grid-row>
      </gov-main-wrapper>
    </template>
  </gov-width-container>
</template>

<script>
import http from "@/http";
import Form from "@/classes/Form";
import EventForm from "@/views/events/forms/EventForm";

export default {
  name: "OrganisationEventEdit",

  components: { EventForm },

  data() {
    return {
      loading: false,
      event: null,
      form: null
    };
  },

  computed: {
    updateButtonText() {
      return this.auth.isGlobalAdmin ? "Update" : "Request update";
    }
  },

  methods: {
    async fetchEvent() {
      this.loading = true;

      const response = await http.get(
        `/organisation-events/${this.$route.params.event}`
      );
      this.event = response.data.data;
      this.form = new Form({
        title: this.event.title,
        start_date: this.event.start_date,
        end_date: this.event.end_date,
        start_time: this.event.start_time,
        end_time: this.event.end_time,
        intro: this.event.intro,
        description: this.event.description,
        is_free: this.event.is_free,
        fees_text: this.event.fees_text || "",
        fees_url: this.event.fees_url || "",
        organiser_name: this.event.organiser_name || "",
        organiser_phone: this.event.organiser_phone || "",
        organiser_email: this.event.organiser_email || "",
        organiser_url: this.event.organiser_url || "",
        booking_title: this.event.booking_title || "",
        booking_summary: this.event.booking_summary || "",
        booking_url: this.event.booking_url || "",
        booking_cta: this.event.booking_cta || "",
        is_virtual: this.event.is_virtual,
        homepage: this.event.homepage || false,
        location_id: this.event.location_id,
        image_file_id: null
      });

      this.loading = false;
    },

    async onSubmit() {
      const response = await this.form.put(
        `/organisation-events/${this.event.id}`,
        (config, data) => {
          // Remove any unchanged values.
          if (data.title === this.event.title) {
            delete data.title;
          }
          if (data.start_date === this.event.start_date) {
            delete data.start_date;
          }
          if (data.end_date === this.event.end_date) {
            delete data.end_date;
          }
          if (data.start_time === this.event.start_time) {
            delete data.start_time;
          }
          if (data.end_time === this.event.end_time) {
            delete data.end_time;
          }
          if (data.intro === this.event.intro) {
            delete data.intro;
          }
          if (data.description === this.event.description) {
            delete data.description;
          }
          if (data.is_free === this.event.is_free) {
            delete data.is_free;
          }
          if (
            data.is_free === true ||
            data.fees_text === this.event.fees_text
          ) {
            delete data.fees_text;
          }
          if (data.is_free === true || data.fees_url === this.event.fees_url) {
            delete data.fees_url;
          }
          if (data.organiser_name === this.event.organiser_name) {
            delete data.organiser_name;
          }
          if (data.organiser_phone === this.event.organiser_phone) {
            delete data.organiser_phone;
          }
          if (data.organiser_email === this.event.organiser_email) {
            delete data.organiser_email;
          }
          if (data.organiser_url === this.event.organiser_url) {
            delete data.organiser_url;
          }
          if (data.booking_title === this.event.booking_title) {
            delete data.booking_title;
          }
          if (data.booking_summary === this.event.booking_summary) {
            delete data.booking_summary;
          }
          if (data.booking_url === this.event.booking_url) {
            delete data.booking_url;
          }
          if (data.booking_cta === this.event.booking_cta) {
            delete data.booking_cta;
          }
          if (data.is_virtual === this.event.is_virtual) {
            delete data.is_virtual;
          }

          if (
            data.is_virtual === true ||
            data.location_id === this.event.location_id
          ) {
            delete data.location_id;
          }

          if (data.homepage === this.event.homepage) {
            delete data.homepage;
          }
          // Remove the logo from the request if null, or delete if false.
          if (data.image_file_id === null) {
            delete data.image_file_id;
          } else if (data.image_file_id === false) {
            data.image_file_id = null;
          }
        }
      );

      const updateRequestId = response.id;
      let next = {
        name: "events-updated",
        params: { event: this.event.id }
      };

      if (this.auth.isGlobalAdmin) {
        try {
          const { data } = await http.get(
            `/update-requests/${updateRequestId}`
          );
          if (data.approved_at) {
            next.name = "events-show";
            next.query = { updated: true };
          }
        } catch (err) {
          console.log(err);
        }
      }
      this.$router.push(next);
    }
  },

  created() {
    this.fetchEvent();
  }
};
</script>

<style lang="scss" scoped></style>
