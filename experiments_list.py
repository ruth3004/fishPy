import csv
import os
from datetime import datetime


def create_experiment_list(path, filename, field_names=["experiment_name", "LM_path", "EM_path"], overwrite=0):
    """CREATE_EXPERIMENT_LIST creates or rewrites a new list with experiment information"""

    filepath = '/'.join([path, filename + '.csv'])
    if not os.path.exists(filepath) or overwrite == 1:
        with open(filepath, 'w') as f:
            f.write(','.join(field_names))


def get_parent_path(user='montruth'):
    """
    GET_PARENT_PATH returns the parent path until the username folder. Python compatible path.
    OPTIONAL: user: str username
    """
    current_path = os.getcwd()
    parts = current_path.split('\\')
    parts_to_join = parts[:parts.index(user) + 1]
    parent_folder = '/'.join(parts_to_join)
    return parent_folder


def extract_path_from_experiment_name(experiment_name):
    """
    EXTRACT_PATH_FROM_EXPERIMENT_NAME reads experiment name (eg. str: DATE_FISHLINE_AGE_PARAM1_SAMPLENUMBER)
        and returns the relative path to the experiment
    """
    params = experiment_name.split('_')
    date = datetime.strptime(params[0], '%Y%m%d').strftime('%Y-%m-%d')
    sample_number = params[-1]  # TODO: detect DATE_FISHLINE_AGE_PARAM1_SAMPLENUMBER

    relative_path = '/'.join(["2P_RawData", date, sample_number])
    return relative_path



def add_sample(experiment_name, list_path):
    """ ADD_SAMPLE adds a sample to the experiment list
        :experiment_name: str - with the DATE_FISHLINE_AGE_PARAM1_SAMPLENUMBER format
        :list_path: str - absolute path of the list
    """
    try:
        experiment_path = extract_path_from_experiment_name(experiment_name)
    except ValueError:
        print("Experiment name should be in format DATE_FISHLINE_AGE_PARAM1_SAMPLENUMBER")

    with open(list_path, "r+", newline="\n") as file:
        for line in file:
            if experiment_name in line:
                print("This experiment is already in the list!")
                break
            else:  # not found, we are at the eof
                file.write('\n')
                file.write(','.join([experiment_name,experiment_path,""]))  # append missing data


def add_column(list_path, added_column):
    pass


list_path = 'C:/Users/montruth/fishPy/tests/experiments_list.csv'
create_experiment_list('C:/Users/montruth/fishPy/tests', "experiments_list", overwrite=1)
add_sample("20220117_RM0012_128hpf_fP16_f2", list_path)
add_sample("20220117_RM0012_128hpf_fP16_f2", list_path)