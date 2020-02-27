<template>
  <div>
    <h1 class="formHeading">Welcome {{userData.name}}</h1>
  </div>
</template>

<script>
export default {
  created() {
    window.location.href = "/"
  },
  computed: {
    userData() {
      return this.$store.state.userData
    }
  },
}
</script>