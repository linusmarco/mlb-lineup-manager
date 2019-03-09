<template>
    <div id="control-panel">
        <Slider
            v-bind:label-start="'Historical'"
            v-bind:label-end="'Hot Hand'"
            v-bind:range="[-100, 100]"
        />
        <Slider
            v-bind:label-start="'Overall'"
            v-bind:label-end="'Platoon'"
            v-bind:range="[-100, 100]"
        />
        <Slider
            v-bind:label-start="'Offense'"
            v-bind:label-end="'Defense'"
            v-bind:range="[-100, 100]"
        />
    </div>
</template>

<script>
import Slider from './Slider.vue';

export default {
    name: 'ControlPanel',
    components: { Slider }
};
</script>

<style scoped>
#control-panel {
    width: 100%;
    border: 1px solid grey;
    padding: 2rem;
    margin: 2rem 0;
}
</style>
