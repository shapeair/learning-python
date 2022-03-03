#Longest and useless way to say hello world.


import time
import random 
#always write comments to help your future self and others understand what you are doing


start = time.time()
message = "hellow world"
#a array of all the alphabets 
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

random_message=""

for word in message:
    while True:
        #we loop through all the words in the message and select a random word from the character array if the word mathes we add it to the new string 
        #in short this is the most useeless way o print a message
        random_number = random.randint(0,alphabets.__len__()-1)
        if word == alphabets[random_number]:
            random_message += word
            break
        else:
            continue

end= time.time()

print (random_message)
print ("I took around ", end-start)
