from tethys_sdk.base import TethysAppBase


class App(TethysAppBase):
    """
    Tethys app class for Az Map.
    """
    name = 'Az Map'
    description = 'An app containing details about water in Arizona. Demo project for Aquaveo.'
    package = 'az_map'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'az-map'
    color = '#00aa00'
    tags = ''
    enable_feedback = False
    feedback_emails = []
