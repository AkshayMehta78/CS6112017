import re
file = open("email.txt", "r")
f1 = file.read()
k = re.findall(r'(\w(?:[-.+]?\w+)+\@(?:[a-zA-Z0-9](?:[-+]?\w+)*\.)+[a-zA-Z]{2,})', f1) 
for j in k:
    print(j)