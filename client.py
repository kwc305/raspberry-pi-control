import pxssh
import getpass

print "client side testing"
try:                                                            
    s = pxssh.pxssh()
    hostname = raw_input('client board number: ')
    client = raw_input('server board: ')
    username = "pi"
    #username = raw_input('username: ')
    password = "thugl1f3"
    size = raw_input('size of packet: ')
    command = "iperf -c 192.168.100."+client+ " -u -b 1000M -P 8 -f M -w 100M -n "+ size
    s.login ("192.168.100."+hostname, username, password)
    
    print "login successful"

    print command 

    s.sendline ('ls -l')
    s.prompt()
    print s.before
    


    s.sendline(command)
    s.prompt()
    print s.before
    s.logout()
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)