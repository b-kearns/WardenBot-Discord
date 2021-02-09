#Script to define the Tracker class
#Defines the initiative tracker functionality

class Tracker:
    #Roster tracks the name of actors and their turn order
    def __init__(self):
        self.roster = {}
        self.tracker = []
        print(f'Created Tracker')

    def Add(self, name, value):
        self.roster[name] = value

    def Reset(self):
        self.roster = {}

    def Print(self):
        keys = self.roster.keys()
        output = 'Current Initiative Order:\n'
        self.tracker.clear()

        for key in keys:
            self.tracker.append((key, self.roster[key]))
            self.tracker.sort(reverse=True, key=lambda x: x[1])
        
        for pair in self.tracker:
            output += f'{pair[0]} | {pair[1]}\n'

        return output

