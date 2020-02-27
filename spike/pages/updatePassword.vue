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
        <ChangePasswordForm />
      </v-col>
      <v-spacer></v-spacer>
    </v-row>
    <Footer />
  </div>
</template>

<script>
import NavBar from '~/components/NavBar'
import Footer from '~/components/Footer'
import ChangePasswordForm from '~/components/ChangePasswordForm'
export default {
  components: {
    NavBar,
    ChangePasswordForm,
    Footer
  }
}
</script>