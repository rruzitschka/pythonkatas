from src.lift import *

# test file for lift kata
# a lift moves between a number of floors.
# a lift has a panel of buttons passengers can press to request floors.
# people can call the lift from other floors. A call has both a floor and a desired direction.
# a lift has doors which may be open or closed.
# a lift fulfills a request when it moves to the requested floor and opens the doors.
# a lift fulfills a call when it moves to the correct floor, is about to go in the called direction, and opens the doors.
# a lift can only move between floors if the doors are closed.

#initialize lift object

test_lift=Lift(5)

OPEN = True
CLOSED = False

def test_lift_postion():
    assert (test_lift.current_floor == 5)


def test_lift_doors():
    test_lift.set_door_status (OPEN)
    assert (test_lift.door() == OPEN)

    test_lift.set_door_status (CLOSED)
    assert (test_lift.door() == CLOSED)

def test_floor_request():
    assert (test_lift.floor_request(7) == 7)
    assert (test_lift.current_floor == 7)
    assert (test_lift.door() == OPEN)


def test_floor_request_open_door():
    # lift is not allowed to move if doors are open
    test_lift.set_door_status(OPEN)
    assert (test_lift.floor_request(3) == "Not allowed - Doors open")

def test_lift_call():
    cf = test_lift.current_floor
    target_floor=2
    assert (test_lift.call(cf,target_floor) == 2)
    assert (test_lift.current_floor == 2)

