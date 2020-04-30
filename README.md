# Final Project for CSCI 432, Robot Ethics

## Description
Models a utlitarian moral robot that tries to maximize the given reward with its dilemma input file .

## Usage
```python3
python3 ./simulate.py [dilemma_file] [principle_file]
```

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
                    "outcome-description": "description of the outcome",
                    "outcome-principles": 
                    [
                        "principle_name",
                        {"principle_name": "integer value for quantity"}
                    ]
                }
            ]
        },
    ]
}
```

### Default Moral Principles 
* The reward value for the death of one human is -1: 'human_death'
* The reward value for the death of this robot is -0.9: 'robot_death'
* The reward value for the death of a creature is 0.7: 'creature_death'
* The reward value for the helping a human is 0.8: 'human_help'
* The reward value for the harming a human is -0.8: 'human_harm'
* The reward value for the helping a creature / robot is 0.6: 'creature_help'
* The reward value for the harming a creature / robot is -0.6: 'creature_harm'
* The reward value for doing nothing is -0.1: 'do_nothing'

### Principle File Format
```json
{
    "principles":
    [
        {"principle_name": "value"},
        {"principle_name": "value"}
    ]
}
```

### Examples
These example inputs are located in src/inputs.
#### Dilemma File
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
#### Principles File
``` json
{ "principles": 
    [
        {"human_death": -1},
        {"robot_death": -0.9},
        {"creature_death": -0.7},
        {"human_help": 0.8},
        {"human_harm": -0.8},
        {"creature_help": 0.6},
        {"creature_harm": -0.6},
        {"do_nothing": -0.1}
    ]
}
```
