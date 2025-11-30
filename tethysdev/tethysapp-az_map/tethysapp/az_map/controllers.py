from tethys_sdk.gizmos import Button, DatePicker, SelectInput, TextInput
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
  #Define form gizmos
  name_input = TextInput(
    display_text='Name',
    name='name'
  )

  owner_input = SelectInput(
    display_text='Owner',
    name='owner',
    multiple=False,
    options=[('Reclamation', 'Reclamation'), ('Army Corp', 'Army Corp'), ('Other', 'Other')],
    initial=['Reclamation']
  )

  river_input = TextInput(
    display_text='River',
    name='river',
    placeholder='e.g.: Mississippi River'
  )

  date_built = DatePicker(
    name='date-built',
    display_text='Date Built',
    autoclose=True,
    format='MM d, yyyy',
    start_view='decade',
    today_button=True,
    initial='February 15, 2017'
  )

  add_button = Button(
    display_text='Add',
    name='add-button',
    icon='plus-square',
    style='success',
    attributes={'form': 'add-dam-form'},
    submit=True
  )

  cancel_button = Button(
    display_text='Cancel',
    name='cancel-button',
    href=App.reverse('home')
  )

  context = {
    'name_input': name_input,
    'owner_input': owner_input,
    'river_input': river_input,
    'date_built_input': date_built,
    'add_button': add_button,
    'cancel_button': cancel_button,
  }

  return App.render(request, 'add_data.html', context)
