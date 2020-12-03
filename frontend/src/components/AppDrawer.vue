<template>
  <section>
    <v-navigation-drawer v-model="drawer" app right width="300">
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            Disciplinas salvas
          </v-list-item-title>
          <v-list-item-subtitle>
            Utilize como um rascunho.
          </v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-avatar v-if="getSavedCourses.length" left>
          <v-btn icon @click="openDialog()">
            <v-icon> mdi-trash-can</v-icon>
          </v-btn>
        </v-list-item-avatar>
      </v-list-item>

      <v-list v-if="getSavedCourses.length">
        <v-list-item-content
          v-for="(course, index) in getSavedCourses"
          :key="index"
          class="pa-2"
        >
          <CourseCard :course="course">
            <v-btn icon large @click.stop="removeCourse(course, index)">
              <v-icon> mdi-playlist-remove</v-icon>
            </v-btn>
          </CourseCard>
        </v-list-item-content>
      </v-list>
    </v-navigation-drawer>

    <v-dialog v-model="dialog" max-width="300px">
      <v-card>
        <v-card-title>
          <span>Deseja limpar o rascunho?</span>
        </v-card-title>
        <v-card-actions>
          <v-spacer> </v-spacer>
          <v-btn text color="primary" @click="closeDialog()">Cancelar</v-btn>
          <v-btn color="primary" @click="removeAllSavedCourses()"
            >Confirmar</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </section>
</template>

<script>
import CourseCard from "@/components/CourseCard";
import { mapState, mapGetters } from "vuex";

export default {
  name: "AppDrawer",
  components: {
    CourseCard,
  },
  data: () => ({
    drawer: false,
    dialog: false,
  }),
  computed: {
    ...mapState(["courses"]),
    ...mapGetters(["getSavedCourses"]),
  },
  watch: {
    getSavedCourses() {
      if (this.getSavedCourses.length > 0) {
        if (!this.$vuetify.breakpoint.mobile) {
          this.drawer = true;
        }
      }
    },
  },
  methods: {
    getCampusColor(campus) {
      switch (campus) {
        case "Darcy Ribeiro":
          return "blue-grey lighten-5";
        case "FCE":
          return "light-blue lighten-4";
        case "FGA":
          return "light-green lighten-4";
        case "FUP":
          return "amber lighten-4";
        default:
          return "";
      }
    },
    removeCourse(course, index) {
      this.$store.dispatch("removeCourse", { course, index });
    },
    removeAllSavedCourses() {
      this.$store.dispatch("removeAllSavedCourses");
      this.closeDialog();
    },
    openDialog() {
      this.dialog = true;
    },
    closeDialog() {
      this.dialog = false;
    },
  },
};
</script>