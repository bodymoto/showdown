import os
from netmiko import ConnectHandler


def requestHost():
    host = input('Enter a host name: ')
    return host


def requestUsername():
    username = input('Enter your username: ')
    return username


def requestPassword():
    password = input('Enter your password: ')
    return password


def createDeviceDictionary(host, username, password):  # used with ConnectHandler()
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password
    }
    return device


def sshConnect(device):  # ssh to host
    connectDevice = ConnectHandler(**device)
    return connectDevice


def myCommands():  # input device, spit out commands for device
    commands = [
        'show ssh',
        'show ver',
    ]
    return commands


def createDirectory():  # create a folder on desktop to store output
    try:
        os.mkdir(os.path.expanduser('~/Desktop/Network Checks/'))
    except FileExistsError:
        pass


def runCommands(host, connectDevice, commands):  # runs commands and saves in a file
    path = os.path.expanduser('~/Desktop/Network Checks/')
    with open(path + host + '.txt', 'w') as newfile:
        for command in commands:
            result = connectDevice.send_command(command)
            newfile.write(result)


def sshDisconnect(connectDevice):
    connectDevice.disconnect()


def sessionSetup():  # data that wont change during session
    username, password = requestUsername(), requestPassword()
    createDirectory()
    return username, password


def issueCommands(username, password):  # ssh to host, run commands
    host = requestHost()
    device = createDeviceDictionary(host, username, password)
    connectDevice = sshConnect(device)
    commands = myCommands()  # input device
    runCommands(host, connectDevice, commands)
    sshDisconnect(connectDevice)


def additionalHosts(username, password):  # ask for additional host, repeat if applicable
    while True:
        print('Any additional hosts?')
        confirm = input('Enter "y" to continue: ')
        if confirm == 'y':
            issueCommands(username, password)
        else:
            break


def main():
    username, password = sessionSetup()
    issueCommands(username, password)
    additionalHosts(username, password)


main()
