from netmiko import ConnectHandler


# receive login creds
def askforusername():
    username = input('Please enter username: ')
    return username


def askforpassword():
    password = input('Please enter passphrase: ')
    return password


# ask for device
def askforhostname():
    hostname = input('Please enter host name: ')
    return hostname


def sshconnect(**device):
    # make a connection
    connectdevice = ConnectHandler(**device)
    return connectdevice


def runcommands(commands, connectdevice):
    with open('{}'.format(host), 'w') as newfile:
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


username = askforusername()
password = askforpassword()
host = askforhostname()


device = {
    'device_type': 'cisco_ios',  # use device type 'juniper' for juniper equipment
    'host': host,
    'username': username,
    'password': password,
    # 'port': defaults to port '22' but may be specified
}


connectdevice = sshconnect(**device)
runcommands(commands, connectdevice)
disconnectdevice = sshdisconnect(connectdevice)


# make a directory - os.mkdir()? to upload multiple files?
# learn/apply encryption for the file? use hash?
# additional devices?

