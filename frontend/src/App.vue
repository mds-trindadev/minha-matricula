<template>
  <v-app>
    <AppToolbar></AppToolbar>
    <AppDrawer></AppDrawer>

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
  data: () => ({
    drawer: false,
  }),
};
</script>
