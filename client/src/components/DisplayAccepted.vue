<template>
  <div class="accepted">
    <p>Accepted</p>
    <ul id="horizontal-list">
      
      <li v-for="(item, index) in data.items" v-bind:key="index">{{ item }}</li>
    </ul>
    <ul>
      <p>Eligible Applicants Statistics</p>
      <li v-for="(stat, index) in data.stats" v-bind:key="index">{{ stat }}</li>
    </ul>
    <button v-on:click="displayData();">Display Accepted</button>
  </div>
</template>

<script>
export default {
  name: 'DisplayAccepted',
  props: [
    'data'
  ],
}
</script>

<style>

.accepted {
    display: accepted;
    margin: 0 auto;
}

ul#horizontal-list {
  list-style-type: none;
  
}
ul#horizontal-list li{
  float: left;
  
  
}
ul#horizontal-list li:after {
  content: ", ";
  
  
}
</style>