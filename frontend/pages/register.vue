<template>
  <v-form v-model="valid" ref="form">
    <v-card>
      <v-card-title primary-title>User Registration</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="8">
            <v-text-field
              :rules="[rules.required, rules.min]"
              label="User Name"
              v-model="name"
              outlined
            />
            <v-text-field :rules="[rules.required]" label="Gamer Tag" v-model="gamer_tag" outlined />
            <v-text-field
              :rules="[rules.required, rules.email]"
              label="Email"
              v-model="email"
              outlined
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="4">
            <v-text-field
              label="Password"
              v-model="password"
              :append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
              :type="showPass ? 'text' : 'password'"
              :rules="[rules.required, rules.min]"
              outlined
              @click:append="showPass = !showPass"
            />
          </v-col>
          <v-col cols="4">
            <v-text-field
              label="Confirm Password"
              v-model="confPassword"
              :append-icon="showConfPass ? 'mdi-eye' : 'mdi-eye-off'"
              :type="showConfPass ? 'text' : 'password'"
              :rules="[rules.required, rules.min, passwordConfirmationRule]"
              outlined
              @click:append="showConfPass = !showConfPass"
            />
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-btn color="red" @click="register()">Register</v-btn>
        <v-btn text @click="reset()">Clear</v-btn>
        <v-spacer />
        <v-btn nuxt to="/" color="red" text x-small>Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-form>
</template>

<script>
import AppApi from '~api'
import Snacks from '~/helpers/Snacks.js'

export default {
  data: () => ({
    name: '',
    gamer_tag: '',
    email: '',
    password: '',
    avatar: '',

    valid: false,
    showPass: false,
    showConfPass: false,
    confPassword: '',

    rules: {
      required: value => !!value || 'Required.',
      min: v => (v && v.length >= 8) || 'Min 8 characters',
      email: v => /.+@.+/.test(v) || 'E-mail must be valid'
    }
  }),

  computed: {
    passwordConfirmationRule () {
      return () => this.password === this.confPassword || 'Password must match'
    }
  },

  methods: {
    register () {
      if (this.$refs.form.validate()) {
        const user = {}

        user.name = this.name
        user.gamer_tag = this.gamer_tag
        user.email = this.email
        user.password = this.password

        AppApi.register(user).then(response => {
          const result = JSON.parse(response.data)
          if (!result.error) {
            Snacks.show(this.$store, {
              text: 'Usuario Registrado',
              visible: true,
              color: 'success'
            })
            this.$router.push('/')
          }
        })
      } else {
        Snacks.show(this.$store, {
          text: 'Erro',
          visible: true,
          color: 'red'
        })
      }
    },

    reset () {
      this.$refs.form.reset()
    }
  }
}
</script>
