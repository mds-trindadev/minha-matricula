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
          <v-slide-item v-for="(filter, key) of filters" :key="filter.label">
            <v-btn class="mx-2" outlined rounded small @click="openFilter(key)">
              {{ filter.label }}
            </v-btn>
          </v-slide-item>
        </v-slide-group>
      </v-col>
    </v-row>
    <v-row v-if="dialog" justify="center">
      <v-dialog v-model="dialog" scrollable max-width="500px">
        <v-card>
          <v-card-title>{{ filters[dialogKey].label }}</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-checkbox
              v-for="(option, key) of filters[dialogKey].options"
              :key="key"
              v-model="selected[dialogKey]"
              :value="option"
              :label="option.toString()"
              hideDetails
            >
            </v-checkbox>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn color="blue darken-1" text @click="dialog = false">
              Fechar
            </v-btn>
            <v-btn color="blue darken-1" text @click="dialog = false">
              Salvar
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </section>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "SearchToolbar",
  data: () => ({
    columns: 3,
    dialog: false,
    dialogKey: null,
    selected: {
      campi: [],
      departments: [],
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
    openFilter(key) {
      this.dialogKey = key;
      this.dialog = true;
    },
  },
};
</script>