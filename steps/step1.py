import os


def go(args):
    
#     outdir = os.path.join(
#         os.environ['CNVRG_WORKDIR'], 
#         os.environ['CNVRG_OUTPUT_DIR']
#     )
    with open(args.output_artifact, "w+") as fp:
        fp.write("Some content")

    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Step 1')
    
#     parser.add_argument(
#         "--input_artifact", 
#         required=True, 
#         type=pathlib.Path
#     )
    
    parser.add_argument(
        "--output_artifact", 
        required=True, 
        type=pathlib.Path
    )
    
    args = parser.parse_args()
    
    go(args)