<template>
  <nuxt />
</template>

<style lang="scss">
  * {
    font-family: sans-serif !important;
  }
  .content {
    text-align: left;
    min-height: calc(100vh - 60px);
    padding-top: 120px;
    padding-bottom: 150px;
  }
  .editBtnContainer {
    text-align: right;
  }
  .formStyles {
    text-align: center;
  }
  .formHeading {
    text-align: center;
  }
  .profileCard {
    margin: 16px;
    background-color: #303030 !important;
    color: #f5f5f5 !important;
  }
  .cardHeading {
    font-size: 32px;
    font-weight: 600;
  }
  .cardText {
    color: #f5f5f5 !important;
    a {
      color: #f5f5f5 !important;
    }
  }
  .socialTag {
    color: #0074D9;
    text-decoration: none;
  }
  .userRow {
    min-height: calc(100vh - 60px);
    padding-top: 120px;
    padding-bottom: 150px;
    align-items: center;
  }
  .submitBtn {
    background: #0074D9 !important;
    color: #f5f5f5 !important;
    padding: 10px 30px !important;
    a{
      text-transform: none !important; 
      text-decoration: none;
      color: #f5f5f5 !important;
    }
  }
  .editBtn {
    background: #0074D9 !important;
    color: #f5f5f5 !important;
    padding: 2px 6px !important;
    text-transform: none !important; 
    text-decoration: none;
    margin: 16px 0px;
  }
  .textBtn {
    cursor: pointer;
    margin: 12px 0px;
    font-size: 12px;
  }
  .homeSection {
    .cardHeading{
     justify-content: center !important;
    }
    text-align: center !important;
    .v-card{
      background-color: #0074D9 !important;
    }
  }
</style>