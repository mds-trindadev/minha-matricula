<template>
  <section id="home">
    <AppToolbar :title="title" />

    <v-main>
      <v-container fluid>
        <v-row justify="center">
          <v-col cols="8">
            <TheCourse></TheCourse>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </section>
</template>

<script>
import AppToolbar from "@/components/AppToolbar";
import TheCourse from "@/views/TheCourse";

export default {
  name: "TheHome",
  components: {
    AppToolbar,
    TheCourse,
  },
  data: () => ({
    title: "Home",
  }),
};
</script>