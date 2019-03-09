<template>
    <div id="roster">
        <div id="roster-table-container">
            <h3>
                Full Roster
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
    name: 'Roster',
    props: ['players'],
    data() {
        return {};
    }
};
</script>

<style scoped>
#roster-table-container {
    width: 100%;
    margin: auto;
}
</style>
