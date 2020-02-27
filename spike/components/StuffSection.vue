<template>
  <div>
    <v-card v-if="this.text" class="profileCard">
      <v-card-title class="cardHeading">{{this.heading}}</v-card-title>
      <v-card-text class="cardText">{{this.text}}</v-card-text>
      <v-card-text v-if="page && !page=='home'" class="cardText"><nuxt-link :to='`/${page}`'>View More</nuxt-link></v-card-text>
      <v-card-text v-if="!page" class="cardText"><nuxt-link :to='`/profile`'>View Profile</nuxt-link></v-card-text>
      <v-card-text v-if="page=='home' && !loggedIn" class="cardText"><nuxt-link :to='`/login`'>Log In</nuxt-link></v-card-text>
      <v-card-text v-if="page=='home' && loggedIn" class="cardText"><nuxt-link :to='`/profile`'>View Profile</nuxt-link></v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  props:{
    heading: String,
    text: String,
    page: String
  },
  computed: {
    loggedIn () {
      return this.$store.state.loggedIn
    },
  }
}
</script>