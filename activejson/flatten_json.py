from itertools import chain, starmap


def flatten_json(dictionary):
    """Flatten a nested json file"""

    while True:
        dictionary = dict(chain.from_iterable(starmap(_unpack,
                                                      dictionary.items())))
        if _atomic_values(dictionary):
            break
    return dictionary


def _atomic_values(dictionary):
    return not _nested_dict(dictionary) and not _nested_list(dictionary)


def _process_dict_values(parent_key, key, value):
    temp1 = parent_key + '_' + key
    return temp1, value


def _proccess_list(parent_key, i, value):
    temp2 = parent_key + '_'+str(i)
    return temp2, value


def _nested_dict(dictionary):
    return any(isinstance(value, dict) for value in dictionary.values())


def _nested_list(dictionary):
    return any(isinstance(value, list) for value in dictionary.values())


def _unpack(parent_key, parent_value):
    """Unpack one level of nesting in json file"""
    # Unpack one level only!!!

    if isinstance(parent_value, dict):
        for key, value in parent_value.items():
            yield _process_dict_values(parent_key, key, value)
    elif isinstance(parent_value, list):
        for i, value in enumerate(parent_value):
            yield _proccess_list(parent_key, i, value)
    else:
        yield parent_key, parent_value
