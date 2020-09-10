import getpass
import telnetlib

user = input('Enter your telnet username: ')
password = getpass.getpass()

f = open('switches')

for ip in f:
    print('Configuring switch ' + (ip))
    HOST = ip
    tn = telnetlib.Telnet(HOST)
 
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
    	tn.read_until(b'Password: ')
    	tn.write(password.encode('ascii') + b'\n')
    
    tn.write(b'enable\n')
    tn.write(b'cisco\n')
    
    tn.write(b'configure terminal\n')
    
    for n in range (2,11):
    	tn.write(b'vlan ' + str(n).encode('ascii') + b'\n')
    	tn.write(b'name Python_VLAN_' + str(n).encode('ascii') + b'\n')
    
    tn.write(b'end\n')
    tn.write(b'wr\n')
    tn.write(b'exit\n')
    
    print(tn.read_all().decode('ascii'))