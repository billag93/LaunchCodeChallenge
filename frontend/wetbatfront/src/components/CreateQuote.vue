<template>
  <div>
    <div id="createquote">
      <div>
        <h1>Create A Quote</h1>
      </div>
      <div>
          <h2>Enter Your Departure</h2>
        <input id="departure" class="quote" type="date" v-model="departure" />
      </div>
      <div>
          <h2>Enter Your Arrival</h2>
        <input id="arrival" class="quote" type="date" v-model="arrival" />
      </div>
      <div>
          <h2>Choose Your Destination</h2>
       <select  id="destination" class="quote" v-model="alldestinations">
         <!-- Here we are accessing our array using a for loop and identifying and individaul object using the destination Id -->
           <option v-for="destination in destinations" :key="destination.Id">
               {{destination.name}}
           </option>
       </select>
      </div>
      <div>
          How Many People Will be travelling
        <input id="travellers" class="quote" type="number" min="1" v-model="travellers"/>
      </div>
      <div>
          <h2>Choose Your transportation</h2>
       <select  id="destination" class="quote" v-model="alltransportations">
         <!-- Here we are accessing our array using a for loop and identifying and individaul object using the transportation Id -->
           <option v-for="transportation in transportations" :key="transportation.Id">
               {{transportation.name}}
           </option>
       </select>
      </div>
      <div>
          <h2>Enter Your First and Last Name</h2>
        <input id="name" class="quote" type="text" v-model="name" />
      </div>
      <div>
          <h2>Enter your email address</h2>
        <input id="email" class="quote" type="text" v-model="email" />
      </div>
      <div>
          <h2>Enter your phone number</h2>
        <input id="phoneNumber" class="quote" type="text" v-model="phonenumber" />
      </div>
      <div>
        <h2>Estimate</h2>
        <input id="finalprice" class="quote" type="number" v-model="finalprice">
      </div>
      <div class="button">
      <button @click="createQuote">Create Quote</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "create-quote",

  data() {
    return {
      departure: "",
      arrival:"",
      // all the airports are sent back in an array
      destinations: [],
      travellers: Number,
      // all the transportation compnaies are sent back in an array
      transportations:[],
      name:"",
      email:"",
      phonenumber:"",
      finalprice: Number,
      alltransportations:"",
      alldestinations:"",
    }
  },

   mounted:function() {
        this.getDestinations(),
        this.getTransportations()
        
        },
    // This is the axios request that will create a quote by communicating with flask and input it into our DB. 
    methods: {
        createQuote:function(){
            axios.request({
                url: "http://127.0.0.1:5000/api/quotes",
                method: "POST",
                headers: {
                "Content-Type": "application/json",
                },
                data:{
                    departure: this.departure,
                    arrival: this.arrival,
                    destination: this.alldestinations,
                    travellers: this.travellers,
                    transportation: this.alltransportations,
                    name: this.name,
                    email: this.email,
                    phonenumber: this.phonenumber,
                    finalprice: this.finalprice

                }
            }).then((response)=>{
                console.log(response)
            }).catch((error)=>{
                console.log(error)
            })
        },
      // Here we are communicating with flask to retrieve our airports from the Db
        getDestinations:function(){
            axios.request({
            url: "http://127.0.0.1:5000/api/airports",
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          })
          .then(response => {
            console.log(response);
           this.destinations = response.data
            
          })
          .catch(error => {
            console.log(error);
          });
        },
      // Here we are communicating with flask to retrieve our rental companies from the Db
        getTransportations:function(){
            return axios.request({
            url: "http://127.0.0.1:5000/api/transportation",
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          })
          .then(response => {
            console.log(response);
           this.transportations = response.data
            
          })
          .catch(error => {
            console.log(error);
          });
        }, 

    },

};
</script>

<style lang="scss" scoped>
#createquote{
    display:grid;
    align-items: center;
    justify-items: left;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size:0.6em;
    color: #5F6CAF;
    border: 2px solid #5BBFBA;
    border-radius:8%;
    margin:10% 10%;
    padding: 5% 5%;
    background-color: white;
    .quote{
    border: 1px solid #5BBFBA;
    border-radius:8%;
    }
    .button button{
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size:1.75em;
    background-color: #5BBFBA;
    text-decoration: none;
    color:white;
    }
    h1{
     margin-bottom: 10%;
    }
    h2{
      margin-top: 5%;
      margin-bottom: 5%;
    }
}
</style>