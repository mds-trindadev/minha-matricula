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
			this.$store.dispatch("getSearch");
		}
	}
}
</script>