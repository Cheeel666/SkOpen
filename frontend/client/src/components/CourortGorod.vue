<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Красная поляна</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Название дороги</th>
              <th scope="col">Тип дороги</th>
              <th scope="col">Работает</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(courort, index) in courorts" :key="index">
              <td>{{ courort.name_road }}</td>
              <td><span v-if="courort.type_road==='lift'">Подъемник</span>
                <span v-else>Канатная дорога</span></td>
              <td><span v-if="courort.work_status===0">Рабротает</span>
                <span v-else>Не работает</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="comments-outside">
    <div class="comments-header">
        <div class="comments-stats">
            <span><i class="fa fa-comment"></i>Комментариев: {{ comments.length }}</span>
        </div>
    </div>
</div>
  <div>
      <div class="comment-form">
        <textarea type="text" v-model="comment"
        placeholder="Comment is here:"></textarea>
        <button @click="addComment">Добавить комментарий</button>
   </div>
    <div v-for="(comment, index) in comments" :key = "index" class="comments-box">
         <p class="author">
           {{comment.email}}
        </p>
        <p class="content-comment"> {{comment.text}}</p>
        <p v-if="admin!='user'"
        @click="removeComment(comment.email, comment.text)" class="delete">Удалить</p>
    </div>
</div>
  </div>
</template>


<script>
import axios from 'axios';
/* eslint-disable */
export default {
  data() {
    return {
      courorts: [],
      comments: [],
      admin: localStorage.getItem('role'),
    };
  },
  methods: {
    getTraces() {
      const path = 'http://localhost:5005/get_gorod';
      axios.get(path)
        .then((res) => {
          this.courorts = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getComments() {
      this.$http.post('//localhost:5005/get_comments', {
                id_courort: "2"
            })
            .then(response => {
              this.comments = response.data
            })
            .catch(function (error) {
              console.error(error.response);
            });
    },
    addComment: function() {
            if(this.comment){
              this.$http.post('//localhost:5005/add_comment', {
                email: localStorage.getItem('email'),
                text: this.comment,
                id_courort: 2
            })
            .then(response => {
              alert('Success')
              this.$emit('commentAdded')
              this.$router.go()
            })
            .catch(function (error) {
              console.error(error.response);
            });
            }else{
                alert('Введите комментарий');
            }
        },
    removeComment: function(e, t){
            this.$http.post('//localhost:5005/delete_comment', {
                email: e,
                text: t,
                id_courort: 2
            })
            .then(response => {
              alert('Success')
              this.$emit('commentDeleted')
              this.$router.go()
            })
            .catch(function (error) {
              console.error(error.response);
            });
        },
    },
  created() {
    this.getTraces();
    this.getComments();
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
*{
    padding: 0;
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
}

#demo{
    margin: 20px 0 0 0;
}

.comment-form{
    display: block;
    width: 80%;
    margin: auto;
}

textarea{
    width: 100%;
    border: 2px solid #ccc;
    border-radius: 7px;
    height: 70px;
    font-family: Verdana, Helvetica, sans-serif;
    padding: 5px;
}

input{
    border: 2px solid #ccc;
    border-radius: 5px;
    padding: 5px;
}

button{
    background: #333;
    color: #ccc;
    border: 0;
    padding: 5px;
    cursor: pointer;
}

/*Comment Box*/

.comments-box{
    width: 90%;
    margin: auto;
    padding: 20px 0;
    border-bottom: 1px solid #000;
}

.delete{
    background: red;
    color: #fff;
    font-size: 12px;
    cursor: pointer;
    display: inline;
    padding: 3px;
}

.author{
    margin: 10px 0;
    font-weight: bold;
}
</style>
