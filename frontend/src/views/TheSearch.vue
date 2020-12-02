<template>
  <section id="home">
    <v-container fluid>
      <v-row justify="center">
        <v-col cols="12" md="11" lg="9" xl="8">
          <SearchToolbar></SearchToolbar>
          <SearchList></SearchList>
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
import SearchToolbar from "@/components/SearchToolbar";
import SearchList from "@/components/SearchList";

export default {
  name: "TheSearch",
  components: {
    SearchToolbar,
    SearchList,
  },
  data: () => ({
    title: "Home",
  }),
};
</script>