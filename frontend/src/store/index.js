import Vue from 'vue'
import Vuex from 'vuex'
import http from '../http'

Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
		token: null,
	},
	mutations: {
		getBusca(state, token){
			state.token = token
		},

		getDisciplina(state, token){
			state.token = token
		},

		getGradeHoraria(state, token){
			state.token = token
		}
	},
	actions: {
		async getBusca(context, data) {
			const response = await http.post("/pesquisa", data )
			context.commit("getSearch", response.data)
		},

		async getDisciplina(context, data) {
			const response = await http.post("/disciplina", data )
			context.commit("getDisciplina", response.data)
		},

		async getGradeHoraria(context, data) {
			const response = await http.post("/gradeHoraria", data )
			context.commit("getGradeHoraria", response.data)
		}
	},
	modules: {

	}
})

export default store