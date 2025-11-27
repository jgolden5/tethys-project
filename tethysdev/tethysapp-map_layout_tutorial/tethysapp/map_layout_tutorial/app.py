from tethys_sdk.base import TethysAppBase


class App(TethysAppBase):
    """
    Tethys app class for tutorial.
    """
    name = 'tutorial'
    description = 'it's a tutorial for tethys so I can apply to aquaveo'
    package = 'map_layout_tutorial'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'map-layout-tutorial'
    color = '#ff00ff'
    tags = ''
    enable_feedback = False
    feedback_emails = []
