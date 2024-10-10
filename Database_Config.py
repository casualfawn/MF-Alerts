from sqlalchemy import create_engine

class BF_Con:
    def __init__(self, user, password, server = None):
        self.user = user
        self.password = password
        self.server = server if server else 'biofac-llc.io'
