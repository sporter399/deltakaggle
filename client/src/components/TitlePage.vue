<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <ul>
      <li v-for="animal in array"> {{ animal }}</li>
    </ul>
    <input v-model="inputValue"/>
    <button @click="handleAddTodoClick">Add New Animal</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "TitlePage",
  props: ['title'],
  data () {
    return {
      array: ['a', 'b', 'c'],
      inputValue: ''
    }


  },
  methods: {
    handleAddTodoClick() {
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


