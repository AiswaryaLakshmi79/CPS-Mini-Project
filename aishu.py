

from prettytable import PrettyTable
import random

class AiswaryaParkingSystem:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * capacity
        self.car_info = {}
        self.token_counter = 1

    def park(self, car_id, owner_name, vehicle_type, vehicle_name):
        if None in self.slots:
            slot_index = self.slots.index(None)
            self.slots[slot_index] = car_id
            token_number = self.generate_token()
            self.car_info[car_id] = {"owner": owner_name, "type": vehicle_type, "slot": slot_index + 1, "token": token_number, "vehicle_name": vehicle_name}
            print(f"Car {car_id} parked in slot {slot_index + 1} in Aiswarya Parking System")
            print(f"Owner: {owner_name}, Vehicle Type: {vehicle_type}, Vehicle Name: {vehicle_name}, Token Number: {token_number}")
        else:
            print("Aiswarya Parking System is full")

    def unpark(self, car_id):
        if car_id in self.car_info:
            slot_index = self.car_info[car_id]["slot"] - 1
            self.slots[slot_index] = None
            del self.car_info[car_id]
            print(f"Car {car_id} unparked from slot {slot_index + 1} in Aiswarya Parking System")
        else:
            print(f"Car {car_id} not found in Aiswarya Parking System")

    def display_status(self):
        table = PrettyTable(["Slot", "Car ID", "Owner Name", "Vehicle Type", "Vehicle Name", "Token Number"])
        for i, car_id in enumerate(self.slots):
            if car_id is not None:
                car_info = self.car_info[car_id]
                table.add_row([i + 1, car_id, car_info["owner"], car_info["type"], car_info["vehicle_name"], car_info["token"]])
            else:
                table.add_row([i + 1, "Empty", "-", "-", "-", "-"])
        print("Aiswarya Parking System Status:")  # Changed table title
        print(table)

    def generate_token(self):
        token = self.token_counter
        self.token_counter += 1
        return token

# Main program loop
parking_lot = AiswaryaParkingSystem(10)  # Create Aiswarya Parking System with 10 slots

while True:
    action = input("Enter action (1-park, 2-unpark, 3-status, 4-exit): ")

    if action == "1":
        car_id = input("Enter car ID: ")
        owner_name = input("Enter owner name: ")
        vehicle_type = input("Enter vehicle type (two-wheeler/four-wheeler): ").lower()
        vehicle_name = input("Enter vehicle name (e.g., Porsche, BMW): ")
        parking_lot.park(car_id, owner_name, vehicle_type, vehicle_name)
    elif action == "2":
        car_id = input("Enter car ID to unpark: ")
        parking_lot.unpark(car_id)
    elif action == "3":
        parking_lot.display_status()
    elif action == "4":
        break
    else:
        print("Invalid action. Please enter 1, 2, 3, or 4.")