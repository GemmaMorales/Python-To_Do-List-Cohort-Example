import random

descrip =["A spooky ","A terrifying ","A nice ","A misterious ","An evil "]
who =["sorcerer ","extraterrestrial ","man ","monster ", "unicorn "]
accion=["burned ","decorated ","pulverized ","painted ", "disintegrated ", "disappeared "]
what=["my car ","my computer ","my sandwidch ","my phone ", "my homework "]
where=["on the street ","in the lake ","in front of the office ","in my house "]
when=["yesterday. ","this morning. ","last night. ","just now. "]

def excuse_generator():

 desRand = random.randrange(len(descrip))   
 whoRand = random.randrange(len(who))  
 accRand = random.randrange(len(accion)) 
 whatRand = random.randrange(len(what)) 
 wherRand = random.randrange(len(where))  
 wheRand = random.randrange(len(when)) 

 excuse = (descrip[desRand]+""+who[whoRand]+""+accion[accRand]+""+what[whatRand]+""+where[wherRand]+""+when[wheRand])

 print(excuse)

excuse_generator()
