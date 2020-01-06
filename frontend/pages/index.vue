<template>
  <v-form v-model="valid" ref="form">
    <v-container>
      <v-row>
        <v-col cols="12" md="3">
          <v-select
            :items="platforms"
            v-model="platform"
            label="Platform"
            :rules="platformRules"
            required
            outlined
          />
        </v-col>

        <v-col cols="12" md="3">
          <v-text-field label="Activity" v-model="activityName" outlined />
        </v-col>

        <v-col cols="12" md="3">
          <v-menu
            v-model="dateMenu"
            :close-on-content-click="true"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
                v-model="date"
                label="Start Date"
                append-icon="mdi-calendar"
                readonly
                v-on="on"
              />
            </template>
            <v-date-picker
              v-model="date"
              no-title
              :min="today"
              :locale="locale"
              @input="dateMenu = false"
            />
          </v-menu>
        </v-col>
        <v-col cols="12" md="3">
          <v-btn :disabled="!valid" @click="search">Flter</v-btn>
          <v-btn :disabled="!valid" @click="clear()">Clear</v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col v-for="a in activities" :key="a.id" cols="12" md="4">
          <activity :activity="a" />
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import moment from 'moment'
import AppApi from '~api'
import Activity from '~/components/destiny2/activity.vue'
import Snacks from '~/helpers/Snacks.js'
import Destiny2 from '~/helpers/destiny2.js'

export default {

  components: {
    activity: Activity
  },

  data: () => ({
    locale: moment.locale,
    today: moment().format('L'),
    date: new Date().toISOString().substr(0, 10),
    dateMenu: false,
    platforms: Destiny2.platforms,
    valid: false,
    platform: -1,
    activityName: '',
    platformRules: [v => !!v || 'Platform is required']
  }),
  // layout: "defaultindex copy",

  asyncData (ctx) {
    return AppApi.list_activities().then(response => {
      Snacks.show(ctx.app.store, { text: 'Done' })
      return {
        activities: JSON.parse(response.data)
      }
    })
  },

  mounted () {
    window.moment = moment
  },

  methods: {
    search () {
      if (this.$refs.form.validate()) {
        AppApi.search_activity(
          this.platform,
          this.activityName,
          this.date
        ).then(response => {
          const result = JSON.parse(response.data)
          this.activities = result
          Snacks.show(this.$store, {
            text: 'Atualizado',
            visible: true,
            color: 'success'
          })
        })
      } else {
        Snacks.show(this.$store, {
          text: 'Erro',
          visible: true,
          color: 'red'
        })
      }
    },

    clear () {
      this.date = new Date().toISOString().substr(0, 10)
      this.platform = -1
      this.activityName = ''
      this.search()
    }
  }
}
</script>
