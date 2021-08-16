<template>
    <div>
        <h4>Login</h4>
        <form>
            <label for="email" >E-Mail Address</label>
            <div>
                <input id="email" type="email" v-model="email" required autofocus>
            </div>
            <div>
                <label for="password" >Password</label>
                <div>
                    <input id="password" type="password" v-model="password" required>
                </div>
            </div>
            <div>
                <button type="submit" @click="handleSubmit">
                    Login
                </button>
            </div>
        </form>
    </div>
</template>
<script>
/* eslint-disable */
export default {
  data() {
    return {
      email: "",
      password: ""
    }
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault()
      if (this.password.length > 0) {
        this.$http.post('//localhost:5005/login', {
            email: this.email,
            password: this.password
          })
          .then(response => {
            let is_admin = false
            if (response.data.is_admin === 0){
              is_admin = true
            }
            localStorage.setItem('user', JSON.stringify(response
              .data.user))
            localStorage.setItem('email', response
              .data.email)
            localStorage.setItem('jwt', response.data.token)
            localStorage.setItem('role', response.data.is_admin)
            if (localStorage.getItem('jwt') != null) {
              this.$emit('loggedIn')
              if (this.$route.params.nextUrl != null) {
                this.$router.push(this.$route.params.nextUrl)
              } else {
                if (is_admin === 0) {
                  this.$router.push('/');
                } else {
                  this.$router.push('/profile');
                }
              }
            }
          })
          .catch(function (error) {
            console.error(error.response);
          });
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
