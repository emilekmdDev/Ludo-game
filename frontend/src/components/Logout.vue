<template>
    <div class="login-container">
      <h2>Logout</h2>
      <button type="submit" @click="logoutUser">Logout</button>
      <div v-if="errorMessage">{{ errorMessage }}</div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  axios.defaults.withCredentials=true
  export default {
    data() {
      return {
        username: '',
        password: '',
        errorMessage: '',
      };
    },

    beforeMount() {
      const isAuthenticated = !!localStorage.getItem('user');
      if (!isAuthenticated) {
        this.$router.push({ name: 'login' });  // Rediriger si l'utilisateur est déjà connecté
      }
    },

    methods: {
      async logoutUser() {
        try{
          const response = await axios.post('http://localhost:8000/api/logout/',{})
          if (response.data.status === 'success') {
            localStorage.removeItem('user');
            this.$router.push({ name: 'login' });
          }
        }catch(error){
          console.log(error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Styles de base pour la page de login */
  .login-container {
    width: 300px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  </style>
  