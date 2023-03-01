**Python SSH Command Line Tool**
___

Showdown was developed to automate steps during network infrastructure work within the domain of IT. The tool automates the process of taking a network *snapshot* before work has began with another *snapshot* taken after work has completed. This snapshot includes logging into network switches, running a set of commands, and saving the command output for documentation and later, verifiability.

Showdown prompts the user for login credentials, and local switch host names. A folder is then created on the users desktop before establishing an SSH connection into each host and running a set of commands - predetermined within the codebase. The output of each command is copied to a HOSTNAME.txt file and saved to the desktop folder. The user is then prompted to either repeat the process, asking for additional host names, or terminates the session.

Many useful Cisco commands use the verbose *show* which was a source of inspiration when naming this repo.
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
