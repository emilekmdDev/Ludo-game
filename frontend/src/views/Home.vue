<template>
    <div class="container">
      <h1>Home</h1>
      <div class="mode">
        <router-link to="jcb"><button>j vs bot</button></router-link>
        <router-link to="jcj"><button>j vs j (local)</button></router-link>
        <router-link :to="{name:'room_config'}"><button>j vs j (room)</button></router-link>
        <!-- <router-link :to="{name:'Table_jcb-online'}"><button>j vs j (online)</button></router-link> -->
      </div>
    </div>
</template>

<script>
import Player from './Player.vue';

export default {
  
  components:{Player},  
  data(){
    return{
      names:['player 1','player 2'],
      playername:''
    }
  },

  beforeMount() {
    const isAuthenticated = !!localStorage.getItem('user');
    if (!isAuthenticated) {
      this.$router.push({ name: 'login' });  // Rediriger si l'utilisateur est déjà connecté
    }
  },

  methods:{
    addplayer(name){
      if (this.names.length<4) {
        this.names.push(name)
      }
      this.playername=''
    },

    deleteplayer(removename){
      if (this.names.length>2) {
        this.names=this.names.filter(name=>name!=removename)
      }
    },

    share(){
      this.$router.push({name:'table', params:{data:1}})
    }

  }
}

</script>

<style scoped>
  button{
    width: 100px;
    height: 100px;
    border: gray solid 2px;
    border-radius: 20px;
    transition-property: filter,transform;
    transition: .3s ease;
    transition-delay: .1s;
  }

  button:hover{
    transform: scale(1.1);
    filter: brightness(1.1);
  }
  
  .mode{
    width: 400px;
    display: grid;
    gap: 20px;
    grid-template-columns: repeat(2, 0fr); 
    grid-template-rows: repeat(2, 0fr); 
    align-items: center;
    justify-content: center;
  }
  
  .container{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 40px;
    justify-content: center;
  }
</style>