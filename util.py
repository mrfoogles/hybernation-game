# Useful functions that you don't want to duplicate across files
def has(**kwargs):
    def fn(x):
        for v in kwargs:
            if not hasattr(x,v):
                return False
            elif getattr(x,v) != kwargs[v]:
                return False
        return True
    return fn

def gate(fn,**kwargs):
    def newfn(x):
        if has(**kwargs)(x):
            fn(x)
    return newfn
    