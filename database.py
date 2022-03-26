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

        print(len(self._neos))        #23,967
        print(len(self._approaches)) #406,785
        i = 0

        # TODO: What additional auxiliary data structures will be useful?
        # filtered dictionary?  # ['a0001036', '1036', 'Ganymed', '37.675', 'N', 'Y'],
        # python3 main.py inspect --verbose --name Ganymed
            # NEO 1036 (Ganymed) has a diameter of 37.675 km and is not potentially hazardous.
            # - On 1911-10-15 19:16, '1036 (Ganymed)' approaches Earth at a distance of 0.38 au and a velocity of 17.09 km/s.
            # - On 1924-10-17 00:51, '1036 (Ganymed)' approaches Earth at a distance of 0.50 au and a velocity of 19.36 km/s.
            # - On 1998-10-14 05:12, '1036 (Ganymed)' approaches Earth at a distance of 0.46 au and a velocity of 13.64 km/s.
            # - On 2011-10-13 00:04, '1036 (Ganymed)' approaches Earth at a distance of 0.36 au and a velocity of 14.30 km/s.
            # - On 2024-10-13 01:56, '1036 (Ganymed)' approaches Earth at a distance of 0.37 au and a velocity of 16.33 km/s.
            # - On 2037-10-15 18:31, '1036 (Ganymed)' approaches Earth at a distance of 0.47 au and a velocity of 18.68 km/s.
        # LISTS
        # data structure NearEarthObject
        # ['a0001036', '1036', 'Ganymed', '37.675', 'N', 'Y'
         # [ 
          # ['1036', '1911-Oct-15 19:16', '0.381362839855777', '17.0936978226911', '794'],
          # ['1036', '1924-Oct-17 00:51', '0.496274614603618', '19.3628654227641', '794'],
          # ['1036', '1998-Oct-14 05:12', '0.464262946654528', '13.6399792167938', '794'],
          # ['1036', '2011-Oct-13 00:04', '0.359104318674552', '14.304703704289', '794'],
          # ['1036', '2024-Oct-13 01:56', '0.37409718734356', '16.3343740524295', '794'],
          # ['1036', '2037-Oct-15 18:31', '0.466187644979184', '18.6810529423632', '794']
         # ]
        # ]

        # data structure CloseApproach
        # ['1036', '1911-Oct-15 19:16', '0.381362839855777', '17.0936978226911', '794'
         # [['a0001036', '1036', 'Ganymed', '37.675', 'N', 'Y']]]

        #DICTS


        # xmethods to fetch an NEO by primary designation or by name,
        # ?collection of _neos that match filter
        # ?collection of _approaches that match filter 
        
        # TODO: Link together the NEOs and their close approaches.

        i = 0
        for i in range(len(self._approaches)):        
            if self._approaches[i][0] == '1036':
                print(self._approaches[i])   
        # neo by designation
        for i in range(len(self._neos)):
            if self._neos[i][1] == '1036':
                print(self._neos[i])  
        
        # neo by name
        for i in range(len(self._neos)):
            if self._neos[i][2] == 'Ganymed':
                print(self._neos[i])  
   

            # if self._approaches[i][0] == '1036':
                # print(self._neos[i], self._approaches[i])          
                # assign the CloseApproach's .neo attribue(curently NONE) == NearEarthObject{all attributes?}
                # self._approaches[i][-1] = self._neos[i] # move this down? to include the list of close approaches?    
                # neo.approaches[] += cad(des, cd, dist, and v_rel) time, designation, distance and velocity
                # self._neos.approaches += self._approaches
                # self._neos[i][-1].append(self._approaches[i])      
            i+=i
        # print(self._neos)
        # print(self._approaches[:50])
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
        return None

    def query(self, filters=()):
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
        for approach in self._approaches:
            yield approach
