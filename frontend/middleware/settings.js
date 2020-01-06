export default (ctx) => {
  if (!ctx.store.getters['settings/loaded'] && !ctx.req.url.startsWith('/erro')) {
    return ctx.store.dispatch('settings/load').catch(e => {
      if (process.server) {
        console.error(`settings middleware error on ${ctx.req.url}`)  // eslint-disable-line
      }
    })
  }
}
