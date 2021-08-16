<template>
    <div id="home">
  <div class="search-wrapper">
  <label>Введите название дороги:</label>
    <input type="text" v-model="search" placeholder="Search title.."/>
  </div>
  <div class="wrapper">
    <div class="card" v-for="(post, index) in filteredList" :key="index">
      <a v-bind:href="post.link" target="_blank">
        <small>{{ post.road }}</small>
        {{post.resort}}
      </a>
    </div>
  </div>
</div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
class Road {
  constructor(resort, road) {
    this.road = road;
    if(resort == "Rosa"){
      this.resort = "Роза хутор"
    } else if (resort == "Laura"){
      this.resort = "Лаура"
    } else {
      this.resort = "Красная поляна"
    }
    this.link = "http://localhost:8080/resorts/" + resort;
  }
}
export default {
  data() {
    return {
      resultData: [],
      search: ''
    };
  },
  methods: {
    getData() {
      const path = 'http://localhost:5005/get_roads_and_courorts';
      axios.get(path)
        .then((res) => {
          res.data.forEach(element => this.resultData.push(new Road(element["name_courort"], element["name_road"])));
          
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    },
    computed: {
    filteredList() {
      return this.resultData.filter(post => {
        return post.road.toLowerCase().includes(this.search.toLowerCase())
      })
    }
    },
  created() {
    this.getData();
  },
};
</script>
    <!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.search-wrapper {
    position: relative;
    label {
      position: absolute;
      font-size: 12px;
      color: rgba(0,0,0,.50);
      top: 8px;
      left: 12px;
      z-index: -1;
      transition: .15s all ease-in-out;
    }
    input {
      padding: 4px 12px;
      color: rgba(0,0,0,.70);
      border: 1px solid rgba(0,0,0,.12);
      transition: .15s all ease-in-out;
      background: white;
      &:focus {
        outline: none;
        transform: scale(1.05);
        & + label  {
          font-size: 10px;
          transform: translateY(-24px) translateX(-12px);
        }
      }
      &::-webkit-input-placeholder {
          font-size: 12px;
          color: rgba(0,0,0,.50);
          font-weight: 100;
      }
    }
}
.wrapper {
    display: flex;
    max-width: 666px;
    flex-wrap: wrap;
    padding-top: 12px;
  }
.card {
    box-shadow: rgba(0, 0, 0, 0.117647) 0px 1px 6px, rgba(0, 0, 0, 0.117647) 0px 1px 4px;
    max-width: 124px;
    margin: 12px;
    transition: .15s all ease-in-out;
    &:hover {
      transform: scale(1.1);
    }
     a {
      text-decoration: none;
      padding: 12px;
      color: #03A9F4;
      font-size: 24px;
      display: flex;
      flex-direction: column;
      align-items: center;
      img {
        height: 100px;
      }
      small {
        font-size: 10px;
        padding: 4px;
      }
    }
  }



  .hotpink {
    background: hotpink;
  }

  .green {
    background: green;
  }

  .box {
    width: 300px;
    height: 300px;
    border: 1px solid rgba(0,0,0,.12);
  }
  div #home{
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  margin-top: 16px;
  margin-bottom: 16px;
}
</style>
