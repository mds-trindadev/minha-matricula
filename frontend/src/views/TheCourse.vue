<template>
  <section id="course">
    <v-card v-if="getCourse(id)" flat>
      <v-card-subtitle class="text-h3 title">{{
        getCourse(id).title
      }}</v-card-subtitle>
      <v-card-title class="department pt-0">
        {{ getCourse(id).department }}
      </v-card-title>
      <v-card-text>
        <v-expansion-panels v-model="expansionPanel" flat multiple>
          <v-expansion-panel>
            <v-expansion-panel-header class="px-0 text-h5">
              <template v-slot:actions>
                <v-icon class="icon">mdi-36px mdi-chevron-down</v-icon>
              </template>
              <span class="header">Ementa</span>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ligula
              ullamcorper malesuada proin libero nunc consequat interdum varius
              sit. Eros donec ac odio tempor orci. Id porta nibh venenatis cras
              sed felis eget velit aliquet. Habitasse platea dictumst quisque
              sagittis purus. Fusce ut placerat orci nulla pellentesque
              dignissim enim sit amet. Morbi enim nunc faucibus a pellentesque
              sit. Faucibus pulvinar elementum integer enim. Vulputate mi sit
              amet mauris commodo quis imperdiet massa. Est lorem ipsum dolor
              sit amet. Nisl tincidunt eget nullam non nisi est. Blandit massa
              enim nec dui nunc mattis enim. Et pharetra pharetra massa massa
              ultricies mi quis hendrerit.
            </v-expansion-panel-content>
          </v-expansion-panel>
          <v-expansion-panel>
            <v-expansion-panel-header class="px-0 text-h5">
              <template v-slot:actions>
                <v-icon class="icon">mdi-36px mdi-chevron-down</v-icon>
              </template>
              <span class="header">Pré-requisitos</span>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row>
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
              </v-row>
            </v-expansion-panel-content>
          </v-expansion-panel>
          <v-expansion-panel>
            <v-expansion-panel-header class="px-0 text-h5">
              <template v-slot:actions>
                <v-icon class="icon">mdi-36px mdi-chevron-down</v-icon>
              </template>
              <span class="header">Turmas</span>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row>
                Cards das turmas disponíveis.
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
import CourseCard from "@/components/CourseCard";

export default {
  name: "TheCourse",
  data: () => ({
    expansionPanel: [2],
  }),
  components: {
    CourseCard,
  },
  props: {
    id: {
      required: true,
    },
  },
  computed: {
    ...mapGetters(["getCourse"]),
  },
  created() {
    this.requestCourseAndPrerequisites(this.id);
  },
  methods: {
    requestCourseAndPrerequisites(id) {
      this.$store.dispatch("getCourseAndPrerequisites", id);
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
</style>