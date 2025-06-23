export default new Vuex.Store({
    state: {
      socket: null
    },
    mutations: {
      setSocket(state, socket) {
        state.socket = socket;
      }
    },
    actions: {
      initializeSocket({ commit }, socket) {
        commit('setSocket', socket);
      }
    },
    getters: {
      getSocket: (state) => state.socket
    }
  });
  