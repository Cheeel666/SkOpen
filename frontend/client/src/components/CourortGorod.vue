<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Роза Хутор</h1>
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
  },
  created() {
    this.getBooks();
  },
};
</script>
