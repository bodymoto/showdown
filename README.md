**Python SSH Command Line Tool**
___

*"This GitHub repository project is a Python-based internal tool that was developed to automate work conducted before and after any system or network-related project work. It was designed with the intention to help ensure the integrity of the network remained while within the expected downtime window. The tool starts by asking for login credentials, followed by a series of switch host names. It then logs into each switch and runs a series of commands predetermined within the codebase. If a folder does not exist, a new folder is created on the user's desktop and each switch output is saved within a text file stored within said folder with the appropriate switch host name as the file name. After completing the process for all the switches, the application prompts the user to ask if any additional switches existed - to repeat the process. If not, the application terminates. This tool was specifically developed for use in the IT industry and was used in a previously held position to streamline and automate work processes."*

<sub>With the exception of one edit, this description was written by GPT (Generative Pre-training Transformer) model created by OpenAI. No specific version number has been provided at this time. ChatGPT Jan 9th, 2023 release.</sub>
___

**Requirements**
>Python 3.8

>Windows 10

**Install:**

>pip install showdown.ssh

**Run:**

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
