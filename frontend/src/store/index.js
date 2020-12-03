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
    courses: [],
  },
  mutations: {
    SAVE_FILTERS(state, filters) {
      state.filters = filters;
    },
    SAVE_ALL_COURSES(state, courses) {
      // state.courses = [...courses];
      state.courses = courses;
      state.courses.forEach((course, index) => {
        Vue.set(state.courses[index], "saved", false);
      });
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
    SAVE_COURSE(state, course) {
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
    removeCourse({ commit }, courseAndIndex) {
      commit("REMOVE_COURSE", courseAndIndex);
    },
    removeAllSavedCourses({ commit }) {
      commit("REMOVE_ALL_SAVED_COURSES");
    },
  },
  getters: {
    savedCourses(state) {
      return state.courses.filter((course) => course.saved);
    },
  },
});
