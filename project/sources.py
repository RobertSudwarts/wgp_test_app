import json

from ojota.sources import JSONSource


class CustomJSONSource(JSONSource):

    def read_elements(self, cls, filepath):
        json_path = '%s.json' % filepath
        try:
            json_file = open(json_path, 'r')
            data = json.load(json_file)
        except IOError:
            if self.create_empty:
                json_file = open(json_path, 'w')
                json_file.write("[]")
                json_file.close()
                json_file = open(json_path, 'r')
                data = json.load(json_file)
            else:
                data = []

        import ipdb; ipdb.set_trace()
        try:
            elements = dict((element_data[cls.pk_field], element_data) for element_data in data)
        except KeyError:
            msg = "Primary key was not found. Check that you have "
            msg += "configured the class correctly. In case you "
            msg += "have check your data source"
            raise AttributeError(msg)

        return elements