<template>
    <div id="roster">
        <div id="roster-table-container">
            <h3>
                Full Roster
            </h3>
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Position</th>
                        <th scope="col">Bats</th>
                        <th scope="col">PA</th>
                        <th scope="col">AVG</th>
                        <th scope="col">OBP</th>
                        <th scope="col">SLG</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="p in players" :key="p.id">
                        <td>{{ p.name }}</td>
                        <td>{{ p.pos }}</td>
                        <td>{{ p.bats }}</td>
                        <td>{{ p.PA }}</td>
                        <td>{{ p.AVG }}</td>
                        <td>{{ p.OBP }}</td>
                        <td>{{ p.SLG }}</td>
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
