# An Airbnb clonning project
# we are starting with the console. A console is a control panel where commands run through for there to be any form of interraction between user and the app
# We shall start creating the console by creating the command prompt which works like the shell terminal. the CMD will be created using cmd.Cmd
# this is the code:

import cmd

class Airbnb1cmd(cmd.Cmd):
	prompt = "(AirbnbJM) "

Airbnb1cmd().cmdloop()
