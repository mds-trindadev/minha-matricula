<template>
  <section id="schedule">
    <AppToolbar :title="title" />
    <h1>Schedule</h1>
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