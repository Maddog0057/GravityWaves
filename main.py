import object as object
import tkinter as tk

window = tk.Tk()
window.title('GravityWaves')

textfields = ('Object Mass', 'Drop Height', 'Drop Time')

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
    "Custom": "custom",
    "Find": 0
}

def test(entries):
    print(float (entries['Object Mass'].get()))

def buildEntries(window, textfields):
    entries = {}
    for field in textfields:
        row = tk.Frame(window)
        lab = tk.Label(row, width=10, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    row = tk.Frame(window)
    lab = tk.Label(row, width=10, text="Location: ", anchor='w')
    var = tk.StringVar(window)
    default = "Earth"
    var.set(default)
    dropdown = tk.OptionMenu(row,var, *planets.keys())
    row.pack(side=tk.TOP, 
             fill=tk.X, 
             padx=5, 
             pady=5)
    lab.pack(side=tk.LEFT)
    dropdown.pack(side=tk.RIGHT,
                  expand=tk.YES,
                  fill=tk.X)
    build = dict()
    build['ent'] = ent
    build['dropdown'] = dropdown
    #build['window'] = window 
    return dict(build)
    
def main():
    ret = buildEntries(window, textfields)
    ents = ret['ent']
    dropdown = ret['dropdown']
    #window = ret['window']
    row = tk.Frame(window)
    solve = tk.Button(window, text='Solve', command=(lambda e=ents: test(e)))
    solve.pack(side = tk.LEFT, padx=5, pady=5)
    window.mainloop()

main()



