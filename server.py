
# Name     : Chirag Hemmanahalli Girish
# UTA ID   : 1001244131
# Course ID: CSE 5344


import socket # importing socket functionalities
from socket import *
import sys 
import thread #importing thread functionalities

def server(connectionSocket):
  try:
     message= connectionSocket.recv(1024)# http request recieved
     print "message is .."+ message # http request message printed
     print 'host name of the client: Localhost' # printing name of client
     print 'Socket family: AF_INET' # printing socket family
     print 'Socket type: SOCK_STREAM' #printing socket type
     print 'protocol : TCP'# printing type of protocol
     filename= message.split()[1] #extracting filename from the request message
     if filename[1:] != "favicon.ico": # avoiding exception caused due to icon when requsted through browser
       f=open(filename[1:])# opening the file
       outputdata= f.read()# reading the contents from the file
       connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n')# sending http response
       for i in range(0, len(outputdata)): #sending charter by charter to client
          connectionSocket.send(outputdata[i])

       connectionSocket.close()#closing socket connection
        
      

  except IOError:
     #Send response message for file not found
        print "something bad happened..."
        connectionSocket.send('404 Not Found')# printing file not found message
        connectionSocket.close()#closing socket connection
        

HOST = ''# host
PORT = 814 # specifying port
serverSocket = socket(AF_INET, SOCK_STREAM)#create an INET, STREAMing socket
serverSocket.bind((HOST, PORT))#binding socket to host
serverSocket.listen(10)#listening upto 10 request connection
print 'ready to serve...'
while 1:# while loop to accept connection request continuosly 
 #print 'ready to serve...'
 connectionSocket, addr = serverSocket.accept()#accepting connection
 print 'ready to serve...'
 thread.start_new_thread(server,(connectionSocket,))  #starting a new thread


if __name__== '__server__':
    server()

   
