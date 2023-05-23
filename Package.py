
class Package:

    def __init__(self, package_id, address, city, state, zipcode,
                 delivery_deadline, kilo, special_notes, delivery_status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self. kilo = kilo
        self.special_notes = special_notes
        self.delivery_status = delivery_status
