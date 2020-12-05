<template>
  <section>
    <v-row>
      <v-col cols="12">
        <v-text-field
          v-model="searchParams.string"
          outlined
          rounded
          label="Busque por uma disciplina"
          hide-details
          clearable
          append-icon="mdi-arrow-right"
          @click:append="search()"
        ></v-text-field>
      </v-col>

      <v-col>
        <v-slide-group show-arrows>
          <v-slide-item v-for="filter in getFilters" :key="filter.title">
            <v-btn
              class="mx-2"
              outlined
              rounded
              small
              @click="openFilter(filter.name)"
            >
              {{ filter.title }}
            </v-btn>
          </v-slide-item>
        </v-slide-group>
      </v-col>
    </v-row>
    <v-row v-if="dialog" justify="center">
      <v-dialog v-model="dialog" scrollable max-width="500px">
        <v-card>
          <v-card-title>{{ getFilterOptions(dialogKey).title }}</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-checkbox
              v-for="option in getFilterOptions(dialogKey).options"
              :key="dialogKey === 'departments' ? option.initials : option"
              v-model="searchParams[dialogKey]"
              :value="option"
              :label="
                dialogKey === 'departments' ? option.title : option.toString()
              "
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
import { mapGetters } from "vuex";

export default {
  name: "SearchToolbar",
  data: () => ({
    columns: 3,
    dialog: false,
    dialogKey: null,
    searchParams: {
      string: "",
      // campi: [],
      departments: [],
      credits: [],
    },
  }),
  computed: {
    ...mapGetters(["getFilters", "getFilterOptions"]),
  },

  methods: {
    openFilter(key) {
      this.dialogKey = key;
      this.dialog = true;
    },
    search() {
      this.$emit("handle-search", this.searchParams);
    },
  },
};
</script>