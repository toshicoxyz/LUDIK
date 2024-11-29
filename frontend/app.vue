<template>
  <div>
    <NuxtPage />
  </div>
</template>

<script setup lang="ts">
useServerHead({
  htmlAttrs: { lang: 'es' },
})
useSeoMeta({
  titleTemplate: 'To-do List',
  description: 'Prueba Técnica 24h',
  ogImage: '',
  ogImageAlt: 'Sin Image',
  twitterCreator: 'pedro',
  twitterCard: 'summary_large_image',
})
</script>


<style lang="postcss">
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  font-size: 15px;
  background-color: #F4F4F5;
  margin: 0;
  padding: 0;
  color: #020420;
  overflow-y: scroll;
}
</style>