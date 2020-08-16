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
    <ul>
      <li v-for="(game, key) in data" :key="key">{{ key }}</li>
    </ul>
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