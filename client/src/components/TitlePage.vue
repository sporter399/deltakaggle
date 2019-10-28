<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    
    <ul>
      <li v-for="items in eligible_applicants" v-bind:key="items">{{ items }}</li>
    </ul>

    <input v-model="inputValue"/>
    <button @click="getMinAge">Choose Minimum Age</button>
    <br>
    <input v-model="inputValueBeta"/>
    <button @click="getMaxAge">Choose Maximum Age</button>
    <br>
    <input v-model="inputValueDelta"/>
    <button @click="getMinIncome">Choose Minimum Monthly Income</button>

   
  </div>
</template>

<script>
import axios from 'axios';


export default {
  name: "TitlePage",
  props: ['title'],
  data () {
    return {
      age_range: [],
      min_income: [],
      eligible_applicants: [],
      inputValue: '',
      inputValueBeta: '',
      inputValueDelta: ''
      
    }


  },
  methods: {
    getMinAge() {
      this.age_range.push(this.inputValue)
      this.inputValue = '';
    },

    getMaxAge() {
      this.age_range.push(this.inputValueBeta)
      this.inputValueBeta = '';
    },

    getMinIncome() {
      this.min_income.push(this.inputValueDelta)
       axios.post('user_vars', { age_item: this.age_range, income_item: this.min_income })
        .then(() => {
          axios.get('/applicants').then( res => this.eligible_applicants = res.data.items);
        })

      this.inputValueDelta = '';
    },

    
  },
  
  mounted() {
   
    }
  }

</script>


