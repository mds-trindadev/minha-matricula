<template>
  <section id="schedule">
    <AppToolbar :title="title" />
    <v-main>Schedule</v-main>
  </section>
</template>

<script>
import AppToolbar from "@/components/AppToolbar";

export default {
  name: "TheSchedule",
  components: {
    AppToolbar,
  },
  data: () => ({
    title: "Grade Horária",
  }),
};
</script>