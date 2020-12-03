import Vue from "vue";
import Vuex from "vuex";
import router from "@/router";
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
      courses.forEach((course, index) => {
        Vue.set(courses[index], "saved", false);
      });
      state.courses = courses;
    },
    SAVE_COURSE(state, course) {
      Vue.set(course, "saved", false);
      state.courses.push(course);
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
      commit("CAPITALIZE_ALL_COURSES");
    },
    async getCourseAndPrerequisites({ commit }, id) {
      try {
        const { data } = await CourseService.getCourse(id);
        if (data[0]) {
          commit("SAVE_COURSE", data[0]);
        }

        data[0].prerequisites.forEach(async (prerequisite) => {
          const { data } = await CourseService.getCourse(prerequisite);
          if (data[0]) {
            commit("SAVE_COURSE", data[0]);
          }
        });
      } catch (error) {
        router.push({ path: "/" });
      }

      commit("CAPITALIZE_ALL_COURSES");
    },
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
    getSavedCourses: (state) => {
      return state.courses.filter((course) => course.saved);
    },
    getCourse: (state) => (id) => {
      return state.courses.find((course) => course.code === id);
    },
  },
});
