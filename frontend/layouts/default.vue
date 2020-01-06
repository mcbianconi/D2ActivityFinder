<template>
  <v-app id="inspire">
    <toolbar :state="layout" />
    <sidenav-left :state="layout" />
    <v-content>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-content>
    <v-snackbar
      :timeout="snack.timeout"
      :color="snack.color"
      bottom
      v-model="snack.visible"
    >
      {{snack.text}}
      <v-btn dark text @click.native="closeSnack">Close</v-btn>
    </v-snackbar>
  </v-app>
</template>

<script>
import toolbar from '~/components/toolbar.vue'
import sidenavLeft from '~/components/sidenav-left.vue'
export default {
  components: {
    toolbar,
    sidenavLeft
  },
  data: () => ({
    layout: {
      drawer: true
    }
  }),
  computed: {
    snack () {
      return JSON.parse(JSON.stringify(this.$store.state.snack.snack))
    }
  },
  methods: {
    closeSnack () {
      this.$store.commit('snack/hide')
    }
  }
}
</script>
