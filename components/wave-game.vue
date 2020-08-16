<template>
  <div>
    <h3>game: {{ game }}</h3>
    <div>
      waves: {{ waves }}
    </div>
  </div>
</template>

<script>
  export default {
    props: ['game', 'waves'],
  }
</script>