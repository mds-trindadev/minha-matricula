<template>
  <section>
    <v-card
      class="rounded-lg"
      outlined
      @click="saveCourse(course)"
      width="100%"
    >
      <v-app-bar color="toolbar transparent" dense flat>
        <v-toolbar-title :class="getCampusColor(course.campus)">{{
          course.campus
        }}</v-toolbar-title>

        <v-spacer />

        <v-toolbar-title> {{ course.credits }} créditos </v-toolbar-title>
      </v-app-bar>

      <v-card-title class="title pt-0">{{ course.title }}</v-card-title>

      <v-card-text class="department">{{ course.department }}</v-card-text>

      <v-card-text>
        <div
          v-for="(class_, index) in course.classes"
          :key="index"
          class="mr-1 my-1"
        >
          <v-chip small>
            {{ class_ }}
          </v-chip>
        </div>
      </v-card-text>
    </v-card>
  </section>
</template>

<script>
export default {
  name: "SearchListCard",
  props: {
    course: {
      type: Object,
      required: true,
    },
  },
  methods: {
    getCampusColor(campus) {
      switch (campus) {
        case "Darcy Ribeiro":
          return "blue-grey lighten-5";
        case "FCE":
          return "light-blue lighten-4";
        case "FGA":
          return "light-green lighten-4";
        case "FUP":
          return "amber lighten-4";
        default:
          return "";
      }
    },

    saveCourse(course) {
      this.$store.dispatch("saveCourse", course);
    },
  },
};
</script>

<style scoped>
.toolbar * {
  font-weight: 300 !important;
  font-size: 12px !important;
}

.title {
  font-size: 16px !important;
  font-weight: 400 !important;
  line-height: 1.1 !important;
}

.department {
  font-size: 14px !important;
  font-weight: 300 !important;
  line-height: 1.1 !important;
}

.v-card__text,
.v-card__title {
  word-break: break-word;
}
</style>