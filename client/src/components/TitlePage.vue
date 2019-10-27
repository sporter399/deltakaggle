<template>
  <div class="hello">
    <h1>{{ title }}</h1>

    <input v-model="inputValue"/>
    <button @click="getAge">Choose Minimum Age</button>
    <ul>
      <li v-for="items in required_age" v-bind:key="items">{{ items }}</li>
    </ul>
    <ul>
      <li v-for="test in applicants" v-bind:key="test"> {{ test }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  name: "TitlePage",
  props: ['title'],
  data () {
    return {
      required_age: [48, 22, 41],
      applicants: ['a', 'b', 'c'],
      inputValue: ''
    }


  },
  methods: {
    getAge() {
      axios.post('/age_var', { item: this.inputValue })
      this.required_age.push(item.item)
         .then(() =>  {
           axios.get('/applicants').then( res => this.required_age = res.data.items);
           
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


