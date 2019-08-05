from tkinter import *

class GravityWaves:
    def __init__(self):
        window = Tk()
        window.title("Gravity Waves")

        self.planets = {
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
        "Custom": "custom",
        "Find": 0
        }

        # Create labels
        Label(window, text = "Object Mass: ").grid(row = 1, column = 1, sticky = W)
        Label(window, text = "kg").grid(row = 1, column = 3, sticky = W)
        Label(window, text = "Drop Height: ").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "m").grid(row = 2, column = 3, sticky = W)
        Label(window, text = "Drop Time: ").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "s").grid(row = 3, column = 3, sticky = W)
        Label(window, text = "Final Velocity: ").grid(row = 4, column = 1, sticky = W)
        Label(window, text = "m/s").grid(row = 4, column = 3, sticky = W)
        Label(window, text = "Location: ").grid(row = 5, column = 1, sticky = W)
        Label(window, text = "Custom Acceleration: ").grid(row = 6, column = 1, sticky = W)
        Label(window, text = "m/s^2").grid(row = 6, column = 3, sticky = W)

        # Create entries
        self.objmass = StringVar()
        Entry(window, textvariable = self.objmass, justify = RIGHT).grid(row = 1, column = 2)

        self.dropheight = StringVar()
        Entry(window, textvariable = self.dropheight, justify = RIGHT).grid(row = 2, column = 2)

        self.droptime = StringVar()
        Entry(window, textvariable = self.droptime, justify = RIGHT).grid(row = 3, column = 2)

        self.finalvelocity = StringVar()
        Entry(window, textvariable = self.finalvelocity, justify = RIGHT).grid(row = 4, column = 2)

        self.location = StringVar()
        OptionMenu(window, self.location, *self.planets.keys()).grid(\
            row = 5, column = 2)
        
        self.cusloc = StringVar()
        Entry(window, textvariable = self.cusloc, justify = RIGHT).grid(row = 6, column = 2)

        btSolve = Button(window, text = "Help", command = self.help).grid(\
            row = 7, column = 1, sticky = W)
        
        btSolve = Button(window, text = "Solve", command = self.solve).grid(\
            row = 7, column = 3, sticky = E)

        window.mainloop()
    
    def solveforheight(self):
        height = ((0+self.finalvelocity)/2)*self.droptime
        print('height= '+height)
        return height
    
    def solvefortime(self):
        time = self.finalvelocity/self.planets[self.location.get()]
        print('time= '+time)
        return time
    
    def solveforlocation(self):
        acc = self.finalvelocity/self.droptime
        for (key, value) in self.planets.items():
            testkey = float('{:2.1f}'.format(value))
            testacc = float('{:2.1f}'.format(acc))
            if testkey == testacc:
                print('planet= '+key)
                return key
            else:
                return 'Unknown'
    
    def solve(self):
        self.location = self.location.get()
        if self.location == "Custom":
            self.location = self.cusloc.get()
        elif self.location == '':
            self.location = self.cusloc.get()
        elif self.location == 0:
            planet = self.solveforlocation(self)
        else:
            self.location = self.planets[self.location]
        
        if self.objmass.get() == 0:
            self.solveformass(self)
        elif self.dropheight.get() == 0:
            height = self.solveforheight(self)
        elif self.droptime.get() == 0:
            time = solvefortime(self)
        elif self.finalvelocity.get() == 0:
            velocity = self.solveforvelocity(self)
            
    def help(self):
        print('help')


GravityWaves()