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
      <wave-game :game="key" :game_data="game_data" />
    </div>
  </main>
</template>

<script>
  import data from '~/data/data.json'

  export default {
    asyncData () {
      return { data: data }
    }
  }
</script>