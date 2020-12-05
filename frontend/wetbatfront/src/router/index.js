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
  {
    path: "/quote/:id",
    name: "ViewSingleQuote",
    component: () => import("../views/SingleQuote.vue"),
  },
  
];

const router = new VueRouter({
  routes
});

export default router;
