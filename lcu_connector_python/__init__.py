import os

def connect(leagueExecutablePath = None):
# Get riot games folder location here somehow
    if(leagueExecutablePath == None):
        path = "C:/Riot Games/League of Legends/lockfile"
    else:
        path = leagueExecutablePath.split("/")
        for i, v in enumerate(path):
            if(v == "League of Legends"):
                path = path[:i + 1]
        path = "/".join(path)
        path += "/lockfile"
    if(checkLockFile(path)):
        return readLockFile(path)
    else:
        return "Ensure the client is running and that you supplied the correct path"

def checkLockFile(path): 
    return os.path.exists(path)

def readLockFile(path):
    f = open(path, 'r')
    data = f.read()
    data = data.split(":")
    # data[0] == "LeagueClient"
    # data[1] == idk rn
    # data[2] == port number
    # data[3] == auth token
    # data[4] == connecton method
    toreturn = {
        "port": data[2],
        "url": "127.0.0.1:" + data[2],
        "authorization": data[3],
        "connection_method": data[4]
    }
    return toreturn
