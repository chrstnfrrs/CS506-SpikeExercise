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
        <SignUpForm />
      </v-col>
      <v-spacer></v-spacer>
    </v-row>
    <Footer />
  </div>
</template>

<script>
import NavBar from '~/components/NavBar'
import Footer from '~/components/Footer'

import SignUpForm from '~/components/SignUpForm'

export default {
  components: {
    NavBar,
    Footer,
    SignUpForm
  }
}
</script>