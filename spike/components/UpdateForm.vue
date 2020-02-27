<template>
  <div>
    <div v-if="!loggedIn">
      <h1>Please Log In</h1>
    </div>
    <form class="formStyles" v-if="loggedIn">
      <h1>Update Information</h1>
      <v-text-field v-model="name" label="User Name" required></v-text-field>
      <v-text-field v-model="email" label="Email" required></v-text-field>
      <h2 v-if="passwordMismatch" style="color: red;">Passwords Do Not Match</h2>
      <v-text-field
        v-model="password"
        label="Password"
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
      <v-text-field v-model="about" label="About" required></v-text-field>
      <v-text-field v-model="funfact" label="Fun Fact" required></v-text-field>
      <v-text-field v-model="other" label="Other Information" required></v-text-field>
      <v-text-field v-model="instagram" label="Instagram" required></v-text-field>
      <v-text-field v-model="twitter" label="Twitter" required></v-text-field>
      <v-text-field v-model="github" label="Github" required></v-text-field>
      <v-text-field v-model="linkedin" label="LinkedIn" required></v-text-field>
      <!-- <transition name="hint" appear>
        <div v-if='passwordValidation.errors.length> 0' class='hints'>
          <h2>Password Hints</h2>
          <p v-for='error in passwordValidation.errors' :key="error">{{error}}</p>
        </div>
      </transition> -->
      <p class="textBtn" @click="updatePW">Update Password</p>
      <v-btn class="submitBtn" @click="updateData">Update</v-btn> 
    </form>
  </div>
</template>

<script>
import Welcome from '~/components/Welcome'
import axios from 'axios';

export default {
  components: {
    Welcome
  },
  data: () => ({
    name: '',
    email: '',
    password: '',
    about: '',
    funfact: '',
    other: '',
    instagram: '',
    twitter: '',
    github: '',
    linkedin: '',
    check: '',
    showPassword: false,
    showConfirmPassword: false,
    passwordMismatch: false,
    errorWarning: false
  }),
  created() {
    this.name = this.userData.name
    this.email = this.userData.email
    this.password = this.userData.password
    this.about = this.userData.about
    this.funfact = this.userData.funfact
    this.other = this.userData.other
    this.instagram = this.userData.instagram
    this.twitter = this.userData.twitter
    this.github = this.userData.github
    this.linkedin = this.userData.linkedin
  },
  computed: {
    loggedIn () {
      return this.$store.state.loggedIn
    },
    userData() {
      return this.$store.state.userData
    },
    getEdit() {
      return this.$store.state.edit
    }
  },
  methods: {
    updatePW() {
      this.$store.commit('getEdit')
      window.location.href = "/updatePassword"
    },
    updateData() {
      if(this.password == this.check){
        axios.put(`http://localhost:5000/updateUser`, {
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
          console.log(res.data.json_list[0])
          this.$store.commit('setData', res.data.json_list[0])
          this.$store.commit('getEdit')
        })
        .catch((error) => {
          console.log(error);
        });
      } else {
        this.passwordMismatch = true;
      }
    }
  }
}
</script>
