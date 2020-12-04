<template>
  <section id="schedule">
    <v-card full-width outlined>
      <v-card-title class="text-h4 title">
        Recomendação personalizada!
      </v-card-title>
      <v-card-subtitle class="py-4">
        Faça o <i>upload</i> do seu <strong>Histórico Escolar</strong> para
        receber uma recomendação de próximas disciplinas para cursar.
        <br />
        <br />
        O Histórico pode ser emitido no portal <strong>SIGAA</strong>, em
        <mark><i>Ensino</i> > <i>Emitir Histórico</i> </mark>.
      </v-card-subtitle>
      <v-card-text>
        <v-row justify="center">
          <v-col
            class="text-center"
            :cols="this.$vuetify.breakpoint.mobile ? 12 : 5"
          >
            <v-file-input
              v-model="file"
              accept="application/pdf"
              truncate-length="30"
              prepend-icon=""
              prepend-inner-icon="mdi-file"
              label="Faça o upload"
              outlined
              rounded
            >
            </v-file-input>
            <v-btn
              :disabled="!file"
              :loading="loading"
              color="blue-grey"
              class="ma-2 white--text"
              @click="submitFile()"
            >
              Enviar
              <v-icon right dark> mdi-cloud-upload </v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-card-text>

      <v-card-text>
        <v-expansion-panels v-model="expansionPanel" accordion flat multiple>
          <v-expansion-panel>
            <v-expansion-panel-header class="px-0 text-h5">
              <template v-slot:actions>
                <v-icon class="icon">mdi-36px mdi-chevron-down</v-icon>
              </template>

              <span class="header">Recomendação</span>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row>
                <v-col
                  cols="12"
                  v-for="course in getConcludedCourses"
                  :key="course.code"
                >
                  <CourseCard :course="course">
                    <v-btn icon large @click.stop="saveCourse(course)">
                      <v-icon v-if="course.saved" color="primary">
                        mdi-playlist-check</v-icon
                      >
                      <v-icon v-else> mdi-playlist-plus</v-icon>
                    </v-btn>
                  </CourseCard>
                </v-col>
              </v-row>
            </v-expansion-panel-content>
          </v-expansion-panel>
          <v-expansion-panel>
            <v-expansion-panel-header class="px-0 text-h5">
              <template v-slot:actions>
                <v-icon class="icon">mdi-36px mdi-chevron-down</v-icon>
              </template>

              <span class="header">Disciplinas cursadas</span>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row>
                <v-col
                  cols="12"
                  v-for="course in getConcludedCourses"
                  :key="course.code"
                >
                  <CourseCard :course="course">
                    <v-btn icon large @click.stop="saveCourse(course)">
                      <v-icon v-if="course.saved" color="primary">
                        mdi-playlist-check</v-icon
                      >
                      <v-icon v-else> mdi-playlist-plus</v-icon>
                    </v-btn>
                  </CourseCard>
                </v-col>
              </v-row>
            </v-expansion-panel-content>
          </v-expansion-panel>
          <v-expansion-panel>
            <v-expansion-panel-header class="px-0 text-h5">
              <template v-slot:actions>
                <v-icon class="icon">mdi-36px mdi-chevron-down</v-icon>
              </template>

              <span class="header"> Obrigatórias do curso</span>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row>
                <v-col
                  cols="12"
                  v-for="course in getConcludedCourses"
                  :key="course.code"
                >
                  <CourseCard :course="course">
                    <v-btn icon large @click.stop="saveCourse(course)">
                      <v-icon v-if="course.saved" color="primary">
                        mdi-playlist-check</v-icon
                      >
                      <v-icon v-else> mdi-playlist-plus</v-icon>
                    </v-btn>
                  </CourseCard>
                </v-col>
              </v-row>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-card-text>
    </v-card>

    <!-- <v-card>
      <v-card-title class="title">Título da grade</v-card-title>
      <v-card-subtitle class="department">Subtítulo da grade.</v-card-subtitle>
      <v-card-text>
        <v-data-table
          :headers="table.days"
          :items="table.classes"
          :items-per-page="5"
          class="elevation-1"
        ></v-data-table>
      </v-card-text>
    </v-card> -->
  </section>
</template>

<script>
import { mapGetters } from "vuex";
import CourseCard from "@/components/CourseCard";

export default {
  name: "TheSchedule",
  components: {
    CourseCard,
  },

  data: () => ({
    expansionPanel: [0],
    file: null,
    loading: false,
  }),
  computed: {
    ...mapGetters(["getConcludedCourses"]),
  },
  watch: {
    getConcludedCourses() {
      if (this.getConcludedCourses) {
        this.loading = false;
      }
    },
  },
  methods: {
    getTitle(id) {
      switch (id) {
        case 1:
          return "Disciplinas obrigatórias";
        case 2:
          return "Disciplinas cursadas";
        case 3:
          return "Recomendação";
      }
    },
    submitFile() {
      if (this.file) {
        let formData = new FormData();

        formData.append("file", this.file);

        this.$store.dispatch("uploadFile", formData);
        this.loading = true;
      }
    },
    saveCourse(course) {
      this.$store.dispatch("saveCourse", course);
    },
  },
};
</script>

<style scoped>
.title {
  font-weight: 400 !important;
  line-height: 1.1 !important;
}

.department {
  font-size: 30px !important;
  font-weight: 300 !important;
  line-height: 1.1 !important;
}

.v-card__text,
.v-card__title {
  word-break: normal;
}

mark {
  background-color: #ffd394;
}
</style>