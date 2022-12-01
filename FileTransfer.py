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

localpath = '*/data.csv' #locapath
remotepath = '*/data.csv' #destinationpath
server = '10.10.1.78'
password = "mclen123"
userName = 'root'

# -- Function Call
winlin(localpath, remotepath, server, userName, password)


# ------------------------------------------------------------------------------
# Local filecopy
def copyfile(src, dec):
    import shutil
    shutil.copy2(src, dec)
    print("File Copied",src,dec)
    
src = "/home/mclen/dex/sql_files/DBData_encrypted"
dec = "/home/mclen/dex/sql_files/DBData_encrypted"

# -- Function Call
copyfile(src, dec)
# ------------------------------------------------------------------------------

# Windows to Windows File Transfer

import shutil, sys
def Copy(source, destination, include_empty_dirs=True):
    
    source = os.path.abspath(source)
    for p, ds, fs in os.walk(source):
        if include_empty_dirs:
            for d in ds:
                d_path = os.path.join(destination, p[len(source):], d)
                # Make dirs
                if not os.path.isdir(d_path):
                    print('Making {0}'.format(d_path))
                    os.makedirs(d_path)
        for f in fs:
            s_path = os.path.join(p, f)
            d_path = os.path.join(destination, p[len(source) + 1:], f)
            print('Copying {0} -> {1}'.format(s_path, d_path))
            # Make dirs
            if not os.path.isdir(os.path.dirname(d_path)):
                print('Making {0}'.format(d_path))
                os.makedirs(os.path.dirname(d_path))
            # Copy the file
            shutil.copy(s_path, d_path)
            
    print("File Transfer Complete")
            
source = "\\\\10.10.1.50\\DeX_Source_Win\\"
destination = "\\\\10.10.1.100\\DeX_Target_Win\\"

Copy(source, destination, include_empty_dirs=True)
# ------------------------------------------------------------------------------