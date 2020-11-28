<template>
  <section id="home">
    <AppToolbar :title="title" />

    <v-main>
      <v-container fluid>
        <v-row justify="center">
          <v-col cols="8">
            <SearchToolbar></SearchToolbar>
            <SearchList></SearchList>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </section>
</template>

<script>
import AppToolbar from "@/components/AppToolbar";
import SearchToolbar from "@/components/SearchToolbar";
import SearchList from "@/components/SearchList";

export default {
  name: "TheSearch",
  components: {
    AppToolbar,
    SearchToolbar,
    SearchList,
  },
  data: () => ({
    title: "Home",
  }),
};
</script>