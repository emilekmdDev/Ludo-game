<template>
  <div class="selection">
      <h2>number of player</h2>
      <p>{{ members }}</p>
      <p>{{users}}</p>
      <div class="roomplayerdisplay">
        <div v-for="(user,index) in users" :key="index" class="playerdisplayer">
          {{user['username']}}
          <div  @click="changecolor(user['username'])" class="color" :class="{red:user['color']=='r',yellow:user['color']=='y',blue:user['color']=='b',green:user['color']=='g'}"></div>
        </div>
      </div>
    </div>  
</template>

<script>
export default {
  props:{
    members:Number,
    users:Array
  },

  methods:{
    changecolor(name){
      let tmp= localStorage.getItem('user')
      tmp=JSON.parse(tmp)
      
      if (tmp.username==name) {
        this.$emit('change_c',name)
      }
    }
  }
}
</script>

<style>
  .roomplayerdisplay{
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 20px;
  }

  .playerdisplayer{
    background: rgb(248, 248, 248);
    border-left: 10px solid rgb(206, 206, 206);
    width: 50%;
    padding: 7px 20px;
    text-align: start;
  }

  .color{
    width: 50px;
    height: 50px;
  }

  .yellow{
    background: yellow;
  }

  .green{
    background: green;
  }

  .blue{
    background: blue;
  }

  .red{
    background: red;
  }
</style>