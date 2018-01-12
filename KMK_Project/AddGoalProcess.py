from Users import Users

def registerNewUser(name, goal, duration):
    userdata = name + ',' + goal +',' + duration +'\n'
    user_file = open('file/addgoals.txt', 'a')
    user_file.write(userdata)

registerNewUser('kmk','Car','180 days')
