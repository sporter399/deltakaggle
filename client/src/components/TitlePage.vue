<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <ul>
      <li v-for="applicant in fetched_info" v-bind:key="applicant"> {{ applicant }}</li>
    </ul>
    <input v-model="inputValue"/>
    <button @click="userSelectsAgeClick">Choose Minimum Age</button>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  name: "TitlePage",
  props: ['title'],
  data () {
    return {
      vars: [1, 2, 3],
      array: ['a', 'b', 'c'],
      fetched_info: [4, 5, 6],
      inputValue: ''
    }


  },
  methods: {
    userSelectsAgeClick() {
      
      
      axios.post('/uservar', { item: this.inputValue } )
         .then(() => {
          axios.get('/fetched_info').then( res => this.fetched_info = res.data.items);
        })
      this.inputValue = '';
      
    }
  },
  
  mounted() {
    
  
     

  }
}

</script>


