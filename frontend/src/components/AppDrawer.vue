<template>
  <section>
    <v-navigation-drawer v-model="drawer" app right>
      <div v-if="courses.saved.length">
        <div v-for="(course, index) in courses.saved" :key="index">
          <CourseCard :course="course" @handle-course="removeCourse">
          </CourseCard>
        </div>
      </div>
    </v-navigation-drawer>
  </section>
</template>

<script>
import CourseCard from "@/components/CourseCard";
import { mapState } from "vuex";

export default {
  name: "AppDrawer",
  components: {
    CourseCard,
  },
  data: () => ({
    drawer: false,
  }),
  computed: {
    ...mapState(["courses"]),
  },
  watch: {
    "courses.saved"() {
      this.drawer = true;
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
    removeCourse() {
      console.log("Remover disciplina");
    },
  },
};
</script>