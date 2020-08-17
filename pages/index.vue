<template>
  <main>
    Tone to play:
    <wave-tone-select v-model="frequency"/>
    <h2>Games</h2>
    <!--
    <nuxt-link to="/about">
      About
    </nuxt-link>
    <br>
    <a href="https://nuxtjs.org">External Link to another page</a>
    -->
    <div v-for="(game_data, key) in data" :key="key">
      <wave-game :game="key" :game_data="game_data" v-on:play-sample="play" />
    </div>
  </main>
</template>

<script>
  import data from '~/data/data.json'
  import * as Tone from 'tone';

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
      }
    },
    methods: {
      play: function(wave) {
        console.log("boop");
        const SAMPLE_RATE = 48000;
        const SAMPLE_LENGTH = 20000;
        const WAVE_WIDTH = 32;

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
          
          sample.push((amplitude/16) * volume);
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