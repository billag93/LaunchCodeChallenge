<template>
    <div>
        <button @click="DeleteQuote">Delete</button>
    </div>
</template>

<script>
import axios from "axios"
    export default {
        name:"delete-quote",
       
        props: {
            quoteId: {
                type: Number,
                required: true, 
            },
        },
        methods: {
            // This axios request will delete a quote with the Id being passed down using props from the single quote component
            DeleteQuote: function(){
                axios.request({
                    url: "http://wetbat.ml/api/quotes",
                    method: "DELETE",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    data:{
                        quoteId: this.quoteId
                    },

                }).then((response) => {
                    console.log(response)
                }).catch((error) => {
                    console.log(error)
                })
            }
        },
    }
</script>

<style lang="scss" scoped>
button{
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size:1.2em;
    background-color: #5BBFBA;
    text-decoration: none;
    color:white;
    padding: 2% 2%;
    margin: 1% 1%;
    cursor: pointer;
}

</style>