<template>
    <div id="lineup">
        <div id="lineup-table-container">
            <h3>
                My Lineup
            </h3>
            <table class="table">
                <thead>
                    <tr>
                        <th>&nbsp;</th>
                        <th>Name</th>
                        <th>Position</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(p, i) in players" :key="p.id">
                        <td>{{ i + 1 }}</td>
                        <td>{{ p.name }}</td>
                        <td>{{ p.pos }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Lineup',
    props: ['players'],
    data() {
        return {};
    }
};
</script>

<style scoped>
#lineup-table-container {
    width: 40%;
    margin: auto;
}
</style>
