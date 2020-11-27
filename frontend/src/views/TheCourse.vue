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
          counter
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
      campus: {
        label: "Campus",
        options: ["Darcy Ribeiro", "FCE", "FGA", "FUP"],
      },
      department: {
        label: "Departamento",
        options: [
          "Departamento de Matemática",
          "Departamento de Estudos Latino Americanos Departamento de Estudos Latino Americanos",
          "Faculdade do Gama",
          "Departamento de Farmácia",
        ],
      },
      credit: {
        label: "Créditos",
        options: [1, 2, 4, 6, 8],
      },
    },
    courses: [
      {
        cod: "MAT0010",
        campus: "Darcy Ribeiro",
        credits: 6,
        title: "GEOMETRIA ANALÍTICA PARA MATEMÁTICA",
        department: "Departamento de Matemática",
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
        cod: "DIN0001",
        campus: "Darcy Ribeiro",
        credits: 4,
        title: "FUNDAMENTOS DA LÍNGUAGEM APLICADOS AO DESIGN",
        department: "DEPARTAMENTO DE DESIGN",
        classes: ["B | sex 14h", "A | ter 10h, qui 16h"],
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
        classes: ["B | sex 14h", "A | ter 10h, qui 16h"],
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
        classes: ["B | sex 14h", "A | ter 10h, qui 16h"],
      },
    ],
  }),
};
</script>