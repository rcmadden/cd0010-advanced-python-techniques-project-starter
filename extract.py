"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
from dataclasses import fields
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neo_collection = []
    with open(neo_csv_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
      
             neo_collection.append((dict([('id', row['id']),('designation',row['pdes']), ('name', row['name']),('diameter', row['diameter']),('hazardous', row['pha']),('neo', row['neo']),('full_name', row['full_name'])])))
          
    return neo_collection


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
  
    cad_collection = []

  
    with open(cad_json_path, 'r') as json_file:
        json_reader = json.load(json_file)

    for i in range(len(json_reader['data'])):

        cad_collection += [dict(zip(['_designation', 'time', 'distance', 'velocity'], [json_reader['data'][i][0], json_reader['data'][i][3], json_reader['data'][i][4], json_reader['data'][i][7]]))] 
  
    return cad_collection

