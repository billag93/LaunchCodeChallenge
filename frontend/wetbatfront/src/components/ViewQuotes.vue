<template>
  <div>
    <h1 id="click" @click="getQuotes">Click Here to get All the Quotes</h1>
    <div id="myposts" v-for="quote in quotes" :key="quote.quoteId">
      <router-link :to="'/quote/'+quote.quoteId">
        <div>
          <p>Name: {{ quote.name }}</p>
          <p>Email: {{ quote.email }}</p>
          <p>Phone Number: {{ quote.phoneNumber }}</p>
        </div>
      </router-link>
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
#click {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 1.2em;
  color: #5f6caf;
  align-items: center;
  justify-items: center;
}
#myposts {
  display: grid;
  align-items: center;
  justify-items: left;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 0.6em;
  color: #5f6caf;
  border: 4px solid #5bbfba;
  border-radius: 8%;
  margin: 2% 2%;
  padding: 3% 3%;
  .quote {
    border: 4px solid #5bbfba;
    border-radius: 8%;
  }
}
</style>