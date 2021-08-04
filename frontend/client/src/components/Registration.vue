<template>
    <div>
        <div class="topnav">
            <a class="active" href="/">SkOpen</a>
            <a href="/resorts">Курорты</a>
            <a href="/login">Вход</a>
            <a href="/register">Регистрация</a>
        </div>
        <h4>Register</h4>
        <form>
            <label for="name">Name</label>
            <div>
                <input id="name" type="text" v-model="name" required autofocus>
            </div>

            <label for="email" >E-Mail Address</label>
            <div>
                <input id="email" type="email" v-model="email" required>
            </div>

            <label for="password">Password</label>
            <div>
                <input id="password" type="password" v-model="password" required>
            </div>

            <label for="password-confirm">Confirm Password</label>
            <div>
                <input id="password-confirm" type="password"
                v-model="password_confirmation" required>
            </div>
            <div>
                <button type="submit" @click="handleSubmit">
                    Register
                </button>
            </div>
        </form>
    </div>
</template>

<script>
/* eslint-disable */
    export default {
        props : ["nextUrl"],
        data(){
            return {
                name : "",
                email : "",
                password : "",
                password_confirmation : "",
                is_admin : null
            }
        },
        methods : {
            handleSubmit(e) {
                e.preventDefault()
 
                if (this.password === this.password_confirmation && this.password.length > 0)
                {
                    let url = "//localhost:5005/add_user"
                    if(this.is_admin != null || this.is_admin == 0) url = "//localhost:5005/add_user"
                    this.$http.post(url, {
                        username: this.name,
                        email: this.email,
                        password: this.password,
                        role: 1
                    })
                    .then(response => {
                        if(this.$route.params.nextUrl != null){
                                this.$router.push(this.$route.params.nextUrl)
                            }
                            else{
                                this.$router.push('/login')
                            }
                    })
                    // .then(response => {
                    //     localStorage.setItem('user',JSON.stringify(response.data.user))
                    //     localStorage.setItem('jwt',response.data.token)
                    //     localStorage.setItem('admin', false)
                    //     if (localStorage.getItem('jwt') != null || localStorage.getItem('jwt') != undefined ){
                    //         this.$emit('loggedIn')
                    //         if(this.$route.params.nextUrl != null){
                    //             this.$router.push(this.$route.params.nextUrl)
                    //         }
                    //         else{
                    //             this.$router.push('/')
                    //         }
                    //     }
                    // })
                    // .catch(error => {
                    //     console.error(error);
                    // });
                } else {
                    this.password = ""
                    this.passwordConfirm = ""
 
                    return alert("Passwords do not match")
                }
            }
        }
    }
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
