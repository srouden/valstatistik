class NestedDict(dict):
    def __getitem__(self, key):
        if key in self: 
            return self.get(key)

        return self.setdefault(key, NestedDict())
