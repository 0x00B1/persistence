"""

"""

import click
import cytominer_database.utils
import os
import pandas as pd


def munge(config, source, target=None):
    """ Searches ``source`` for directories containing a CSV file corresponding to 
    per-object measurements, then splits the CSV file into one CSV file per compartment.
    For instance, the CSV file may comprise of measurements combined across Cells, 
    Cytoplasm, and Nuclei. ``munge`` will split this CSV file into 3 CSV files: 
    Cells.csv, Cytoplasm.csv, and Nuclei.csv.

    :param config: Configuration file.

    :param source: Directory containing subdirectories that contain an object CSV file.

    :param target: Output directory. If not specified, then it is same as ``source``.

    :return: list of subdirectories that have an object CSV file.

    """

    if not target:
        target = source

    directories = sorted(list(cytominer_database.utils.find_directories(source)))

    valid_directories = [] # list of subdirectories that have an object CSV file.

    for directory in directories:
        try:
            obj = pd.read_csv(os.path.join(directory, config["filenames"]["object"]), header=[0, 1])

        except IOError as e:
            click.echo(e)

            continue

        valid_directories.append(directory)

        target_directory = directory.replace(source, target)

        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        for compartment_name in set(obj.columns.get_level_values(0).tolist()) - {'Image'}:

            # select columns of the compartment
            compartment = pd.concat([obj['Image'], obj[compartment_name]], axis=1)

            # Create a new column
            compartment['ObjectNumber'] = compartment['Number_Object_Number']

            cols = compartment.columns.tolist()

            # Move ImageNumber and ObjectNumber to the front

            cols.insert(0, cols.pop(cols.index('ObjectNumber')))

            cols.insert(0, cols.pop(cols.index('ImageNumber')))

            compartment = compartment.ix[:, cols]

            compartment.to_csv(os.path.join(target_directory, compartment_name + '.csv'), index=False)

    return valid_directories