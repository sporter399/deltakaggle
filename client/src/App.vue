<template>
  <div id="app">
    <!--<img alt="Vue logo" src="./assets/logo.png">-->
    <div>
      <button @click="handleNavClick">{{buttonText}}</button>
    </div>
    <Eligible v-if="!showInputFields" />
    <TitlePage v-if="showInputFields" title="Delta Bank Credit Applications"/>
    
  </div>
</template>

<script>
import TitlePage from './components/TitlePage.vue'
import Eligible from './components/Eligible.vue'


export default {
  name: 'app',
  components: {
    TitlePage,
    Eligible
  },

  data() {
    return {
      showInputFields: false,
      buttonText: "Show Fields for Input of Variables"

    }
  },


methods: {  
   handleNavClick() {
      this.showInputFields = !this.showInputFields;
      if (this.buttonText ===  'Show Fields for Input of Variables') {
        this.buttonText = 'Show Welcome Screen'
      } else {
        this.buttonText =  'Show Fields for Input of Variables'
      }
    }
 
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
.nav-bar-elem {
  margin: 0 10px;
}
</style>
