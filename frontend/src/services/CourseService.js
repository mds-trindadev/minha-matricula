import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:5000/" /* real */,
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

export default {
  getFilters() {
    return apiClient.get("/filters");
  },

  getSearchResults(string, campus, department, credits) {
    return apiClient.post("/pesquisa", {
      nome: string,
      campus: campus,
      creditos: credits,
    });
  },
  getCourse(id) {
    return apiClient.post("/disciplina", { codigo: id }); /* real */
  },
  uploadFile(formData) {
    return apiClient.post("/upload", formData);
  },
  getConcludedCourses() {
    return apiClient.post("/gradeHoraria", { op: "getTurmas" });
  },
  suggestSchedule() {
    return apiClient.post("/gradeHoraria", { op: "sugerirGradeHoraria" });
  },
  getSuggestedSchedule() {
    return apiClient.post("/gradeHoraria", { op: "getGradeHoraria" });
  },
};
