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
sports_directory["soccer"] = ["Andres", "Ronaldo", "Rooney"]
z[0]["y"] = 30

#2. Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for i in some_list:
        for k,v in i.items():
            return k, "-", v

#3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):

#4. Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    
