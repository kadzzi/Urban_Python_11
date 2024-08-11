from module_11_3 import introspection_info
from pprint import pprint


class MyTestClass:
    some_class_attr = [1, 15]

    def __init__(self):
        self.size = 54
        self.weight = 67

    def count_some_index(self):
        result = round((self.weight / self.size), 2)
        return result

    def print_info(self):
        print(f'Size: {self.size}\nWeight: {self.weight}\nIndex: {self.count_some_index()}')


if __name__ == "__main__":
    pprint(introspection_info(MyTestClass()))
