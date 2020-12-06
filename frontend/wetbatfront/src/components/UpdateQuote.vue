<template>
  <div>
    <div id="updatequote">
      <!-- Updating the quote is very similar to creating a quote -->
      <button @click="updateGrid = !updateGrid">Update</button>
      <div v-if="updateGrid">
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
          <select id="destination" class="quote" v-model="alldestinations">
            <option v-for="destination in destinations" :key="destination.Id">
              {{ destination.name }}
            </option>
          </select>
        </div>
        <div>
          How Many People Will be travelling
          <input min="1"
            id="travellers"
            class="quote"
            type="number"
            v-model="travellers"
          />
        </div>
        <div>
          <h2>Choose Your transportation</h2>
          <select id="transportation" class="quote" v-model="alltransportations">
            <option
              v-for="transportation in transportations"
              :key="transportation.Id"
            >
              {{ transportation.name}}
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
          <input
            id="phoneNumber"
            class="quote"
            type="text"
            v-model="phonenumber"
          />
        </div>
        <div>
          <h2>Estimate</h2>
          <input
            id="finalprice"
            class="quote"
            type="number"
            v-model="finalprice"
          />
        </div>
        <div>
          <button @click="updateQuote">Update This Quote</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "create-quote",

  data() {
    return {
      departure: "",
      arrival: "",
      destinations: [],
      travellers: Number,
      transportations: [],
      name: "",
      email: "",
      phonenumber: "",
      finalprice: Number,
      updateGrid: false,
      alldestinations:"",
      alltransportations:"",

    };
  },
  props: {
    quoteId: {
      type: Number,
      required: true,
    },
  },

  mounted: function () {
    this.getDestinations(), this.getTransportations();
  },

  methods: {
    updateQuote: function () {
      axios
        .request({
          url: "http://wetbat.ml/api/quotes",
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
          },
          data: {
            departure: this.departure,
            arrival: this.arrival,
            destination: this.alldestinations,
            travellers: this.travellers,
            name: this.name,
            email: this.email,
            phonenumber: this.phonenumber,
            finalprice: this.finalprice,
            quoteId: this.quoteId,
            transportation: this.alltransportations,
          },
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getDestinations: function () {
      axios
        .request({
          url: "http://wetbat.ml/api/airports",
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          console.log(response);
          this.destinations = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getTransportations: function () {
      return axios
        .request({
          url: "http://wetbat.ml/api/transportation",
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          console.log(response);
          this.transportations = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
#updatequote{
    display:grid;
    align-items: center;
    justify-items: left;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size:0.65em;
    color: #5F6CAF;
    border-radius:8%;
    margin:2% 2%;
    padding: 3% 3%;
    
    button{
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size:1.75em;
    background-color: #5BBFBA;
    text-decoration: none;
    color:white;
    cursor: pointer;
    }
}
</style>