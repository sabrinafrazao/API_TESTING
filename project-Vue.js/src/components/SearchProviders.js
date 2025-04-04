import api from '../services/api.js';

export default {

/*
  OPERATOR SEARCH COMPONENT:
  1. Manages a search field (searchTerm)
  2. Makes an API call when the user types
  3. Controls 3 states:
  - loading: during the request
  - operators: list of results
  - error: error messages
  4. Main logic:
  - Ignores empty searches
  - Makes an asynchronous API call
  - Updates results or displays an error
  - Always removes the loading state
*/

  data() {
    return {
      searchTerm: '',
      operadoras: [], 
      loading: false,
      error: null
    };
  },
  methods: {
    async searchProviders() {
      if (!this.searchTerm.trim()) {
        this.operadoras = [];
        return;
      }

      this.loading = true;
      this.error = null;

      try {
        const response = await api.searchProviders(this.searchTerm); 
        this.operadoras = response.data;
      } catch (error) {
        this.error = error.response?.data?.message || 'Error searching for operators';
      } finally {
        this.loading = false;
      }
    }
  }
};
