<template>
  <div id="app2"> 
    <div class="EndContainer" elevation="4">
        <v-btn RUN elevation="2" @click="hi">HI</v-btn>
        RawData_row : {{RawData_row}} <br>
        RawData_col : {{RawData_col}}
    </div>
    
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'app2',
  data :()=>({
      RawData_row:0,
      RawData_col:0,
  }),
  methods:{
    hi: function() {
      var temp = 0;
      axios.post('http://localhost:5000/hi', {data:temp}).then((r) => { 
        console.log("r.data : "  + r.data) 
        this.RawData_row = r.data.row;
        this.RawData_col = r.data.col;
      }).catch((e)=>console.log(e)); 
    }
  }
}
</script>

<style scoped>

.EndContainer{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 330px;
    /* margin-right: auto;
    margin-left: auto; */
    background:rgb(236, 232, 232);
}
</style>