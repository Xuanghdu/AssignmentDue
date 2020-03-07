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

    def get_properties_dict(self):
        raise NotImplementedError()

    def loads(self, s):
        json_data = json.loads(s)
        properties_dict = self.get_properties_dict()
        for key in properties_dict:
            properties_dict[key] = json_data[key]

    def dumps(self, fp):
        return json.dumps(self.get_properties_dict())
