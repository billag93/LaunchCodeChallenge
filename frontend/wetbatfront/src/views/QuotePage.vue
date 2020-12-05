<template>
        <div id="quotepage">
        <div id="header">
        <page-header></page-header>
        </div>
        <div id="page">
        <create-quote></create-quote>
        <view-quotes></view-quotes>
        </div>
        </div>
</template>

<script>
import CreateQuote from '../components/CreateQuote.vue';
import PageHeader from '../components/PageHeader.vue';
import ViewQuotes from '../components/ViewQuotes.vue';
    export default {
  components: { CreateQuote, ViewQuotes, PageHeader, },
        name:"quote-page"
    }
    
</script>

<style lang="scss" scoped>
#quotepage{
display: grid;
align-items: center;
justify-items: center;
grid-template-columns: 1fr 3fr;

    #header{
        top:0px;
        position:static;
        height:100%;
    }
    #page{
        display:grid;
        grid-template-columns:1fr 1fr;
       
       
    }
}

</style>