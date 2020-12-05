import Vue from "vue";
import Vuex from "vuex";
import CourseService from "@/services/CourseService.js";

Vue.use(Vuex);

function capitalizeText(string) {
  var capitalized = [];

  string.split(" ").forEach((substring) => {
    var newString = substring.toLowerCase();

    if (substring.length > 3) {
      newString = substring.charAt(0).toUpperCase();
      newString += substring.slice(1).toLowerCase();
    }

    capitalized.push(newString);
  });

  return capitalized.join(" ");
}

function formatCourseData({
  course,
  curriculum = false,
  suggested = false,
  available = true,
  concluded = false,
}) {
  console.log(`[${course.codigo}] ${course.nome}`);
  return {
    campus: course.campus,
    timeLoad: course.cargaHoraria,
    code: course.codigo,
    credits: course.creditos,
    department: course.departamento,
    syllabus: course.ementa,
    title: capitalizeText(course.nome),
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
    saved: false,
    curriculum,
    suggested,
    available,
    concluded,
  };
}

export default new Vuex.Store({
  state: {
    filters: {
      credits: [1, 2, 3, 4, 5, 6],
      departments: [],
      campi: ["FGA", "FCE"],
    },
    courses: [],
    concluded: [],
  },
  mutations: {
    // Pesquisa
    // Disciplina
    SAVE_COURSE(state, course) {
      const formattedCourse = formatCourseData(course);
      state.courses.push(formattedCourse);
    },

    SAVE_CONCLUDED(state, courses) {
      console.log("Concluídas");
      // console.log(courses);

      for (var newCourse in courses) {
        const index = state.courses.findIndex(
          (course) => courses[newCourse].codigo === course.code
        );

        if (index !== -1) {
          state.courses[index].concluded = true;
        } else {
          const formattedCourse = formatCourseData({
            course: courses[newCourse],
            concluded: true,
          });

          state.courses.push(formattedCourse);
        }
      }
    },

    SAVE_SUGGESTED(state, courses) {
      console.log("Sugeridas");
      // console.log(courses);

      for (var newCourse in courses) {
        const index = state.courses.findIndex(
          (course) => courses[newCourse].codigo === course.code
        );

        if (index !== -1) {
          state.courses[index].suggested = true;
        } else {
          const formattedCourse = formatCourseData({
            course: courses[newCourse],
            suggested: true,
          });

          state.courses.push(formattedCourse);
        }
      }
    },

    SAVE_UNAVAILABLE(state, courses) {
      console.log("Pode cursar");
      // console.log(courses);

      for (var newCourse in courses) {
        const index = state.courses.findIndex(
          (course) => courses[newCourse].codigo === course.code
        );

        if (index !== -1) {
          state.courses[index].available = false;
        } else {
          const formattedCourse = formatCourseData({
            course: courses[newCourse],
            available: false,
          });

          state.courses.push(formattedCourse);
        }
      }
    },

    SAVE_CURRICULUM(state, courses) {
      console.log("Obigatórias");
      // console.log(courses);

      for (var semester in courses) {
        for (var prop in courses[semester]) {
          const formattedCourse = formatCourseData({
            course: courses[semester][prop],
            curriculum: true,
          });

          state.courses.push(formattedCourse);
        }
      }
    },

    SET_CONCLUDED(state, courses) {
      for (const property in courses) {
        const formattedCourse = formatCourseData(courses[property]);
        state.concluded.push(formattedCourse);
      }
    },

    // Rascunho
    SAVE_COURSE_LOCALLY(state, course) {
      state.courses.forEach((elem, index) => {
        if (course.code === elem.code) {
          state.courses[index].saved = true;
        }
      });
    },
    REMOVE_COURSE_LOCALLY(state, courseAndIndex) {
      state.courses.forEach((elem, elemIndex) => {
        if (courseAndIndex.course.code === elem.code) {
          state.courses[elemIndex].saved = false;
        }
      });
    },
    REMOVE_ALL_COURSES_LOCALLY(state) {
      state.courses.forEach((course, index) => {
        state.courses[index].saved = false;
      });
    },
  },
  actions: {
    // Pesquisa

    // Disciplina
    async requestGetCourse({ commit }, id) {
      const { data } = await CourseService.getCourse(id);
      commit("SAVE_COURSE", data);
    },

    // Grade
    async requestUploadFile({ commit, state }, formData) {
      try {
        const { data } = await CourseService.uploadFile(formData);
        console.log(data);

        const {
          // fluxoCurso: curriculum,
          gradeHoraria: suggested,
          naoPodeCursar: unavailable,
          turmasCursadas: concluded,
        } = data;

        commit("SAVE_CONCLUDED", concluded);
        commit("SAVE_SUGGESTED", suggested);
        commit("SAVE_UNAVAILABLE", unavailable);
        // commit("SAVE_CURRICULUM", curriculum);

        console.log(state.courses);
      } catch (error) {
        console.log(error);
      }
    },

    // Rascunho
    saveCourseLocally({ commit }, course) {
      commit("SAVE_COURSE_LOCALLY", course);
    },
    removeCourseLocally({ commit }, courseAndIndex) {
      commit("REMOVE_COURSE_LOCALLY", courseAndIndex);
    },
    removeAllCoursesLocally({ commit }) {
      commit("REMOVE_ALL_COURSES_LOCALLY");
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
    // getCourses: (state) => (params) => {
    //   return state.courses.find((campus) => campus !== params);
    // },
    getCourses: (state) => {
      return state.courses;
    },
  },
});
