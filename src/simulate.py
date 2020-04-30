from copy import deepcopy
import math
import json
import os, sys

# Gets Principle, Outcome, and Dilemma classes
from classes import *

def main():
    principles = {  }
    dilemmas = []

    # Set up the principles
    if (len(sys.argv) > 2): 
        principles = parse_principle_file(sys.argv[2])
    else:
        print("No principles file specified, using default principles.")
        principles['human_death'] = (Principle("human_death", -1))
        principles['robot_death'] = (Principle("robot_death", -0.9))
        principles['creature_death'] = (Principle("creature_death", -0.7))
        principles['human_help'] = (Principle("human_help", 0.8))
        principles['human_harm'] = (Principle("human_harm", -0.8))
        principles['creature_help'] = (Principle("creature_help", 0.6))
        principles['creature_harm'] = (Principle("creature_harm", -0.6))
        principles['do_nothing'] = (Principle("do_nothing", -0.1))

    # Setup the dilemmas
    if (len(sys.argv) > 1): 
        dilemmas = parse_dilemma_file(sys.argv[1])
    else: usage()

    # Have the "robot" make a decision for each dilemma
    for dilemma in dilemmas:
        decide(dilemma, principles)

def decide(dilemma, principles):
    print(dilemma)
    outcomes = dilemma.outcomes
    best_outcome = outcomes[0]
    best_utility = -math.inf

    for outcome in outcomes:
        # determine best outcome
        current_utility = 0
        for princ in outcome.principles:
            if (isinstance(princ, dict)):
                # add principle value times princ.values()
                current_utility += principles[list(princ.keys())[0]].value * list(princ.values())[0]
            else:
                current_utility += principles[princ].value
            
        if current_utility > best_utility: best_utility = current_utility; best_outcome = outcome 

    best_utility = round(best_utility, 2)
    

    # This shouldnt really be printed, it should be contained in the classes and sent back to main.
    # Each dilemma should have an outcome that gets set in decide. Decide should be a method in the Dilemma class
    print("\033[32mBest Outcome: \033[31m{}\033[37m".format(best_outcome))
    print("\033[32mBest Utility: \033[31m{}\033[37m".format(best_utility))
    
def parse_dilemma_file(dilemma_file_name):
    try:
        dilemma_file = open(dilemma_file_name)
    except:
        print("Error opening {}".format(dilemma_file_name))
        sys.exit(-1)

    dilemma_data = json.load(dilemma_file)

    dilemmas = []

    # For each dilemma in the file
    for dilemma in dilemma_data['dilemmas']:
        outcomes=[]
        # create a new dilemma with the given title, description and outcomes 
        for outcome in dilemma['outcomes']:
            temp_principles = []
            for principle in outcome['outcome-principles']:
                temp_principles.append(principle)

            outcomes.append(Outcome(outcome['outcome-description'], deepcopy(temp_principles)))

        dilemmas.append(deepcopy(Dilemma(dilemma['title'], dilemma['description'], outcomes)))

    return dilemmas

def parse_principle_file(principle_file_name):
    principles = {  }
    try:
        principle_file = open(principle_file_name)
    except:
        print("Error opening {}".format(principle_file_name))
        sys.exit(-1)

    principle_data = json.load(principle_file)

    for principle in principle_data['principles']:
        new_principle = Principle(list(principle.keys())[0], list(principle.values())[0])
        principles[new_principle.principle] = new_principle
        #principles.append(new_principle)

    return principles

def usage(): print("usage: \n \tpython3 simulate.py [dilemma_file] [principle_file]")

if __name__ == "__main__":
    main()