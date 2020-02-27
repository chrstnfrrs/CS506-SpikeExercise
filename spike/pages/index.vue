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
        class="homeSection"
        heading = "All About Me"
        text = "This is a web application where you can make a profile about yourself!"
        page = "home"
      />
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

import axios from 'axios'

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
  methods: {
    putTest() {
      axios.put(`http://localhost:5000/updateUser`, {
        id: this.userData.id,
        about: "testing"
      }).then((res) => {
        // this.$store.commit('setData', res.data.json_list[0])
        
        console.log(this.userData)
      }).catch(function (err){
        console.log(err)
      });
    }
  }
}
</script>