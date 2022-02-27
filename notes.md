Project Rubric: https://review.udacity.com/#!/rubrics/2935/view

Initial file review questions from Project: Section 4 Scaffolding:
1. main.py  
**won't need to write any code that prompts the user for input**
- 397 DO NOT MODIFY "wraps the command-line tool, orchestrates the data pipeline by ***invoking the functions and classes that you'll write"*** 
- 397 lines of code - do I try to unerstand this? to what level?
- []what is shlex?
- What does this do? from database import NEODatabase
- How does this work? from filters import create_filters, limit
- How do paths work? # Paths to the root of the project and the `data` subfolder.
PROJECT_ROOT = pathlib.Path(__file__).parent.resolve()
- How does this start? stop? `cmd.Cmd` shell - a specialized tool for command-based REPL sessions.
- "POSIX shell-like syntax" What is a POSIX shell? what is it's syntax like?
- why does do_q only seem to call do_query?  Is this neccessary?
- line 365: can I rewrite this the trey way? changed = [f for f in PROJECT_ROOT.glob('*.py') if f.stat().st_mtime > _START]
- line 381: does this assign the return value of this function to all 3 variables? parser, inspect_parser, query_parser = make_parser()
- line 385: # Extract data from the data files into structured Python objects. How do args work?
- [x] what starts the program? main() with the command line arguments and database file load
TASK 1: - 10 TODOs
    [ ] 
    2. models.py need to review:
        [] classes 
        [] change argument on constructor 
        [] @property decorators
        [] f-strings and string formatting
    - line 12 `CloseApproach` maintains a reference to its NEO.  ? with an attribute? dict?
    - line 70 "!r" in f-strings??
    - line 83 - (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor. how and where was it "private"? and what does/did that look like? How does it change after being replaced in the constuctor?
    - class NearEarthObject
        * maintains a collection of its close approaches -
        initialized to an empty collection, but eventually populated in the
        `NEODatabase` constructor.
Task 2a
    3. extract.py - write functions to read information from data files, creating NearEarthObjects and CloseApproaches from the data.
    - what is the signifacnace of :param :return ':'? in the doc strings?
    - TODOs 2 functions to extract data from the csv and json files
    - accept command line arguments for the file path??
    - return a collection of NearEarthObject's and CloseApproach'es. What file are these in? Are these classes? what do I need to pass to them ?

Task 2 & 3
    4. database.py - is this really a "database"? is this a python industry term of this structure?
    - link the colose approaches and neos 
        - .approaches` attribute of each NEO has a collection of that NEO's close approaches, and 
        - the `.neo` attribute of each close approach references the appropriate NEO.
    - write functions
        - find neo's by name
        - find neos by primary designation
        - Query close approaches to generate those that match a collection of filters.
        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.
            - query the dataset with a collection of user-specified filters to generate an iterable stream of matching results.
Tasks 3a & 3c
    5. filters.py
    WHAT does all this vocabulary mean in terms of implementation details and how would I describe this (interfac?) in my own words
    - create_filters can be thought to return 
        * a collection of instances of subclasses of `AttributeFilter` - a 
        * 1-argument callable (on a `CloseApproach`) 
        * constructed from a 
        * comparator (from the `operator` module), a 
        * reference value, and 
        * a class method `get` that 
        * subclasses can 
        * override to fetch an attribute of interest from the supplied `CloseApproach`.
        * functions as a callable predicate 
        * infix notation
        * Concrete subclasses can override the `get` classmethod to provide 
        * custom behavior 
        * binary predicate
        * the second (right-hand side) argument to the operator function. For example, an `AttributeFilter` with `op=operator.le` and `value=10` will, when called on an approach, evaluate `some_attribute <= 10`.
        *  :param op: A 2-argument predicate comparator (such as `operator.le`).
        * line 59  @classmethod decorator?
        * line 63 Concrete subclasses must override this method 
        * create filters function accepts a bunch of named arguments
        * Each option is `None` if not specified at the command line (in particular, this means that the `--not-hazardous` flag results in `hazardous=False`, not to be confused with `hazardous=None`)
        * The return value must be compatible with the `query` method of `NEODatabase`
    because the main module directly passes this result to that method. For now,
    this can be thought of as a collection of `AttributeFilter`s.
        * limt function Produce a limited stream of values from an iterator.
        * 5. Tasks: Task3a Creating filters: filters.py class AttributeFilter:
            - abstract superclass's get method raises UnsupportedCriterionError
            - a custom subclass of NotImplementedError, but 
            - concrete subclasses will be able to override this method to actually get a specific attribute of interest.
        * Task 3c limit
            - As a hint, (although not necessary) you may find the itertools.islice function helpful: https://docs.python.org/3/library/itertools.html#itertools.islice
            - test this funciton: python3 -m unittest tests.test_query tests.test_limit
    
Task 4 write.py
        * write a stream to csv or json based on filename ending supplied on command line
        * If there are no results, then write_to_csv should just write a header row, and write_to_json should just write an empty list.
        The csv module will be able to handle some of these requirements for you:
        * write_to_csv header columns should be: 'datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous'
        * A missing name must be represented in the CSV output by the empty string (not the string 'None'). 
        * A missing diameter must be represented in the CSV output either by the empty string or by the string 'nan'. 
        * The potentially_hazardous flag must be represented in the CSV output either by the string 'False' or the string 'True' 
        * write_to_json The top-level JSON object must be a list, with each entry representing one CloseApproach from the stream 
        * Each entry should be a dictionary mapping the keys 'datetime_utc', 'distance_au', 'velocity_km_s' to the associated values on the CloseApproach object and the 
        * key neo to a dictionary mapping the keys 'designation', 'name', 'diameter_km', 'potentially_hazardous' to the associated values on the close approach's NEO.
        JSON DATA TYPES
        * datetime_utc value should be a string formatted with datetime_to_str from the helpers module;  
        * distance_au and velocity_km_s values should be floats;  
        * designation and name should be strings (if the name is missing, it must be the empty string); 
        * diameter_km should be a float (if the diameter_km is missing, it should be the JSON value NaN, which Python's json loader successfully rehydrates as float('nan'));  
        * potentially_hazardous should be a boolean (i.e. the JSON literals false or true, not the strings 'False' nor 'True').
    Deduplicating Serialization
        * While you are free to concretely implement these methods in any way you would like, we recommend that you 
        * add .serialize()methods to the NearEarthObject and CloseApproach classes that each produce a dictionary containing relevant attributes for CSV or JSON serialization.
        Example: 
        >>> neo = NearEarthObject(...)
        >>> approach = CloseApproach(...)
        >>> print(neo.serialize())
        {'designation': '433', 'name': 'Eros', 'diameter_km': 16.84, 'potentially_hazardous': False}
        >>> print(approach.serialize())

helpers.py
    * uses datetime module to convert values to and from strings 
run tests/ 'python3 -m unittest --verbose'

Testing:
    To run all 73 unit tests
    Commands:
        python3 -m unittest
        python3 -m unittest --verbose
    Tests for this specific task are in the tests.test_write module.

Tasks to Complete Overview:

[x] Task 0: Inspect the data. (data/neos.csv and data/cad.json). You already did this!
[ ] Task 1: Build models to represent the data. (models.py)
    * Write __init__ and __str__ methods for NearEarthObject and CloseApproach
[ ] Task 2: Extract the data into a custom database (2a. extract.py and 2.b database.py)
    - able to run the inspect subcommand.
        Task 2a: Extract data. (extract.py): Implement load_neos and load_approaches to read data from CSV and JSON files.
        Task 2b: Process data. (database.py) Implement the constructor for NEODatabase, preprocessing the data to help with future queries.
        Write methods to get NEOs by primary designation or by name.


[ ] Task 3: Create filters to query the database to generate a stream of matching CloseApproach objects, and limit the result size. (3a. & 3.c filters.py and 3.b database.py)
    - able to run the query subcommand without the --outfile argument
    Task 3a: Create filters. (filters.py) - Define a hierarchy of Filters.
    Implement create_filters to create a collection of filters from user-specified criteria.

    Task 3b: Query matching close approaches (database.py) Implement the query method to generate a stream of CloseApproaches that match the given filters.
    
    Task 3c: Limit results. (filter.py) Write limit to produce only the first values from a generator.


[ ] Task 4: Save the data to a file. (write.py)
    -  able to run 
    Implement write_to_csv and write_to_json to save structured data to a formatted file.