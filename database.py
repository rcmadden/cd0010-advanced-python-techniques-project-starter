"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """
    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches

        # this takes >12 minuetes to run only do this in function/filters
        # for i in range(len(self._neos)):
            # self._neos[i]['approaches'] = ([x for x in self._approaches if x['_designation'] == self._neos[i]['designation']])


        # TODO: What additional auxiliary data structures will be useful?
        # add_neo and add_approaches proper
        # filtered dictionary?  # ['a0001036', '1036', 'Ganymed', '37.675', 'N', 'Y'],
        # python3 main.py inspect --verbose --name Ganymed
            # NEO 1036 (Ganymed) has a diameter of 37.675 km and is not potentially hazardous.
            # - On 1911-10-15 19:16, '1036 (Ganymed)' approaches Earth at a distance of 0.38 au and a velocity of 17.09 km/s.
            # - On 1924-10-17 00:51, '1036 (Ganymed)' approaches Earth at a distance of 0.50 au and a velocity of 19.36 km/s.
            # - On 1998-10-14 05:12, '1036 (Ganymed)' approaches Earth at a distance of 0.46 au and a velocity of 13.64 km/s.
            # - On 2011-10-13 00:04, '1036 (Ganymed)' approaches Earth at a distance of 0.36 au and a velocity of 14.30 km/s.
            # - On 2024-10-13 01:56, '1036 (Ganymed)' approaches Earth at a distance of 0.37 au and a velocity of 16.33 km/s.
            # - On 2037-10-15 18:31, '1036 (Ganymed)' approaches Earth at a distance of 0.47 au and a velocity of 18.68 km/s.

        
        # TODO: Link together the NEOs and their close approaches.

        ##########################
        # #DICTS 
        # neos
        # [{'id': 'a0000433', 'designation': '433', 'name': 'Eros', 'diameter': '16.84', 'hazardous': 'N', 'neo': 'Y', 'full_name': '   433 Eros (A898 PA)'}, {'id': 'a0000719', 'designation': '719', 'name': 'Albert', 'diameter': '', 'hazardous': 'N', 'neo': 'Y', 'full_name': '   719 Albert (A911 TB)'}, {'id': 'a0000887', 'designation': '887', 'name': 'Alinda', 'diameter': '4.2', 'hazardous': 'N', 'neo': 'Y', 'full_name': '   887 Alinda (A918 AA)'}, {'id': 'a0001036', 'designation': '1036', 'name': 'Ganymed', 'diameter': '37.675', 'hazardous': 'N', 'neo': 'Y', 'full_name': '  1036 Ganymed (A924 UB)'}, {'id': 'a0001221', 'designation': '1221', 'name': 'Amor', 'diameter': '1.0', 'hazardous': 'N', 'neo': 'Y', 'full_name': '  1221 Amor (1932 EA1)'}]

        # close approaches
        # [{'_designation': '170903', 'time': '1900-Jan-01 00:11', 'distance': '0.0921795123769547', 'velocity': '16.7523040362574', 'orbit_id': '105'}, {'_designation': '2005 OE3', 'time': '1900-Jan-01 02:33', 'distance': '0.414975519685102', 'velocity': '17.918395877175', 'orbit_id': '52'}, {'_designation': '2006 XO4', 'time': '1900-Jan-01 03:13', 'distance': '0.114291499199114', 'velocity': '7.39720266467069', 'orbit_id': '15'}, {'_designation': '7088', 'time': '1900-Jan-01 05:01', 'distance': '0.237367466253556', 'velocity': '4.78123058453747', 'orbit_id': '233'}, {'_designation': '2017 EE23', 'time': '1900-Jan-01 07:16', 'distance': '0.388708125934362', 'velocity': '9.93428771818077', 'orbit_id': '6'}] 
        # 
        # print(len(self._neos))        #23,967
        # print(len(self._approaches)) #406,785
        
        # neos with approaches:
        # ganymed = {'id': 'a0001036', 'designation': '1036', 'name': 'Ganymed', 'diameter': '37.675', 'hazardous': 'N', 'neo': 'Y', 'full_name': '  1036 Ganymed (A924 UB)', 'approaches': 
        # [{'_designation': '1036', 'time': '1911-Oct-15 19:16', 'distance': '0.381362839855777', 'velocity': '17.0936978226911', 'orbit_id': '794'}, {'_designation': '1036', 'time': '1924-Oct-17 00:51', 'distance': '0.496274614603618', 'velocity': '19.3628654227641', 'orbit_id': '794'}, {'_designation': '1036', 'time': '1998-Oct-14 05:12', 'distance': '0.464262946654528', 'velocity': '13.6399792167938', 'orbit_id': '794'}, {'_designation': '1036', 'time': '2011-Oct-13 00:04', 'distance': '0.359104318674552', 'velocity': '14.304703704289', 'orbit_id': '794'}, {'_designation': '1036', 'time': '2024-Oct-13 01:56', 'distance': '0.37409718734356', 'velocity': '16.3343740524295', 'orbit_id': '794'}, {'_designation': '1036', 'time': '2037-Oct-15 18:31', 'distance': '0.466187644979184', 'velocity': '18.6810529423632', 'orbit_id': '794'}]}
        
        #`.approaches` attribute of each NEO 
        # has a collection of that NEO's close approaches
        # the `.neo` attribute of each close approach references the appropriate NEO

        #########
        # approaches[x].neo property == neos['designation']

        # approaches0=self._approaches[0]

        # approaches0['approaches']=[]

        # approaches0['approaches'].append({'_designation': '170903', 'time': '1900-Jan-01 00:11', 'distance': '0.0921795123769547', 'velocity': '16.7523040362574', 'orbit_id': '105'})

        # approaches0['approaches'][0]['_designation']
        

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        # TODO: Fetch an NEO by its primary designation.

        for i in range(len(self._neos)):
            if self._neos[i]['designation'] == designation:
                # only add approaches for mathches
                self._neos[i]['approaches'] = ([x for x in self._approaches if x['_designation'] == self._neos[i]['designation']])
                return self._neos[i]

        return None


    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        # TODO: Fetch an NEO by its name.
        for i in range(len(self._neos)):
            if self._neos[i]['name'] == name:
                # only add approaches for mathches
                self._neos[i]['approaches'] = ([x for x in self._approaches if x['_designation'] == self._neos[i]['designation']])
                return self._neos[i]
        
        # result = [x for x in self._neos if x['name'] == name]
        # if result:
        #     return result
        # else:
        #     return None
        return None

    # def query(self, filters=()):
    def query(self, filters):

        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaningfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        # TODO: Generate `CloseApproach` objects that match all of the filters.

        self.filters = filters
        print('filters: ', self.filters)
        


        for approach in self._approaches:
            # print('yield approach: ', approach)
            # if self.filters['date'] and self.filters['date'] != approach['time']:
                # continue
            if self.filters['distance_min'] and not self.filters['distance_min'] <= float(approach['distance']):
                continue
            yield approach


# str '1900-Jan-03 02:43'
# time.strptime(approach_date,'%y-%b-%d %I:%M')
# filter datetime.date 1969-07-29
        # return self.filters


        # assign the aproaches['neo'] key to the matching neo['designation']
        # carefull there are 400k self._approaches so get the filtered set first 
        # convert this list comprehension into a loop
        
        # for i in range(len(self._approaches)):
        #     if self._approaches[i]['name'] == name:
        #         # only add approaches for mathches
        #         self._approaches[i]['neo'] = ([x for x in self._approaches if x['_designation'] == self._neos[i]['designation']])
        #         return self._approaches[i]    

     