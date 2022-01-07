import definitions as do


def staticdata():
    username, password = do.requestusername(), do.requestpassword()
    do.createdirectory()
    return username, password


def dynamicdata(username, password):
    host = do.requesthost()
    device = do.createdevicedictionary(host, username, password)
    connectdevice = do.sshconnect(device)
    commands = do.mycommands()  # input device
    do.runcommands(host, connectdevice, commands)
    do.sshdisconnect(connectdevice)


def repeatdynamicdata(username, password):
    while True:
        print('Any additional hosts?')
        confirm = input('Enter "y" to continue: ')
        if confirm == 'y':
            dynamicdata(username, password)
        else:
            break


def main():
    username, password = staticdata()
    dynamicdata(username, password)
    repeatdynamicdata(username, password)


main()
