<template>
  <div>
    <gov-heading size="l">
      Create an account
    </gov-heading>

    <gov-body>
      Please enter your details below to create an account.
    </gov-body>

    <gov-hint>
      By signing up you agree to our
      <gov-link :to="{ name: 'admin-index-cms-frontend-terms-and-conditions' }"
        >T&amp;Cs</gov-link
      >
      and
      <gov-link :to="{ name: 'admin-index-cms-frontend-privacy-policy' }"
        >Privacy Policy</gov-link
      >
    </gov-hint>

    <ck-text-input
      v-model="form.user.first_name"
      id="first_name"
      label="First name"
      type="text"
      :error="errors.get('user.first_name')"
    />

    <ck-text-input
      v-model="form.user.last_name"
      id="last_name"
      label="Last name"
      type="text"
      :error="errors.get('user.last_name')"
    />

    <ck-text-input
      v-model="form.user.email"
      id="email"
      label="Email"
      type="email"
      :error="errors.get('user.email')"
    />

    <ck-text-input
      v-model="form.user.phone"
      id="phone"
      label="Phone"
      type="tel"
      :error="errors.get('user.phone')"
    />

    <ck-text-input
      v-model="form.user.password"
      id="password"
      label="Password"
      type="password"
      :error="errors.get('user.password')"
    />
  </div>
</template>

<script>
export default {
  props: {
    form: {
      type: Object,
      required: true
    },

    errors: {
      type: Object,
      required: true
    }
  },

  methods: {}
};
</script>

<style lang="scss" scoped></style>
