@view_config(route_name='index', renderer='json')
def index(request):
    return dict(count=279)
def includeme(config):
    config.scan(_name_)
    config.add_route('index', '/')
