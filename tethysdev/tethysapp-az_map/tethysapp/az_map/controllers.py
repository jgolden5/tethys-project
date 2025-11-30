from tethys_sdk.layouts import MapLayout
from tethys_sdk.routing import controller
from .app import App


@controller(name="home")
class HomeMap(MapLayout):
    app = App
    base_template = f'{App.package}/base.html'
    map_title = 'AZ Water'
    map_subtitle = 'Aquaveo Project'
    basemaps = ['OpenStreetMap', 'ESRI']

@controller(url='data/add')
def add_data(request):
    """
    Controller for the Add Data page.
    """
    context = {}
    return App.render(request, 'add_data.html', context)
