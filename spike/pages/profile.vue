<template>
  <div>
    <NavBar />
    <v-row>
      <v-spacer></v-spacer>
      <v-col
        :lg="4"
        :md="4"
        :sm="5"
        cols="10"
      >
        <div v-if="!loggedIn">
          <div class="content">
            <h1>Please Log In</h1>
          </div>
          <Footer />
        </div>
        <div v-if="loggedIn && this.$store.state.edit" class="content">
          <div class="editBtnContainer">
            <v-btn class="editBtn" @click="editSubmit()">Done</v-btn>
          </div>
          <UpdateForm />
        </div>
        <div v-if="loggedIn && !this.$store.state.edit" class="content">
          <h1 v-if="userData.name">{{userData.name}}</h1>
          <h2 v-if="userData.email">{{userData.email}}</h2>
          <div class="editBtnContainer">
            <v-btn class="editBtn" @click="editSubmit()">Edit</v-btn>
          </div>
          <StuffSection 
            heading="About Me"
            :text='this.userData.about'
            page="about"/>
          <StuffSection 
            heading="Fun Fact"
            :text='this.userData.funfact'
            page="funfact"/>
          <MyLinks />
          <StuffSection 
            heading="Other Stuff"
            :text='this.userData.other'
            page="other"/>
        </div>
      </v-col>
      <v-spacer></v-spacer>
    </v-row>
    <Footer />
  </div>
</template>

<script>
import NavBar from '~/components/NavBar'
import Footer from '~/components/Footer'
import UpdateForm from '~/components/UpdateForm'
import MyLinks from '~/components/MyLinks'
import StuffSection from '~/components/StuffSection'

export default {
  components: {
    NavBar,
    Footer,
    MyLinks,
    UpdateForm,
    StuffSection
  },
  computed: {
    loggedIn () {
      return this.$store.state.loggedIn
    },
    userData() {
      return this.$store.state.userData
    },
  },
  // data() {
  //   return {
  //     edit: false,
  //   }
  // },
  methods: {
    editSubmit(){
      this.$store.commit('getEdit')
    }
  }
}
</script>

<style lang="scss">
  .editBtn{
    text-align: right;
  }
</style>