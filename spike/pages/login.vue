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
        <LogInForm />
      </v-col>
      <v-spacer></v-spacer>
    </v-row>
    <Footer />
  </div>
</template>

<script>
import NavBar from '~/components/NavBar'
import Footer from '~/components/Footer'
import LogInForm from '~/components/LogInForm'

import axios from 'axios'

export default {
  components: {
    NavBar,
    Footer,
    LogInForm
  },
  data() {
    return {
      show: false,
      name: '',
      password: '',
      posts: []
    }
  },
  computed: {
    loggedIn () {
      return this.$store.state.loggedIn
    },
    userData() {
      return this.$store.state.userData
    }
  },
  methods: {
    logIn() {
      axios.get(`http://localhost:5000/logIn?name=${this.name}&password=${this.password}`)
      .then((res) => {
        this.$store.commit('setData', res.data.json_list[0])
        console.log(this.userData)
      }).catch(function (err){
        console.log(err)
      });
      this.$store.commit('logIn')
    },
  }
}
</script>

<style lang="scss">
</style>