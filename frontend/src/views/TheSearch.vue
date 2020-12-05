<template>
  <section id="home">
    <SearchToolbar @handle-search="setParams"></SearchToolbar>
    <SearchList :params="params" :key="updateCards"></SearchList>
  </section>
</template>

<script>
import SearchToolbar from "@/components/SearchToolbar";
import SearchList from "@/components/SearchList";

export default {
  name: "TheSearch",
  components: {
    SearchToolbar,
    SearchList,
  },
  data: () => ({
    params: {},
    updateCards: 0,
  }),

  created() {
    this.$store.dispatch("setCourses");
  },

  methods: {
    setParams(params) {
      this.params = params;
      this.updateCards += 1;
    },
  },
};
</script>