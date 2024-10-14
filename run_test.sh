#!/bin/bash

# Loop through test cases 1 to 12
for i in {1..12}
do
    # Define input and output file paths
    input_file="test_cases/test${i}.csv"
    output_file="output_files/output${i}.txt"
    
    # Run the Python script with the input file and redirect output to the output file
    echo "Running test case $i: $input_file"
    python3 ./ham_circuit_bogosort.py < "$input_file" > "$output_file"
    
    # Check if the command was successful
    if [ $? -eq 0 ]; then
        echo "Output for test case $i written to $output_file"
    else
        echo "Error running test case $i"
    fi
done
