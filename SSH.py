def SSH_get(server, username, password, localpath, remotepath):
    import os
    import paramiko
    #os.system('mkdir ' + localpath)
    ssh = paramiko.SSHClient() 
    #ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.get(remotepath, localpath)
    print("File Retrived from Location:",{remotepath}, "And Stored in Location:",{localpath})
    sftp.close()
    ssh.close() 


def SSH_put(server, username, password, localpath, remotepath):
    import os
    import paramiko
    #os.system('mkdir ' + localpath)
    ssh = paramiko.SSHClient() 
    #ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(localpath, remotepath)
    print("File Pushed from Location:",{localpath}, "And Stored in Location:",{remotepath})
    sftp.close()
    ssh.close()
    
    
remotepath = "*/TEST2.csv"
localpath = '*/TEST2.csv'
server = "10.10.1.100"
username = "ID\Vignesh"
password= "Welcome@2021"

#GET data
SSH_get(server, username, password, localpath, remotepath)

remotepath = "*/TEST2.csv"
localpath = '*/TEST2.csv'
server = "10.10.1.100"
username = "ID\Vignesh"
password= "Welcome@2021"

SSH_put(server, username, password, localpath, remotepath)