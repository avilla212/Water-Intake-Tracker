# main .py will use the WaterTracker class to create a tracker object.
from waterTracker import WaterTracker

tracker = WaterTracker()

# user will set their goal intake
# user will input their current intake
# we will display the current intake all the time
def main():
    isOn = True
    tracker.setGoal()
    print(f'Your goal intake is {tracker.goalIntake} oz')

    while isOn:
        tracker.addIntake(0)
main()