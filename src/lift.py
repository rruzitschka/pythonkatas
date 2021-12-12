# implement lift functions
import time
# constant number of floors
NR_FLOORS = 10
OPEN= True
CLOSED = False

class Lift:
    def __init__(self, initial_floor):
        self.current_floor = initial_floor

    def set_door_status(self, status):
        self.door_status = status

    def door(self):
        return self.door_status

    def floor_request (self, target_floor):
        if self.door_status == CLOSED:
            self.current_floor = target_floor
            self.set_door_status(OPEN)
            return self.current_floor
        else:
            return "Not allowed - Doors open"

    def call(self, call_floor, target_floor):
        # first move the lift to the floor where it was called and update the current floor
        self.current_floor=self.floor_request(call_floor)
        #now move it to the target floor nd update the curent floor
        print("Get into the lift, please")
        time.sleep(5)
        print ("Closing door")
        self.set_door_status(CLOSED)
        time.sleep(2)
        print ("Door closed - moving to floor:", target_floor)
        self.current_floor=self.floor_request(target_floor)

        return self.current_floor

