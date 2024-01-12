import json
import logging
import os
import sys
from __init__ import generate_nodes_and_edges

def main():
    # Check if directory path is provided
    if len(sys.argv) < 2:
        print("Directory path not provided.")
        sys.exit(1)

    directory_path = sys.argv[1]

    # Check if directory path exists
    if not os.path.exists(directory_path):
        print(f"The given directory_path '{directory_path}' does not exist.")
        sys.exit(1)

    try:
        nodes, edges = generate_nodes_and_edges(directory_path)
    except Exception as e:
        print(f"Failed to generate nodes and edges. Error: {str(e)}")
        sys.exit(1)

    # Output the nodes and edges to stdout
    print(json.dumps({'nodes': nodes, 'edges': edges}, indent=4))

if __name__ == "__main__":
    main()