import pxssh
import getpass

print "server side iperf testing"
try:                                                            
    s = pxssh.pxssh()
    hostname = raw_input('server board number: ')
    username = raw_input('username: ')
    password = "thugl1f3"
    command = "iperf -s -u"
    s.login ("192.168.100."+hostname, username, password)

    s.sendline(command)
    s.prompt()
    print s.before
    s.logout()
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)