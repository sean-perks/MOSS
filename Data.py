import json
from pathlib import Path


# save in file
def write_json(dict, file_path = "StringHarmonics/text/accounts.json"):
    with open(file_path, 'w') as f:
        json.dump(dict, f)


# load back to verify
def read_json(file_path = "StringHarmonics/text/accounts.json"):
    with open(file_path, 'r') as f:
        my_dict = json.load(f)
    
    return my_dict


def get_project_data(proj, my_json="MOSS/database/projects.json"):
    all_projects = read_json(my_json)
    proj_dict = all_projects[proj]
    return proj_dict

def get_project_plants(proj, my_json="MOSS/database/project_plants.json"):
    all_projects = read_json(my_json)
    proj_dict = all_projects[proj]

    return proj_dict


if __name__ == "__main__":
    print("hi")
    my_dict = get_project_data("Hebo")
    print(my_dict["Location"][0])
    my_plants = get_project_plants("Hebo")
    print(my_plants.keys())