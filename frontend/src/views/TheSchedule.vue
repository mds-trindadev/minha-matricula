<template>
  <section id="schedule">
    <AppToolbar :title="title"/>
  </section>
</template>

<script>
import AppToolbar from "@/components/AppToolbar";

export default {
  name: "TheHome",
  components: {
    AppToolbar,
  },
  data: () => ({
    title: "Grade Horária",
  }),
};
</script>