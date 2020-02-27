<template>
  <div>
    <NavBar />
    <v-row class="userRow">
      <v-spacer></v-spacer>
      <v-col
        :lg="4"
        :md="4"
        :sm="5"
        cols="10"
      >
        <StuffSection 
            heading="Other Information"
            :text='this.userData.other'/>
      </v-col>
      <v-spacer></v-spacer>
    </v-row>
    <Footer />
  </div>
</template>

<script>
import NavBar from '~/components/NavBar'
import StuffSection from '~/components/StuffSection'
import Footer from '~/components/Footer'
export default {
  components: {
    NavBar,
    StuffSection,
    Footer
  },
  computed: {
    userData() {
      return this.$store.state.userData
    }
  },
}
</script>