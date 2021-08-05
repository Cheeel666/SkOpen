<template>
  <div class="container">
    <div class="topnav">
            <a class="active" href="/">SkOpen</a>
            <a href="/resorts">Курорты</a>
            <a href="/login">Вход</a>
            <a href="/register">Регистрация</a>
    </div>
    <div class="row">
      <div class="col-sm-10">
        <h1>Курорты</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Курорт</th>
              <th scope="col"></th>
              <th scope="col"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(courort, index) in courorts" :key="index">
              <router-link :to="'/resorts/' + courort.name_courort">
              <td>{{ courort.name_courort }}</td>
              <td>{{ courort.city }}</td>
              <td>
                <button type="button" class="btn btn-warning btn-sm">Смотреть</button>
              </td>
              </router-link>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      courorts: [],
    };
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5005/get_courorts';
      axios.get(path)
        .then((res) => {
          this.courorts = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>

<style>
   .topnav {
  background-color: #333;
  overflow: hidden;
}

/* Style the links inside the navigation bar */
.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Add a color to the active/current link */
.topnav a.active {
  background-color: #04AA6D;
  color: white;
}
</style>
