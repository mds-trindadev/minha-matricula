<template>
  <section id="course">
    <!-- Search bar -->
    <v-row>
      <v-col cols="3">
        <v-text-field
          outlined
          rounded
          label="Busque por uma disciplina"
        ></v-text-field>
      </v-col>

      <v-col v-for="(filter, index) of filters" :key="filter.label" cols="3">
        <v-select
          v-model="selections[index]"
          :items="filter.options"
          :label="filter.label"
          :menu-props="{
            bottom: true,
            offsetY: true,
            rounded: 'xl',
            allowOverflow: false,
          }"
          transition="slide-x-transition"
          height="56"
          multiple
          clearable
          outlined
          rounded
        >
          <template v-slot:selection="{ index }">
            <span>{{ index }} </span>
          </template>
        </v-select>
      </v-col>
    </v-row>

    <!-- Course list -->
    <v-row>
      <v-col v-for="(course, index) in courses" :key="index" :cols="columns">
        <CourseCard :course="course"> </CourseCard>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import CourseCard from "@/components/CourseCard";
import Services from "@/services";

export default {
  name: "TheCourse",
  components: {
    CourseCard,
  },
  data: () => ({
    columns: 3,
    selections: {
      campus: [],
      department: [],
      credits: [],
    },
    filters: {
      campi: {
        label: "Campi",
        options: [],
      },
      credits: {
        label: "Créditos",
        options: [],
      },
      departments: {
        label: "Departamentos",
        options: [],
      },
    },
    courses: [],
  }),

  created() {
    Services.getFilters()
      .then((response) => {
        this.filters = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

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