<template>
  <v-card class="mx-auto" max-width="450">
    <v-img
      height="150"
      lazy-src="/activity_placeholder.jpg"
      :src="activity.image"
      gradient="to bottom, rgba(0,0,0,.01), rgba(0,0,0,.6)"
    >
      <v-row align="end" class="fill-height">
        <v-col>
          <v-icon large class="ml-2">{{get_platform_icon(activity.platform)}}</v-icon>
        </v-col>
        <v-spacer />
        <v-col>
          <v-chip outlined class="mr-1">
            <v-icon left small>mdi-calendar</v-icon>
            {{activity.date}}
          </v-chip>
          <!-- <v-img height="80" width="80" :src="activity.icon"></v-img> -->
        </v-col>
      </v-row>
    </v-img>

    <v-card-title>
      <v-row>
        <v-col cols="8">
          <span class="title font-weight-light">{{activity.name }}</span>
        </v-col>
        <v-spacer />
        <v-col />
      </v-row>
      <v-row />
    </v-card-title>
    <v-card-text>
      <v-row align="center" class="mx-0">
        <v-col>
          <v-rating
            :length="activity.max_players"
            readonly
            color="red"
            background-color="grey lighten-1"
            :value="activity.members.length"
            full-icon="mdi-account"
            empty-icon="mdi-account-outline"
            dense
          />
        </v-col>
        <!-- <v-spacer></v-spacer> -->
        <v-col>
          <div
            class="grey--text ml-4"
          >
            {{activity.members.length}} / {{activity.max_players}} players
          </div>
        </v-col>
      </v-row>
      <div>{{activity.description}}</div>
    </v-card-text>

    <v-divider class="mx-4" />
    <v-card-actions>
      <v-btn
        color="dark-blue"
        @click="open(activity)"
      >
        View
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>

export default {

  props: ['activity'],
  data () {
    return {
      media_url: 'https://bungie.net'
    }
  },
  methods: {
    open () {
      this.$router.push({
        name: 'activity-id',
        params: { id: this.activity.id }
      })
    },

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
    }
  }
}
</script>
