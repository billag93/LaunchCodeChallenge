<template>
  <div>
    <div id="dashboard">
      <div id="writing">
        <h1>Welcome To The Dashboard</h1>
        <p>
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Non hic
          magni eos commodi amet qui quam quis aperiam dicta labore, sequi eaque
          deserunt tenetur minima eius beatae explicabo consectetur assumenda!
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Non hic
          magni eos commodi amet qui quam quis aperiam dicta labore, sequi eaque
          deserunt tenetur minima eius beatae explicabo consectetur assumenda!
        </p>
      </div>
      <div id="images">
          <div id="teamwork">
              <!-- <a href='https://www.freepik.com/vectors/banner'>Banner vector created by katemangostar - www.freepik.com</a> -->
              <img src="@/assets/team.jpg" alt="team work">
          </div>
            <div id="thenumbers">
                <div class="leads">
                    <h2>101</h2>
                    <h2>NEW LEADS</h2>
                </div>
                <div class="leads">
                    <h2>35</h2>
                    <h2>Quotes Created</h2>
                </div>
                <div class="leads">
                    <h2>40</h2>
                    <h2>Pending Orders</h2>
                </div>
            </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: "page-dashboard"
};
</script>

<style lang="scss" scoped>
#dashboard{
    display: grid;
    grid-template-columns: 1fr 2fr;
    row-gap:5%;
    align-items: center;
    justify-items: center;
    margin: 3% 3%;
    padding: 2% 2%;
    border: 1px solid white;
    border-radius:5%;
    background-image: linear-gradient(#5BBFBA, rgb(9, 92, 201));
    #writing{
        display: grid;
        grid-template-rows: 1fr 1fr;
        row-gap: 5%;
        padding: 2% 2%;
        margin: 2% 2%;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        color: white;
    }
    #images{
        display: grid;
        align-items: center;
        justify-items: center;
        grid-template-rows: 3fr 1fr;
        #teamwork{
            img{
                width: 100%;
                border: 1px solid white;
                border-radius: 8%;
            }
        }
        #thenumbers{
            display: grid;
            align-items: center;
            justify-items: center;
            grid-template-columns: 1fr 1fr 1fr;
            .leads{
            display: grid;
            align-items: center;
            justify-items: center;
            grid-template-rows: 1fr 1fr;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            }
        }
    }
}
</style>