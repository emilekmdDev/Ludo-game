<template>
  {{ socket }}
  {{ user }}
  <div v-if="!start">
    <button @click="createroom=true,joinroom=false" :disabled="roomjoined">create</button>
    <button @click="joinroom=true ,createroom=false" :disabled="roomcreated">join</button>
      <div class="selection" v-if="createroom">
          <form @submit.prevent="createRoom">
            <input type="text" v-model="roomname" required>
            <input type="radio" v-model="private_">
            <button type="submit">create room</button>
          </form>
      </div>
  
      <div class="selection" v-if="joinroom">
        <form @submit.prevent="joinRoom">
          <input type="text" v-model="roomname">
          <button type="submit">join room</button>
        </form>
      </div>
      <div class="selection">
        <button style="background-color: brown;" @click="leave">quit</button>
      </div>
      <h3>{{ error }}</h3>

      <div v-if="createroom">
        <button :disabled="members<2 || members>4 || !roomname" @click="launch"> launch party </button>
      </div>
      <Room :members="members" :users="users" @change_c="updatecolor"></Room>

  </div>

  <div v-if="start">
  </div>
    
</template>  

<script>

import axios from 'axios';
import Room from './Room.vue';

export default{
  
  components:{Room},

  data(){
    return{
      roomname:'',
      createroom:true,
      joinroom:false,
      roomcreated:false,
      roomjoined:false,
      members:0,
      private_:false,
      socket: null,
      user:localStorage.getItem('user'),
      error:'',
      users:[],
      start:false
    }
  },

  methods:{
    launch(){
      if (this.socket && this.socket.readyState ===WebSocket.OPEN){
        const message ={
          message:'start online party',
          action:'startparty',
          roomname:this.roomname
        }
      }
      localStorage.setItem('currentsocket', JSON.stringify(this.socket));  // Stocker l'utilisateur dans localStorage
      this.$router.push({name:'table_jcj_multi_room',params:{room_name:this.roomname}});
    },

    updatecolor(name){
      if (this.socket && this.socket.readyState === WebSocket.OPEN) {
        const message = {
          message: 'update color created successfully',
          action:'changecolor',
          playername:name,
        };
        this.socket.send(JSON.stringify(message));
      }
    },

    async createRoom() {
      // Connecter à la WebSocket pour créer la room
      this.connectToSocket('create');

      // Créer la room dans la base de données
      try {
        const response = await axios.post('http://localhost:8000/api/create_room/', {
          roomname: this.roomname,
          private_: this.private_,
        });

        if (response.data.status === 'success') {
          this.roomcreated = true;
          console.log('Room successfully created');
        } else {
          console.log('Room not created');
          this.errorMessage = 'Room creation failed';
        }
      } catch (error) {
        console.log(error);
        this.errorMessage = 'Room creation failed. Please try again.';
      }
    },

    async joinRoom() {
      // Connecter à la WebSocket pour rejoindre la room
      this.connectToSocket('join');
    },

    connectToSocket(action) {
      // Assurez-vous que la socket n'est pas déjà connectée
      if (this.socket == null) {
        this.socket = new WebSocket(`ws://localhost:8000/ws/ludo/${this.roomname}/${action}/`);

        this.socket.onopen = () => {
          console.log("WebSocket is connected.");
          if (action === 'create') {
            this.sendMessage(); // Envoyer un message après création
          }
        };

        this.socket.onmessage = (event) => {
          
          let data = JSON.parse(event.data);
          console.log("Message received from server: ", data);

          if (data.error) {
            this.errorMessage = data.error;  // Afficher l'erreur si elle existe
          } 
          
          if (data.message.online_count !== undefined) {
            this.members = data.message.online_count;  // Mise à jour du nombre de membres en ligne
          }

          if (data.message.users !== undefined) {
            this.users = data.message.users;  // Mise à jour du nombre de membres en ligne
          }

          if(data.message){}

        };

        this.socket.onerror = (error) => {
          console.error("WebSocket error: ", error);
          this.errorMessage = 'WebSocket connection error. Please try again.';
        };

        this.socket.onclose = () => {
          console.log("WebSocket connection closed.");
          
          // this.error='incorect room name'
          // setTimeout(() => {
          //   this.error=''
          // }, 2000);

          this.socket = null;
          this.users=[]
          this.members=''
        };
      }
    },

    sendMessage() {
      // Envoyer un message via WebSocket après la connexion
      if (this.socket && this.socket.readyState === WebSocket.OPEN) {
        const message = {
          message: 'Room created successfully',
        };
        this.socket.send(JSON.stringify(message));
      }
    },

    leave() {
      // Envoyer un message via WebSocket après la connexion
      if (this.socket && this.socket.readyState === WebSocket.OPEN) {
        const message = {
          message: 'leaving room',
          action:'leave'
        };
        this.socket.send(JSON.stringify(message));
      }
    }
  },
}
</script>
<!--  -->
<style>
    .selection button{
    width: 100px;
    height: 100px;
    border: gray solid 2px;
    border-radius: 20px;
    transition-property: filter,transform;
    transition: .3s ease;
    transition-delay: .1s;
    margin: 20px;
  }

  .selection button:hover{
    transform: scale(1.1);
    filter: brightness(1.1);
  }
  
  
  
  </style>