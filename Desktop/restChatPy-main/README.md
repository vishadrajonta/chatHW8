# restChatCpp
A REST based web chat program using C++
 - https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
 - https://pypi.org/project/Flask-Cors/

## Prequisites
 - Apache2 muct be installed
 - Ports 5000-5010 must be open on the VM firewall

## Setup pip3, Flask and FLASK-CORS
 - ```sudo apt install python3-pip```
 - ```sudo apt install python3-flask```
 - ```pip3 install -U flask-cors```

## Edit Javascript IP address to your VM address
 - Edit ```restChat.js``` so that ```baseUrl``` is your VM's IP address
 
## Setup app (from command line)
 - ```sudo mkdir /var/www/html/restChatPy```
 - ```sudo chown ubuntu /var/www/html/restChatPy```
 - ```make```
 - ```./start.sh```

Then web to the http://ip:port
