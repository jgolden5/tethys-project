from tethys_sdk.layouts import MapLayout
from tethys_sdk.routing import controller
from .app import App


@controller(name="home")
class HomeMap(MapLayout):
    app = App
    base_template = f'{App.package}/base.html'
    map_title = 'AZ Water'
    map_subtitle = 'Tutorial for Aquaveo interview'
    basemaps = ['OpenStreetMap', 'ESRI']
