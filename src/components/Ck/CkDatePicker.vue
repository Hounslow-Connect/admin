<template>
  <gov-form-group :invalid="error !== null">
    <gov-label :for="id" v-text="label" />
    <duet-date-picker
      :identifier="id"
      :localization.prop="localisation_uk"
      :value="value"
      :max="max"
      :min="min"
      @duetChange="dateSelected"
    >
    </duet-date-picker>
    <gov-error-message v-if="error" v-text="error" :for="id" />
  </gov-form-group>
</template>

<script>
export default {
  name: "CkDatePicker",

  props: {
    value: {
      type: String,
      required: true
    },
    label: {
      type: String,
      required: true
    },
    error: {
      required: true
    },
    id: {
      type: String,
      required: true
    },
    max: {
      type: String,
      default: ""
    },
    min: {
      type: String,
      default: ""
    }
  },

  data() {
    return {
      localisation_uk: {
        buttonLabel: "Choose date",
        placeholder: "DD/MM/YYYY",
        selectedDateMessage: "Selected date is",
        prevMonthLabel: "Previous month",
        nextMonthLabel: "Next month",
        monthSelectLabel: "Month",
        yearSelectLabel: "Year",
        closeLabel: "Close window",
        calendarHeading: "Choose a date",
        dayNames: [
          "Sunday",
          "Monday",
          "Tuesday",
          "Wednesday",
          "Thursday",
          "Friday",
          "Saturday"
        ],
        monthNames: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
        ],
        monthNamesShort: [
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec"
        ]
      }
    };
  },

  methods: {
    dateSelected(e) {
      this.$emit("input", e.detail.value);
    }
  }
};
</script>

<style lang="scss">
@import "@/scss/app.scss";

:root {
  --duet-color-primary: #005fcc;
  --duet-color-text: #333;
  --duet-color-text-active: #fff;
  --duet-color-placeholder: #666;
  --duet-color-button: #f5f5f5;
  --duet-color-surface: #fff;
  --duet-color-overlay: rgba(0, 0, 0, 0.8);
  --duet-color-border: #333;

  --duet-font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica,
    Arial, sans-serif;
  --duet-font-normal: 400;
  --duet-font-bold: 600;

  --duet-radius: 4px;
  --duet-z-index: 600;
}

.duet-date__input {
  @extend .govuk-input;
}
</style>
