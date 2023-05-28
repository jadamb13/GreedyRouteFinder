class Truck:
    def __init__(self):
        self.packages = []
        self.mileage = 0
        self.last_delivered_package_time = "08:00"
        self.location = ""

    def get_packages(self):
        return self.packages

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, mileage):
        self.mileage = mileage

    def set_last_delivered_package_time(self, time):
        self.last_delivered_package_time = time

    def get_last_delivered_package_time(self):
        return self.last_delivered_package_time

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location
