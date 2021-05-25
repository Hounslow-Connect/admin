<template>
  <div>
    <ck-text-input
      :value="banner.title || ''"
      @input="onInput({ field: 'title', value: $event })"
      label="What is the banner title?"
      help="This text will appear as the large heading on the banner (70 characters max)"
      :error="errors.title"
      id="banner.title"
    />

    <ck-wysiwyg-input
      :value="banner.content || ''"
      @input="onInput({ field: 'content', value: $event })"
      label="Banner description"
      help="This text will appear as the smaller description text on the banner (200 characters max)"
      :error="errors.content"
      id="banner.content"
    />

    <ck-image-input
      v-if="banner.has_image"
      @input="onInput({ field: 'image_file_id', value: $event.file_id })"
      id="logo"
      label="Add a logo"
      hint="Click 'Choose file' below to upload a logo to be displayed on the banner"
      accept="image/x-png"
      :existing-url="
        banner.has_image
          ? apiUrl(`/settings/banner-image.png?v=${now}`)
          : undefined
      "
    />

    <ck-text-input
      :value="banner.button_text || ''"
      @input="onInput({ field: 'button_text', value: $event })"
      label="What should the button say?"
      hint='eg. "Find out more" (30 characters max)'
      :error="errors.button_text"
      id="banner.button_text"
    />

    <ck-text-input
      :value="banner.button_url || ''"
      @input="onInput({ field: 'button_url', value: $event })"
      label="What page should the banner link to?"
      hint="Copy and paste the web address below"
      :error="errors.button_url"
      id="banner.button_url"
      type="url"
    />
  </div>
</template>

<script>
  import CkImageInput from './CkImageInput';

  export default {
    components: {
      CkImageInput,
    },

    props: {
      banner: {
        type: Object,
        default() {
          return {
            title: '',
            content: '',
            button_text: '',
            button_url: '',
          };
        },
      },
      errors: {
        type: Object,
        default() {
          return {};
        },
      },
    },

    methods: {
      onInput({ field, value }) {
        const banner = { ...this.banner };

        banner[field] = value;

        this.$emit('update', banner);
        this.$emit('clear', `banner.${field}`);
      },
    },
  };
</script>

<style lang="scss" scoped></style>
