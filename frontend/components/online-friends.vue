<template>
  <v-list dense>
    <v-subheader class="mt-4 grey--text text--darken-1">Online Guardians (not implemented)</v-subheader>
    <v-list>
      <v-list-item v-for="item in items2" :key="item.text" link>
        <v-list-item-avatar>
          <v-skeleton-loader boilerplate tile type="avatar" />
        </v-list-item-avatar>
        <v-list-item-title v-text="item.text" />
      </v-list-item>
    </v-list>
  </v-list>
</template>

<script>
export default {
  props: {
  },
  data: () => ({
    items2: [
      { picture: 28, text: 'Guardian 1' },
      { picture: 38, text: 'Titan' },
      { picture: 48, text: 'Ranger' },
      { picture: 58, text: 'Warlock' },
      { picture: 78, text: 'Human' }
    ]
  })
}
</script>
