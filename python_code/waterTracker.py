
class WaterTracker:
    def __init__(self):

        self.intakeArray = []
        self.currIntake = 0
        
    def addIntake(self,amount=0):

        try:
            amount = int(input("How much water have you consumed? "))
            
            # amount == -1, we will return the currIntake data to firebase and then close the program
            if amount == -1:
                quit()
            else:
                self.currIntake += amount
                self.intakeArray.append(amount)
                self.checkIntake()

        except ValueError:
            print("Please enter a valid number")
            return
    
    # testing for firebase, when user hits -1 to close the program, we will send the currIntake data to firebase
    def endOfDay(self):
        return self.currIntake

    def setGoal(self):
        # user will enter goal intake but if user enters non int or negative int, we will ask again
        try:
            self.goalIntake = int(input("What is your goal intake? "))
            if self.goalIntake < 0:
                print("Please enter a valid number")
                self.setGoal()
        except ValueError:
            print("Please enter a valid number")
            self.setGoal()
     # function will let user know when they are almost at their goal intake
     # reminders at 30% of the goal, 50% of the goal, and 80% of the goal
    def checkIntake(self):
        
        goalReached = False

        thirtyPercent = self.goalIntake * .3
        fiftyPercent = self.goalIntake * .5
        fiftyOnePercent = self.goalIntake * .51
        eightyPercent = self.goalIntake * .8

        if self.currIntake < self.goalIntake:

            print(f'Your current intake is {self.currIntake} oz and your goal is {self.goalIntake} oz')

            if self.currIntake >= eightyPercent:
                print("You are so close to your goal intake!")
            elif self.currIntake >= fiftyOnePercent:
                print("You are more than halfway to your goal intake!")
            elif self.currIntake >= fiftyPercent:
                print("You are halfway to your goal intake!")
            elif self.currIntake >= thirtyPercent:
                print("You are 30% to your goal intake!")
        
        else:
            print(f'You have reached your goal intake of {self.goalIntake} oz! and your current intake is {self.currIntake} oz')
            
    # functions to print and check the current intake and goal intake
    def getCurrIntake(self):
        print(f'Current intake: {self.currIntake} oz')

