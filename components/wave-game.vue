<template>
  <div>
    <h3 v-on:click="expand()">
      game: {{ game }}
    </h3>
    <div class="waves" v-if="expanded">
      <wave-wave v-for="(wave_data, wave) in game_data.waves" :key="wave"
        v-on="$listeners" :wave_data="wave_data" :wave="wave" />
    </div>
  </div>
</template>

<script>
  export default {
    props: ['game', 'game_data'],
    data() {
      return {
        expanded: false
      }
    },
    methods: {
      expand() {
        this.expanded = !this.expanded;
      }
    }
  }
</script>


<style lang="scss" scoped>
  h3 {
    color: #228;
    cursor: pointer;

    &:hover {
      color: #44b;
    }
  }

  .waves {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
  }

  .waves > div {
    
  }
</style>