import { get, post } from './ajaxutils'

export default {
  login (username, password) {
    return post('/api/login', { username, password }).then(response => response.data)
  },
  logout () {
    return post('/api/logout').then(response => response.data)
  },
  whoami () {
    return get('/api/whoami').then(response => response.data)
  },
  settings () {
    return get('/api/settings').then(response => response.data)
  },
  list_todos () {
    return get('/api/list_todos').then(response => response.data)
  },
  add_todo (newtask) {
    return post('/api/add_todo', { new_task: newtask }).then(response => response.data)
  },
  list_activities () {
    return this.search_activity(null, null, null)
  },

  search_activity (platform, name, date) {
    return get('/api/search_activity', {
      platform: JSON.stringify(platform),
      name: JSON.stringify(name),
      date: JSON.stringify(date)
    })
  },

  get_activity (id) {
    return get('/api/get_activity', { id })
  },

  save_activity (activity) {
    return post('/api/activity', { activity: JSON.stringify(activity) })
  },

  register (user) {
    return post('/api/register', { user: JSON.stringify(user) })
  },

  join_activity (activity_id) {
    return post('/api/activity/join', { activity_id: JSON.stringify(activity_id) })
  },

  leave_activity (activity_id) {
    return post('/api/activity/leave', { activity_id: JSON.stringify(activity_id) })
  }
}
