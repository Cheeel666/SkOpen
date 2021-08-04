<template>
    <div class="hello">
        <div class="topnav">
            <a class="active" href="/">SkOpen</a>
            <a href="/resorts">Курорты</a>
            <a href="/login">Вход</a>
            <a href="/register">Регистрация</a>
        </div>
    <h1>Welcome to admin page</h1>
    <h2>{{msg}}</h2>
    </div>
</template>

<script>
/* eslint-disable */
    export default {
        data () {
            return {
                msg: 'The superheros'
            }
        }
    }
</script>
<style scoped>
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
