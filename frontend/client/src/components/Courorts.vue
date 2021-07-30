<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Курорты</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Курорт</th>
              <th scope="col">Город</th>
              <th scope="col">Отслеживать</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(courort, index) in courorts" :key="index">
              <td>{{ courort.name_courort }}</td>
              <td>{{ courort.city }}</td>
              <td>
                <button type="button" class="btn btn-warning btn-sm">Следить</button>
              </td>
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
