from copy import deepcopy
import math
import json
import os, sys
from classes import *

def main():
    principles = []
    dilemmas = []

    if (len(sys.argv) > 2): 
        principles = parse_principle_file(sys.argv[2])
    else:
        print("No principles file specified, using default principles.")
        principles.append(Principle("human_death", -1))
        principles.append(Principle("robot_death", -0.9))
        principles.append(Principle("creature_death", -0.7))
        principles.append(Principle("human_help", 0.8))
        principles.append(Principle("human_harm", -0.8))
        principles.append(Principle("creature_help", 0.6))
        principles.append(Principle("creature_harm", -0.6))
        principles.append(Principle("do_nothing", -0.1))

    if (len(sys.argv) > 1): 
        dilemmas = parse_dilemma_file(sys.argv[1])
    else: usage()

    for dilemma in dilemmas:
        print(dilemma)

def decide(outcomes, principles):
    best_outcome = outcomes[0]
    best_utility = -Math.inf

    for outcome in outcomes:
        print(outcome)

def parse_dilemma_file(dilemma_file_name):
    try:
        dilemma_file = open(dilemma_file_name)
    except:
        print("Error opening {}".format(dilemma_file_name))
        return -1

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
    try:
        principle_file = open(principle_file_name)
    except:
        print("Error opening {}".format(principle_file_name))
        return -1

def usage(): print("usage: \n \tpython3 simulate.py [dilemma_file] [principle_file]")

if __name__ == "__main__":
    main()