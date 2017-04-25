#encoding:utf-8
#!/usr/bin/env python2.7
#description:generating the weak password

keywords = ["@", "@123", "#", "#123", "!@#", "!", "$", "123", "?"]

usernames = open("username.txt", "r")
password = open("password_temp.txt", "a+")
temp = []
for username in usernames.readlines():
    username = username.strip('\n')
    for key in keywords:
        temp.append(username + key + '\n')
        temp.append(key + username + '\n')
password.writelines(temp)
password.close()
usernames.close()
