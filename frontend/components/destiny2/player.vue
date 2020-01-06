<template>
  <v-card class="mx-auto" outlined>
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4">{{player.id}}</div>
        <v-list-item-title class="headline mb-1">{{player.name}}</v-list-item-title>
        <v-list-item-subtitle>{{player.gamer_tag}}</v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar size="50">
        <v-img :src="player.avatar" />
      </v-list-item-avatar>
    </v-list-item>
  </v-card>
</template>

<script>
export default {
  props: ['player'],
  data () { return {} },
  methods: {}
}
</script>
