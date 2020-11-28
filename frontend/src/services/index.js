import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://localhost:3000",
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
  getCourses() {
    return apiClient.get("/courses");
  },
  getCourse(id) {
    return apiClient.get("/courses?code=" + id);
  },
};
