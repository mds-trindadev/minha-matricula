<template>
  <section>
    <v-row>
      <v-col v-for="(course, index) in courses" :key="index" :cols="columns">
        <SearchListCard :course="course"> </SearchListCard>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import SearchListCard from "@/components/SearchListCard";
import Services from "@/services";

export default {
  name: "SearchList",
  components: {
    SearchListCard,
  },
  data: () => ({
    columns: 3,
    courses: [],
  }),
  created() {
    Services.getCourses()
      .then((response) => {
        this.courses = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>