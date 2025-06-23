<template>
  <form @submit.prevent="sign_in">
      <input type="text" required  v-model="name" placeholder="name"><br>
      <input type="password" required v-model="password" placeholder="password">
      <input type="email" required  v-model="email" placeholder="email"><br>
      <button type="submit">submit</button>
    </form>
</template>

<script>
import axios from 'axios';

export default {

    data(){
        return{
            name:'',
            password:'',
            email:'',
        }
    },

    methods:{
        async sign_in(){
            try {
                const response = await axios.post('http://localhost:8000/api/sign-in/',
                {
                    username:this.name,
                    password:this.password,
                    email:this.email,
                });

                if (response.status==201) {
                    console.log(response);
                    localStorage.setItem('user', JSON.stringify(response.data.user));  // Stocker l'utilisateur dans localStorage
                    this.$router.push({name:'home'})
                } ; 

                } catch (error) {
                console.log(error);    
            };
        },

    }
}
</script>

<style>

</style>