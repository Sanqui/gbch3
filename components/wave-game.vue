<template>
  <div>
    <h3>game: {{ game }}</h3>
    <div v-for="(wave_data, wave) in game_data.waves" :key="wave">
      <wave-wave v-on="$listeners" :wave_data="wave_data" :wave="wave" />
    </div>
  </div>
</template>

<script>
  export default {
    props: ['game', 'game_data'],
  }
</script>