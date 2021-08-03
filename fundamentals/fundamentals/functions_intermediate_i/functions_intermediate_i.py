#1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] = 30

#2. Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for i in range(0,len(some_list)):
        output = ""
        for k,v in some_list[i].items():
            output += f"{k} - {v}, "
        print(output)

#3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range(0,len(some_list)):
        for k,v in some_list[i].items():
            if k == key_name:
                print(v)

#4. Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for k,v in some_dict.items():
        print(f"{len(v)} {k.upper()}")
        for i in range(0,len(v)):
            print(v[i])