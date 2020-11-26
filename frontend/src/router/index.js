import Vue from "vue";
import VueRouter from "vue-router";
import TheHome from "@/views/TheHome";
import TheSchedule from "@/views/TheSchedule";
// import pesquisa from '../views/pesquisa'
// import disciplina from '../views/disciplina'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: TheHome,
  },
  {
    path: "/grade",
    name: "grade",
    component: TheSchedule,
  },
  // {
  // 	path: '/pesquisa',
  // 	name: 'pesquisa',
  // 	component: pesquisa
  // },
  // {
  // 	path: '/disciplina',
  // 	name: 'disciplina',
  // 	component: disciplina
  // },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
