import {createStore} from "vuex";

export default createStore({
  state: {
    messages: []
  },
  mutations: {
    addMessage(state, message) {
      state.messages.push({
        id: Date.now(),
        ...message
      });
    }
  }
}); 