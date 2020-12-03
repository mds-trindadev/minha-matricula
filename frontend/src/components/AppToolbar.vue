<template>
  <section>
    <v-app-bar app flat outlined>
      <v-app-bar-nav-icon>
        <v-img src="@/assets/logo1.svg" width="50" @click="goToHome()"></v-img>
      </v-app-bar-nav-icon>
      <v-spacer />
      <v-btn icon @click="toggleDrawer">
        <v-badge
          v-if="getSavedCourses.length > 0"
          color="orange"
          :content="getSavedCourses.length"
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
    ...mapGetters(["getSavedCourses"]),
  },

  methods: {
    toggleDrawer() {
      this.$emit("toggle-drawer");
    },
    goToHome() {
      this.$router.push({ path: "/" });
    },
  },
};
</script>

<style scoped>
.theme--light.v-app-bar.v-toolbar.v-sheet {
  background-color: white;
}
</style>