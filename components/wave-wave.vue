<template>
  <div class="wave">
    <div class="left">
      <tt>{{ wave }}</tt>
    </div>
    <div>
      <button>Play</button>
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
  export default {
    props: ['wave_data', 'wave'],
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