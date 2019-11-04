<template>
  <div id="app">
    <!--<img alt="Vue logo" src="./assets/logo.png">-->
    <TitlePage title="Delta Bank Credit Applications"/>
  </div>
</template>

<script>
import TitlePage from './components/TitlePage.vue'

export default {
  name: 'app',
  components: {
    TitlePage
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
