import inspect


def introspection_info(obj):
    total_info = {}
    total_info['type'] = type(obj).__name__
    total_info['attributes'] = [x for x in dir(obj) if not callable(x)]
    total_info['methods'] = [x for x in dir(obj) if callable(x)]
    total_info['module'] = __name__
    if inspect.getmodule(obj) is None:
        total_info['source'] = '__main__'
    else:
        total_info['source'] = inspect.getmodule(obj).__name__

    return total_info


number_info = introspection_info(42)
print(number_info)
