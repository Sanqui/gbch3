<template>
  <main>
    <div class="tone-select">
      Tone to play:
      <wave-tone-select v-model="frequency"/>
    </div>
    <h2>Games</h2>
    <div>
      <input type="radio" id="games-show-select" value="select" v-model="games_show" @input="change_games_show">
      <label for="games-show-select">Show select games</label>
      <input type="radio" id="games-show-all" value="all" v-model="games_show" @input="change_games_show">
      <label for="games-show-all">Show all games</label>
    </div>
    <div v-for="game in show_games" :key="game">
      <wave-game :game="game" :game_data="data[game]" v-on:play-sample="play" />
    </div>
  </main>
</template>

<script>
  import data from '~/data/data.json'
  import * as Tone from 'tone';

  const SELECT_GAMES = [
    "Kirby's Dream Land (1992)(HAL Laboratory)",
    "Legend of Zelda - Link's Awakening DX (1993)(Nintendo)",
    "Pokemon Crystal (2001)(Game Freak, Nintendo)",
    "Pokemon Red (1998)(Game Freak, Nintendo)",
    "Pokemon Trading Card Game (1998)(Nintendo)",
    "Super Mario Land (1989)(Nintendo)",
    "Tetris (1989)(BPS, Nintendo)",
    "Wario Land 2 (1998)(Nintendo)",
  ]


  export default {
    asyncData () {
      return {
        data: data
      }
    },
    data() {
      return {
        player: null,
        frequency: "440.00",
        show_games: SELECT_GAMES,
        games_show: "select"
      }
    },
    methods: {
      change_games_show: function() {
        // XXX this condition is reversed, most likely
        // @input gets fired before the games_show variable gets changed
        // TODO fix

        if (this.games_show == 'all') {
          this.show_games = SELECT_GAMES;
        } else {
          this.show_games = Object.keys(data);
        }
        
      },
      play: function(wave) {
        console.log("boop");
        const SAMPLE_RATE = 48000;
        const SAMPLE_LENGTH = 20000;
        const WAVE_WIDTH = 32;
        const FINAL_VOLUME = 0.2;

        var amplitude_hold = SAMPLE_RATE / parseFloat(this.frequency) / WAVE_WIDTH;
        var step = 0;
        
        var sample = [];
        
        for (var step=0; step<SAMPLE_LENGTH; step++) {
          var volume = 1.0;
          if (step/SAMPLE_LENGTH > 0.9) {
            volume = 0.25;
          } else if (step/SAMPLE_LENGTH > 0.75) {
            volume = 0.5;
          }
          var n = Math.floor((step / amplitude_hold) % WAVE_WIDTH);
          var amplitude = parseInt(wave[n], 16);
          
          sample.push(((amplitude/16) - 0.5) * volume * FINAL_VOLUME);
        }

        // console.log(sample)
        const buffer = Tone.ToneAudioBuffer.fromArray(Float32Array.from(sample));
        if (this.player) {
          this.player.stop();
          this.player.dispose();
        }
        this.player = new Tone.Player(buffer).toDestination();
        this.player.start();
      },
    },
  }
</script>

<style scoped>
  .tone-select {
    text-align: center;
  }
</style>