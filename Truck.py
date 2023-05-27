class Truck:
    def __init__(self):
        self.packages = []
        self.mileage = 0

    def get_packages(self):
        return self.packages

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, mileage):
        self.mileage = mileage
