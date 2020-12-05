<template>
  <div>
    <div>
      <div id="mobile-header">
        <div id="mobile-header-logo">
          <img src="@/assets/wetBatlogo.png" alt="profile picture" />
        </div>
        <div id="mobile-header-space"></div>
        <div id="mobile-hamburger-menu">
          <div @click="IsOpen = !IsOpen" id="hamburger_icon">
            <img src="@/assets/square.svg" alt="" />
            <!-- Icons made by <a href="https://icon54.com/" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a> -->
          </div>
          <div :class="{'mobileheadermenuopen':IsOpen,'mobileheadermenuclosed':true}" id="mobile-header-menu">
            <img src="@/assets/wetBatlogo.png" alt="Wetbat picture" />
            <router-link class="menu-links" to="/">Home</router-link>
            <router-link class="menu-links" to="/about">quotes</router-link>
          </div>
        </div>
      </div>
      <div id="header">
        <img src="@/assets/wetBatlogo.png" alt="profile picture" />
        <router-link to="/">Home</router-link>
        <router-link to="/about">Quotes</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "profile-header",
  data() {
    return {
      IsOpen:false,
    }
  },
  methods: {
    
  },
};


</script>

<style lang="scss" scoped>
#header {
  display: none;
}
#mobile-header {
  display: grid;
  grid-template-columns: 2fr 4fr 2fr;
  align-items: center;
  justify-items: center;
  min-height: 10vh;
  background: #5F6CAF;
  position: sticky;
  top: 0;
  #mobile-header-logo {
    img {
      height: 70px;
    }
  }

  #mobile-hamburger-menu {
    display: grid;
    justify-items: center;
    align-items: center;
    #hamburger_icon {
      img {
        width: 100%;
        height: 50px;
        z-index: 1;
        position: relative;
      }
    }
    .mobileheadermenuclosed{
      top: -40vh;
      opacity: 0;
      transition: all 0.3s ease-in-out;
    }
    .mobileheadermenuopen{
      top: 0;
      opacity: 1;
      transition: all 0.3s ease-in-out;
    }

    #mobile-header-menu {
      position: absolute;
      width: 100%;
      background: #5F6CAF;
      display: grid;
      justify-items: center;
      align-items: center;
      left: 0;
      min-height: 40vh;
      font-family: "Racing Sans One", cursive;
      img {
        width: 60px;
      }
      .menu-links {
        color: white;
        text-decoration: none;
        font-weight: bold;
        border: 2px solid white;
        border-radius: 10%;
        background: black;
        padding: 1% 1%;
        margin: 1% 1%;
      }

      //   I will format this later once the menu actually works
    }
  }
}
</style>