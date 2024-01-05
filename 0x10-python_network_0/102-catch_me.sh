#!/bin/bash
#we will make a script shell to make a request to 0x0x0x0:500/catch_me  
#you got me responding a message useing curl 
#t makes a request that causes the server to respond with a specific message.
curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"

