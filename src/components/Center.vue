<template>
  <div> 
    <div class="CenterContainer" elevation="4">
      <div id="app">
        <vueper-slides class="no-shadow" :slide-ratio="1/3">
          <vueper-slide v-for="i in 5" :key="i" :title="i.toString()"></vueper-slide>
        </vueper-slides>
      </div>
    </div>
</div>
</template>
<script>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

  export default {
    components: { VueperSlides, VueperSlide},

    data() {
      return {
        data: [
          '<div class="example-slide">Slide 1</div>',
          '<div class="example-slide">Slide 2</div>',
          '<div class="example-slide">Slide 3</div>',
        ],
      };
    },
    
  };
</script>
          
<style>

.CenterContainer{
    width: 100%;
    height: 596px;
    /* background:rgb(236, 232, 232);  */
}
.vueperslide {
  background: linear-gradient(-45deg, #EE7752, #E73C7E, #23A6D5, #23D5AB);
}
.vueperslide__title {
  font-size: 7em;
  opacity: 0.6;
}
</style>
    