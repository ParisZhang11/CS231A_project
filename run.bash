#!/bin/bash

# Define the array of x values
x_values=("room" "horns" "leaves" "orchids" "trex" "fortress")

# Iterate over each value of x
for x in "${x_values[@]}"; do
    # Construct the command
    command="python train.py -s nerf_llff_fewshot_resize/${x} --eval --port 6312 --model_path output/${x}_gs_2 --resolution 1 --kshot 2 --seed 3"
    
    # Run the command
    echo "Running command for ${x}..."
    eval $command

    # Check if the command was successful
    if [ $? -eq 0 ]; then
        echo "Command succeeded for ${x}"
    else
        echo "Command failed for ${x}"
    fi
done