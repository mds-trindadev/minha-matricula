<template>
  <v-app>
    <AppToolbar @toggle-drawer="toggleDrawer"></AppToolbar>
    <AppDrawer ref="appDrawer"></AppDrawer>

    <v-main>
      <v-container fluid>
        <v-row justify="center">
          <v-col cols="12" md="11" lg="9" xl="8">
            <router-view />
          </v-col>
        </v-row>
      </v-container>
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
