# Final Project for CSCI 432, Robot Ethics

## Description
Models a utlitarian moral robot that tries to maximize the given reward with its dilemma input file .

## Dilemma File Format
The dilemma file can contain one or more dilemma with the given format:
```json
{
    "dilemmas": [ 
        "dilemma name": {
            "description": "Example description",
            "outcomes": [ 
                "moral principle": "Description",
                "moral principle": "Description"
            ]
        },
        "dilemma name 2": {
            ...
        }
  ]
}
```

### Moral Principles 
1. The reward value for the death of one human is -1
2. The reward value for the death of this robot is -0.9
3. The reward value for the death of another robot -0.9
4. The reward value for the helping a human is 0.8
5. The reward value for the harming a human is -0.8
6. The reward value for doing nothing is -0.1


## Usage

python3 ./simulate.py dilemma_file