<template>
    <div class="accepted">
    <p>Accepted</p>
    
    <ul>
      <li v-for="items in eligible_applicants" v-bind:key="items">{{ items }}</li>
    </ul>
    
    <ul>
      <li v-for="stats in statistics" v-bind:key="stats">{{ stats }}</li>
    </ul>
    
    
    <button v-on:click="displayData();">Display Accepted</button>
    
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'DisplayAccepted',
    
    data () {
        return {
            eligible_applicants: [],
            statistics: []
        }  
    },
    methods: {
        displayData() {
            axios.get('/accepted_applicants')
                    .then((resp) => {
                        this.eligible_applicants = resp.data.items;
        }),
            axios.get('/applicants_stats')
                .then((resp) => {
                    this.statistics = resp.data.stats;
    })


     }
     },
    
    
    mounted: function () {
        this.$nextTick(function () {
            this.displayData();
        })
    }
}

</script>
 
<style>
</style>