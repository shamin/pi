from pywizlight import wizlight, PilotBuilder, discovery

await discovery.discover_lights()

bulbs = await discovery.discover_lights()

light = wizlight(bulbs[0].ip)

await light.turn_off(PilotBuilder())
