#encoding:utf-8
#!/usr/bin/env python2.7
#description:get chinses first character

usernames = open("temp1.txt", 'r')
short_name = open("short_name", 'a+')
"""
all = usernames.readlines()
test = all[0].strip('\n')
test = test.split('-')
print test
print len(test)
print type(test[0])
print test[0][0]
print type(test[0][0])
print test[0][0]+test[1][0]
"""
all = []
for username in usernames.readlines():
    username = username.strip('\n')
    split_username = username.split('-')
    short_n = ""
    for key in split_username:
        short_n += key[0]
    all.append(short_n + '\n')
short_name.writelines(all)
