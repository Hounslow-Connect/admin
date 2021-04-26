<template>
  <div>
    <gov-back-link :to="{ name: 'dashboard' }">
      Back to dashboard
    </gov-back-link>

    <gov-main-wrapper>
      <gov-grid-row>
        <gov-grid-column width="two-thirds">
          <gov-heading size="l">
            Is your Organisation already listed?
          </gov-heading>

          <gov-body>
            Before you register an account on One Hounslow Connect, we need to
            check if your organisation is already registered in our database.
          </gov-body>
          <gov-body
            >Type the name of your organisation below to check if it is already
            registered.</gov-body
          >
        </gov-grid-column>
      </gov-grid-row>
      <gov-grid-row>
        <gov-grid-column width="full">
          <organisation-search />
        </gov-grid-column>
      </gov-grid-row>
      <gov-grid-row>
        <gov-grid-column width="two-thirds">
          <gov-body>Select your organisation and click "next"</gov-body>
          <gov-button start :to="{ name: 'register-existing' }">
            Next
          </gov-button>
          <gov-body
            >Can’t find your organisation?
            <gov-link :to="{ name: 'register-new' }"
              >Register new organisation</gov-link
            ></gov-body
          >
        </gov-grid-column>
      </gov-grid-row>
    </gov-main-wrapper>
  </div>
</template>

<script>
  import OrganisationSearch from './index/forms/OrganisationSearch.vue';

  export default {
    components: {
      OrganisationSearch,
    },
  };
</script>

<style lang="scss" scoped></style>
