<template>
    <header id="site-header-wrap">
        <div id="site-header">
            <h1 id="site-title">
                MLB Lineup Manager
            </h1>
        </div>
    </header>
</template>

<script>
export default {
    name: 'Header'
};
</script>

<style scoped>
#site-header-wrap {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background-color: white;
    border-bottom: 2px solid black;

    z-index: 99;
}

#site-header {
    position: relative;
    height: 5.8rem;
    width: 90%;
    max-width: 1000px;
    margin: auto;
}

#site-title {
    color: black;
    display: block;
    position: absolute;
}

#site-title {
    left: 0;
    bottom: 0;

    text-align: left;
    margin: 0;

    display: block;

    z-index: 99;
}

#site-title a {
    font-size: 2rem;
    font-weight: 600;
}
</style>
