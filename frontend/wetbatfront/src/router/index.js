import Vue from "vue";
import VueRouter from "vue-router";
import QuotePage from "../views/QuotePage.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "quotepage",
    component: QuotePage
  },
  
];

const router = new VueRouter({
  routes
});

export default router;
