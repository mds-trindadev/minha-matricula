import axios from "axios";

const apiClient = axios.create({
  // baseURL: "http://192.168.15.7:3000" /* fake */,
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
  // getCourses() {
  //   return apiClient.get("/courses");
  // },
  getSearchResults(string, campus, department, credits) {
    return apiClient.post("/pesquisa", {
      nome: string,
      campus: campus,
      // departamento: department,
      creditos: credits,
    });
  },
  getCourse(id) {
    return apiClient.get(`/disciplina?codigo=${id}`); /* fake */
    // return apiClient.post("/disciplina", { codigo: id }); /* real */
  },
};
