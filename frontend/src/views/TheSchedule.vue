<template>
  <section id="schedule">
    <v-card full-width flat>
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

      <v-row>
        <v-col
          v-for="(course, index) in getCourses"
          :key="index"
          cols="12"
          sm="6"
          md="4"
          lg="4"
          xl="3"
        >
          <CourseCard :course="course" :index="index" :maxCredits="20">
            <v-btn icon large @click.stop="saveCourse(course)">
              <v-icon v-if="course.saved" color="primary">
                mdi-playlist-check</v-icon
              >
              <v-icon v-else> mdi-playlist-plus</v-icon>
            </v-btn>
          </CourseCard>
        </v-col>
      </v-row>
    </v-card>
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
    totalCredits: 0,
  }),
  computed: {
    ...mapGetters(["getCourses"]),
  },
  watch: {
    getCourses() {
      if (this.getCourses) {
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

        this.$store.dispatch("requestUploadFile", formData);
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

.icon {
  order: 0;
}

.header {
  order: 1;
}

.v-card__text,
.v-card__title {
  word-break: normal;
}

mark {
  background-color: #ffd394;
}
</style>