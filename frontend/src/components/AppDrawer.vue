<template>
  <section>
    <v-navigation-drawer v-model="drawer" app right>
      <div v-for="(course, index) in courses.saved" :key="index">
        {{ course.title }}
      </div>
    </v-navigation-drawer>
  </section>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "AppDrawer",
  props: {
    drawer: {
      type: Boolean,
      required: true,
    },
  },
  computed: {
    ...mapState(["courses"]),
  },
};
</script>