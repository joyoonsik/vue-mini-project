<template>
    <div class="RendContainer">
        
        <div class="Final" >
            <table style='width:100%'>
                <tr style='height:60px;'>
                <td style='text-align:left;'>
                <v-img :src="require('../assets/foot.png')"
                        height="50"
                        width="350"
                            />
                </td>
                <td style='text-align:right;'>
                010-6287-9891 | joyoonsik18011@gmail.com | 대양AI센터 460호<br>
                COPYRIGHT ⓒ 세종대학교 영앤리치 ALL RIGHT RESERVED. <br>
                </td>
                </tr>
            </table>
        </div>
    </div>

</template>

<script>
export default {
  name: 'app3',
  data :()=>({
      msg:'마지막 컴포넌트'
  })
}
</script>

<style scoped>

.RendContainer{
    width: 100%;
    height: 100px;
    
}

.Final{
    margin-left: 20%;
    margin-right: 20%;
    margin-top: 30px;
    text-align: left;
}
.Final2{
    text-align: right;
}
 div.caption{
      font-size: 20px;
      position: relative;
      bottom: 58px;
      right: 10%;
      
  }
</style>