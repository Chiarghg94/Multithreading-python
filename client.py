# Name     : Chirag Hemmanahalli Girish
# UTA ID   : 1001244131
# Course ID: CSE 5344
import socket
from socket import *
import sys 
import thread
import time

def clientexmp():
    
    HOST = "localhost" #host
    PORT = 814 #specifying port
    serverSocket = socket(AF_INET, SOCK_STREAM)#create an INET, STREAMing socket
    serverSocket.connect((HOST, PORT))#connecting socket to host

    result=raw_input('if you want to end the connection press N,if you want to continue press any other key: ')#acceting user input
    if result!= 'N':# checking condition
     filename= raw_input("enter the filename: ") #accepting filename
     serverSocket.send('GET /'+filename+' HTTP/1.1')# sending filename to server
     t0= time.time()#clock begings
     data=serverSocket.recv(1024)#http response message recieved
     t1= time.time()#clock stops
     print 'RRT' #printing RTT
     print float(t1-t0)#RTT
     print 'host name of the server: Localhost'# printing name of server
     print 'Socket family: AF_INET'#printing socket family
     print 'socket type: SOCK_STREAM'#printing socket type
     print 'http response message is below'#HTTP response
     print data #HTTP response
     xyz=serverSocket.recv(1024)# recieving file contents
     print 'data recieved' # printing message
     print xyz # displaying data recieved
     print '**************' # request accomplished
     clientexmp()# calling function to accept user input
    else:
     serverSocket.close()#serverSocket.close()


if __name__== '__main__':
    clientexmp()
