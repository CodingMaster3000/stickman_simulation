# stickman_simulation
simulating stickman

Ich habe hier ein Strichmänchen, dass man mit den Pfeiltasten bewegen kann. Nun soll es ab und zu Meteoriten geben, denen man ausweichen muss. Dafür habe ich die Klasse Object in wellcher die Meteoriten die Instanzen sind. 

class Object:
    def __init__(self, type, verticies, edges, vel, on_thef_floor, falling_time):
        self.type = type
        self.verticies = verticies
        self.edges = edges
        self.vel = vel
        self.on_thef_floor = on_thef_floor
        self.falling_time = falling_time

Mit dem ersten klappt das auch, aber ich möchte in der while-Schleife jedes mal wenn der vorherige den Boden erreicht einen neuen erstellen. 
1. noch vor der Schleife: 
    meteorite = Object("meteorite", meteorite_verticies, meteorite_edges, 0, False, 0)
2. in der Schleife unter der gegebenen Bedingung:
    meteorite = Object("meteorite", new, meteorite_edges, 0, False, 0)

der Objektname sollte irgendwie abhängig von einer Zählvariable sein.

Beim Aufrufen der Meteorite Funktion (in welcher der "Meteoriten" gemalt wird) übergebe ich bisher einfach das Objekt meteorite. Kann man mehrere Objekte in einer Liste zusammenfassen, sodass ich in einer foor-Schleife für jeden Meteoriten die draw Funktion einzeln aufrufe und dann das jeweilige Objekt übergebe? Also nach dem Schema:
  for i in listOfObjects:
      Meteorite(i)


