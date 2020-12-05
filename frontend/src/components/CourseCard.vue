<template>
  <section>
    <v-hover v-slot="{ hover }">
      <v-card
        :elevation="hover ? 4 : 0"
        :class="{
          'rounded-lg': true,
          'on-hover': hover,
        }"
        outlined
        width="100%"
        @click="openCourse(course)"
      >
        <v-app-bar class="toolbar" color="transparent" dense flat>
          <v-toolbar-title :class="getCampusColor(course.campus)">{{
            course.campus
          }}</v-toolbar-title>

          <v-spacer />

          <v-toolbar-title> {{ course.credits }} créditos </v-toolbar-title>
        </v-app-bar>

        <v-card-title class="title pt-0">{{ course.title }}</v-card-title>

        <v-card-text class="department">{{ course.department }}</v-card-text>

        <v-card-actions class="py-0 pl-0">
          <v-card-text v-if="course.classes[0].code">
            <div
              v-for="(classHour, index) in course.classes"
              :key="index"
              class="mr-1 my-1"
            >
              <v-chip v-if="index === 0" small> </v-chip>
              <v-chip
                v-else-if="index === 1 && course.classes.length === 2"
                small
              >
                {{ classHour }}
              </v-chip>
              <v-chip
                v-else-if="index === 1 && course.classes.length > 2"
                color="primary"
                outlined
                small
              >
                + {{ course.classes.length - 1 }}
              </v-chip>
            </div>
          </v-card-text>

          <v-spacer></v-spacer>
          <slot></slot>
        </v-card-actions>
      </v-card>
    </v-hover>
  </section>
</template>

<script>
export default {
  name: "CourseCard",
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
    openCourse(course) {
      this.$router.push({
        path: `/disciplina/${course.code}`,
      });
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