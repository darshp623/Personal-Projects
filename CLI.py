"""
File: file_system.py
Author: Darsh Patel
Date: 12/1/2022
Lab Section: 35-DIS
Email:  dpatel37@umbc.edu
Description:  This program shows the layout of code in a Python file, and greets
the user with the name of the programmer
"""


def splitter(string):
    """
    Splits inputs
    :param string: the inputted string
    """
    slash_split = string.split("/")
    # splits every input with slashes in it
    return slash_split
    # returns the string


def locate(name, dictionary, path):
    """
    Recursively locates the path of a file in the system
    :param name: the inputted target file
    :param dictionary: the current place in the file_system
    :param path: the path of the dictionaries in currDict
    :return y: the boolean if x is true
    """
    y = False
    # setting a boolean, y, to False
    for key in dictionary.keys():
        # this for loop runs for each key in the dictionary currDict
        if dictionary[key] == "" and key != name:
            # this if only executes, if the key is not empty and the key does not equal name
            y = y
            # just to pass over the if
        elif key == name:
            # executes if the key equals the input for the target file
            print(path + "/" + name)
            # prints the path the file name was in, plus the target files name
            y = True
            # y = True if a path is found
        else:
            # executes only if the above 'if statement' does not work
            if key in dictionary.keys():
                # if the key is in the dictionary currDict, this if statement executes
                x = locate(name, dictionary[key], path + "/" + key)
                # finally locate recursively checks and gets the name of the file, the dictionary it is in
                # the path, and the key of said dictionary
                if x:
                    # this if executes, if x is true
                    y = True
                    # y now equals True
    return y
    # returns True, or y if a file is located


def touch(name, dictionary):
    """
    Makes a string of the inputted 'file' name
    :param name: the inputted target files name
    :param dictionary: the current place in the file_system
    """
    if name[1] not in dictionary.keys():
        # executes if the inputted string at index 1 is not in any keys in currDict
        dictionary[name] = str("")
        # sets the dictionary name to a string


def mkdir(name, dictionary):
    """
    Makes a dictionary of the inputted 'directory' name
    :param name: the inputted target files name
    :param dictionary: the current place in the file_system
    """
    if name[1] not in dictionary.keys():
        # executes if the inputted string at index 1 is not in any keys in currDict
        dictionary[name] = dict()
        # sets the dictionary name to an input


def pwd(path):
    """
    Prints the current path at wherever someone is in a dictionary
    :param path: the path of the dictionaries in currDict
    """
    if path == "":
        # executes only if the path is empty
        print("/")
        # prints a /, as the path would only be empty in the root directory
    else:
        # executes if the path is not empty
        print(path + "/")
        # prints the current path, plus a / to mimic a real system


