<template>
  <div>
    <div v-if="loggedIn">
      <Welcome />
    </div>
    <div v-if="error">
      <h1 class="formHeading">Incorrect Log In, Try Again</h1>
    </div>
    <div v-if="!error && !loggedIn">
      <h1 class="formHeading">Log In</h1>
    </div>
    <form v-if="!loggedIn" class="formStyles">
      <v-text-field 
        v-model="email" 
        label="Email" 
        required></v-text-field>
      <v-text-field 
        :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
        :type="show ? 'text' : 'password'"
        v-model="password" 
        label="Password" 
        @click:append="show = !show"
        required
        ></v-text-field>
      <!-- TODO: Add href to homepage -->
      <v-btn class="submitBtn" @click="logIn">Log In</v-btn> 
    </form>
  </div>
</template>

<script>
import Welcome from '~/components/Welcome'
import axios from 'axios'
export default {
  components: {
    Welcome
  },
  data() {
    return {
      show: false,
      email: '',
      password: '',
      error: false
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
      axios.get(`http://localhost:5000/logIn?email=${this.email}&password=${this.password}`)
      .then((res) => {
        this.$store.commit('setData', res.data.json_list[0])
        this.$store.commit('logIn')
      }).catch((err) => {
        this.error = true
      });
    },
  }
}
</script>
