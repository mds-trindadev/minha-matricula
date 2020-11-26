<template>
  <section>
    <v-card class="rounded-xl" outlined>
      <v-app-bar color="transparent" dense flat>
        <v-toolbar-title class="header">{{ course.campus }}</v-toolbar-title>

        <v-spacer />

        <v-toolbar-title class="header">
          {{ course.credits }} créditos
        </v-toolbar-title>
      </v-app-bar>

      <v-card-title class="text-h5 pt-1">{{
        capitalizeTitle(course.title)
      }}</v-card-title>

      <v-card-text class="department">{{ course.department }}</v-card-text>

      <v-card-text>
        <v-chip
          v-for="(class_, index) in course.classes"
          :key="index"
          class="mr-1 my-1"
        >
          {{ class_ }}
        </v-chip>
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
    capitalizeTitle(title) {
      var newTitle = [];

      title.split(" ").forEach((string) => {
        var newString = string.toLowerCase();

        if (string.length > 4) {
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
.header {
  font-weight: 300;
  font-size: 16px;
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