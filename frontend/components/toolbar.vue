<template>
  <v-app-bar color="red" fixed app clipped-right>
    <v-app-bar-nav-icon @click.stop="state.drawer = !state.drawer" />
    <v-toolbar-title>Destiny 2 Activity Finder</v-toolbar-title>
    <v-spacer />
    <v-btn
      v-if="!logged_user"
      text
      dark
      ripple
      class="ma-0 ml-5"
      @click="open_login_dialog($event)"
    >
      Login
    </v-btn>

    <!-- <template v-slot:activator="{ on }"><v-btn v-on="on"> -->
    <v-menu v-if="logged_user" offset-y>
      <template v-slot:activator="{ on }">
        <v-btn icon v-on="on">
          <v-img
            color="transparent"
            height="45"
            width="45"
            lazy-src="/avatar_placeholder.png"
            :src="logged_user.avatar"
          />
        </v-btn>
      </template>
      <v-card>
        <v-list two-line>
          <v-list-item>
            <v-list-item-avatar>
              <v-img
                color="transparent"
                height="45"
                width="45"
                lazy-src="/avatar_placeholder.png"
                :src="logged_user.avatar"
              />
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title>{{logged_user.username}}</v-list-item-title>
              <v-list-item-subtitle>{{logged_user.email}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-divider />
        <v-list>
          <v-list-item @click="logout()">
            <v-list-item-content>
              <v-list-item-title>Log out</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card>
    </v-menu>
    <login-dialog ref="login_dialog" />
  </v-app-bar>
</template>

<script>
import loginDialog from '~/components/login-dialog.vue'
import Snacks from '~/helpers/Snacks.js'
import api from '~api'

export default {
  components: {
    loginDialog
  },
  props: ['state'],
  computed: {
    logged_user () {
      return this.$store.state.auth.currentUser
    }
  },
  methods: {
    open_login_dialog (evt) {
      this.$refs.login_dialog.open()
      evt.stopPropagation()
    },
    logout () {
      api.logout().then(() => {
        this.$store.commit('auth/setCurrentUser', null)
        Snacks.show(this.$store, { text: 'Até logo!' })
      })
    }
  }
}
</script>
