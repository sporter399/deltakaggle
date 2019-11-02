<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    
    <ul>
      <li v-for="items in eligible_applicants" v-bind:key="items">{{ items }}</li>
    </ul>
    <input v-model="inputMinAgeValue"/>
    <button @click="getMinAge">Choose Minimum Age</button>
    <br>
    <input v-model="inputMaxAgeValue"/>
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
    getMinAge() {
      this.age_range.push(this.inputMinAgeValue)
      this.inputMinAgeValue= '';
      
      
    },

    getMaxAge() {
      this.age_range.push(this.inputMaxAgeValue)
      axios.post('user_vars', { age_item: this.age_range })
        .then(() => {
          axios.get('/applicants').then( res => this.eligible_applicants = res.data.items);
        })
      this.inputMaxAgeValue = '';
      
    },
  },
  
  mounted() {
   
    }
  }

</script>


