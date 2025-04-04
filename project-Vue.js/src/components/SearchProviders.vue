<template>

<!--
  OPERATOR SEARCH COMPONENT:
  Structure:
  1. Input field for search (v-model="searchTerm")
  2. Visual feedback during loading
  3. Error display (error)
  4. List of results (operators)
  Behavior:
  - Automatic search when typing (@input)
  - Displays spinner during loading
  - Shows errors if they occur
  - Renders list of operators found
-->

  <div class="container">
    <h1>🔍 Buscar Operadoras</h1>
    <input 
      v-model="searchTerm" 
      @input="searchProviders" 
      placeholder="Digite o nome da operadora..." 
      class="search-input"
    />

    <div v-if="loading" class="message loading">↻ Buscando...</div>
    <div v-else-if="error" class="message error">⚠️ {{ error }}</div>
    <ul v-else class="providers-list">
      <li v-for="operadora in operadoras" :key="operadora.Registro_ANS" class="provider-item">
        <h3>{{ operadora.Razao_Social }}</h3>
        <p>{{ operadora.Cidade }} - {{ operadora.UF }}</p>
      </li>
    </ul>
  </div>
</template>

<script src="./SearchProviders.js"></script>
<style scoped src="./SearchProviders.css"></style>
