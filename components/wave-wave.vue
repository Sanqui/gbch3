<template>
  <div class="wave">
    <div class="left">
      <svg viewBox="0 0 1 1" preserveAspectRatio="none">
        <polygon :points="wavePoints" />
      </svg>
      <tt ref="code">{{ wave }}</tt>
      <!-- TODO copy as ascii button -->
    </div>
    <div>
      <button v-on:click="$emit('play-sample', wave)">Play</button>
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
    computed: {
      wavePoints() {
        var points = []
        points.push("0,1")
        for (var n = 0; n < 32; n++) {
          var amplitude = parseInt(this.wave[n], 16);
          var point = { x: (n) / 32.0, y: 1.0 - amplitude / 16.0 };
          points.push(point.x + "," + point.y)
          points.push((n+1) / 32.0 + "," + point.y)
        }
        points.push("1,1")
        return points.join(" ");
      }
    },
  }
</script>

<style lang="scss" scoped>
  .wave {
    display: flex;
    border: 1px solid #999;
    padding: 4px;
    margin: 4px;
    
    .left {
      font-size: 150%;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 4px;

      svg {
        display: block;
        width: 100%;
        height: 128px;
        flex-grow: -1;
        flex-shrink: 10;

        polygon {
          fill: rgba(#0000ff, 0.5);
        }
      }

      tt {
        display: block;
      }
    }
    
    > div {
      margin: 2px 12px;
    }

    button {
      height: 100%;
    }
  }
</style>