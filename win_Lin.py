# WINDOWS TO LINUX
def winlin(localpath, remotepath, server, userName, password):
    import os
    import paramiko 
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=userName, password=password)
    sftp = ssh.open_sftp()
    localpath = 
    remotepath = 
    sftp.put(localpath, remotepath)
    print("File Copied from",localpath)
    print("To Location:", remotepath)
    sftp.close()
    ssh.close()

#localpath = 'C:/Users/Poovendran/data.csv'
#remotepath = '/home/mclen/dex/dags/data.csv'
#server = '10.10.1.78'
#password = "mclen123"

#windows path
localpath = '\\10.10.1.50\DeX_Source_Win\' 

#remotepath
remotepath = '\\10.10.1.100\DeX_Target_Win\'
server = 'serverid'
password = "password"

# -- Function Call
winlin(localpath, remotepath, server, userName, password)