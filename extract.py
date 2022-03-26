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
    # TODO: Load NEO data from the given CSV file.
    neo_collection = []
    with open(neo_csv_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # list of neos:
            # neo_collection += [[row['id'], row['pdes'], row['name'] , row['diameter'], row['pha'], row['neo']]]
            # neo_collection.append(row)

            # neo_collection += [dict(zip(['id', 'pdes', 'name', 'diameter', 'pha', 'neo', 'full_name'], [row['id'], row['pdes'], row['name'] , row['diameter'], row['pha'], row['neo'], row['full_name']]))]

            # print(dict([('id', row['id']),('pdes',row['pdes']), ('name', row['name']),('diameter', row['diameter']),('pha', row['pha']),('neo', row['neo']),('full_name', row['full_name'])]))

            #  neo_collection.append((dict([('id', row['id']),('pdes',row['pdes']), ('name', row['name']),('diameter', row['diameter']),('pha', row['pha']),('neo', row['neo']),('full_name', row['full_name'])])))

             neo_collection.append((dict([('id', row['id']),('designation',row['pdes']), ('name', row['name']),('diameter', row['diameter']),('hazardous', row['pha']),('neo', row['neo']),('full_name', row['full_name'])])))

            # neo_collection += dict([('id', row['id']),('pdes',row['pdes']), ('name', row['name']),('diameter', row['diameter']),('pha', row['pha']),('neo', row['neo']),('full_name', row['full_name'])])

            # neo_collection = dict.fromkeys([('id', row['id']),('pdes',row['pdes']), ('name', row['name']),('diameter', row['diameter']),('pha', row['pha']),('neo', row['neo']),('full_name', row['full_name'])])

            # neo_collection['id'] = row['id'],neo_collection['pdes'] = row['pdes'], neo_collection['name'] = row['name'],neo_collection['diameter'] = row['diameter'],neo_collection['pha'] = row['pha'],neo_collection['neo'] = row['neo']

    return neo_collection


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    cad_collection = []

    # with open('data/cad_10.json', 'r') as json_file:
    with open(cad_json_path, 'r') as json_file:
        json_reader = json.load(json_file)

    # list comprehension: # cad_comprehension = [cad for cad in json_reader['data']]

    for i in range(len(json_reader['data'])):
        # cad_collection += [dict(zip(json_reader['fields'],json_reader['data'][i]))]  
        # cad_collection += [dict(zip([json_reader['fields'][0], json_reader['fields'][3], json_reader['fields'][4], json_reader['fields'][7], json_reader['fields'][1]], [json_reader['data'][i][0], json_reader['data'][i][3], json_reader['data'][i][4], json_reader['data'][i][7], json_reader['data'][i][1]]))] 

    # def __init__(self, _designation='', time=None, distance=0.0, velocity=0.0, orbit_id=None, neo=None):

        cad_collection += [dict(zip(['_designation', 'time', 'distance', 'velocity', 'orbit_id'], [json_reader['data'][i][0], json_reader['data'][i][3], json_reader['data'][i][4], json_reader['data'][i][7], json_reader['data'][i][1]]))] 
        # fields        # cad_collection += json_reader['fields'][0], json_reader['fields'][3], json_reader['fields'][4], json_reader['fields'][7], json_reader['fields'][1]  
        # values list        # cad_collection += [[json_reader['data'][i][0], json_reader['data'][i][3], json_reader['data'][i][4], json_reader['data'][i][7], json_reader['data'][i][1]]]

    print(cad_collection)
    return cad_collection

# load_approaches('data/cad_10.json')
# Required - des, cd, dist, and v_rel + orbit_id
