<template>
    <div class="login-container">
      <h2>Login</h2>
      <form @submit.prevent="loginUser">
        <div>
          <label for="username">Username:</label>
          <input type="text" v-model="username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" v-model="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
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
      if (isAuthenticated) {
        this.$router.push({ name: 'home' });  // Rediriger si l'utilisateur est déjà connecté
      }
    },

    methods: {
      async loginUser() {
        try {
          const response = await axios.post('http://localhost:8000/api/login/', {
            username: this.username,
            password: this.password,
          },{});
          console.log(response);
          
          
          if (response.data.status === 'success') {
            
            localStorage.setItem('user', JSON.stringify(response.data.user));  // Stocker l'utilisateur dans localStorage
            // console.log(response);
            
            this.$router.push({ name: 'home' });
          } else {
            this.errorMessage = 'Invalid credentials';
          }
        } catch (error) {
          // console.log(error);
          this.errorMessage = 'Login failed. Please try again.';
        }
      }
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
  