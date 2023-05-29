class Truck:
    def __init__(self, id):
        self.id = id
        self.packages = []
        self.mileage = 0
        self.last_delivered_package_time = "08:00"
        self.location = ""
        self.end_route_time = "N/A"

    def get_truck_id(self):
        return self.id

    def set_truck_id(self, id):
        self.id = id

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

    def set_end_route_time(self, time):
        self.end_route_time = time

    def get_end_route_time(self):
        return self.end_route_time