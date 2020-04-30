class Principle:
    def __init__(self, principle, value, quantity=1):
        self.principle = principle
        self.value = value
        self.quantity = quantity

    def __repr__(self):
        return str(self.principle) + ": " + str(self.value)

class Outcome:
    def __init__(self, desc, principles):
        self.desc = desc
        self.principles = principles

    def __repr__(self):
        outcome = ""
        for princ in self.principles:
            outcome += str(princ) + ", "
        return outcome 
        
class Dilemma:
    def __init__(self, title, description, outcomes):
        self.title = title
        self.description = description
        self.outcomes = outcomes

    def __repr__(self):
        output = str(self.title) + ": " + str(self.description) 
        output += "\nOutcomes: \n"
        for outcome in self.outcomes:
            output += "\t-" + str(outcome.desc) + "\n"
            output += "\t{" + str(outcome) + "}\n"
        return output 