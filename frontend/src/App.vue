<template>
  <v-app>
    <AppToolbar @toggle-drawer="toggleDrawer"></AppToolbar>
    <AppDrawer ref="appDrawer"></AppDrawer>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import AppToolbar from "@/components/AppToolbar";
import AppDrawer from "@/components/AppDrawer";

export default {
  name: "App",
  components: {
    AppToolbar,
    AppDrawer,
  },
  methods: {
    toggleDrawer() {
      this.$refs.appDrawer.drawer = !this.$refs.appDrawer.drawer;
    },
  },
};
</script>
