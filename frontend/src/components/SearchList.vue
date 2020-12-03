<template>
  <section>
    <v-row>
      <v-col
        v-for="(course, index) in courses"
        :key="index"
        cols="12"
        sm="6"
        md="4"
        lg="4"
        xl="3"
      >
        <CourseCard :course="course">
          <v-btn icon large @click.stop="saveCourse(course)">
            <v-icon v-if="course.saved" color="primary">
              mdi-playlist-check</v-icon
            >
            <v-icon v-else> mdi-playlist-plus</v-icon>
          </v-btn>
        </CourseCard>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import CourseCard from "@/components/CourseCard";
import { mapState } from "vuex";

export default {
  name: "SearchList",

  components: {
    CourseCard,
  },

  computed: {
    ...mapState(["courses"]),
  },

  created() {
    this.getCourses();
  },

  methods: {
    getCourses() {
      this.$store.dispatch("getAllCourses");
    },
    saveCourse(course) {
      this.$store.dispatch("saveCourse", course);
    },
  },
};
</script>