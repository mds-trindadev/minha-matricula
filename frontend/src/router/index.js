import Vue from "vue";
import VueRouter from "vue-router";
import TheSearch from "@/views/TheSearch";
import TheCourse from "@/views/TheCourse";
import TheSchedule from "@/views/TheSchedule";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "search",
    component: TheSearch,
  },
  {
    path: "/disciplina",
    name: "course",
    component: TheCourse,
  },
  {
    path: "/grade",
    name: "schedule",
    component: TheSchedule,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
