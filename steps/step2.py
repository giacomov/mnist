"""
Testing input and output. This script takes an input file and write an output
file related to the input, to test that we can find the input and generate
an output based on that.
"""
import os
import argparse
import pathlib


def go(args):
    
    with open(args.input_artifact, "r") as fp:
        content = fp.read()
    
    with open(args.output_artifact, "w+") as fp:
        fp.write(f"This was the content: {content}")

    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Step 2')
    
    parser.add_argument(
        "--input_artifact", 
        required=True, 
        type=pathlib.Path
    )
    
    parser.add_argument(
        "--output_artifact", 
        required=True, 
        type=pathlib.Path
    )
    
    args = parser.parse_args()
    
    go(args)