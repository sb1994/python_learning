# Native decorators can lose importanct metadata
def noop(f):
    def noop_wrapper():
        return f()
    return noop_wrapper


def hello():
    print('Hello world')