def commands():
    """
    Helper function with cd, ls, and rm, as well as function calls.
    """

    home = dict()
    currDict = home
    path = ""
    command = ""
    # setting dictionaries and variables

    while command != "exit":
        # the code below only runs while the command does not equal exit
        command = input("[cmsc201 proj3]$ ")
        # makes a variable equal to the input in the file system
        com = command.split(" ")
        # splits the input into a list by the spaces
        if com[0] == "cd":
            # executes only if the input = cd at index 0 in the split list of the variable com
            if com[1] == "/":
                # executes only if the input = / at index 1 in the split list of the variable com
                currDict = home
                # sets currDict back to home, as this bring the user back to the root directory
                path = ""
                # sets the path to empty, as it brings the user back to the root directory
            elif com[1] == " ":
                # this elif executes only if the input = nothing at index 1 in the split list of the variable com
                currDict = currDict
                # keeps current dictionary the same
            elif com[1] == "..":
                # this elif executes only if the input = ". ." at index 1 in the split list of the variable com
                if path != "":
                    # executes only if the path equals nothing
                    path2 = splitter(path)
                    # sets a variable, path2, to the split of the current path, by the slashes, as done in the function
                    path = ""
                    # path is set to nothing
                    currDict = home
                    # the current dictionary is set to home
                    for i in range(len(path2) - 1):
                        # this for loop runs for the length of the list path2 - 1
                        if path2[i] != "":
                            # this if only executes for when each item in the list path2 is not empty
                            currDict = currDict[path2[i]]
                            # this sets the current dictionary, currDict to the previous variable,
                            # path2 at each iteration
                            path = path + path2[i]
                            # path now is set to equal the previous path, plus the index at path2
                    if path != "":
                        # this if only executes, if the path is not empty
                        path = "/" + path
                        # path is set to a / + the current path
            else:
                # this else executes only when none of the other cases are valid
                if com[1][0] != "/":
                    # this if executes, if the item at index 0 in the 2nd item in the list com does not
                    # equal a slash
                    com2 = splitter(com[1])
                    # sets a variable, com2, to the split of the inputted directory, by the slashes,
                    # as done in the function above
                    tempDict = currDict
                    # sets a temporary dictionary to the current dictionary
                    tempPath = path
                    # sets a temporary path to the current path
                    changed = True
                    # setting a variable, changed, to a boolean value that is True

                    for i in range(len(com2)):
                        # this for loop runs for the length of the list com2
                        if com2[i] != "":
                            # this if statement only executes if the iteration in com2 is not empty
                            if com2[i] in currDict.keys():
                                # this if statement only executes if the item in the list com2 is in
                                # the dictionaries keys
                                path = path + "/" + com2[i]
                                # path is set to the current path, plus a slash, plus each item in the list com2
                                currDict = currDict[com2[i]]
                            else:
                                # this else only executes if the item in the list com2 is not in
                                # the dictionaries keys
                                changed = False
                                # sets the boolean changed to False
                    if not changed:
                        # this if only executes, if changed = False
                        path = tempPath
                        # sets the current path to a temporary path
                        currDict = tempDict
                        # sets the current dictionary to a temporary dictionary
                        print("No such directory")
                else:
                    # this if executes, if the item at index 0 in the 2nd item in the list com does
                    # equal a slash
                    com2 = splitter(com[1])
                    # sets a variable, com2, to the split of the inputted directory, by the slashes,
                    # as done in the function above
                    tempDict = currDict
                    # sets a temporary dictionary to the current dictionary
                    tempPath = path
                    # sets a temporary path to the current path
                    changed = True
                    # sets a boolean, changed, to True
                    currDict = home
                    # sets the current dictionary = to home
                    path = ""
                    # sets path to empty again
                    for i in range(len(com2)):
                        # this for loop runs for the length of the list com2
                        if com2[i] != "":
                            # this if only executes, if the item in the list com2 does not = nothing
                            if com2[i] in currDict.keys():
                                # if the item in the list com2 is in the current dictionaries keys
                                path = path + "/" + com2[i]
                                # sets path = to the current path, plus a slash, plus the item in the list com2
                                currDict = currDict[com2[i]]
                                # sets the current dictionary to the item in the list com2 in the current dictionary
                            else:
                                # this else executes if the item in the list com2 is not
                                # in the current dictionaries keys
                                changed = False
                                # the boolean changed is set to False

                    if not changed:
                        # the if statement executes, if changed does = False
                        path = tempPath
                        # sets the current path to the temporary path
                        currDict = tempDict
                        # sets the current dictionary back to the temporary dictionary
                        print("No such directory")
                        # prints that there is no directory to go to

        elif com[0] == "ls" and len(com) != 1 and com[1][0] != "/":
            # this elif only executes if the index 0 in the list com = ls, and the length of the list com does not
            # equal 1, AND the item at index 0 in the 2nd item in the list, com, does not = a slash
            com2 = splitter(com[1])
            # sets a variable, com2, to the split of the inputted directory, by the slashes,
            # as done in the function above
            tempDict = currDict
            # sets the temporary dictionary back to the current dictionary
            tempPath = path
            # sets the temporary path back to the current path
            changed = True
            # sets a boolean changed to True
            for i in range(len(com2)):
                # this for loop runs for the length of the list com2
                if com2[i] in currDict.keys():
                    # if the item in the list com2 is in the current dictionaries keys
                    path = path + "/" + com2[i]
                    # sets path = to the current path, plus a slash, plus the item in the list com2
                    currDict = currDict[com2[i]]
                    # sets the current dictionary to the item in the list com2 in the current dictionary
                else:
                    # this else executes if the item in the list com2 is not
                    # in the current dictionaries keys
                    changed = False
                    # sets the boolean changed to False
            if changed:
                # this if only executes, if the boolean changed = True
                if path == "":
                    # this if statement only executes if the path is empty
                    print("Contents for /")
                    # clearly shows what the path is
                    for keys in currDict.keys():
                        # this for loop runs for each key in the current dictionary
                        print("   " + keys)
                        # prints the keys tabbed to match the sample
                    print("   ...")
                    # prints ... tabbed, just to match the sample
                elif path != "":
                    # if the path does not equal empty, this elif executes
                    print("Contents for " + path + "/")
                    # clearly shows what the path is
                    for keys in currDict.keys():
                        # this for loop runs for each key in the current dictionary
                        print("   " + keys)
                        # prints the keys tabbed to match the sample
                    print("   ...")
                    # prints ... just to match sample

            currDict = tempDict
            # sets the current dictionary back to the temporary dictionary
            path = tempPath
            # sets the current path back to the temporary path

        elif com[0] == "ls" and len(com) != 1 and com[1][0] == "/":
            # this elif only executes if the index 0 in the list com = ls, and the length of the list com does not
            # equal 1, AND the item at index 0 in the 2nd item in the list, com, does = a slash
            com2 = splitter(com[1])
            # sets a variable, com2, to the split of the inputted directory, by the slashes,
            # as done in the function above
            tempDict = currDict
            # sets a temporary dictionary to the current dictionary
            tempPath = path
            # sets a temporary path = to the current path
            changed = True
            # sets a boolean, changed, to True
            currDict = home
            # sets the current dictionary to home
            path = ""
            # sets path to empty

            for i in range(len(com2)):
                # this for loop runs for the length of the list com2
                if com2[i] != "":
                    # this if only executes, if each item in the list com2 does not = nothing
                    if com2[i] in currDict.keys():
                        # this if only executes, if each item in the list com2 is in the keys of the current dictionary
                        path = path + "/" + com2[i]
                        # sets path to the current path, plus a slash, plus each item in the list com2
                        currDict = currDict[com2[i]]
                        # sets the current dictionary to each item in the list com2 in the current dictionary
                    else:
                        # this if only executes, if each item in the list com2 is not
                        # in the keys of the current dictionary
                        changed = False
                        # sets the boolean changed to False

            if changed:
                # this if only executes, if the boolean changed = True
                if path == "":
                    # this if statement only executes if the path is empty
                    print("Contents for /")
                    # clearly shows what the path is
                    for keys in currDict.keys():
                        # this for loop runs for each key in the current dictionary
                        print("   " + keys)
                        # prints the keys tabbed to match the sample
                    print("   ...")
                    # prints ... tabbed, just to match the sample
                elif path != "":
                    # if the path does not equal empty, this elif executes
                    print("Contents for " + path + "/")
                    # clearly shows what the path is
                    for keys in currDict.keys():
                        # this for loop runs for each key in the current dictionary
                        print("   " + keys)
                        # prints the keys tabbed to match the sample
                    print("   ...")
                    # prints ... just to match sample

            currDict = tempDict
            # sets the current dictionary = to the temporary dictionary
            path = tempPath
            # sets the current path = to the temporary path

        elif com[0] == "ls" and len(com) == 1:
            # this elif executes if the item at index 0 in the list com does not = ls, and if the length
            # of the list com is 1
            if path == "":
                # this if statement only executes if the path is empty
                print("Contents for /")
                # clearly shows what the path is
                for keys in currDict.keys():
                    # this for loop runs for each key in the current dictionary
                    print("   " + keys)
                    # prints the keys tabbed to match the sample
                print("   ...")
                # prints ... tabbed, just to match the sample
            elif path != "":
                # if the path does not equal empty, this elif executes
                print("Contents for " + path + "/")
                # clearly shows what the path is
                for keys in currDict.keys():
                    # this for loop runs for each key in the current dictionary
                    print("   " + keys)
                    # prints the keys tabbed to match the sample
                print("   ...")
                # prints ... just to match sample

        elif com[0] == "rm":
            # if the inputted command at index 0 = rm, this elif is executed
            if com[1] in currDict.keys():
                # executes if the inputted file is in the dictionary
                tempDict = dict()
                # setting a temporary dictionary
                for key in currDict.keys():
                    # this for loop runs for the keys in the dictionary
                    for value in currDict.values():
                        # this for loop runs for the values in the dictionary
                        if key != com[1] and currDict[key] == value:
                            # executes if the key does not equal the inputted file and the dictionary matches the value
                            tempDict[key] = value
                            # the temporary dictionary key is set to the value of currDict
                currDict = tempDict
                # sets currDict equal to the temporary dictionary created before, outside the for loop
            elif com[1] not in currDict.keys():
                # this elif executes if the inputted file is not in the file system
                print(com[1], "not found")
                # prints the input, plus not found

        elif com[0] == "mkdir" and "/" not in com[1]:
            # if the inputted command at index 0 = mkdir, and there is no / in the input, this elif is executed
            mkdir(com[1], currDict)
            # function call

        elif com[0] == "touch":
            # if the inputted command at index 0 = touch, this elif is executed
            touch(com[1], currDict)
            # function call

        elif com[0] == "locate":
            # if the inputted command at index 0 = locate, this elif is executed
            print("A file with that name was found at the following paths: ")
            x = locate(com[1], currDict, path)
            # setting x to a function call
            if not x:
                # this if only executes, if x does not return anything and is False
                print("No such files were found.")
                # prints if no file is found

        elif com[0] == "pwd":
            # if the inputted command at index 0= pwd, this elif is executed
            pwd(path)
            # function call

if __name__ == '__main__':
    commands()
    # singular function call
