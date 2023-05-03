import json

# user_data={}
Songs_List = []
f = open("Allusers_playlist.txt", "a")  # Opens Allusers_playlist.txt if exists else it creates Allusers_playlist
try:
    with open('Allusers_playlist.txt') as f:
        lines = f.read()
    AllPlaylist = json.loads(lines)  # Reads the data in the file
except:
    AllPlaylist = {}  # Initialises the data when file is empty(For the first time,the file will be empty)


def User(username):
    try:
        Songs_List = AllPlaylist[username]["Playlist"]  # Reads the songs stored for the current user
    except:
        Songs_List = []  # Initializes the song list to empty if its a new user
    if len(Songs_List) == 0:

            Initial_capacity = int(
            input("Enter Initial memory capacity of " + username + " user "))  # Executes only for new user

    else:
        print("Initial capacity of " + username + " user is ", AllPlaylist[username]["Index"])
        Initial_capacity = AllPlaylist[username]["Index"]  # stores the memory capacity of the new user

    while True:
        songname = str(input("Enter Song you are listening (Type 'exit' to see your recent playlist) "))
        if songname == "exit":
            break  # Breaks when user enters "eit"
        if len(Songs_List) < Initial_capacity:
            Songs_List.append(
                songname)  # Appends the current playing song to list if len(list)is less than Memory capacity of user
        else:
            Songs_List.pop(0)  # Removes least recently played song
            Songs_List.append(songname)
        AllPlaylist[username] = {}
        AllPlaylist[username]["Playlist"] = Songs_List  # Stores the Recent Playlist
        AllPlaylist[username]["Index"] = Initial_capacity

    return AllPlaylist


username = input("Enter Username ")
Output = User(username)  # Invoking of Function

print("Recent Playlist of " + username + " is", Output[username]['Playlist'])
with open('Allusers_playlist.txt', 'w') as m:
    m.write(json.dumps(Output))  # Store the data after execution into Allusers_playlist.txt
