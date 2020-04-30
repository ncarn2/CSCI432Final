#!/bin/bash

echo -e "\n\nRunning without custom principles"
python3 simulate.py inputs/example_dilemmas.json 

#echo -e "\n\nRunning with custom principles"
#python3 simulate.py inputs/example_dilemmas.json inputs/example_principles.json 