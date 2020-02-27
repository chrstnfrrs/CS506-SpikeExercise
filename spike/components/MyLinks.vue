<template>
  <v-card class="profileCard">
    <v-card-title class="cardHeading">My Links</v-card-title>
    <v-card-text>
    <v-expansion-panels>
      <v-expansion-panel v-if="this.userData.instagram">
        <v-expansion-panel-header>Instagram</v-expansion-panel-header>
          <v-expansion-panel-content>
            <a :href="`https://www.instagram.com/${this.userData.instagram}`" class="socialTag">
              @{{this.userData.instagram}}
            </a>
          </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel v-if="this.userData.twitter">
        <v-expansion-panel-header>Twitter</v-expansion-panel-header>
          <v-expansion-panel-content>
            <a :href="`https://www.twitter.com/${this.userData.twitter}`" class="socialTag">
              @{{this.userData.twitter}}
            </a>
          </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel v-if="this.userData.github">
        <v-expansion-panel-header>Github</v-expansion-panel-header>
          <v-expansion-panel-content>
            <a :href="`https://www.github.com/${this.userData.github}`" class="socialTag">
              @{{this.userData.github}}
            </a>
          </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel v-if="this.userData.linkedin">
        <v-expansion-panel-header>LinkedIn</v-expansion-panel-header>
          <v-expansion-panel-content>
            <a :href="`https://www.linkedin.com/${this.userData.linkedin}`" class="socialTag">
              @{{this.userData.linkedin}}
            </a>
          </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
    </v-card-text>
    <v-card-text v-if="!page" class="cardText"><nuxt-link :to='`/links`'>View More</nuxt-link></v-card-text>
    <v-card-text v-if="page" class="cardText"><nuxt-link :to='`/profile`'>View Profile</nuxt-link></v-card-text>
  </v-card>
</template>

<script>
export default {
  props:{
    page: String
  },
  computed: {
    userData() {
      return this.$store.state.userData
    }
  },
}
</script>
