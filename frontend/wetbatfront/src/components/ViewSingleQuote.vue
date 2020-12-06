<template>
  <div>
    <div v-if="isitready" id="myposts">
      <p>Departure: {{quote.departure}}</p>
      <p>Arrival: {{quote.arrival}}</p>
      <p>Destination: {{quote.destination}}</p>
      <p>Number of Travellers:{{quote.travellers}}</p>
      <p>Rental Company: {{quote.transportation}}</p>
      <p>Name: {{quote.name}}</p>
      <p>Email: {{quote.email}}</p>
      <p>Phone Number: {{quote.phoneNumber}}</p>
      <p>Cost: {{quote.finalprice}}</p>
      <update-quote :quoteId="quote.quoteId" ></update-quote>
      <delete-quote :quoteId="quote.quoteId" ></delete-quote>
    </div>
    <div v-else>
        <h2>Loading</h2>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import DeleteQuote from './DeleteQuote.vue'
import UpdateQuote from './UpdateQuote.vue'
    export default {
        name: "view-quotes",

        components: {
                UpdateQuote,
                DeleteQuote     
        },

        data() {
            return {
                quote: {},
                isitready:false,
            }
        },
        mounted:function() {
            this.getQuotes()
        },

        methods: {
            getQuotes:function() {
                axios.request({
                    url:"http://wetbat.ml/api/quotes",
                    method:"GET",
                    params:{
                        quoteId:this.$route.params.id
                    }
                }).then((response)=>{
                    console.log(response)
                    this.quote = response.data[0]
                    this.isitready = true
                }).catch((error)=>{
                    console.log(error)
                })
            }
        },
    }
</script>

<style lang="scss" scoped>
#click{
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size:1.2em;
    color: #5F6CAF;
    align-items: center;
    justify-items: center;
}
#myposts{
    display:grid;
    align-items: center;
    justify-items: left;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size:1.2em;
    color: #5F6CAF;
    border: 2px solid #5BBFBA;
    border-radius:2%;
    margin:10% 10%;
    padding: 3% 3%;
    background-color: white;
    width:50%;
    p{
        margin:2% 2%;
        
    }
    
}

</style>