<template>
  <gov-width-container>
    <vue-headful title="Hounslow Connect - Add Event" />

    <gov-back-link :to="{ name: 'events-index' }">Back to events</gov-back-link>
    <gov-main-wrapper>
      <gov-grid-row>
        <gov-grid-column width="one-half">
          <gov-heading size="xl">Events</gov-heading>
          <gov-heading size="m">Add event</gov-heading>
          <gov-body
            >The events will appear on their own page, and will be featured on
            the home page</gov-body
          >
          <event-form
            :errors="form.$errors"
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
            :is_virtual.sync="form.is_virtual"
            :organisations="organisations"
            @update:organisation_id="form.organisation_id = $event"
            @update:location_id="form.location_id = $event"
            @update:image_file_id="form.image_file_id = $event"
            @clear="form.$errors.clear($event)"
          />
          <gov-button v-if="form.$submitting" disabled type="submit"
            >Creating...</gov-button
          >
          <gov-button v-else @click="onSubmit" type="submit">Create</gov-button>
          <ck-submit-error v-if="form.$errors.any()" />
        </gov-grid-column>
      </gov-grid-row>
    </gov-main-wrapper>
  </gov-width-container>
</template>

<script>
import Form from "@/classes/Form";
import EventForm from "@/views/events/forms/EventForm";

export default {
  name: "OrganisationEventCreate",

  components: { EventForm },

  data() {
    return {
      form: new Form({
        title: "",
        start_date: "",
        end_date: "",
        start_time: "",
        end_time: "",
        intro: "",
        description: "",
        is_free: true,
        fees_text: "",
        fees_url: "",
        organiser_name: "",
        organiser_phone: "",
        organiser_email: "",
        organiser_url: "",
        booking_title: "",
        booking_summary: "",
        booking_url: "",
        booking_cta: "",
        is_virtual: true,
        location_id: null,
        organisation_id: null,
        image_file_id: null
      }),

      organisations: [{ text: "Please select", value: null, disabled: true }],
      loading: false
    };
  },
  methods: {
    async fetchOrganisations() {
      this.loading = true;
      let fetchedOrganisations = await this.fetchAll("/organisations", {
        "filter[has_permission]": true
      });
      fetchedOrganisations = fetchedOrganisations.map(organisation => {
        return { text: organisation.name, value: organisation.id };
      });
      this.organisations = [...this.organisations, ...fetchedOrganisations];
      this.loading = false;
    },
    async onSubmit() {
      const { data } = await this.form.post("/organisation-events");

      this.$router.push({
        name: "events-show",
        params: { event: data.id }
      });
    }
  },

  created() {
    this.fetchOrganisations();
  }
};
</script>

<style lang="scss" scoped></style>
