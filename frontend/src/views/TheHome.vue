<template>
  <section id="home">
    <AppToolbar :title="title" />

    <v-main>
      <v-container fluid>
        <v-row justify="center">
          <v-col cols="8">
            <v-row wrap>
              <v-col
                v-for="(course, index) in courses"
                :key="index"
                :cols="columns"
              >
                <CourseCard :course="course"> </CourseCard>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </section>
</template>

<script>
import AppToolbar from "@/components/AppToolbar";
import CourseCard from "@/components/CourseCard";

export default {
  name: "TheHome",
  components: {
    AppToolbar,
    CourseCard,
  },
  data: () => ({
    title: "Home",
    columns: 3,
    cards: 8,
    courses: [
      {
        cod: "MAT0010",
        campus: "Darcy Ribeiro",
        credits: 6,
        title: "GEOMETRIA ANALÍTICA PARA MATEMÁTICA",
        department: "Departamento de Matemática",
        classes: [
          "A | ter 10h, qui 16h",
          "B | sex 14h",
          "A | ter 10h, qui 16h",
          "B | sex 14h",
          "A | ter 10h, qui 16h",
          "B | sex 14h",
        ],
      },
      {
        cod: "FGA001",
        campus: "FGA",
        credits: 4,
        title: "Métodos de Desenvolvimento de Software",
        department: "Faculdade do Gama",
        classes: ["A | ter 10h, qui 16h", "B | sex 14h"],
      },
      {
        cod: "FGA001",
        campus: "FGA",
        credits: 4,
        title: "Métodos de Desenvolvimento de Software",
        department: "Faculdade do Gama",
        classes: ["A | ter 10h, qui 16h", "B | sex 14h"],
      },
      {
        cod: "FGA001",
        campus: "FGA",
        credits: 4,
        title: "Métodos de Desenvolvimento de Software",
        department: "Faculdade do Gama",
        classes: ["A | ter 10h, qui 16h", "B | sex 14h"],
      },
      {
        cod: "FGA001",
        campus: "FGA",
        credits: 4,
        title: "Métodos de Desenvolvimento de Software",
        department: "Faculdade do Gama",
        classes: ["A | ter 10h, qui 16h", "B | sex 14h"],
      },
      {
        cod: "FGA001",
        campus: "FGA",
        credits: 4,
        title: "Métodos de Desenvolvimento de Software",
        department: "Faculdade do Gama",
        classes: ["A | ter 10h, qui 16h", "B | sex 14h"],
      },
    ],
  }),
};
</script>