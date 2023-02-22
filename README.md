**Python SSH Command Line Tool**
___

Developed to automate work conducted specific to network infrastructure work, the tool automates the process of taking a *system snapshot* before work has began with a *system snapshot* taken after work has completed. This snapshot includes logging into network switches, running a set of commands, and saving the command output for documentation and later, verifiability.

Showdown prompts the user for login credentials, and switch host names. A folder is then created on the users Desktop and the tool SSH's into each switch and runs a set of commands predetermined within the codebase. The output of each command is saved to a SWITCHHOSTNAMEHERE.txt file placed within the desktop folder. The user is then prompted to either repeat the process, asking for additional switch host names, or to terminate the session.
___

**Requirements**
>Python 3.8

>Windows 10

**Install:**

>pip install showdown.ssh

**View install directory:**

>pip show showdown.ssh

**Launch the app:**

1. navigate to directory 
2. navigate to /showdown
>python showdown.py

**Uninstall:**

>pip uninstall -y showdown.ssh
___

`https://pypi.org/project/showdown.ssh/`
