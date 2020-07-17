#dictionary
dict = {"name": "harshit", "education": "B.Tech" ,"steam": "IT"}
#print dictionary
print(dict)
#print the keys of dictionary
print(dict.keys())
#print the key,values of dictionary
print(dict.items())

#print key for specified value
for key,value in dict.items():
    if value=="B.Tech":
        print(key)
#print the associated value for key 
print(dict.get("name"))

#adding key and value in dictionary
dict['class']="8th"
print(dict)

#define new dictionary
dict1 ={"name":"kapil", "colege": "JECRC"}
#An empty dictionary
dict2 ={}

#concating two dictionary in new empty dictionary
for d in (dict,dict1):
    dict2.update(d)
print(dict2)

#if key is present in dictionary then printing it's present
for key in dict:
    if key == "name1":
        print("it;s already present")
#using funtion for checking key is present in the dictionary or not 
def key_present(a):
    if a in dict :
        print("it's already present")
    else:
        print("it's not present" )
#fucntion calling
key_present("name")
#printing keys with there values
for dict_keys, dict_values in dict.items():
    print(dict_keys ,"->", dict_values )