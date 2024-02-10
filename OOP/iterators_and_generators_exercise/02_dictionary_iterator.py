from typing import Dict


class dictionary_iter:
    def __init__(self, dict_obj: Dict):
        self.dict_obj = tuple(dict_obj.items())
        self.current_index = 0
        self.end_index = len(self.dict_obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.end_index:
            raise StopIteration()
        index = self.current_index
        self.current_index += 1
        return self.dict_obj[index]


#   TEST CODE

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

print()

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)