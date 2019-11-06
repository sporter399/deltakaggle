<template>
  <div id="app">
    <!--<img alt="Vue logo" src="./assets/logo.png">-->
    <div>
      <button @click="handleNavClick">{{buttonText}}</button>
    </div>
    <Welcome v-if="!showInputFields" />
    <UserVars v-if="showInputFields" @dataEntered='dataEntered' title="Delta Bank Credit Applications"/>
    





    <DisplayAccepted v-if="allDataEntered" />


      <!--  That parent reference in the your word document is reference to a state, that
      state I think can be referenced above to accdss DisplayAccepted. The child has to tell
      the parent that the state has changed. UserVars has to tell App of change of state.
      Don't forget that display of data, the axios get request, should going forward take place
      in Display Accepted and not in UserVars. UserVars should post and post only. -->
    
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
.nav-bar-elem {
  margin: 0 10px;
}
</style>
