import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
// import data from "@/assets/data";
import CourseService from "@/services/CourseService.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    filters: {
      credits: [1, 2, 3, 4, 5, 6],
      departments: [],
      campi: ["FGA", "FCE"],
    },
    courses: [],
  },
  mutations: {
    SET_COURSES(state, disciplinas) {
      console.log(disciplinas);
    },
    SAVE_FILTERS(state, filters) {
      console.log(filters);
      state.filters = filters;
    },
    // SAVE_ALL_COURSES(state, courses) {
    //   courses.forEach((course, index) => {
    //     Vue.set(courses[index], "saved", false);
    //   });
    //   state.courses = courses;
    // },
    SAVE_COURSE(state, course) {
      const formattedCourse = {
        campus: course.campus,
        timeLoad: course.cargaHoraria,
        code: course.codigo,
        concluded: course.concluida,
        credits: course.creditos,
        department: course.departamento,
        syllabus: course.ementa,
        title: course.nome,
        prerequisites: course.preRequisitos,
        priority: course.prioridade,
        classes: Object.keys(course.turmas)
          .map((key) => course.turmas[key])
          .map((key) => ({
            time: key.horario,
            period: key.periodo,
            teacher: key.professor,
            code: key.turma,
          })),
      };

      Vue.set(course, "saved", false);
      state.courses.push(formattedCourse);
    },
    CAPITALIZE_ALL_COURSES(state) {
      state.courses.forEach((course, index) => {
        var newTitle = [];
        var newDepartment = [];

        course.title.split(" ").forEach((string) => {
          var newString = string.toLowerCase();

          if (string.length > 3) {
            newString = string.charAt(0).toUpperCase();
            newString += string.slice(1).toLowerCase();
          }

          newTitle.push(newString);
        });

        course.department.split(" ").forEach((string) => {
          var newString = string.toLowerCase();

          if (string.length > 3) {
            newString = string.charAt(0).toUpperCase();
            newString += string.slice(1).toLowerCase();
          }

          newDepartment.push(newString);
        });

        state.courses[index].title = newTitle.join(" ");
        state.courses[index].department = newDepartment.join(" ");
      });
    },
    SAVE_LOCAL_COURSE(state, course) {
      state.courses.forEach((elem, index) => {
        if (course.code === elem.code) {
          state.courses[index].saved = true;
        }
      });
    },
    REMOVE_COURSE(state, courseAndIndex) {
      state.courses.forEach((elem, elemIndex) => {
        if (courseAndIndex.course.code === elem.code) {
          state.courses[elemIndex].saved = false;
        }
      });
    },
    REMOVE_ALL_SAVED_COURSES(state) {
      state.courses.forEach((course, index) => {
        state.courses[index].saved = false;
      });
    },
  },
  actions: {
    async search(state, params) {
      console.log(params);
    },
    async getFilters({ commit }) {
      const { data } = await CourseService.getFilters();
      commit("SAVE_FILTERS", data);
    },
    async getAllCourses({ commit }) {
      const { data } = await CourseService.getCourses();
      commit("SAVE_ALL_COURSES", data);
      commit("CAPITALIZE_ALL_COURSES");
    },
    async getCourse({ commit }, id) {
      const { data } = await CourseService.getCourse(id);
      commit("SAVE_COURSE", data[0]);
      // commit("CAPITALIZE_ALL_COURSES");
    },
    async setCourses({ commit }) {
      axios.get("@/assets/data.json").then((response) => {
        commit("SET_COURSES", response.data.disciplina);
      });
    },
    // async getCourseAndPrerequisites({ commit }, id) {
    //   try {
    //     const { data } = await CourseService.getCourse(id);
    //     if (data) {
    //       commit("SAVE_COURSE", data);
    //     }

    //     data.preRequisitos.forEach(async (prerequisite) => {
    //       const { data } = await CourseService.getCourse(prerequisite);
    //       if (data) {
    //         commit("SAVE_COURSE", data);
    //       }
    //     });
    //   } catch (error) {
    //     // router.push({ path: "/" });
    //     console.log(error);
    //   }

    //   commit("CAPITALIZE_ALL_COURSES");
    // },
    saveCourse({ commit }, course) {
      commit("SAVE_LOCAL_COURSE", course);
    },
    removeCourse({ commit }, courseAndIndex) {
      commit("REMOVE_COURSE", courseAndIndex);
    },
    removeAllSavedCourses({ commit }) {
      commit("REMOVE_ALL_SAVED_COURSES");
    },
  },
  getters: {
    getFilters: (state) => {
      return state.filters;
    },
    getSavedCourses: (state) => {
      return state.courses.filter((course) => course.saved);
    },
    getCourse: (state) => (id) => {
      return state.courses.find((course) => course.code === id);
    },
    getCourses: (state) => (params) => {
      return state.courses.find((campus) => campus !== params);
    },
  },
});
