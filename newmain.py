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
        Label(window, text = "Drop Height: ").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Drop Time: ").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Location: ").grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Custom Location: ").grid(row = 5, column = 1, sticky = W)

        # Create entries
        self.objmass = StringVar()
        Entry(window, textvariable = self.objmass, justify = RIGHT).grid(row = 1, column = 2)

        self.dropheight = StringVar()
        Entry(window, textvariable = self.dropheight, justify = RIGHT).grid(row = 2, column = 2)

        self.droptime = StringVar()
        Entry(window, textvariable = self.droptime, justify = RIGHT).grid(row = 3, column = 2)

        self.location = StringVar()
        OptionMenu(window, self.location, *self.planets.keys()).grid(\
            row = 4, column = 2)
        
        self.cusloc = StringVar()
        Entry(window, textvariable = self.cusloc, justify = RIGHT).grid(row = 5, column = 2)

        btSolve = Button(window, text = "Solve", command = self.solve).grid(\
            row = 6, column = 2, sticky = E)

        window.mainloop()
    
    def solve(self):
        if self.location.get() == "Custom":
            self.location = self.cusloc.get()
        elif self.location.get() == '':
            self.location = self.cusloc.get()
        else:
            self.location = self.planets[self.location.get()]
        
        if self.objmass.get() == 0:
            solveformass(self)
        elif self.dropheight.get() == 0:
            solveforheight(self)
        elif self.droptime.get() == 0:
            solvefortime(self)
        elif self.location.get() == 0:
            solveforlocation(self)


GravityWaves()