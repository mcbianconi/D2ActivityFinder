import moment from 'moment'
import { mockasync } from './mockutils'

const keepLoggedIn = true

const user = {
  id: 1,
  username: 'username',
  name: 'User Name',
  email: 'user@na.me',
  permissions: {ADMIN: true}
}

const activities = [
  {
    id: '1',
    platform: 0,
    name: 'Atividade 1',
    description: 'Descricao da atividade 1',
    date: moment().add(2, 'days').format('L'),
    icon: '/activity_placeholder.jpg',
    image: '/activity_placeholder.jpg',
    max_players: 3,
    members: [{ id: '1', name: 'Guardian 1', gamer_tag: '@tag1', platform: 1, avatar: '/avatar-placeholder.png' },
      { id: '4', name: 'Guardian 4', gamer_tag: '@tag4', platform: 1, avatar: '/avatar-placeholder.png' },
      { id: '5', name: 'Guardian 5', gamer_tag: '@tag5', platform: 1, avatar: '/avatar-placeholder.png' }]
  },
  {
    id: '2',
    platform: 1,
    name: 'Atividade 2 que tem um nome muito grande',
    description: 'Descricao da atividade 2 que tambem e muito muito muito muito muito muito muito muito muito muito muito muito muito muito muito muito muito muito grande mesmoo',
    date: moment().format('L'),
    icon: '/activity_placeholder.jpg',
    image: '/activity_placeholder.jpg',
    max_players: 6,
    members: [{ id: '1', name: 'Guardian 1', gamer_tag: '@tag1', platform: 1, avatar: '/avatar-placeholder.png' },
      { id: '2', name: 'Guardian 2', gamer_tag: '@tag2', platform: 1, avatar: '/avatar-placeholder.png' },
      { id: '3', name: 'Guardian 3', gamer_tag: '@tag3', platform: 1, avatar: '/avatar-placeholder.png' }]
  }
]

export default {
  login (username, password) {
    return mockasync(JSON.stringify(user)).then(response => response.data)
  },
  logout () {
    return mockasync({}).then(response => response.data)
  },
  whoami () {
    const iam = { authenticated: keepLoggedIn }
    if (iam.authenticated) {
      iam.user = user
    }
    return mockasync(iam).then(response => response.data)
  },
  settings () {
    return mockasync({
      SENTRY_DSN_FRONT: ''
      // SENTRY_DSN_FRONT: 'https://abcd1234@sentry.example.com/10'
    }).then(response => response.data)
  },

  list_activities () {
    return mockasync(JSON.stringify(activities))
  },

  search_activity (platform, activityName, date) {
    return mockasync(JSON.stringify(activities))
  },

  get_activity (id) {
    return mockasync(JSON.stringify(activities[id - 1]))
  },

  save_activity (activity) {
    return mockasync(JSON.stringify(1))
  },

  register (user) {
    return mockasync(JSON.stringify(1))
  },

  join_activity (activity_id) {
    return mockasync(JSON.stringify(activities[0]))
  },

  leave_activity (activity_id) {
    return mockasync(JSON.stringify(activities[0]))
  }
}
