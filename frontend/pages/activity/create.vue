<template>
  <v-card flat>
    <v-card-title>Create Activity</v-card-title>
    <v-card-text>
      <v-row>
        <v-col cols="8">
          <v-select
            :items="platforms"
            v-model="activity.platform"
            label="Platform"
            :rules="required"
            required
          />
          <v-text-field label="Activity" class="mt-2" v-model="activity.name" outlined required />
          <v-textarea label="Description" v-model="activity.description" outlined required />
          <v-slider
            class="mt-3"
            v-model="activity.max_players"
            thumb-label="always"
            min="1"
            max="6"
            label="Max Players"
            required
            ticks="always"
            color="red"
          />
        </v-col>
        <v-col cols="4">
          <v-date-picker
            :min="today"
            v-model="activity.date"
            :locale="locale"
            @input="dateMenu = false"
            light
            required
            color="red"
          />
        </v-col>
      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-btn color="red" @click="save()">Save</v-btn>
      <v-btn text nuxt to="/">Cancel</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import moment from 'moment'
import Snacks from '~/helpers/Snacks.js'
import AppApi from '~api'
import Destiny2 from '~/helpers/destiny2.js'

export default {
  data () {
    return {
      step: 1,
      locale: moment().locale(),
      today: moment().format('L'),
      date: new Date().toISOString().substr(0, 10),
      dateMenu: false,
      platforms: Destiny2.platforms,
      required: [v => !!v || 'Must not be null'],

      activity: {
        id: null,
        platform: 0,
        name: '',
        description: '',
        date: new Date().toISOString().substr(0, 10),
        icon: '/activity_placeholder.jpg',
        image: '/activity_placeholder.jpg',
        max_players: 1
      }
    }
  },

  mounted () {
    window.moment = moment
  },

  methods: {
    get_platform_icon (value) {
      switch (value) {
        case 1:
          return 'mdi-playstation'
        case 2:
          return 'mdi-xbox'
        case 3:
          return 'mdi-desktop-mac'
        default:
          return 'mdi-crosshairs-question'
      }
    },

    save () {
      AppApi.save_activity(this.activity).then(response => {
        if (response.error) {
          Snacks.show(this.$store, {
            text: 'Error: ' + response.error.message,
            visible: true,
            color: 'error'
          })
        } else {
          const activity_id = JSON.parse(response.data)
          this.$router.push({
            name: 'activity-id',
            params: { id: activity_id }
          })
        }
      })
    }
  }
}
</script>

<style>
</style>
