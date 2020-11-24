<template>
<div id="app">
<div id="nav">
<router-link to="/disciplina">Disciplina</router-link>
<router-link to="/gradeHoraria">Grade Horaria</router-link>
<router-link to="/pesquisa">Pesquisa</router-link>
<router-link to="/">Home</router-link>
<router-view/>
</div>
</div>
</template>

<script>

export default {
name: "App",

components: {

},

data: () => ({

}),
};
</script>
