import os
from netmiko import ConnectHandler
from time import localtime, strftime


TIME = strftime('%m.%d.%I%M%p', localtime())


def requestusername():
    username = input('Please enter username: ')
    return username


def requestpassword():
    password = input('Please enter passphrase: ')
    return password


def createdevicefile(username, password):
    print('Type and enter each host name.\n\
Type "exit" when finished.')
    with open('devicenames', 'w') as devicefile:
        while True:
            host = input('Host name: ')
            if host != 'exit':
                newline = f'device_type: cisco_ios\n\
host: {host}\n\
username: {username}\n\
password: {password}'
                devicefile.write(newline + '\n')
            else:
                devicefile.close()
                break


def deletedevicefile():
    os.remove('devicenames')


# whid-co-dis-sw#
# whid-co-acc-sw#
# whid-co-acc-rsw#
# whid-co-wlc-#
# whid-fc-agg-r#


def sshconnect(**device):
    # make a connection
    connectdevice = ConnectHandler(**device)
    return connectdevice


def runcommands(commands, connectdevice):
    with open(f'{TIME}', 'w') as newfile:
        for command in commands:
            result = connectdevice.send_command(command)
            newfile.write(result)
    newfile.close()


def sshdisconnect(connectdevice):
    disconnectdevice = connectdevice.disconnect()
    return disconnectdevice


commands = [
    'show ssh',
    'show ver',
]


username, password = requestusername(), requestpassword()
createdevicefile(username, password)

#  pending review  ########################
connectdevice = sshconnect(**device)
runcommands(commands, connectdevice)
disconnectdevice = sshdisconnect(connectdevice)
##########################################

deletedevicefile()


# make a directory - os.mkdir()? to upload multiple files?
# learn/apply encryption for the file? use hash?
# additional devices?

#######################################################################

# config.txt
# mode=development
# host=127.0.0.1
# port=22
# user=admin
# pass=admin

config = {}
with open('config.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        key, value = line.split("=")
        value = value.replace('\n', '')
        config[key] = value
        print(f'Added {key} {value}')

with open('config.txt', 'w') as f:
    for key, value in config.items():
        l = f'{key}={value}\n'
        f.write(l)

# list of required installs for a program
# python3 -m pip install requirements.txt
