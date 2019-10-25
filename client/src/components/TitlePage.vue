<template>
  <div class="hello">
    <h1>{{ title }}</h1>

    <!--
    <ul>
      <li v-for="applicant in fetched_info" v-bind:key="applicant"> {{ applicant }}</li>
    </ul>
    !-->
    
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
      axios.get('/age_var')
      
         .then(res =>  {
           this.requiredAge = res.data.inputValue;
           
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


