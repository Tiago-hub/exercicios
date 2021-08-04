file_names = ['foo.dat','bar.txt','foo.log']
file_owners = ['Me','Someone else','Me']

def group_by_owners(file_names,file_owners):
    try:
        if(len(file_names)!=len(file_owners)):
            raise Exception()
    except Exception:
        print('Error! File_names is not of the same size as file_owners')
        return False

    myDict = dict()
    for name,owner in zip(file_names,file_owners):
        if owner in myDict:
            myDict[owner].append(name)
        else:
            myDict[owner]=[name]
    return myDict

def get_files_owners(mypath):
    from os import listdir, path, stat
    from pwd import getpwuid
    dirfiles = listdir(mypath)
    files = []
    owners = []
    for file in dirfiles:
        if path.isfile(file): 
            files.append(file)
            owners.append(getpwuid(stat(file).st_uid).pw_name)
    return files,owners