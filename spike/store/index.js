export const state = () => ({
  loggedIn: false,
  userData: {},
  edit: false
})

export const mutations = {
  logIn (state) {
    state.loggedIn = !state.loggedIn;
  },
  setData(state, dataObj) {
    state.userData = dataObj;
  },
  getEdit(state) {
    state.edit = !state.edit;
  }
}