<template>
    <div>
        <div id="header">
            <img id="logo" src="@/assets/wetBatlogo.png" alt="wetBatlogo">
            <span></span>
        </div>
    </div>
</template>

<script>
    export default {
        name:"page-header",

    }
</script>

<style lang="scss" scoped>
#header{
    display:grid;
    grid-template-rows:0.5fr 8fr;
    align-items: center;
    justify-items: center;
    top: 0;
    width:100%;
    background-color:#5F6CAF;
    #logo{
        height:10vh,
    }
}

</style>