import os
import json

# PathManipulator class
# Modified from : https://github.com/shubhamakshit/EssentialPythonFunctions/raw/main/pathops.py

class PathManipulator:
    @staticmethod
    def modify_path(path):
        expanded_path = os.path.expandvars(path)
        absolute_path = os.path.abspath(expanded_path)
        modified_path = absolute_path.replace(os.sep, '/')
        return modified_path
    
    @staticmethod
    def generate_directory_tree(root_dir):
        tree = {'name': os.path.basename(root_dir), 'type': 'directory'}
        if os.path.isdir(root_dir):
            tree['contents'] = []
            for item in os.listdir(root_dir):
                item_path = os.path.join(root_dir, item)
                if os.path.isdir(item_path):
                    tree['contents'].append(PathManipulator.generate_directory_tree(item_path))
                else:
                    tree['contents'].append({'name': item, 'type': 'file'})
        return tree

    @staticmethod
    def directory_tree_to_json(root_dir):
        root_dir = PathManipulator.modify_path(root_dir)
        directory_tree = PathManipulator.generate_directory_tree(root_dir)
        return json.dumps(directory_tree, indent=4)