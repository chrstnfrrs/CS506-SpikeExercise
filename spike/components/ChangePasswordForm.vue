<template>
  <div>
    <form class="formStyles" v-if="loggedIn">
      <h1>Change Password</h1>
      <h2 v-if="passwordMismatch" style="color: red;">Passwords Do Not Match</h2>
      <v-text-field
        v-model="password"
        label="New Password"
        required
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        :type="showPassword ? 'text' : 'password'"
        @click:append="showPassword = !showPassword"
      >
      </v-text-field>
      <v-text-field
        v-model="check"
        label="Confirm Password"
        required
        :append-icon="showConfirmPassword ? 'mdi-eye' : 'mdi-eye-off'"
        :type="showConfirmPassword ? 'text' : 'password'"
        @click:append="showConfirmPassword = !showConfirmPassword"
      >
      </v-text-field>
      <v-btn class="submitBtn" @click="updatePassword">Update</v-btn> 
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    password: '',
    check: '',
    showOldPassword: false,
    showPassword: false,
    showConfirmPassword: false,
    passwordMismatch: false,
    errorWarning: false
  }),
  computed: {
    userData() {
      return this.$store.state.userData
    },
    loggedIn () {
      return this.$store.state.loggedIn
    }
  },
  methods: {
    updatePassword() {
      if(this.password == this.check){
        axios.put(`http://localhost:5000/updatePW`, {
          id: this.userData.id,
          name: this.name,
          password: this.password,
          email: this.email,
          about: this.about,
          funfact: this.funfact,
          other: this.other,
          instagram: this.instagram,
          twitter: this.twitter,
          github: this.github,
          linkedin: this.linkedin
        })
        .then((res) => {
          if(res.data.error){
            this.errorWarning = true;
          }
          this.errorWarning = false;
          this.$store.commit('setData', res.data.json_list[0])
          window.location.href = "/"
        })
        .catch((error) => {
          console.log(error);
        });
      } else {
        this.passwordMismatch = true;
      }
    }
  },
}
</script>