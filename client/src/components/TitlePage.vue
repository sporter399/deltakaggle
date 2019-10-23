<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <ul>
      <li v-for="animal in array" v-bind:key="animal"> {{ animal }}</li>
    </ul>
    <ul>
      <li v-for="applicant in fetched_info" v-bind:key="applicant"> {{ applicant }}</li>
    </ul>
    <input v-model="inputValue"/>
    <button @click="userSelectsAgeClick">Choose Minimum Age</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "TitlePage",
  props: ['title'],
  data () {
    return {
      sql_age: [1, 2, 3],
      array: ['a', 'b', 'c'],
      inputValue: ''
    }


  },
  methods: {
    userSelectsAgeClick() {
      axios.post('/todo', { item: this.inputValue } )
        .then(() => {
          axios.get('/array').then( res => this.array = res.data.animals);
        })
      this.inputValue = '';
    }
  },
  mounted() {
    axios.get('/array').then( res => this.array = res.data.animals);
      
     

  }
}

</script>


