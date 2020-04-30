# Final Project for CSCI 432, Robot Ethics

## Description
Models a utlitarian moral robot that tries to maximize the given reward with its dilemma input file .

## Dilemma File Format
The dilemma file can contain one or more dilemma with the given format:
```json
{ "dilemmas":
    [ 
        {
            "title": ,
            "description":,
            "outcomes":
            [
                {
                    "outcome-description": ,
                    "outcome-principles": 
                    [
                        "principle_name",
                        {"principle_name": "quantity : (integer)"}
                    ]
                }
            ]
        }

    ]
}
```

### Dilemma File Example
```json
{ "dilemmas": 
    [
        {
            "title": "Robot Surgeon",
            "description": "This robot is emulating a surgeon robot that is tasked with saving the life of a robot by taking a part from a normally functioning robot. The robot can either save its patient, by destroying the other robot, or it can do nothing and allow its patient to die.",
            "outcomes": 
            [
                { "outcome-description": "The robot decides to do nothing. This results in the death of its patient.",  
                    "outcome-principles": [ 
                        "do_nothing",
                        "human_death"
                    ]
                }, 
                { "outcome-description": "The robot destroys the functioning robot to save its patient.", 
                    "outcome-principles": [ 
                        {"robot_death": 1},
                        "creature_help"
                    ]
                }
            ]
        }
    ]
}
```

### Moral Principles 
* The reward value for the death of one human is -1: 'human_death'
* The reward value for the death of this robot is -0.9: 'robot_death'
* The reward value for the death of a creature is 0.7: 'creature_death'
* The reward value for the helping a human is 0.8: 'human_help'
* The reward value for the harming a human is -0.8: 'human_harm'
* The reward value for the helping a creature / robot is 0.6: 'creature_help'
* The reward value for the harming a creature / robot is -0.6: 'creature_harm'
* The reward value for doing nothing is -0.1: 'do_nothing'


## Usage

python3 ./simulate.py dilemma_file