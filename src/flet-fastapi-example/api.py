

api = {}


def register(f):
    api[f.__name__] = f
    return f


def get():
    return api
