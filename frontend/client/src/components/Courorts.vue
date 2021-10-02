<template>
  <div class="container">
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
            <tr v-for="(courort, index) in courorts" :key="index"
            @click="goToBlabla(courort.name_courort)">

              <td type="name">{{ courort.name_courort }}</td>
              <td type="name"></td>
              <td type="city">{{ courort.city }}</td>
            </tr>
          </tbody>
        </table>
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
    };
  },
  methods: {
    goToBlabla(id) {
      this.$router.push('/resorts/'+id);
    },
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
tbody {
  color: #3c97bf;
  text-decoration: none;

}
a {
  color: #3c97bf;
    text-decoration: none;
}
td {
  
}
</style>
