<template>
    <div id="app">
        <Header />
        <ControlPanel />
        <Lineup />
        <Roster />
        <Footer />
    </div>
</template>

<script>
import ControlPanel from './components/ControlPanel.vue';
import Lineup from './components/Lineup.vue';
import Roster from './components/Roster.vue';
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';

export default {
    name: 'app',
    components: {
        ControlPanel,
        Lineup,
        Roster,
        Header,
        Footer
    }
};
</script>

<style>
html,
body {
    margin: 0;
    padding: 0;

    font-size: 14px;
}

body {
    overflow-y: scroll;
}

#app {
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;

    margin: auto;

    min-height: calc(100vh - 5.8rem - 3rem);
    position: relative;
    padding: 5.8rem 0 3rem 0;
}
</style>
