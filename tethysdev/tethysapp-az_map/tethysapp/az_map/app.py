from tethys_sdk.base import TethysAppBase


class App(TethysAppBase):
    """
    Tethys app class for Az Map.
    """
    name = 'Az Map'
    description = 'An app containing details about water in Arizona. Demo project for Aquaveo.'
    package = 'az_map'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/cactus.jpeg'
    root_url = 'az-map'
    color = '#efcdab'
    tags = ''
    enable_feedback = False
    feedback_emails = []
