import logging
import os
from code2flow.engine import map_it

def generate_nodes_and_edges(directory_path):
    # Generate absolute path
    directory_path = os.path.abspath(directory_path)
    logging.info(f"Processing directory: {directory_path}")

    # Check if directory_path exists
    if not os.path.exists(directory_path):
        logging.error(f"The given directory_path '{directory_path}' does not exist.")
        raise Exception(f"The given directory_path '{directory_path}' does not exist")

    try:
        # Getting all the python files recursively
        all_files = [os.path.abspath(os.path.join(d, f)) for d, _, files in os.walk(directory_path) for f in files if f.endswith('.py')]
        
        _, nodes, edges = map_it(all_files, 'py', [], [], [], [], [], False, None)

        node_list = [n.to_dict() for n in nodes]
        # Renaming the key 'uid' to 'id'
        node_list = [{**{'id': n['uid']}, **{k: v for k, v in n.items() if k != 'uid'}} for n in node_list]

        edges_list = [[e.node0.uid, e.node1.uid] for e in edges]
    except Exception as e:
        logging.error(f"Failed to generate nodes and edges. Error: {str(e)}")
        raise

    return node_list, edges_list