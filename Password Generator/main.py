import random

# function to shuffle the characters
def shuffle(string):
    tempList = list(string);
    random.shuffle(tempList);
    return ''.join(tempList);


#Generating Password
password = '';
for i in range(5):
    password += chr(random.randint(65, 90));
    password += chr(random.randint(97, 122));


#Shuffeling Password
password += '#@';
password = shuffle(password);


# Output
print("Your password is: " +password);