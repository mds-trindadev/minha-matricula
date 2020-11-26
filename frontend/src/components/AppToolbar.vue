<template>
  <section>
    <v-app-bar app flat color="#07005A">
      <v-icon color="yellow">mdi-triangle-outline</v-icon>
      <v-toolbar-title class="white--text">Minha Matrícula</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-text-field
        label="Procure por uma disciplina"
        single-line
        filled
        rounded
        dense
        hide-details
        background-color="white"
        class="mx-1"
      ></v-text-field>
      <v-select
        v-for="filter in filters"
        v-bind:key="filter"
        class="mx-1"
        v-model="selected[filter.name]"
        :items="filter.options"
        v-bind:label="filter.name"
        single-line
        multiple
        filled
        rounded
        dense
        hide-details
        background-color="white"
      >
        <template v-slot:selection="{ item, index }">
          <v-chip v-if="index === 0">
            <span>{{ item }}</span>
          </v-chip>
          <span v-if="index === 1"
            >+{{ selected.campi.length - 1 }} outros</span
          >
        </template>
      </v-select>

      <v-spacer></v-spacer>
    </v-app-bar>
  </section>
</template>
<script>
export default {
  name: "AppToolbar",
  props: {
    title: {
      type: String,
      required: true,
    },
  },
  data: () => ({
    filters: [
      { name: "credits", options: [2, 4, 6] },
      { name: "campi", options: ["Darcy Ribeiro", "FGA", "FUP", "FCE"] },
    ],
    selected: {
      credits: [],
      campi: [],
    },
  }),
};
</script>