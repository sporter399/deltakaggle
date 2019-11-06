<template>
    <div class="accepted">
    <p>Accepted</p>
    <body onload="displayData();"></body>
    <ul>
      <li v-for="items in eligible_applicants" v-bind:key="items">{{ items }}</li>
    </ul>
    </div>
    
</template>

<script>
import axios from 'axios';

export default {
    name: 'DisplayAccepted',
    
    data () {
        return {
            eligible_applicants: []

        }
    },
        displayData() {
            axios.get('/accepted_applicants')
                .then((resp) => {
                    this.eligible_applicants = resp.data.items;
    })
    },
    mounted() {
   
    }
}
</script>


<style>
</style>