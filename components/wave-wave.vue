<template>
  <div class="wave">
    <div class="left">
      <tt>{{ wave }}</tt>
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
        var sample = [];
        for (var n=0; n<32; n++) {
          var amplitude = parseInt(this.wave[n], 16);
          for (var i=0; i<4; i++) {
            sample.push(amplitude/16);
          }
        }
        for (var i=0; i<10; i++) {
          sample = sample.concat(sample);
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