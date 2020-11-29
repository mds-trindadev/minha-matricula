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
        <SearchListCard :course="course"> </SearchListCard>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import SearchListCard from "@/components/SearchListCard";
import { mapState } from "vuex";

export default {
  name: "SearchList",
  components: {
    SearchListCard,
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
  },
};
</script>