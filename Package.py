class Package:

    def __init__(self, package_id, address, city, state, zipcode,
                 deadline, weight):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = "At hub"
        self.delivery_time = "N/A"

    def __str__(self):  # overwrite print(Package), otherwise it will print object reference
        address = self.address + " " + self.city + " " + self.state + " " + self.zipcode

        return "%-5s %-70s %-10s %-15s %-15s %s" % (
            self.package_id, address, self.weight, self.deadline, self.status, self.delivery_time)

    def get_package_id(self):
        return self.package_id

    def get_deadline(self):
        return self.deadline

    def set_delivery_time(self, time):
        self.delivery_time = time

    def get_delivery_time(self):
        return self.delivery_time

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status



