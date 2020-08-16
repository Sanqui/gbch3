<template>
  <div class="wave">
    <div class="left">
      <tt>{{ wave }}</tt>
      <!-- TODO copy as ascii button -->
    </div>
    <div>
      <button @click="play">Play</button>
    </div>
    <div>
      <dl>
        <dt>ticks:</dt>
          <dd>{{ wave_data.ticks }}</dd>
        <dt>songs:</dt>
          <dd>{{ wave_data.songs }}</dd>
      </dl>
    </div>
  </div>
</template>

<script>
  import * as Tone from 'tone';

  export default {
    props: ['wave_data', 'wave'],
    methods: {
      play: function() {
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
            var amplitude = parseInt(this.wave[n], 16);

            for (var i=0; i<4; i++) {
              sample.push((amplitude/16) * volume);
            }
          }
        }

        console.log(sample)
        const buffer = Tone.ToneAudioBuffer.fromArray(Float32Array.from(sample));

        const player = new Tone.Player(buffer).toDestination();
        player.start();
      }
    }
  }
</script>

<style scoped>
  .wave {
    display: flex;
    border: 1px solid #999;
    padding: 4px;
    margin: 4px;
  }
  
  .wave .left {
    font-size: 150%;
    margin: auto 12px;
  }
  .wave > div {
    margin: 2px 12px;
  }
  .wave button {
    height: 100%;
  }
</style>