from .join_api import JoinApi

def init_join_api(api):
    api.add_resource(JoinApi, "/api/users/join")