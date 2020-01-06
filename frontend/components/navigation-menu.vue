<template>
  <v-list dense>
    <v-list-item link to="/">
      <v-list-item-action>
        <v-icon>mdi-home</v-icon>
      </v-list-item-action>
      <v-list-item-title>Home</v-list-item-title>
    </v-list-item>

    <v-list-item link to="/activity/create">
      <v-list-item-action>
        <v-icon color="red">mdi-plus</v-icon>
      </v-list-item-action>
      <v-list-item-title>Create</v-list-item-title>
    </v-list-item>

    <v-list-item link to="/timetable">
      <v-list-item-action>
        <v-icon>mdi-timetable</v-icon>
      </v-list-item-action>
      <v-list-item-title>Scheduled</v-list-item-title>
    </v-list-item>

    <v-list-item link>
      <v-list-item-action>
        <v-icon color="grey darken-1">mdi-timer-sand</v-icon>
      </v-list-item-action>
      <v-list-item-title class="grey--text text--darken-1">Coming Soon</v-list-item-title>
    </v-list-item>

    <v-list-item link>
      <v-list-item-action>
        <v-icon color="grey darken-1">mdi-history</v-icon>
      </v-list-item-action>
      <v-list-item-title class="grey--text text--darken-1">Last Played</v-list-item-title>
    </v-list-item>

    <v-list-item link to="grades">
      <v-list-item-action>
        <v-icon color="grey darken-1">mdi-trending-up</v-icon>
      </v-list-item-action>
      <v-list-item-title class="grey--text text--darken-1">Popular</v-list-item-title>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  props: {
  },
  data: () => ({})
}
</script>
