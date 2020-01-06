<template>
  <v-card>
    <v-list-item>
      <v-list-item-avatar>
        <v-img :src="activity.icon" />
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title class="headline">{{activity.name}}</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-img
      :src="activity.image"
      lazy-src="/activity_placeholder.jpg"
      max-height="200"
      gradient="to bottom, rgba(0,0,0,.01), rgba(0,0,0,.6)"
      class="white--text align-end"
    >
      <v-card-title>
        <v-chip outlined class="mx-1">
          <v-icon>{{get_platform_icon(activity.platform)}}</v-icon>
        </v-chip>
        <v-chip outlined class="mx-1">
          <v-icon>mdi-calendar</v-icon>
          {{activity.date}}
        </v-chip>
        <v-chip outlined class="mx-1">{{activity.members.length}} / {{activity.max_players}} members</v-chip>
      </v-card-title>
    </v-img>

    <v-card-title />
    <v-card-text>{{activity.description}}</v-card-text>
    <v-divider />
    <v-card-title>Members</v-card-title>
    <v-card-text>
      <v-row>
        <v-col v-for="p in activity.members" :key="p.id" cols="4">
          <player :player="p" />
        </v-col>
      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-btn text v-if="logged_user && user_can_join" @click="join()">Join</v-btn>
      <v-btn text v-if="logged_user && user_can_leave" @click="leave()">Leave</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import Snacks from '~/helpers/Snacks.js'
import AppApi from '~api'
import Player from '~/components/destiny2/player.vue'

export default {
  components: {
    player: Player
  },

  data () {
    return {}
  },

  computed: Object.assign(
    {
      user_can_join () {
        return (
          this.logged_user &&
          !this.members_id_list.includes(this.logged_user.id)
        )
      },

      members_id_list () {
        const r = []
        this.activity.members.forEach(member => {
          r.push(member.id)
        })
        return r
      },

      user_can_leave () {
        return (
          this.logged_user && this.members_id_list.includes(this.logged_user.id)
        )
      },
      logged_user () {
        return this.$store.state.auth.currentUser
      }
    }
  ),

  asyncData (ctx) {
    return AppApi.get_activity(ctx.params.id).then(response => {
      return {
        activity: JSON.parse(response.data)
      }
    })
  },

  validate ({ params }) {
    return /^\d+$/.test(params.id)
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

    join () {
      AppApi.join_activity(this.activity.id).then(response => {
        this.activity = JSON.parse(response.data)
        Snacks.show(this.$store, { text: 'Joined' })
      })
    },

    leave () {
      AppApi.leave_activity(this.activity.id).then(response => {
        this.activity = JSON.parse(response.data)
        Snacks.show(this.$store, { text: 'Left' })
      })
    }
  }
}
</script>

<style>
</style>
