import definitions as do

host, username, password = do.requesthost(), do.requestusername(), do.requestpassword()
device = do.createdevicedictionary(host, username, password)
connectdevice = do.sshconnect(device)
commands = do.mycommands()  # input device
do.createdirectory()
do.runcommands(host, connectdevice, commands)
do.sshdisconnect(connectdevice)
