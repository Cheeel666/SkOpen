<template>
    <div class="hello">
    <div class="topnav">
            <a class="active" href="/">SkOpen</a>
            <a href="/resorts">Курорты</a>
            <a href="/login">Вход</a>
            <a href="/register">Регистрация</a>
    </div>
        <h1>Добро пожаловать в профиль!</h1>
        <h2>{{msg}}</h2>
        <h3>admin: {{admin}}</h3>
        <button type="submit" @click="handleSubmit">
            Выход
        </button>
            <div v-if="admin=='true'">
                <button type="submit" @click="adminPage">
                    admin
                </button>
            </div>
    </div>
</template>

<script>
/* eslint-disable */
export default {
    data () {
        return {
            msg: 'Имя пользователя: ' + localStorage.getItem('user'),
            admin: localStorage.getItem('admin'),
            token: localStorage.getItem('jwt')
        }
    },
    methods: {
        handleSubmit(e) {
        e.preventDefault();
        localStorage.removeItem('jwt');
        localStorage.removeItem('user');
        this.$emit('loggedOut')
        this.$router.push('/login');
        },
        adminPage(e) {
            e.preventDefault();
            this.$router.push('/admin');
        },
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
