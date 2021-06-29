# Life in Python
This project is an implementation of Conway's Game of Life (or Life for short) in Python.

## About Life
For information about the game, see [About Life](https://github.com/bshapka/life-in-x/blob/main/ABOUT_LIFE.md).
For information about the creator of the game, see [About John Conway](https://github.com/bshapka/life-in-x/blob/main/ABOUT_CONWAY.md).

## Running the Project
The following is a set of recommended directions for running the project. Note that these directions
assume a Python 3 interpreter exists and that it has been associated with the shell command `python3`.
The project was developed and tested with version 3.8.2 of Python. Compatibility with previous versions may 
exist but is not guaranteed.
* Start a shell session and navigate to the root directory of the project/cloned repo
* Run the command `python3 -m venv venv` to create a Python 3 virtual environment (venv) using your
Python 3 setup
* Run the command `source venv/bin/activate` to activate the venv
* Run the command `pip install --upgrade pip` to upgrade pip (the Python package manager)
* Run the command `python -m pip install -r requirements.txt` to install the required 
packages

From the root of the project directory, you should now be able to do the following:
* To play the game, run the command `./venv/bin/python3 life.py`
* To run all tests, run the command `./venv/bin/python3 -m pytest test/`

When you are done, you can deactivate the venv using the command `deactivate`. If you want to run 
the game or tests again after deactivating the venv, first reactivate the venv using the command 
above.

## Implementation Details
This section assumes basic familiarity with Life. If you are not familiar with Life but want to 
read this section, please read the section [About Life](https://github.com/bshapka/life-in-x/blob/main/ABOUT_LIFE.md), 
or consult a source like Wikipedia on the game.

All source files are well-documented, so explanations of or details about these files will not be supplied here.

Common implementations of Life represent the state of a world as a 2D list of bits or booleans. Typically 
a live cell is truthy while a dead cell is falsy. While this approach is intuitive, dead calls don't need
to be stored, and doing so can have notable costs in terms of memory usage.

An alternative approach is to store only the coordinates of live cells, requiring significantly less
memory. By representing coordinates as tuples and storing them in a set, further efficiencies are 
gained via hashing.

This implementation uses a toroidal grid. As such, objects that leave the screen on one edge will 
re-enter the screen with the same trajectory and velocity at the equivalent location on the opposing
edge.
