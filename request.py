import requests
import json

url=requests.get('https://api.merakilearn.org/courses')
# print(type(url))
a=json.loads(url.text)
# print(a)
with open("file.json","w") as f:
    json.dump(a,f,indent=4)
i=0
while i<len(a):
    # print(a[i])
    print(i+1,a[i]["name"],a[i]["id"])
    i+=19
print(" ")    
user=int(input("select which course you want learn  :"))
print(user,a[user-1]["name"])
b=a[user-1]["id"]

url1=requests.get('https://api.merakilearn.org/courses/'+str(b)+"/exercises")
son=json.loads(url1.text)
with open("parent.json","w") as f2:
    json.dump(son,f2,indent=6)
print(a[user-1]['name'],"-",a[user-1]["id"])
i = 0
while i < len(son["course"]["exercises"]):
    print((i+1),".",son["course"]["exercises"][i]["name"])
    print(son["course"]["exercises"][i]["slug"])
    i+=1
topic=int(input("enter the topic"))
topic=topic-1
i=0
while i<len(son["course"]["exercises"][topic]["content"]):
    print(son["course"]["exercises"][topic]["content"][i]["value"])
    print()
    i=i+1
while topic <= len(son["course"]["exercises"]):
    next_previuos = input("previous or next(p&n):")
    if  next_previuos == "p": 
        topic-=1
        if next_previuos == "p" and topic >=1:
            print(son["course"]["exercises"][topic]["name"],"\n")
            i = 0 
            while i < len(son["course"]["exercises"][topic]["content"]):
                print(son["course"]["exercises"][topic]["content"][i]["value"])
                i+=1
                
        else :
            i = 0
            while i < len(son):
                print(str(i+1),son["course"]["exercises"][i]["name"])
                i+=1
    elif  next_previuos == "n":
        topic+=1
        if next_previuos == "n" and topic < len(son["course"]["exercises"]):
                print(son["course"]["exercises"][topic]["name"],"\n")
                i = 0 
                while i < len(son["course"]["exercises"][topic]["content"]):
                    print(son["course"]["exercises"][topic]["content"][i]["value"])
                    i+=1
        if topic+1 == len(son["course"]["exercises"]):
            print("topic is completed.")
            break

    elif next_previuos=="stop":
        break    
    else:
        print("wrong user_input ")
        break


