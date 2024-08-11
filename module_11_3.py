import inspect


def introspection_info(obj):
    total_info = {}
    total_info['type'] = type(obj).__name__
    total_info['attributes'] = [x for x in dir(obj) if not callable(getattr(obj, x))]
    total_info['methods'] = [x for x in dir(obj) if callable(getattr(obj, x))]
    total_info['bound_methods'] = [x for x in dir(obj) if inspect.ismethod(getattr(obj, x))]
    if inspect.getmodule(obj) is None:
        total_info['module'] = '__main__'
    else:
        total_info['module'] = inspect.getmodule(obj).__name__

    return total_info


if __name__ == "__main__":
    number_info = introspection_info(42)
    print(number_info)
