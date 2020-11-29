<template>
  <section>
    <v-app-bar app flat outlined>
      <v-spacer />
      <v-btn icon>
        <v-icon>mdi-format-list-bulleted-square</v-icon>
      </v-btn>
    </v-app-bar>
  </section>
</template>
<script>
export default {
  name: "AppToolbar",
};
</script>

<style scoped>
.theme--light.v-app-bar.v-toolbar.v-sheet {
  background-color: white;
}
</style>