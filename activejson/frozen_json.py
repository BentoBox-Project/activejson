from collections import abc
import keyword


class FrozenJSON:

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __contains__(self, key):
        return key in self.__data

    def __getattr__(self, name):
        return self._get_attr(name)

    def __getitem__(self, key):
        return self._get_attr(key)

    def _get_attr(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            try:
                return FrozenJSON(self.__data[name])
            except KeyError:
                raise AttributeError

    def __str__(self):
        return f'FrozenJSON with keys: {list(self.__data.keys())}'

    def __repr__(self):
        return f'FrozenJSON with items: {list(self.__data.items())}'
