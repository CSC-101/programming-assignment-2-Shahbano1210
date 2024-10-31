import data

# Write your functions for each part in the space below.

# Part 1

def horizontal(p1:data.Point,p2:data.Point)->None:
    if p1.x >= p2.x:
        leftMost = p2.x
        rightMost = p1.x
    else:
        leftMost = p1.x
        rightMost = p2.x

def vertical(p1:data.Point,p2:data.Point)->None:
    if p1.y >= p2.y:
        highest = p1.y
        lowest = p2.y
    else:
        highest = p2.x
        lowest = p1.x

def create_rectangle(p1:data.Point,p2:data.Point)->data.Rectangle: # takes in two points and returns a rectangle
    rectangle = data.Rectangle((0.0,0.0),(0.0,0.0))
    leftMost = data.Point.x(0.0)
    rightMost = data.Point.x(0.0)
    highest = data.Point.y(0.0)
    lowest = data.Point.y(0.0)
    horizontal(p1,p2)
    vertical(p1,p2)
    top_left = data.Point(leftMost,highest)
    bottom_right = data.Point(rightMost,lowest)
    rectangle = data.Rectangle(top_left, bottom_right)
    return rectangle


# Part 2

def shorter_duration_than(song1:data.Duration,song2:data.Duration)->bool: # takes in two songs of type Duration and
    # returns a bool comparing the duration of both songs
    duration1 = song1.minutes + song1.seconds / 10
    duration2 = song2.minutes + song2.seconds / 10
    if duration1 < duration2:
        return True
    else:
        return False
# Part 3

def song_shorter_than(list:list[data.Song],limit:data.Duration)->list[data.Song]: # takes in a list of type Song and a
    # limit of type Duration and returns a list of type song of all the songs under the limit
    limit = limit.minutes + limit.seconds / 10
    allSongs =[]
    for i in list:
        song = i.duration.minutes + i.duration.seconds / 10
        if song <= limit:
            allSongs.append(i)
    return allSongs

# Part 4

def running_time(songs:list[data.Song],playlist:list[int])->data.Duration: # takes in a list of type Song and a list of
    # type int & returns a type Duration of the total time of all the songs
    totalTime = data.Duration(0,0)
    songsIdx = 0
    songDurations = []
    dur = 0
    for i in range(len(playlist)):
        if playlist[i] >= 0 and playlist[i] < len(songs):
            playlist[i] = songsIdx
            totalTime.minutes = songs[songsIdx].minutes
            totalTime.seconds = songs[songsIdx].seconds
            while totalTime.seconds >= 60:
                totalTime.seconds = totalTime.seconds - 60
                totalTime.minute = totalTime.minute + 1
    return totalTime

# Part 5

# def validate_route (list1:list[list[str]],list2:list[str])->bool:

    # if valid or list1 == [] or len(list1)==1:
      #  return True
   #  if invalid:
      #  return False



# Part 6
