<template>
  <section id="course">
    <v-card v-if="getCourse(id)" flat>
      <v-card-title class="text-h4 title">{{
        getCourse(id).title
      }}</v-card-title>
      <v-card-subtitle class="text-h5 department pt-3">
        {{ getCourse(id).department }}
      </v-card-subtitle>
      <v-card-text>
        <v-expansion-panels :disabled="getCourse(id).syllabus" accordion flat>
          <v-expansion-panel>
            <v-expansion-panel-header class="px-0 text-h5">
              <template v-slot:actions>
                <v-icon class="icon">mdi-36px mdi-chevron-down</v-icon>
              </template>
              <span class="header">Ementa</span>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              {{ getCourse(id).syllabus }}
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
        <v-expansion-panels accordion flat>
          <v-expansion-panel>
            <v-expansion-panel-header class="px-0 text-h5">
              <template v-slot:actions>
                <v-icon class="icon">mdi-36px mdi-chevron-down</v-icon>
              </template>
              <span class="header">Pré-requisitos</span>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              {{ getCourse(id).prerequisites }}
              <!-- <v-row>
                <v-col
                  v-for="prerequisite in getCourse(id).prerequisites"
                  :key="prerequisite"
                  cols="12"
                  sm="6"
                  md="4"
                  lg="4"
                  xl="3"
                >
                  <CourseCard :course="getCourse(prerequisite)"></CourseCard>
                </v-col>
              </v-row> -->
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
        <v-expansion-panels accordion flat>
          <v-expansion-panel>
            <v-expansion-panel-header class="px-0 text-h5">
              <template v-slot:actions>
                <v-icon class="icon">mdi-36px mdi-chevron-down</v-icon>
              </template>
              <span class="header">Turmas</span>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row
                v-for="courseClass in getCourse(id).classes"
                :key="courseClass.code"
              >
                {{ courseClass }}

                <!-- <v-col
                  v-for="prerequisite in getCourse(id).prerequisites"
                  :key="prerequisite"
                  cols="12"
                  sm="6"
                  md="4"
                  lg="4"
                  xl="3"
                >
                  <CourseCard :course="getCourse(prerequisite)"></CourseCard>
                </v-col> -->
              </v-row>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-card-text>
    </v-card>
  </section>
</template>

<script>
import { mapGetters } from "vuex";
// import CourseCard from "@/components/CourseCard";

export default {
  name: "TheCourse",
  components: {
    // CourseCard,
  },
  data: () => ({
    expansionPanel: [2],
  }),

  props: {
    id: {
      required: true,
    },
  },
  computed: {
    ...mapGetters(["getCourse"]),
  },
  created() {
    if (!this.getCourse(this.id)) {
      this.$store.dispatch("requestGetCourse", this.id);
    }
  },
};
</script>

<style scoped>
.title {
  font-weight: 400 !important;
  line-height: 1.1 !important;
}

.department {
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
</style>