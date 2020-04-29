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


## Usage

python3 ./simulate.py dilemma_file