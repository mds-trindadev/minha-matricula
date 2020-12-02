<template>
  <section>
    <v-app-bar app flat outlined>
      <v-spacer />
      <v-btn icon @click="toggleDrawer">
        <v-badge
          v-if="savedQty > 0"
          color="orange"
          :content="savedQty"
          left
        ></v-badge>
        <v-icon>mdi-format-list-bulleted-square</v-icon>
      </v-btn>
    </v-app-bar>
  </section>
</template>
<script>
import { mapState } from "vuex";

export default {
  name: "AppToolbar",
  data: () => ({
    savedQty: 0,
  }),
  computed: {
    ...mapState(["courses"]),
  },
  watch: {
    "courses.saved"() {
      this.savedQty = this.courses.saved.length;
    },
  },
  methods: {
    toggleDrawer() {
      this.$emit("toggle-drawer");
    },
  },
};
</script>

<style scoped>
.theme--light.v-app-bar.v-toolbar.v-sheet {
  background-color: white;
}
</style>