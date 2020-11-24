import Vue from 'vue'
import Vuex from 'vuex'
import http from '../http'

Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
		token: null,
	},
	mutations: {
		getSearch(state, token){
			state.token = token
		}
	},
	actions: {
		async getSearch(context) {
			const response = await http.post("/pesquisa")
			context.commit("getSearch", response.data)
		}
	},
	modules: {

	}
})

export default store