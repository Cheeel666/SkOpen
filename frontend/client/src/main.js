import Axios from 'axios';
import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import App from './App';
import router from './router';


Vue.prototype.$http = Axios;

Vue.config.productionTip = false;


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
