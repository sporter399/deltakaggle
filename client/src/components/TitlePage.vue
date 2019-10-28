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
    <br>
    <input v-model="inputMinIncomeValue"/>
    <button @click="getMinIncome">Choose Minimum Monthly Income</button>
    <br>
    <input v-model="inputMaxUtilValue"/>
    <button @click="getMaxRevolving">Choose Maximum Utilization of Credit</button>
    <br>
    <input v-model="inputThirtySixtyValue"/>
    <button @click="getThirtySixty">Choose Maximum Number of Thirty to Sixty Days Past Due</button>
    <br>
    <input v-model="inputDebtRatioValue"/>
    <button @click="getMaxDebtRatio">Choose Maximum Debt Ratio</button>
    <br>
    <input v-model="inputMinLinesValue"/>
    <button @click="getMinLines">Choose Minimum Number of Open Credit Lines</button>


   
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

      eligible_applicants: [],
      
      inputMinAgeValue: '',
      inputMaxAgeValue: '',
      inputMinIncomeValue: '',
      inputMaxUtilValue: '',
      inputThirtySixtyValue: '',
      inputDebtRatioValue: '',
      inputMinLinesValue: '',

      
    }


  },
  methods: {
    getMinAge() {
      this.age_range.push(this.inputMinAgeValue)
      this.inputMinAgeValue = '';
    },

    getMaxAge() {
      this.age_range.push(this.inputMaxAgeValue)
      this.inputMaxAgeValue = '';
    },

    getMinIncome() {
      this.min_income.push(this.inputMinIncomeValue)
      this.inputMinIncomeValue = '';
    },

    getMaxRevolving() {
      this.max_revolving.push(this.inputMaxUtilValue)
      this.inputMaxUtilValue = '';
    },

    getThirtySixty() {
      this.max_thirtysixty.push(this.inputDebtRatioValue)
      this.inputThirtySixtyValue = '';
    },

    getMaxDebtRatio() {
      this.max_debtratio.push(this.inputDebtRatioValue)
      this.inputDebtRatioValue = '';
    },

    getMinLines() {
      this.min_openlines.push(this.inputMinLinesValue)
       axios.post('user_vars', { age_item: this.age_range, income_item: this.min_income, revolving_item: this.max_revolving, 
                                lessthansixty_item: this.max_thirtysixty, debtratio_item: this.max_debtratio, minlines_item: this.min_openlines })
        .then(() => {
          axios.get('/applicants').then( res => this.eligible_applicants = res.data.items);
        })

      this.inputMinLinesValue = '';
    },








  },
  
  mounted() {
   
    }
  }

</script>


