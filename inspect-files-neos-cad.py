import csv
import json

count = 0
i = 0

CSVInputFile =  'data/neos.csv'

with open(CSVInputFile, newline='') as csv_file:
    reader = csv.DictReader(csv_file)

    print(reader.fieldnames)
    
    for row in reader:
        count +=1
    print('1. How many NEOs are in the neos.csv data set?', count)

with open(CSVInputFile, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # print('type', type(row))
        print('2. What is the primary designation of the first Near Earth Object in the neos.csv data set?', row['pdes'])
        break

with open(CSVInputFile, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if row['name'] == 'Apollo':
            print('3. What is the diameter (in kilometers) of the NEO whose name is "Apollo"?', row['diameter'])

iauCount = 0
blanksCount = 0
with open(CSVInputFile, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if row['name'] != '':
            iauCount +=1
        else:
            blanksCount +=1
    print('4a. How many NEOs have IAU names in the data set?', iauCount)
    print('4b. How many NEOs have Null names in the data set?', blanksCount)

diamterCount = 0
nullDiameter = 0
with open(CSVInputFile, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if row['diameter'] != '':
            diamterCount +=1
        if row['diameter'] == '':
            nullDiameter +=1
    print('5a. How many NEOs have diameters?', diamterCount)
    print('5b. How many NEOs have No diameter?', diamterCount)




# NEO close approaches - moments in time when the orbit of an astronomical body brings it close to Earth
# On which date(s) does Halley's Comet pass near to Earth?" or
# "How fast does Eros pass by Earth, on average?"

# with open('../data/cad.json', 'r') as file:
with open('data/cad.json', 'r') as file:

    #print(type(file))
    jsonData = json.load(file)
    # if type is dict and count of keys < 50
    #print((jsonData.keys()))
    # print('CAD fieldnames: ', jsonData['fields'])
    #print(len(jsonData['fields']))
    #print(type(jsonData['data']))

    #print((jsonData['fields']))
    #print((jsonData['data'][0:3]))


# jsonData['fields']  = ['des', 'orbit_id', 'jd', 'cd', 'dist', 'dist_min', 'dist_max', 'v_rel', 'v_inf', 't_sigma_f', 'h']
# jsonData['data'][0] = ['170903', '105', '2415020.507669610', '1900-Jan-01 00:11', '0.0921795123769547', '0.0912006569517418', '0.0931589328621254', '16.7523040362574', '16.7505784933163', '01:00', '18.1']
# TODO: Map fields to list values to create a list of dicts?
# for des = value in dict list?   {'des': '170903', 'orbit_id': '105', ...}, {'des': '170903', 'orbit_id': '105', ...}
    print('6. How many close approaches are in the cad.json data set?', len(jsonData['data']))
    print('7. On January 1st, 2000, how close did the NEO whose primary designation is "2015 CL" pass by Earth?')
    for i in range(len(jsonData['data'])):
        if '2015 CL' in jsonData['data'][i][0] and '2000-Jan-01' in jsonData['data'][i][3]:
            print(round(float(jsonData['data'][i][5]), 3), 'a/u')
            break
    print('8. On January 1st, 2000, how fast did the NEO whose primary designation is "2002 PB" pass by Earth?')
    for i in range(len(jsonData['data'])):
        if '2002 PB' in jsonData['data'][i][0] and '2000-Jan-01' in jsonData['data'][i][3]:
            result = jsonData['data'][i][8]
            print(round(float(result), 2),'km/s')
    #value2015CL = [dist for dist in jsonData if dist['name']]
    print('CAD:')
    print(jsonData['fields'])
    print(jsonData['data'][0])
    # list of tuples
    # print(list(zip(jsonData['fields'],jsonData['data'][0])))
    # print(list(zip(jsonData['fields'],jsonData['data'][1])))
    
    # dict of key value pairs
    print[(dict(zip(jsonData['fields'],jsonData['data'][2])))]

    
   
    