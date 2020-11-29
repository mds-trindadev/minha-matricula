import Vue from "vue";
import Vuex from "vuex";
import CourseService from "@/services/CourseService.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    filters: {
      credits: [],
      departments: [],
      campi: [],
    },
    courses: {
      all: [],
      saved: [],
    },
  },
  mutations: {
    SAVE_FILTERS(state, filters) {
      state.filters = filters;
    },
    SAVE_ALL_COURSES(state, courses) {
      state.courses.all = courses;
    },
    CAPITALIZE_ALL_COURSES(state) {
      state.courses.all.forEach((course, index) => {
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

        state.courses.all[index].title = newTitle.join(" ");
        state.courses.all[index].department = newDepartment.join(" ");
      });
    },
    SAVE_COURSE(state, course) {
      state.courses.saved.push(course);
    },
    // ADD_COURSE(state, course) {
    //   state.courses.saved.push(course);
    // },
  },
  actions: {
    async getFilters({ commit }) {
      const { data } = await CourseService.getFilters();
      commit("SAVE_FILTERS", data);
    },
    async getAllCourses({ commit }) {
      const { data } = await CourseService.getCourses();
      commit("SAVE_ALL_COURSES", data);
      commit("CAPITALIZE_ALL_COURSES");
    },
    saveCourse({ commit }, course) {
      commit("SAVE_COURSE", course);
    },
  },
  getters: {
    // getCourseById: (state) => (id) => {
    //   return state.courses.find((course) => course.id === id);
    // },
  },
});
