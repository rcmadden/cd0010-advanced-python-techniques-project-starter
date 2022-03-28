"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
# from ast import Pass
# from asyncio.windows_events import NULL
# from curses.ascii import NUL
# from time import time
# from unicodedata import name
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, **kwargs):
    # def __init__(self, id, designation='', name=None, diameter=float('nan'), hazardous=False, full_name=None, approaches=[]):

        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `designation`, `name`, `diameter`, and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by `None`
        # and a missing diameter being represented by `float('nan')`.
        # self.designation = ''
        # self.name = None
        # self.diameter = float('nan')
        # self.hazardous = False
        # self.id = id
        # self.designation = designation # unique
        # self.name = name # may be missing but will have id
        # self.diameter = diameter # optional
        # self.hazardous = hazardous
        # self.full_name = full_name # explore the datas full_name field

        # # Create an empty initial collection of linked approaches.
        # self.approaches = [] #create a new emplty approach for each neo
            
        for key, value in kwargs.items():
            setattr(self, key, value)

            if hasattr(self,'diameter') and type(self.diameter) == str:
                if self.diameter != '':
                    self.diameter = float(self.diameter)  
                elif self.diameter == '':
                    self.diameter = float('nan')

            # if hasattr(self,'diameter'):
            #     if self.diameter != '':
            #         self.diameter = float(self.diameter)  
            #     else:
            #         self.diameter = float('nan')


    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        # TODO: Use self.designation and self.name to build a fullname for this object.
        if self.name == None or self.name == '':
            fullname = self.designation
        else:
            fullname = self.designation + ' ' + self.name
        return f"NEO Fullname: {fullname} {self.full_name}"

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        # TODO: find a better way to writ this
        if self.hazardous == True:
            hazard_staus = 'is poteintially hazardous'
        else: 
            hazard_staus = 'is not likely hazardous'

        return f"{self.designation} fullname ({self.fullname}) full_name {self.full_name}  has a diameter of {self.diameter:.3f} km and {hazard_staus} id: {self.id}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""

        return f"NearEarthObject(id={self.id}, designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"



class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, **kwargs):
    # def __init__(self, _designation='', time=None, distance=0.0, velocity=0.0, orbit_id=None, neo=None):

        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        # self._designation = ''
        # self.distance = 0.0
        # self.velocity = 0.0
        # self._designation = _designation
        # self.distance = float(distance)
        # self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        
        # self.orbit_id = orbit_id # explore the values in this field
        # dict.setdefault(key, None) # can defaults be set? yes
            # TODO: collections.defaultdict – dict subclass that calls a factory function to supply missing 
        for key, value in kwargs.items():
            setattr(self, key, value)
            if hasattr(self,'distance') and type(self.distance) == str:
                if(self.distance != ''):
                    self.distance = float(self.distance)
                else:
                    self.distance = float(0.0)
     
            if hasattr(self,'velocity') and type(self.velocity) == str:
                if(self.velocity != ''):
                    self.velocity = float(self.velocity)
                else:
                    self.velocity = float(0.0)

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # xTODO: Use this object's `.time` attribute and the `datetime_to_str` function to
        # build a formatted representation of the approach time.
        # TODO: Use self.designation and self.name to build a fullname for this object.
        # print('BEFORE', self.time, type(self.time))

        if self.time == '':
            self.time = None
        else:
            self.time = cd_to_datetime(self.time)  # TODO: Use the cd_to_datetime function for this attribute.
        # print('AFTER', self.time, type(self.time))
        # print('datetime_to_str', datetime_to_str(self.time), type(self.time))
        # return f"CloseAproach Time({self.time})"
        return self.time

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return f"On {self.time_str!r}, '{self._designation}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s. Orbit Id {self.orbit_id}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(_designation={self._designation}, time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}."

# use to run module from cli
#CloseApproach(**{'_designation': '170903', 'time': '1900-Jan-01 00:11', 'distance': '0.0921795123769547', 'velocity': '16.7523040362574', 'orbit_id': '105'})
# NearEarthObject(**{'id': 'a0000433', 'designation': '433', 'name': 'Eros', 'diameter': '', 'hazardous': 'N', 'neo': 'Y', 'full_name': '433 Eros (A898 PA)'})