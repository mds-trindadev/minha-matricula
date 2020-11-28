<template>
  <section>
    <v-row>
      <v-col cols="4">
        <v-text-field
          outlined
          rounded
          label="Busque por uma disciplina"
        ></v-text-field>
      </v-col>

      <v-col v-for="(filter, index) of filters" :key="filter.label">
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
  </section>
</template>

<script>
import Services from "@/services";

export default {
  name: "SearchToolbar",
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
  }),

  created() {
    Services.getFilters()
      .then((response) => {
        this.filters = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>