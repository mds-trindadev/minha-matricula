<template>
  <section>
    <v-row>
      <v-col
        v-for="(course, index) in courses.all"
        :key="index"
        cols="12"
        sm="6"
        md="4"
        lg="3"
      >
        <CourseCard :course="course" @handle-course="saveCourse(course)">
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