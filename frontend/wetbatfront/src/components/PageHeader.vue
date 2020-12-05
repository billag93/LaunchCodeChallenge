<template>
  <div>
    <div id="header">
      <img id="logo" src="@/assets/wetBatlogo.png" alt="wetBatlogo" />
      <span></span>
      <input id="search" type="text" placeholder="Search.." />
      <!-- Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> -->
      <a class="fakelinks" href="#"><img src="@/assets/notification.svg" alt="notification" /></a>
      <!-- Icons made by <a href="https://www.flaticon.com/authors/becris" title="Becris">Becris</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> -->
      <a class="fakelinks" href="#"><img src="@/assets/chat.svg" alt="" /></a>
      <!-- Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> -->
      <a class="fakelinks" href="#"><img src="@/assets/settings.svg" alt="" /></a>
      <span></span>
    </div>
  </div>
</template>

<script>
export default {
  name: "page-header",
};
</script>

<style lang="scss" scoped>
#header {
  display: grid;
  grid-template-columns: 0.5fr 5fr 2fr 1fr 1fr 1fr 1fr;
  align-items: center;
  justify-items: center;
  top: 0px;
  width: 100%;
  background-color: #5f6caf;
  position: static;

  #search{
      height:4vh;
      width:20vw;
      border:1px solid grey;
      border-radius: 10%;
      margin: 1% 1%;
      padding: 2% 2%;
  }

  #logo {
    height: 10vh;
  }
  .fakelinks{
      height: 4vh;
      img{
          height:4vh;
      }
  }
}
</style>