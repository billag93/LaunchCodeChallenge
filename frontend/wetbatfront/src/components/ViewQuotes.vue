<template>
  <div>
    <div id="scroll">
        <!-- @click will un the function that calls the axios request -->
      <h1 id="click" @click="getQuotes">Click Here to get All the Quotes</h1>
      <!-- similar to getting the destinations and transportation we are sent back an array of quotes and access each inidivial quote object with the quote Id. -->
      <div id="myposts" v-for="quote in quotes" :key="quote.quoteId">
        <router-link :to="'/quote/' + quote.quoteId">
          <div>
            <p>Name: {{ quote.name }}</p>
            <p>Email: {{ quote.email }}</p>
            <p>Phone Number: {{ quote.phoneNumber }}</p>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "view-quotes",

  components: {},

  data() {
    return {
      quotes: [],
    };
  },

  methods: {
    getQuotes: function () {
      axios
        .request({
          url: "http://127.0.0.1:5000/api/quotes",
          method: "GET",
        })
        .then((response) => {
          console.log(response);
          this.quotes = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
#scroll{
overflow:scroll;
height: 75vh;
#click {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 1.2em;
  color: #5f6caf;
  align-items: center;
  justify-items: center;

  &:hover{
      cursor:pointer;
  }
}
#myposts {
  display: grid;
  align-items: center;
  justify-items: left;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 0.6em;
  color: #5f6caf;
  border: 2px solid #5bbfba;
  border-radius: 3%;
  margin: 2% 2%;
  padding: 3% 3%;
  background-color: white;

  a {
    text-decoration: none;
  }
}

}

</style>