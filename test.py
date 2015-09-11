
import  threading, time 
import sys
from fabric.api import *
import re

print ("do ssh stuff")

stop = [2]
stop[0] = '0'

class  config(threading.Thread):    
    def  __init__( self , cond, name):    
        super(config,  self ).__init__()    
        self.cond = cond    
        self.name = name    
        
    def  run( self ):    
                
            
        for a in range (0,10):           
            print("router config ing b")  
        self.cond.acquire()  #b   
        self.cond.notify()  
        self.cond.wait() 
        
        print "try to get result 1 f "
        
        self.cond.notify()  
        stop[0] = '1'
        
        self.cond.release() 

                            #g    
          
            
class  iperfc(threading.Thread):    
    def  __init__( self , cond, name):    
        super(iperfc,  self ).__init__()    
        self.cond = cond    
        self.name = name    
    def  run( self ):   
        
        self.cond.acquire()  
        print "start iperf connection"

        for a in range (0,20):
            print ("do iperf connection") 
         
        self.cond.wait()

        print("done iperf d")  
        
        self.cond.notify()  
        self.cond.release()     
          
            

class iperfs(threading.Thread):
    def __init__(self, cond, name):
        super(iperfs, self).__init__()
        self.cond = cond
        self.name = name
    def run(self):
        while (stop[0] == '0'):
            print("iperf -s -u")
        


cond = threading.Condition()    
iperfc = iperfc(cond,  'iperfc' )    
config = config(cond,  'hider' )  
iperfs = iperfs(cond,  'iperfs')  
iperfs.start()
iperfc.start()    
config.start()  
