<template>
    <b-container fluid>
        <b-row class="my-1">
            <b-col sm="2" class="text-right">
                <span>{{ labelStart }}</span>
            </b-col>
            <b-col sm="8">
                <b-form-input
                    type="range"
                    :min="range[0]"
                    :max="range[1]"
                    :step="range[2]"
                    :value="val"
                    @change.native="emit($event)"
                />
            </b-col>
            <b-col sm="2" class="text-left">
                <span>{{ labelEnd }}</span>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
export default {
    name: 'Slider',
    props: ['labelStart', 'labelEnd', 'range', 'val'],
    methods: {
        emit(event) {
            this.$emit('valueChange', Number(event.currentTarget.value));
        }
    },
    data() {
        return {};
    }
};
</script>

<style scoped>
#slider {
}
</style>
