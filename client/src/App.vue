<template>
  <div id="app">
    <!--<img alt="Vue logo" src="./assets/logo.png">-->
    <div>
      <button @click="handleNavClick">{{buttonText}}</button>
    </div>
    <Welcome v-if="!showInputFields" />
    <UserVars v-if="showInputFields" @dataEntered='dataEntered' title="Delta Bank Credit Applications"/>
    <DisplayAccepted v-if="allDataEntered" />
    
  </div>
</template>

<script>

import UserVars from './components/UserVars.vue'
import Welcome from './components/Welcome.vue'
import DisplayAccepted from './components/DisplayAccepted.vue'



export default {
  name: 'app',
  components: {
    UserVars,
    Welcome,
    DisplayAccepted
    
  },

  data() {
    return {
      showInputFields: false,
      allDataEntered: false,
      buttonText: "Show Fields for Input of Variables",
      fromUserVars: '',
      eligible_applicants: [],

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
    },
     dataEntered (value) {
     this.allDataEntered = value
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

</style>
