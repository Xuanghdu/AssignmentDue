import json


class Base:

    uuid_count = 0
    uuid_to_object = {}

    @classmethod
    def generate_uuid(cls):
        cls.uuid_count += 1
        return cls.uuid_count - 1

    def __init__(self):
        self.uuid = Base.generate_uuid()
        assert(self.uuid not in Base.uuid_to_object)
        Base.uuid_to_object[self.uuid] = self

    def load_json_dict(self, json_dict):
        raise NotImplementedError()

    def dump_json_dict(self):
        raise NotImplementedError()
