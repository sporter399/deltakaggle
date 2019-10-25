<template>
  <div class="hello">
    <h1>{{ title }}</h1>

    <input v-model="inputValue"/>
    <button @click="getAge">Choose Minimum Age</button>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  name: "TitlePage",
  props: ['title'],
  data () {
    return {
      required_age: [],
      applicants: ['a', 'b', 'c'],
      inputValue: ''
    }


  },
  methods: {
    getAge() {
      axios.post('/age_var', { item: this.inputValue })
      
         .then(() =>  {
           axios.get('/applicants').then( res => this.applicants = res.data.items);
           
         })
      
      this.inputValue = '';
    }
  },
  
  mounted() {
     axios.get('/applicants')
      .then(res =>  this.applicants = res.data.inputValue)
  
    }
  }

</script>


