<template>
    <div class="accepted">
    <p>Accepted</p>
    
    <ul>
      <li v-for="items in eligible_applicants" v-bind:key="items">{{ items }}</li>
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
            
        }  
    },
    methods: {
        displayData() {
            axios.get('/accepted_applicants')
                .then((resp) => {
                    this.eligible_applicants = resp.data.items;
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