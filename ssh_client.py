import paramiko

try:
    host = "127.0.0.1"
    user = "kali"
    passwd = "kali"
    
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    cliente.connect(host, username=user, password=passwd)
    
    stdin, stdout, stderr = cliente.exec_command("whoami")
    
    print(stdout.read().decode())
    
    error_output = stderr.read().decode()
    if error_output:
        print("Error:", error_output)

except Exception as error:
    print(error)

finally:
    cliente.close()
