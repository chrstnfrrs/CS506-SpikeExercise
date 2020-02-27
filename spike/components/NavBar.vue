<template>
  <nav>
    <!-- <v-row> -->
      <v-col
        :md="8"
        cols="6"
      >
        <nuxt-link class="navItem" to="/">Home</nuxt-link>
      </v-col>
      <v-spacer></v-spacer>
      <v-col
        class="userCol"
        v-if="!this.loggedIn"
        :md="2"
        cols="6"
      >
        <nuxt-link class="navItem" to="/login">Log In</nuxt-link>
        <nuxt-link class="navItem" to="/signup">Sign Up</nuxt-link>
      </v-col>
      <v-col
        class="userCol"
        v-if="this.loggedIn"
        :md="3"
        cols="6"
      >
        <nuxt-link class="navItem" to="/profile">View Profile</nuxt-link>
        <span @click="logOut" class="logOut navItem">Log Out</span>
      </v-col>
    <!-- </v-row> -->
  </nav>
</template>

<script>
export default {
  computed: {
    loggedIn () {
      return this.$store.state.loggedIn
    }
  },
  methods: {
    logOut() {
      // console.log(e)
      this.$store.commit('logIn')
      window.location.href = ('/')
    }
  }
}
</script>

<style lang="scss">
  nav {
    padding: 0px 120px;
    height: 60px;
    display: flex;
    align-items: center;
    background: #0074D9;
    color: #f5f5f5;
    box-shadow: 0 4px 5px 0 rgba(0,0,0,0.14), 0 1px 10px 0 rgba(0,0,0,0.12), 0 2px 4px -1px rgba(0,0,0,0.20);
    a{
      color: #f5f5f5;
      text-decoration: none;
    }
  }
  .userCol {
    text-align: right;
  }
  .navItem {
    padding: 0px 5px;
  }
  .logOut{
    cursor: pointer;
  }
  @media screen and (max-width: 600px) {
    nav {
      padding: 0px 60px;
    }
  }
</style>