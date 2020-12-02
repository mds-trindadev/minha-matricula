<template>
  <section>
    <v-row>
      <v-col
        v-for="(course, index) in courses.all"
        :key="index"
        cols="12"
        sm="6"
        md="4"
        lg="4"
        xl="3"
      >
        <CourseCard
          :key="updateCard"
          :course="course"
          @handle-course="saveCourse(course)"
        >
          <v-btn icon large @click="saveCourse(course)">
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
  data: () => ({
    updateCard: 0,
  }),
  components: {
    CourseCard,
  },
  computed: {
    ...mapState(["courses"]),
  },
  watch: {
    "courses.saved"() {
      this.updateCard += 1;
    },
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