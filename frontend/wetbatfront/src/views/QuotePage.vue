<template>
  <div id="quotepage">
    <div id="header">
      <page-header></page-header>
    </div>
    <div id="page">
      <div id="sidebar">
        <side-bar></side-bar>
      </div>
      <div id="thequotes">
          <div>
              <dash-board></dash-board>
          </div>
          <div id="splitquotes">
        <create-quote></create-quote>
        <view-quotes></view-quotes>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CreateQuote from "../components/CreateQuote.vue";
import DashBoard from '../components/DashBoard.vue';
import PageHeader from "../components/PageHeader.vue";
import SideBar from "../components/SideBar.vue";
import ViewQuotes from "../components/ViewQuotes.vue";
export default {
  components: { CreateQuote, ViewQuotes, PageHeader, SideBar, DashBoard },
  name: "quote-page",
};
</script>

<style lang="scss" scoped>
#quotepage {
  display: grid;


  #header {
    top: 0px;
    position: static;
    height: 100%;
  }
  #page {
    display: grid;
    grid-template-columns: 0.5fr 4fr;
    position: relative;
    left: 0px;
    #sidebar{
        position:sticky;
        left: 0px;
    }
    #thequotes{
        display: grid;
       
        #splitquotes{
            display: grid;
            grid-template-columns:1fr 1fr;
        }
    }
  }
}
</style>