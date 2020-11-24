<template>
	<div>
		<h1>HOME PAGE</h1>
		<button @click="retornarGradeHoraria">Sugestao Grade Horaria</button>
	</div>
</template>

<script>
export default {
	name: 'home',

	methods: {
		retornarGradeHoraria() {
			this.$store.dispatch("getGradeHoraria", { 'dados': 'dados' });
		}
	}
}
</script>