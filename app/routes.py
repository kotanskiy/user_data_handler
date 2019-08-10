from .views import *


def setup_routes(app):
    app.router.add_route('GET', '/', index_handler)
    app.router.add_route('GET', '/ws_user_data_handler', websocket_user_data_handler)
