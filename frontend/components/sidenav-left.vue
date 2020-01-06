<template>
  <v-navigation-drawer fixed v-model="state.drawer" app>
    <navigation-menu />
    <online-friends />
  </v-navigation-drawer>
</template>

<script>
import navigation_menu from '@/components/navigation-menu.vue'
import online_friends from '@/components/online-friends.vue'

export default {

  components: {
    navigationMenu: navigation_menu,
    onlineFriends: online_friends
  },
  props: ['state']
}
</script>
