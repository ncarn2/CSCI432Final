
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
        # TODO: Move all of these prints into output
        print("\033[93m{}\033[37m".format(str(self.title).upper()))
        print("\033[32mDescription:\n\033[37m")
        print("\033[32m{}\033[37m".format(str(self.description)))

        print("\033[34mOutcomes:\n\033[37m")
        for outcome in self.outcomes:
            print("\033[34m{}\033[37m".format("\t- " + str(outcome.desc)))

        return output 