<template>
  <div>
    <select 
      v-bind:value="value"
      v-on:input="$emit('input', $event.target.value)"
    >
      <option value="261.63">C4</option>
      <option value="440.00" selected>A4</option>
      <option value="523.25">C5</option>
      </select>
    <span>{{ value }}</span>
  </div>
</template>

<script>
  export default {
    props: ['value']
  }
</script>