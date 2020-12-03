<template>
  <section>
    <v-app-bar app flat outlined>
      <v-spacer />
      <v-btn icon @click="toggleDrawer">
        <v-badge
          v-if="savedCourses.length > 0"
          color="orange"
          :content="savedCourses.length"
          left
        ></v-badge>
        <v-icon>mdi-format-list-bulleted-square</v-icon>
      </v-btn>
    </v-app-bar>
  </section>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  name: "AppToolbar",

  data: () => ({
    savedQty: 0,
  }),

  computed: {
    ...mapGetters(["savedCourses"]),
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