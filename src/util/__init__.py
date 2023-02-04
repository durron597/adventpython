def maybe(function):
    try:
        return function()
    except:
        return None


def coalesce(*arg):
    for el in arg:
        if el is not None:
            return el
    return None
