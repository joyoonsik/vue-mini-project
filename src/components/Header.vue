<template>
  <div>  
  <b-navbar type="light" variant="light"> 
    <b-navbar-nav>
      <b-nav-item><router-link to="/" class="btn">홈</router-link></b-nav-item>
      <b-nav-item><router-link to="/Home" class="btn">공지사항</router-link></b-nav-item>
      <b-nav-item><router-link to="/About" class="btn">게시판</router-link></b-nav-item>
    </b-navbar-nav>
    <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-button v-on:click="say('hi')" variant="outline-success" class="my-2 my-sm-0">로그인</b-button>
        </b-nav-form>
    </b-navbar-nav>
  </b-navbar>
</div>
</template>

<script>
export default {
  name: 'app',
    data: () => ({
      msg: 'hi'
    }),
    methods: {
        say:function(event){
            alert(event)
        }
    }
    

}
</script>
<style>
#app  {
  margin-left: 10%;
  margin-right: 10%;
}
</style>