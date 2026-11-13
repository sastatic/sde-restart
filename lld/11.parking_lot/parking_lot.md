# Design a Parking Lot system.

1. can have multiple entry/exit gate.
    - 1 Entry
    - 1 Exit
2. can support multiple vehicles
    - bike (small/bike spot)
    - cars (Large spot)

3. Charges
    - Base
    - Hourly

4. Parking spot should be nearest
5. For now only single floor.


### Nouns:
- vehicle
    - type (enum=bike/car)
    - id

- parkingSpot
    - SpotType enum: SMALL, LARGE
    - is_occupied
    - distance_from_gate

- floor
    - parkingfloor


