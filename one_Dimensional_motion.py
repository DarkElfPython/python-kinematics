from __future__ import division
import sympy as sp
import math
def finalvelocitypathways():
    typeofequation = str(input("""What values do you know?       1. Acceleration, Initial Velocity, Time    
                                                                 2. Acceleration, Initial Velocity, Displacement
                                                                 3. Displacement as a function of time
                                                                 4. Acceleration as a function of time
                                                                 Enter Your Choice: """))
    if typeofequation == "1":
        ivelocity = float(input('enter the  initial velocity '))
        acc = float(input('enter the acceleration '))  # acceleration
        timetrue = float(input('enter the time taken '))  # time taken
        finvelocity = ivelocity + acc * timetrue  # using the first equation of motion, we find the final velocity
        print(finvelocity)
    elif typeofequation == "2":
        ivelo = float(input('enter the initial velocity '))
        acc2 = float(input('enter the acceleration '))  # acceleration 
        displace2 = float(input('enter the displacement '))  # time taken
        velosquare = 2 * acc2 * displace2 + (ivelo ** 2)
        velofinal = math.sqrt(velosquare)    # through a two step process we can calculate final velocity using third eqn
        if velofinal < 0:
            print("Wrong Values. use another method")
        else:
            print(velofinal)
    elif typeofequation == "3":
        timetaken = float(input('Enter the time '))
        varx = input("enter the equation x = ")
        velo = sp.diff(varx, t)
        finvelocity = sp.solve(velo, timetaken)
        print(finvelocity)
    elif typeofequation == "4":
        timetaken = float(input('Enter the time '))
        varx = input("enter the equation a = ")
        velo = sp.integrate(varx, t)
        finvelocity = sp.solve(velo, timetaken)
        print(finvelocity)
    else:
        print(' please provide the correct information ')
        finalvelocitypathways()
def initialvelocitypathways():
    typeofequation = str(input("""What values do you know?       1. Acceleration, Fianl Velocity, Time    
                                                                 2. Acceleration, Final Velocity, Displacement
                                                                 3. Acceleration, Time, Displacement 
                                                                 Enter Your Choice: """))
    # enter the serial number
    if typeofequation == "1":  # type of equation of motion
        fivelocity = float(input('enter the  Final velocity '))  # final velocity
        acc = float(input('enter the acceleration '))  # acceleration
        timetrue = float(input('enter the time taken '))  # time taken
        invelocity = fivelocity - acc * timetrue  # first eqn of motion
        print(invelocity)
    elif typeofequation == "2":
        fivelo = float(input('enter the final velocity '))
        acc2 = float(input('enter the acceleration '))  # acceleration
        displace2 = float(input('enter the displacement '))  # time taken
        ivelosquare = fivelo ** 2 - 2 * acc2 * displace2  # two step third eqn of motion
        velofinal = math.sqrt(ivelosquare)
        print(velofinal)
    elif typeofequation == "3":
        displace2 = float(input('enter the displacememnt '))
        acc2 = float(input('enter the acceleration '))  # acceleration
        timetrue = float(input('enter the time taken '))
        initvelocity = (displace2 - (acc2 * timetrue ** 2) * 1 / 2) * (1 / timetrue)
        print(initvelocity)
    else:
        print(' please provide the correct information ')
        initialvelocitypathways()     
def accelerationpathways():
    typeofequation = str(input("""what values do you know?         1. Initial velocity, Final velocity, time 
                                                                   2. Displacement, Initial Velocity, time
                                                                   3. Displacement, Final velocity, Initial Velocity
                                                                   4. Displcaement as a function of time
                                                                   5. Velocity as a function of time
                                                                   Enter Your Choice: """))
    if typeofequation == "1":
        initialv = float(input("Enter the Initial Velocity "))
        finalv = float(input("Enter the Final Veocity "))
        time = float(input('enter the time '))
        acc = (finalv - initialv) / time
        print(acc)
    elif typeofequation == "2":
        initialv = float(input("Enter the Initial Velocity "))
        time = float(input('enter the time '))
        dispacement = float(input('Enter the Displacement' ))
        acc = (dispacement - (initialv * time)) / time ** 2
        print(acc)
    elif typeofequation == "3":
        initialv = float(input("Enter the Initial Velocity "))
        dispacement = float(input('Enter the Displacement'))
        finalv = float(input("Enter the Final Veocity "))
        acc =  (finalv ** 2 - initialv ** 2) / (2 * dispacement)
        print(acc)
    elif typeofequation ==  "4":
        dx = input("enter the Equation x = ")
        ddx = sp.diff(dx , t)
        acc = sp.diff(ddx , t)
        print(acc)
    elif typeofequation == "5":
        dx = input("Enter the equation x = ")
        acc = sp.diff(dx, t)
        print(acc)
    else:
        print('enter the correct information')
        accelerationpathways()
def displacementpathways():
    typeofequation = str(input("""What do you know?                 1. Acceleration, Initial Velocity, Time
                                                                    2. Acceleration, Initial Velocity, Final Velocity
                                                                    Enter Your Choice: """))
    if typeofequation == "1":
        acc = float(input('enter the acceleration '))
        initialv = float(input('enter the Initial velocity '))
        timetrue = float(input('enter the time taken '))
        displacement = initialv * timetrue + (1/2) * acc * (t) ** 2
        print(displacement)
    elif typeofequation == "2":
        fivelocity = float(input('enter the  Final velocity '))
        acc = float(input('enter the acceleration '))
        initialv = float(input('enter the Initial velocity '))
        if acc != 0:
            print('acceleration can\'t be zero in this equation. use the other equation instead')
        else:
            displacement = ((fivelocity ** 2) - (initialv ** 2)) / 2 * acc
            print(displacement)
    else:
        print('enter the correct information')
        displacementpathways()
def timepathways():
    fivelocity = float(input('enter the  Final velocity '))
    acc = float(input('enter the acceleration '))
    initialv = float(input('enter the Initial velocity '))
    time = (fivelocity - initialv) / acc
    print(time)
def welcome():
    typeof = str(input("What do you want to calculate?                                     1. Initial Velocity\n"
                       "                                                                   2. Final Velocity\n"
                       "                                                                   3. Acceleration\n"
                       "                                                                   4. Time\n"
                       "                                                                   5. Displacement\n"
                       	"																   Enter Your Choice: "))
    if typeof == "1":
        initialvelocitypathways()
    elif typeof == "2":
        finalvelocitypathways()
    elif typeof == "3":
        accelerationpathways()
    elif typeof == "4": 
        timepathways()
    elif typeof == "5":
        displacementpathways()
    else:
        print('not a valid choice')
        welcome()
t = sp.Symbol('t')
welcome()


