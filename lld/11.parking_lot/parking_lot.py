from enum import Enum
from datetime import datetime
import math

class VehicleType(Enum):
    BIKE = "bike"
    CAR = "car"

class ParkingSpotType(Enum):
    SMALL = "small"
    LARGE = "large"

class Vehicle:
    def __init__(self, id, vehicleType: VehicleType):
        self.id = id
        self.type = vehicleType

class ParkingSpot:
    def __init__(self, id, parkingSpotType: ParkingSpotType):
        self.id = id
        self.type = parkingSpotType
        self.isOccupied = False
        self.vehicle = None

    def parkVehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.isOccupied = True
    
    def unparkVehicle(self):
        self.vehicle = None
        self.isOccupied = False


class Ticket:
    def __init__(self, id, vehicle: Vehicle, parkingSpot: ParkingSpot):
        self.id = id
        self.vehicle = vehicle
        self.parkingSpot = parkingSpot
        self.entryTime = datetime.now()
        self.exitTime = None
        self.is_paid = False


class HourlyPricing:
    def __init__(self):
        self.rates = {
            ParkingSpotType.SMALL: (10, 5),   # Bikes: $10 base + $5/hr
            ParkingSpotType.LARGE: (20, 15),  # Cars:  $20 base + $15/hr
        }

    def calculate_fee(self, ticket: Ticket):
        duration = datetime.now() - ticket.entryTime
        total_hours = max(1, math.ceil(duration.total_seconds() / 3600))
        
        spot_type = ticket.parkingSpot.type
        base_fee, hourly_rate = self.rates[spot_type]
        
        return base_fee + (total_hours * hourly_rate)


class ParkingLot:
    def __init__(self, spots, pricing):
        self.spots = spots
        self.pricing = pricing
        self.ticket_counter = 1
        self.active_tickets = {}
        self.vehicle_to_spot = {
            VehicleType.BIKE: ParkingSpotType.SMALL,
            VehicleType.CAR: ParkingSpotType.LARGE,
        }

    def park_vehicle(self, vehicle):
        required_spot_type = self.vehicle_to_spot[vehicle.type]
        for spot in self.spots:
            if not spot.isOccupied and spot.type == required_spot_type:
                spot.isOccupied = True
                ticket = Ticket(self.ticket_counter, vehicle, spot)
                self.ticket_counter += 1
                self.active_tickets[ticket.id] = ticket
                print(f"Parked {vehicle.id} at spot {spot.id}. Ticket #{ticket.id}")
                return ticket

        print(f"Sorry, no spots available for {vehicle.type.value}")
        return None

    def exit_vehicle(self, ticket):
        if ticket is None or ticket.id not in self.active_tickets or ticket.is_paid:
            print("Error: Invalid or already used ticket!")
            return None
        fee = self.pricing.calculate_fee(ticket)
        ticket.exitTime = datetime.now()
        ticket.is_paid = True
        ticket.parkingSpot.isOccupied = False
        del self.active_tickets[ticket.id]
        print(f"Vehicle {ticket.vehicle.id} exited. Total Fee: ${fee}")
        return fee

# Test the parking lot setup
spots = [
    ParkingSpot("S1", ParkingSpotType.SMALL),
    ParkingSpot("L1", ParkingSpotType.LARGE),
]
pricing = HourlyPricing()
lot = ParkingLot(spots, pricing)

# Flow
bike = Vehicle("UP32-AB-1234", VehicleType.BIKE)
ticket = lot.park_vehicle(bike)   # Assigns S1, returns Ticket #1
fee = lot.exit_vehicle(ticket)    # Frees S1, charges $15 (10 + 5*1)