<template>
  <main>
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
      }
    },
    methods: {
      play: function(wave) {
        console.log("boop");
        const SAMPLE_LENGTH = 200;
        var sample = [];
        
        for (var j=0; j<SAMPLE_LENGTH; j++) {
          var volume = 1.0;
          if (j/SAMPLE_LENGTH > 0.9) {
            volume = 0.25;
          } else if (j/SAMPLE_LENGTH > 0.75) {
            volume = 0.5;
          }
          for (var n=0; n<32; n++) {
            var amplitude = parseInt(wave[n], 16);

            for (var i=0; i<4; i++) {
              sample.push((amplitude/16) * volume);
            }
          }
        }

        // console.log(sample)
        const buffer = Tone.ToneAudioBuffer.fromArray(Float32Array.from(sample));
        if (this.player) {
          this.player.stop();
          this.player.dispose();
        }
        this.player = new Tone.Player(buffer).toDestination();
        this.player.start();
      }
    },
  }
</script>