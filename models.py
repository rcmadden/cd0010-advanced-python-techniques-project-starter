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
   
    def __init__(self, **kwargs):

        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """

            
        for key, value in kwargs.items():
            setattr(self, key, value)

            if hasattr(self,'diameter') and type(self.diameter) == str:
                if self.diameter != '':
                    self.diameter = float(self.diameter)  
                elif self.diameter == '':
                    self.diameter = float('nan')


    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name == None or self.name == '':
            fullname = self.designation
        else:
            fullname = self.designation + ' ' + self.name
        return f"NEO Fullname: {fullname} {self.full_name}"

    def __str__(self):
        """Return `str(self)`."""
      
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
 
    def __init__(self, **kwargs):

        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
   
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
        
        if self.time == '':
            self.time = None
        else:
            self.time = cd_to_datetime(self.time)  

        return self.time

    def __str__(self):
        """Return `str(self)`."""

        return f"On {self.time_str!r}, '{self._designation}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s. Orbit Id {self.orbit_id}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(_designation={self._designation}, time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}."
