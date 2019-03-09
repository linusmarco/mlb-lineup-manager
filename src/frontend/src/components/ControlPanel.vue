<template>
    <div id="control-panel">
        <b-form-select
            v-on:change="updateValue('pitchHand', $event)"
            :options="[
                { value: 'R', text: 'Right handed opposing pitcher' },
                { value: 'L', text: 'Left handed opposing pitcher' }
            ]"
            :value="pitchHand"
        />
        <Slider
            v-bind:label-start="'Historical'"
            v-bind:label-end="'Hot Hand'"
            v-bind:range="[0, 100, 1]"
            v-bind:val="hot"
            v-on:valueChange="updateValue('hot', $event)"
        />
        <Slider
            v-bind:label-start="'Overall'"
            v-bind:label-end="'Platoon'"
            v-bind:range="[0, 100, 1]"
            v-bind:val="platoon"
            v-on:valueChange="updateValue('platoon', $event)"
        />
        <!-- <Slider
            v-bind:label-start="'Regular'"
            v-bind:label-end="'New guy'"
            v-bind:range="[0, 100, 1]"
        /> -->
    </div>
</template>

<script>
import Slider from './Slider.vue';

export default {
    name: 'ControlPanel',
    props: ['hot', 'platoon', 'pitchHand'],
    components: { Slider },
    methods: {
        updateValue(key, val) {
            this.$emit('update', { key, val });
        }
    }
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
