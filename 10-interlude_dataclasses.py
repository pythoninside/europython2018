def dataclass(cls):
    def __init__(self, *args, **kwargs):
        for k, v in zip(cls.__annotations__.keys(), args):
            setattr(self, k, v)
        for k, v in kwargs.items():
            if k not in cls.__annotations__:
                raise TypeError(
                    f"__init__() got an unexpected keyword argument '{k}'"
                )
            setattr(self, k, v)

        post_init = getattr(self, '__post_init__', None)
        if callable(post_init):
            post_init()

    def __repr__(self):
        kwargs = {k: getattr(self, k) for k in cls.__annotations__}
        kwstr = ', '.join([f'{k}={v}' for k, v in kwargs.items()])
        return f'{cls.__name__}({kwstr})'

    setattr(cls, '__init__', __init__)
    setattr(cls, '__repr__', __repr__)
    setattr(cls, '__str__', __repr__)
    return cls


@dataclass
class Point:
    x: int
    y: int

    def __post_init__(self):
        print('  <<<Any further customizaion goes here>>>')
