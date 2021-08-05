<template>
    <div class="hello">
        <div class="topnav">
            <a class="active" href="/">SkOpen</a>
            <a href="/resorts">Курорты</a>
            <a href="/login">Вход</a>
            <a href="/register">Регистрация</a>
        </div>
    <h1>Добро пожаловать на страницу Администратора.</h1>
    <h1>Список пользователей:</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Имя</th>
              <th scope="col">Почта</th>
              <th scope="col">Роль</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in users" :key="index">
              <td>{{ user.name }}</td>
              <td>{{ user.email }}</td>
              <td> {{ user.role }}</td>
              <td v-if="user.role =='user'">
                <button type="submit" @click="deleteUser(user.email)" class="btn btn-danger btn-sm">
                    Удалить
                </button>
              </td>
            </tr>
          </tbody>
        </table>
    <tr></tr>
    </div>
</template>

<script>
import axios from 'axios';
/* eslint-disable */
    export default {
        data () {
            return {
                users: []
            }
        },
        methods: {
          getUsers() {
            const path = 'http://localhost:5005/get_all_users';
            axios.get(path)
              .then((res) => {
                this.users = res.data;
              })
            .catch((error) => {
          // eslint-disable-next-line
                console.error(error);
            });
          },
          deleteUser(email) {
            this.$http.post('//localhost:5005/delete_user', {
            email: email,
          })
            this.$emit('userDeleted')
            this.$router.go()
          },
        },
        created() {
            this.getUsers();
        },
    }
    
</script>
<style scoped>
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
h1, h2 {
        font-weight: normal;
    }
ul {
        list-style-type: none;
        padding: 0;
    }
li {
        display: inline-block;
        margin: 0 10px;
    }
a {
        color: #42b983;
    }
</style>
