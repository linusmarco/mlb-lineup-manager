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
                        <!-- <th scope="col">SLG</th> -->
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="p in players" :key="p.id">
                        <td>{{ `${p.LAST_NAME}, ${p.FIRST_NAME}` }}</td>
                        <td>{{ p.pos }}</td>
                        <td>{{ p.BAT_HAND }}</td>
                        <td>{{ p.PLATE_APPEARANCE_COUNT }}</td>
                        <td>{{ (p.HIT_COUNT / p.AT_BAT_COUNT).toFixed(3) }}</td>
                        <td>
                            {{
                                ((p.HIT_COUNT + p.WALK_COUNT) / p.PLATE_APPEARANCE_COUNT).toFixed(3)
                            }}
                        </td>
                        <!-- <td>{{ p.SLG }}</td> -->
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
        console.log(players);
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
