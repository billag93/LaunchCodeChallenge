<template>
    <div>
        <div id="side_bar">
            <!-- Icons made by <a href="https://www.flaticon.com/authors/dave-gandy" title="Dave Gandy">Dave Gandy</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> -->
            <a class="fakelinks" href="#"><img src="@/assets/home.svg" alt="notification" />Home</a>
            <!--Icons made by <a href="https://www.flaticon.com/authors/gregor-cresnar" title="Gregor Cresnar">Gregor Cresnar</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> -->
            <a class="fakelinks" href="#"><img src="@/assets/dollar.svg" alt="dollar sign" />Quotes</a>
            <!-- Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> -->
            <a class="fakelinks" href="#"><img src="@/assets/bullet-list.svg" alt="bullet list" />Leads</a>
            <!-- Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> -->
            <a class="fakelinks" href="#"><img src="@/assets/send.svg" alt="airplane" />Tours</a>
            <!-- Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>-->
            <a class="fakelinks" href="#"><img src="@/assets/financial.svg" alt="financial" />Invoice</a>
            <!-- Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> -->
            <a class="fakelinks" href="#"><img src="@/assets/analytics.svg" alt="analytics" />Analytics</a>
            <!-- Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> -->
            <a class="fakelinks" href="#"><img src="@/assets/group.svg" alt="group" />Group</a>
            <!-- Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> -->
            <a class="fakelinks" href="#"><img src="@/assets/gear.svg" alt="gear" />Admin</a>
            <!-- Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>-->
            <a class="fakelinks" href="#"><img src="@/assets/headset.svg" alt="headset" />Support</a>
        </div>
    </div>
</template>

<script>
    export default {
        name: "side-bar",

    }
</script>

<style lang="scss" scoped>
#side_bar{
    display:grid;
    justify-items: center;
    align-items: center;
    background-color: rgb(199, 198, 198);
    color: #5F6CAF;
    .fakelinks{
        display: grid;
        align-items: left;
        justify-items: left;
        grid-template-columns:1fr 1fr;
        row-gap:15%;
        column-gap: 8%;
        color:#5F6CAF;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        margin: 5% 5%;
        padding: 8% 8%;
    }
    a{
        text-decoration: none;
    }
    img{
        height:4vh;
        width:auto;
    }
}
</style>