<template>
  <section>
    <v-card class="header rounded-xl" outlined>
      <v-app-bar color="transparent" dense flat>
        <v-toolbar-title :class="getCampusColor(course.campus)">{{
          course.campus
        }}</v-toolbar-title>

        <v-spacer />

        <v-toolbar-title> {{ course.credits }} créditos </v-toolbar-title>
      </v-app-bar>

      <v-card-title class="text-h5 pt-1">{{
        capitalize(course.title)
      }}</v-card-title>

      <v-card-text class="department">{{
        capitalize(course.department)
      }}</v-card-text>

      <v-card-text>
        <div
          v-for="(class_, index) in course.classes"
          :key="index"
          class="mr-1 my-1"
        >
          <v-chip>
            {{ class_ }}
          </v-chip>
        </div>
      </v-card-text>
    </v-card>
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
    capitalize(title) {
      var newTitle = [];

      title.split(" ").forEach((string) => {
        var newString = string.toLowerCase();

        if (string.length > 3) {
          newString = string.charAt(0).toUpperCase();
          newString += string.slice(1).toLowerCase();
        }

        newTitle.push(newString);
      });

      return newTitle.join(" ");
    },
  },
};
</script>

<style scoped>
.header * {
  font-weight: 300;
  font-size: 15px;
}

.department {
  font-weight: 300;
  font-size: 20px;
}

.v-card__text,
.v-card__title {
  word-break: break-word;
}
</style>