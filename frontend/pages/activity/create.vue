<template>
  <v-card flat>
    <v-img
      height="200"
      color="transparent"
      lazy-src="/activity_placeholder.jpg"
      :src="image_url"
      gradient="to bottom, rgba(0,0,0,.04), rgba(0,0,0,.9)"
      class="white--text align-end"
    >
      <v-card-title>Create Activity</v-card-title>
      <v-card-text>
        <v-autocomplete
          :items="activity_list"
          v-model="suggestion"
          label="Suggestion"
          :rules="required"
          required
          return-object
          item-text="displayProperties.description"
          item-value="hash"
          @change="suggest()"
        />
      </v-card-text>
    </v-img>
    <v-card-text>
      <v-row class="mt-0">
        <v-col cols="8">
          <v-select
            :items="platforms"
            v-model="activity.platform"
            label="Platform"
            :rules="required"
            required
            :append-icon="platform_icon"
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
      suggestion: {},
      activity: {
        id: null,
        platform: -1,
        name: '',
        description: '',
        date: new Date().toISOString().substr(0, 10),
        icon: '/activity_placeholder.jpg',
        image: this.image_url,
        max_players: 1
      }

    }
  },

  computed: {
    platform_icon () {
      switch (this.activity.platform) {
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

    image_url () {
      return this.suggestion.pgcrImage != null
        ? Destiny2.media_url + this.suggestion.pgcrImage : Destiny2.activity_images[0]
    }

  },

  asyncData (ctx) {
    return Destiny2.get_activity_list().then(response => {
      const list = []
      debugger
      Object.keys(response.data).forEach(k => {
        const obj = response.data[k]
        if (obj.displayProperties && obj.displayProperties.description) {
          list.push(obj)
        }
      })

      return {
        activity_list: list
      }
    })
  },

  mounted () {
    window.moment = moment
  },

  methods: {
    suggest () {
      this.activity.description = this.suggestion.displayProperties.description
      this.activity.name = this.suggestion.displayProperties.name
      this.activity.image = this.image_url
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
