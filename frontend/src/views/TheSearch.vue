<template>
  <section id="home">
    <SearchToolbar></SearchToolbar>
    <SearchList></SearchList>
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
    title: "Home",
  }),
};
</script>