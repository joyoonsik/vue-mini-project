<template>
<div>
    <div>
        <Center/>
        <End/>
        <Rend/>
    </div>
</div>
</template>

<script>
import Center from '../components/Center.vue'
import End from '../components/End.vue'
import Rend from '../components/Rend.vue'

export default {
    name: 'App',
  components: {
        Center, End, Rend
  }
};
</script>



