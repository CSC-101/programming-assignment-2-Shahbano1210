import data

# Write your functions for each part in the space below.

# Part 1

def create_rectangle(p1:data.Point,p2:data.Point)->data.Rectangle: # takes in two points and returns a rectangle
    rectangle = data.Rectangle((0.0,0.0),(0.0,0.0))
    # horizontal
    if p1.x >= p2.x:
        leftMost = p2.x
        rightMost = p1.x
    else:
        leftMost = p1.x
        rightMost = p2.x

  # vertical
    if p1.y >= p2.y:
        highest = p1.y
        lowest = p2.y
    else:
        highest = p2.y
        lowest = p1.y

  # putting it together
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

def song_shorter_than(songs:list[data.Song],limit:data.Duration)->list[data.Song]: # takes in a list of type Song and a
    # limit of type Duration and returns a list of type song of all the songs under the limit
    Limit = limit.minutes + limit.seconds / 60
    allSongs =[]
    for i in songs:
        song = i.duration.minutes + i.duration.seconds / 60
        if song <= Limit:
            allSongs.append(songs)
    return allSongs

# Part 4

def running_time(songs:list[data.Song],playlist:list[int])->data.Duration: # takes in a list of type Song and a list of
    # type int & returns a type Duration of the total time of all the songs
    totalTime = data.Duration(0,0)
    songsIdx = 0
    for i in playlist:
        if 0 <= i < len(songs):
            songsIdx = i
            totalTime.minutes = songs[songsIdx].duration.minutes + totalTime.minutes
            totalTime.seconds = songs[songsIdx].duration.seconds + totalTime.seconds
    while totalTime.seconds >= 60:
        totalTime.seconds = totalTime.seconds - 60
        totalTime.minutes = totalTime.minutes + 1
    return totalTime

# Part 5

# def validate_route (list1:list[list[str]],list2:list[str])->bool:

    # if valid or list1 == [] or len(list1)==1:
      #  return True
   #  if invalid:
      #  return False



# Part 6
