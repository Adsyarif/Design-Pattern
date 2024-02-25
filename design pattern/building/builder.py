class HomeBuilder:
    def __init__(self):
        self.home = {
            "size": 0,
            "bedroom": 0,
            "bathroom": 0,
            "kitchen": 0,
            "garage": 0
        }

    def set_size(self, size):
        self.home["size"] = size
        return self

    def add_bedroom(self, bedroom):
        self.home["bedroom"] += bedroom
        return self

    def add_bathroom(self, bathroom):
        self.home["bathroom"] += bathroom
        return self

    def add_kitchen(self, kitchen):
        self.home["kitchen"] += kitchen
        return self

    def add_garage(self, garage):
        self.home["garage"] = garage
        return self

    def build(self):
        return self


builder = HomeBuilder()
my_home = builder.set_size(10)\
    .add_bathroom(2)\
    .add_bedroom(4)\
    .add_garage(1)\
    .add_kitchen(1)\
    .build()

print(my_home.home)
