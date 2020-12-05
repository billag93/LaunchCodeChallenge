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
            DeleteQuote: function(){
                axios.request({
                    url: "http://127.0.0.1:5000/api/quotes",
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

</style>