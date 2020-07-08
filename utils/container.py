

class Container:
    """Dependency Injection Container Class"""

    def __init__(self):
        self.bindings = {}

    def register(self, abstract, factory):
        self.bindings[abstract] = factory

    def get(self, abstract):
        return self.bindings[abstract](self)
