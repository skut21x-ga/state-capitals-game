from capitals import states

# print(states)


class States:
    def __init__(self):
        self.states = states
        for states in self.states:
            self.name = states.name
            self.capital = states.capital
            print(self.name)


States()

# "name": "Alabama",
# "capital": "Montgomery"
