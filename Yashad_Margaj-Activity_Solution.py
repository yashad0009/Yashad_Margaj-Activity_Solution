#creating a class for code reusability
class ParkingLotManager:
    #a function to initialize the required variables
    def __init__(self):
        #creating a dictionary to represent the parking lot
        self.parking_lot = {}

    #a function to create a parking lot
    def create_parking_lot(self, n):
        #initializing the parking slots as zeros to represent empty slots
        for _ in range(1, n + 1):
            self.parking_lot[_] = 0
        return 'Created parking of {} slots'.format(n)

    #a function to allocate a parking slot to a car
    def park_a_car(self, num, age):
        for _ in self.parking_lot:
            if self.parking_lot[_] == 0:
                self.parking_lot[_] = [num, age]
                return 'Car with vehicle registration number {} has been parked at slot number {}'.format(num, _)
        return 'Currently, the parking lot is full. Please come again after some time'

    #a function to vacate a parking slot
    def vacate_a_slot(self, slot):
        if self.parking_lot[slot] == 0:
            return 'Slot already vacant.'
        res = 'Slot number {} vacated, the car with vehicle registration number {} left the space, the driver of the car was of age {}'.format(slot, self.parking_lot[slot][0], self.parking_lot[slot][1])
        self.parking_lot[slot] = 0
        return res

    #a function to print the parking slot number, considering the vehicle registration number
    def print_slot_number(self, num):
        for _ in self.parking_lot:
            if self.parking_lot[_] != 0:
                if self.parking_lot[_][0] == num:
                    return _
        return 'Currently, no such car with the specified vehicle registration number is present in the parking lot'

    #a function to fetch the parking slot numbers, considering the age of the driver
    def get_slot_numbers(self, age):
        res = []
        for _ in self.parking_lot:
            if self.parking_lot[_] != 0:
                if self.parking_lot[_][1] == age:
                    res.append(str(_))
        return ', '.join(res)

    #a function to fetch the vehicle registration numbers, considering the age of the driver
    def get_vehicle_registration_numbers(self, age):
        res = []
        for _ in self.parking_lot:
            if self.parking_lot[_] != 0:
                if self.parking_lot[_][1] == age:
                    res.append(self.parking_lot[_][0])
        return ', '.join(res)

parking_lot_manager = ParkingLotManager()
file = open('input.txt', 'r')
for _ in file.readlines():
    command = _.split()
    if command[0] == 'Create_parking_lot':
        print(parking_lot_manager.create_parking_lot(int(command[1])))
    if command[0] == 'Park':
        print(parking_lot_manager.park_a_car(command[1], command[3]))
    if command[0] == 'Leave':
        print(parking_lot_manager.vacate_a_slot(int(command[1])))
    if command[0] == 'Slot_number_for_car_with_number':
        print(parking_lot_manager.print_slot_number(command[1]))
    if command[0] == 'Slot_numbers_for_driver_of_age':
        print(parking_lot_manager.get_slot_numbers(command[1]))
    if command[0] == 'Vehicle_registration_number_for_driver_of_age':
        print(parking_lot_manager.get_vehicle_registration_numbers(command[1]))
file.close()
