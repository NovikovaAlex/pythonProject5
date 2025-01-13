def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and method.startswith("__") is False]
    try:
        obj_module = obj.__module__
    except AttributeError:
        obj_module = "N/A"
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
    }
    return info

class House():
    def __init__(self, name, numbers_of_floor):
        self.name = name
        self.numbers_of_floor = numbers_of_floor

number_info = introspection_info(42)
print(number_info)
str_info = introspection_info('Hello')
print(str_info)
list_info = introspection_info([1,2,'hi'])
print(list_info)
house = House('Home', 4)
house_info = introspection_info(house)
print(house_info)