<template>
    <div id="app">
        <Header />
        <main>
            <ControlPanel
                :hot="inputs.hot"
                :platoon="inputs.platoon"
                :pitch-hand="inputs.pitchHand"
                v-on:update="updateInputs($event)"
            />
            <Lineup :players="players" />
            <Roster :players="roster" />
        </main>
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
    },
    methods: {
        updateInputs(val) {
            this.inputs[val.key] = val.val;
            this.players = getRandom(
                this.roster.map(p => {
                    return {
                        name: `${p.LAST_NAME}, ${p.FIRST_NAME}`,
                        pos: 'CF'
                    };
                }),
                9
            );
        }
    },
    mounted() {
        fetch('https://fnlylv1jjh.execute-api.us-east-1.amazonaws.com/dev/getRoster')
            .then(response => {
                return response.json();
            })
            .then(myJson => {
                console.log(myJson);
                this.roster = JSON.parse(myJson);
                this.players = getRandom(
                    this.roster.map(p => {
                        return {
                            name: `${p.LAST_NAME}, ${p.FIRST_NAME}`,
                            pos: 'CF'
                        };
                    }),
                    9
                );
            });

        // fetch(
        //     `https://fnlylv1jjh.execute-api.us-east-1.amazonaws.com/dev/getRanks?hot=${
        //         this.hot
        //     }&platoon=${this.platoon}&pitch_hand=${this.pitch_hand}`
        // )
        //     .then(response => {
        //         return response.json();
        //     })
        //     .then(myJson => {
        //         console.log(JSON.stringify(myJson));
        //         this.lineup = myJson;
        //     });
    },
    data() {
        return {
            players: [],
            testPlayers: [
                { name: 'Player 1', pos: 'P' },
                { name: 'Player 2', pos: 'C' },
                { name: 'Player 3', pos: '1B' },
                { name: 'Player 4', pos: '2B' },
                { name: 'Player 5', pos: '3B' },
                { name: 'Player 6', pos: 'SS' },
                { name: 'Player 7', pos: 'LF' },
                { name: 'Player 8', pos: 'CF' },
                { name: 'Player 9', pos: 'RF' }
            ],
            roster: [],
            testRoster: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].map(
                d => {
                    return {
                        name: `Player ${d}`,
                        pos: 'CF',
                        bats: 'R',
                        PA: Math.round(Math.random() * 600),
                        AVG: Math.round(Math.random() * 0.35, 3),
                        OBP: Math.round(Math.random() * 0.4, 3),
                        SLG: Math.round(Math.random(), 3)
                    };
                }
            ),
            inputs: {
                hot: 50,
                platoon: 50,
                pitchHand: 'R'
            }
        };
    }
};

function getRandom(arr, n) {
    var result = new Array(n),
        len = arr.length,
        taken = new Array(len);
    if (n > len) throw new RangeError('getRandom: more elements taken than available');
    while (n--) {
        var x = Math.floor(Math.random() * len);
        result[n] = arr[x in taken ? taken[x] : x];
        taken[x] = --len in taken ? taken[len] : len;
    }
    return result;
}
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

#app > :nth-child(2) {
    max-width: 1000px;
    margin: auto;
}

h1,
h2 {
    font-weight: 600;
}
</style>
