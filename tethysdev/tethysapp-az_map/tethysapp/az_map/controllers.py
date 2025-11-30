from django.contrib import messages
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
  #Default values
  name = ''
  owner = 'Reclamation'
  river = ''
  date_built = ''

  # Errors
  name_error = ''
  owner_error = ''
  river_error = ''
  date_error = ''

  # Handle form submission
  if request.POST and 'add-button' in request.POST:
    # Get values
    has_errors = False
    name = request.POST.get('name', None)
    owner = request.POST.get('owner', None)
    river = request.POST.get('river', None)
    date_built = request.POST.get('date-built', None)

    # Validate
    if not name:
      has_errors = True
      name_error = 'Name is required.'

    if not owner:
      has_errors = True
      owner_error = 'Owner is required.'

    if not river:
      has_errors = True
      river_error = 'River is required.'

    if not date_built:
      has_errors = True
      date_error = 'Date Built is required.'

    if not has_errors:
      # Do stuff here
      return App.redirect(App.reverse('home'))

    messages.error(request, "Please fix errors.")

  #Define form gizmos
  name_input = TextInput(
    display_text='Name',
    name='name',
    initial=name,
    error=name_error
  )

  owner_input = SelectInput(
    display_text='Owner',
    name='owner',
    multiple=False,
    options=[('Reclamation', 'Reclamation'), ('Army Corp', 'Army Corp'), ('Other', 'Other')],
    initial=owner,
    error=owner_error
  )

  river_input = TextInput(
    display_text='River',
    name='river',
    placeholder='Salt River',
    initial=river,
    error=river_error
  )

  date_built = DatePicker(
    name='date-built',
    display_text='Date Built',
    autoclose=True,
    format='MM d, yyyy',
    start_view='decade',
    today_button=True,
    initial=date_built,
    error=date_error
  )

  add_button = Button(
    display_text='Add',
    name='add-button',
    icon='plus-square',
    style='success',
    attributes={'form': 'add-data-form'},
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

