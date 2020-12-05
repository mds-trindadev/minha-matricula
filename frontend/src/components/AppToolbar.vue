<template>
  <section>
    <v-app-bar app flat outlined>
      <v-app-bar-nav-icon>
        <v-img
          src="@/assets/logo1.svg"
          width="50"
          @click="goToPath('/')"
        ></v-img>
      </v-app-bar-nav-icon>
      <v-spacer />

      <v-tabs right :value="getTab()">
        <v-tab to="/">Busca</v-tab>
        <v-tab to="/grade">Sugestão</v-tab>
      </v-tabs>
      <v-btn icon @click="toggleDrawer">
        <!-- <v-badge
          v-if="getSavedCourses.length > 0"
          color="orange"
          :content="getSavedCourses.length"
          left
        ></v-badge> -->
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
    goToPath(path) {
      this.$router.push({ path: path });
    },
    getTab() {
      switch (this.$route.name) {
        case "search":
          return "tab-1";
        case "schedule":
          return "tab-2";
      }
    },
  },
};
</script>

<style scoped>
.theme--light.v-app-bar.v-toolbar.v-sheet {
  background-color: white;
}
</style>