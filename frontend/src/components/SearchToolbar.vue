<template>
  <section>
    <v-row>
      <v-col cols="12">
        <v-text-field
          outlined
          rounded
          label="Busque por uma disciplina"
          hide-details
        ></v-text-field>
      </v-col>

      <v-col>
        <v-slide-group show-arrows>
          <v-slide-item v-for="filter of filters" :key="filter.label">
            <v-btn class="mx-2" outlined rounded small>
              {{ filter.label }}
            </v-btn>
          </v-slide-item>
        </v-slide-group>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "SearchToolbar",
  data: () => ({
    columns: 3,
    selections: {
      campus: [],
      department: [],
      credits: [],
    },
  }),
  computed: {
    ...mapState(["filters"]),
  },

  created() {
    this.getFilters();
  },

  methods: {
    getFilters() {
      this.$store.dispatch("getFilters");
    },
  },
};
</script>