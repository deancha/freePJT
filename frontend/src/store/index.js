import Vue from 'vue'
import Vuex from 'vuex'
import calendarStore from './modules/calendarStore'
import counselorInfoStore from './modules/counselorInfoStore'
import chatStore from './modules/chatStore'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    myName: "",
    cc: 1,
    myStatus: -1,

    //상담일지 등록할 때 쓰는 data
    counselmeetingData: [],
    plugins: [createPersistedState()],

  },
  mutations: {
  },
  actions: {
  },
  modules: {
    calendarStore : calendarStore,
    counselorInfoStore : counselorInfoStore,
    chatStore: chatStore
  },
})
