from netmiko import ConnectHandler


# receive login creds
def askforusername():
    username = input('Please enter username: ')
    return username


def askforkeyphrase():
    keyphrase = input('Please enter passphrase: ')
    return keyphrase


# ask for device
def askfordevice():
    device = input('Please enter device: ')
    return device


# username = askforusername
# keyphrase = askforkeyphrase
device = askfordevice()

# list of commands
commands = ['show ap sum',
            'show ver',]

# make a connection
def connectdevice(device, commands):
    # ssh
    # provide creds
    # create file
    # run commands
    # write commands
    # close file
    # close ssh

    ssh = ConnectHandler(device)
    # make a directory - os.mkdir()? to upload multiple files?
    with open('{}'.format(device), 'w') as newfile:
        for command in commands:
            result = ssh.send_command(commands)
            newfile.write(result)
    newfile.close()
    ssh.disconnect()


# store data
# close connection
# additional devices?

