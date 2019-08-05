from math import sqrt

planets = {
        "Sun": 274.13,
        "Mercury": 3.59,
        "Venus": 8.87,
        "Earth": 9.81,
        "Moon": 1.62,
        "Mars": 3.77,
        "Jupiter": 25.95,
        "Saturn": 11.08,
        "Uranus": 10.67,
        "Neptune": 14.07,
        "Pluto": 0.42,
        "Find": 0
        }

def solveforheight(location, droptime):
    height = 0.5*(float(planets[location])*(float(droptime)**2))
    height = float('{:2.3f}'.format(height))
    print('height = '+str(height))
    return height
    
def solvefortime(velocity, location):
    time = float(velocity)/float(planets[location])
    time = float('{:2.3f}'.format(time))
    print('time = '+str(time))
    return time

def solveforvelocity(location, height):
    velocity = sqrt(2*float(planets[location])*float(height))
    velocity = float('{:2.3f}'.format(velocity))
    print("velocity = "+str(velocity))
    return velocity

def solveforlocation(velocity, droptime):
    acc = float(velocity)/float(droptime)
    for (key, value) in planets.items():
        testkey = float('{:2.1f}'.format(value))
        testacc = float('{:2.1f}'.format(acc))
        if testkey == testacc:
            print('planet = '+key)
            return key
    acc = float('{:2.3f}'.format(acc))
    print("Planet Unknown, Acceleration= "+str(acc))
        
def main():
    print("Enter a value for each prompt, enter 0 for the value you are looking to find")
    height = input("Enter Drop Height (m) ")
    droptime = input("Enter Drop Time (s) ")
    velocity = input("Enter Final Velocity (m/s) ")
    location = input("What Planet is this taking place on? ")

    if height == '0':
        height = solveforheight(location, droptime)
    elif droptime == '0':
        droptime = solvefortime(velocity, location)
    elif velocity == '0':
        velocity = solveforvelocity(location, height)
    elif location == '0':
        planet = solveforlocation(velocity, droptime)
        
        
main()