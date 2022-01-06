import os
from netmiko import ConnectHandler


def requesthost():
    host = input('Enter a host name: ')
    return host


def requestusername():
    username = input('Enter your username: ')
    return username


def requestpassword():
    password = input('Enter your password: ')
    return password


def createdevicedictionary(host, username, password):
    # used with ConnectHandler()
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password
    }
    return device


def sshconnect(device):
    # make a connection
    connectdevice = ConnectHandler(**device)
    return connectdevice


def mycommands():  # input device, spit out commands for device
    commands = [
        'show ssh',
        'show ver',
    ]
    return commands


def createdirectory():
    # create a folder on user desktop
    try:
        os.mkdir(os.path.expanduser('~/Desktop/Network Checks/'))
    except FileExistsError:
        pass


def runcommands(host, connectdevice, commands):
    # create a file inside desktop folder and record command output
    path = os.path.expanduser('~/Desktop/Network Checks/')
    with open(path + host + '.txt', 'w') as newfile:
        for command in commands:
            result = connectdevice.send_command(command)
            newfile.write(result)


def sshdisconnect(connectdevice):
    connectdevice.disconnect()
