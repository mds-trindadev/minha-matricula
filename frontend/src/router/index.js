import Vue from 'vue'
import VueRouter from 'vue-router'
import home from '../views/home'
import gradeHoraria from '../views/gradeHoraria'
import pesquisa from '../views/pesquisa'
import disciplina from '../views/disciplina'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'home',
		component: home
	},
	{
		path: '/gradeHoraria',
		name: 'gradeHoraria',
		component: gradeHoraria
	},
	{
		path: '/pesquisa',
		name: 'pesquisa',
		component: pesquisa
	},
	{
		path: '/disciplina',
		name: 'disciplina',
		component: disciplina
	},
]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
})

export default router