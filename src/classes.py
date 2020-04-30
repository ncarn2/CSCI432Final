from term_colors import cprint 

class Principle:
    def __init__(self, principle, value):
        self.principle = principle
        self.value = value

    def __repr__(self):
        return str(self.principle) + ": " + str(self.value)

class Outcome:
    def __init__(self, desc, principles):
        self.desc = desc
        self.principles = principles

    def __repr__(self):
        outcome = self.desc
        return outcome 
        
class Dilemma:
    def __init__(self, title, description, outcomes):
        self.title = title
        self.description = description
        self.outcomes = outcomes

    def __repr__(self):
        output = ""
        cprint("y", str(self.title).upper())
        cprint("g", "Description:")
        cprint("g", str(self.description))

        cprint("b", "Outcomes:")
        for outcome in self.outcomes:
            cprint("b", ("\t- " + str(outcome.desc)))

        return output 