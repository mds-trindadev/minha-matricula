<template>
  <section>
    <v-hover v-slot="{ hover }">
      <v-card
        :elevation="hover ? 4 : 0"
        :class="[
          getSideColor(),
          {
            'rounded-lg': true,
            'on-hover': hover,
          },
        ]"
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
    index: {
      type: Number,
      required: false,
    },
    maxCredits: {
      type: Number,
      required: false,
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
    getSideColor() {
      if (this.course.concluded) {
        return "concluded";
      } else if (this.course.suggested) {
        return "suggested";
      } else if (!this.course.available) {
        return "unavailable";
      }
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

.concluded {
  border-left: 5px solid gray !important;
}

.suggested {
  border-left: 5px solid green !important;
}

.available {
  border-left: 5px solid blue !important;
}

.unavailable {
  border-left: 5px solid red !important;
}
</style>