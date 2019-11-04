<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    
    <ul>
      <li v-for="items in eligible_applicants" v-bind:key="items">{{ items }}</li>
    </ul>
    <input v-model="inputMinAgeValue"/><label for="inputMinAgeValue"> Enter Minimum Age</label>
    <br>
    <input v-model="inputMaxAgeValue"/><label for="inputMaxAgeValue"> Enter Maximum Age</label>
    <br>
    <input v-model="inputMinIncomeValue"/><label for="inputMinIncomeValue"> Enter Minimum Monthly Income</label>
    <br>
    
    
    
    
    
    
    
    
    
    
    
    
    
    <button @click="displayAccepted">Display Accepted Applicants</button>
    


   
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
      max_revolving: [],
      max_thirtysixty: [],
      max_debtratio: [],
      min_openlines: [],
      max_ninety: [],
      min_realestate: [],
      max_sixtyninety: [],
      max_dependents: [],

      eligible_applicants: [],
      
      inputMinAgeValue: '',
      inputMaxAgeValue: '',
      inputMinIncomeValue: '',
      inputMaxUtilValue: '',
      inputThirtySixtyValue: '',
      inputDebtRatioValue: '',
      inputMinLinesValue: '',
      inputOverNinetyValue: '',
      inputMinRealEstateValue: '',
      inputMaxSixtyNinetyValue: '',
      inputMaxDependentsValue: '',

      
    }


  },
  methods: {
    displayAccepted() {
      this.age_range.push(this.inputMinAgeValue)
      this.age_range.push(this.inputMaxAgeValue)
      this.min_income.push(this.inputMinIncomeValue)
      axios.post('user_vars', { age_item: this.age_range, income_item: this.min_income })
      .then(() => {
        axios.get('/applicants').then( res => this.eligible_applicants = res.data.items);
        })
      
     
    },
  },
  
  mounted() {
   
    }
  }

</script>


