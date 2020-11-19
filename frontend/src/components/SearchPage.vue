<template>
<section id="searchpage">
    <SearchBar/>
</section>

</template>

<script>
import SearchBar from "./searchPage/SearchBar"
export default {
    name: "SearchPage",
    components: {
        SearchBar: SearchBar,
    }
};
</script>