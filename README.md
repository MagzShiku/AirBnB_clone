# An Airbnb cloning project
# We are starting with the console portion of the project. A console is a control panel where commands run through for interaction between the user and the app.


# We shall start creating the console with the command line interpreter, which works like the shell terminal. The CMD line interpreter will be created using cmd.Cmd method. By importing cmd.

# What we build during this project will be used for HTML/CSS, templating, database storage, API, and front-end integration...

# the tasks:
	# Create a BaseModel
	# Create a serialization/deserialization
	# Create Classes: (User, State, City, Place ...)
	# Create the first abstracted storage engine (File Storage)
	# Create unittests to validate the Classes and Storage Engine

# This is the code for creating the command line interpreter:

	import cmd

	class Airbnb1cmd(cmd.Cmd):
		prompt = "(AirbnbJM) "

	Airbnb1cmd().cmdloop()


# The command line Interprettershouls be able to:
	# Create a new object (New use, New Place)
	# Retrieve an object from a file, a database, etc...
	# Do operations on objects (Count, compute stats, etc...)
	# Update attributes of an object
	# Destroy an object

# Our Shell will work like this in an interactive mode:
	$ ./console.py
	(hbnb) help
	
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	
	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$

# and like this in non-interactive mode:
	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$

# All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
