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

### Default Moral Principles 
*  "human_death": -1
*  "robot_death": -0.9
*  "creature_death": -0.7
*  "human_help": 0.8
*  "human_harm": -0.8
*  "creature_help": 0.6
*  "creature_harm": -0.6
*  "do_nothing": -0.1

## Examples
There are two examples in src/inputs that can be used with
``` python
python3 simulate.py inputs/examples_dilemmas.json inputs/example_principles.json
```