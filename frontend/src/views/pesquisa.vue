<template>
	<div>
	<v-app>
		<v-main>
			<SearchPage />
		</v-main>
	</v-app>
	<div>
		<h1>PESQUISA</h1>
		<button @click="pesquisar">Requisitar dados</button>
		<button @click="retornarDisciplina">Retornar Disciplina</button>
	</div>
	</div>
</template>

<script>
import SearchPage from "../components/SearchPage";

export default {
	name: 'pesquisa',

	components: {
		SearchPage,
	},

	methods: {
		pesquisar() {
			this.$store.dispatch("getBusca", { 'campus': 'FGA', 'nome': 'compiladores', 'creditos': 4 });
		},

		retornarDisciplina() {
			this.$store.dispatch("getDisciplina", { 'codigo': 'FGA0003' });
		}
	}
}
</script>