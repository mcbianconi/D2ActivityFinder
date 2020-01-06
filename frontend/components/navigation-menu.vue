<template>
  <v-list dense>
    <v-list-item link to="/">
      <v-list-item-action>
        <v-icon>mdi-home</v-icon>
      </v-list-item-action>
      <v-list-item-title>Home</v-list-item-title>
    </v-list-item>

    <v-list-item link to="/activity/create" v-if="logged_user">
      <v-list-item-action>
        <v-icon color="red">mdi-plus</v-icon>
      </v-list-item-action>
      <v-list-item-title>Create</v-list-item-title>
    </v-list-item>

    <v-list-item link to="/timetable" v-if="logged_user">
      <v-list-item-action>
        <v-icon>mdi-timetable</v-icon>
      </v-list-item-action>
      <v-list-item-title>Scheduled</v-list-item-title>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  props: {},
  data: () => ({}),
  computed: {
    logged_user () {
      return this.$store.state.auth.currentUser
    }
  }
}
</script>
