import axios from '~/plugins/axios'

const X_API_KEY = '96dc1e28312448378b1f8c0d28532ec9'
const BUNGIE_API_URL = '/destiny2'
const api = {

  media_url: 'https://bungie.net',

  get_activity_list () {
    const manifest = '/DestinyActivityDefinition.json'
    return axios.get(manifest)
  },

  platforms: [
    { text: 'All', value: -1 },
    { text: 'PS4', value: 1 },
    { text: 'XBOX', value: 2 },
    { text: 'PC', value: 3 }
  ],

  avatars: [
    { name: 'Default', path: '/avatar_placeholder.png' },
    { name: 'Ghost', path: '/avatars/ghost.png' },
    { name: 'Hunter', path: '/avatars/hunter.png' },
    { name: 'Titan', path: '/avatars/titan.png' },
    { name: 'Warlock', path: '/avatars/warlock.png' }
  ],

  activity_images: [
    { name: 'Default', path: '/avatar_placeholder.png' },
    { name: 'Ghost', path: '/avatars/ghost.png' },
    { name: 'Hunter', path: '/avatars/hunter.png' },
    { name: 'Titan', path: '/avatars/titan.png' }
  ],

  search_activities (term) {
    const ENDPOINT = '/Armory/Search/DestinyActivityDefinition/' + term
    return get(BUNGIE_API_URL + ENDPOINT, {})
  }

}
export default api

function get (url, config) {
  config.headers = {}
  config.headers['X-API-Key'] = X_API_KEY
  config.headers['Content-Type'] = 'application/json; charset=utf-8'
  return axios.get(url, config)
}
