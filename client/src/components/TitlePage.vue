<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <ul>
      <li v-for="items in required_age" v-bind:key="items">{{ items }}</li>
    </ul>

    <input v-model="inputValue"/>
    <button @click="getMinAge">Choose Minimum Age</button>
    <br>
    <input v-model="inputValueBeta"/>
    <button @click="getMaxAge">Choose Maximum Age</button>
   
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
      age_range: [],
      
      inputValue: ''
    }


  },
  methods: {
    getMinAge() {
      this.age_range.push(this.inputValue)

      /*
      axios.post('/age_var', { item: this.inputValue })
         
         .then(() => {
           axios.get('/applicants').then( res => this.required_age = res.data.items);
              
         })
      */
      this.inputValue = '';
    },

    getMaxAge() {
      this.age_range.push(this.inputValueBeta)
      axios.post('age_var', { item: this.age_range })
        .then(() => {
          axios.get('/applicants').then( res => this.required_age = res.data.items);
        })
      
      this.inputValue = '';
    },

  },
  
  mounted() {
    /*
     axios.get('/applicants')
      .then(res =>  this.applicants = res.data.inputValue)
    */
    }
  }

</script>


