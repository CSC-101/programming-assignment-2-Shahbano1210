import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        p1 = data.Point(2.0,5.0)
        p2 = data.Point(8.0,9.0)
        expected = data.Rectangle(data.Point(2.0,9.0),data.Point(8.0,5.0))
        result = hw2.create_rectangle(p1,p2)
        self.assertEqual(expected,result)

    def test_create_rectangle_2(self):
        p1 = data.Point(5.0,4.0)
        p2 = data.Point(8.0,9.0)
        expected = data.Rectangle(data.Point(5.0,9.0),data.Point(8.0,4.0))
        result = hw2.create_rectangle(p1,p2)
        self.assertEqual(expected,result)

    # Part 2

    def test_shorter_duration_than_1(self):
        song1 = data.Duration(5,4)
        song2 = data.Duration(3, 4)
        expected = False
        result = hw2.shorter_duration_than(song1,song2)
        self.assertEqual(expected,result)

    def test_shorter_duration_than_2(self):
        song1 = data.Duration(4,0)
        song2 = data.Duration(7, 54)
        expected = True
        result = hw2.shorter_duration_than(song1,song2)
        self.assertEqual(expected,result)

    # Part 3

    def test_song_shorter_than_1(self):
        songs = [
            data.Song("Tyler the Creator","St.Chroma",data.Duration(3,17)),
            data.Song("ZAYN","Stardust",data.Duration(3,52)),
            data.Song("Ariana Grande","ordinary things",data.Duration(2,48))
        ]
        limit = data.Duration(3,18)
        expected = [
            data.Song("Tyler the Creator","St.Chroma",data.Duration(3,17)),
            data.Song("Ariana Grande","ordinary things",data.Duration(2,48))
        ]
        result = hw2.song_shorter_than(songs,limit)
        self.assertEqual(len(result),len(expected))

    def test_song_shorter_than_2(self):
        songs = [
            data.Song("Tyler the Creator","St.Chroma",data.Duration(3,17)),
            data.Song("ZAYN","Stardust",data.Duration(3,52)),
            data.Song("Ariana Grande","ordinary things",data.Duration(2,48))
        ]
        limit = data.Duration(3,0)
        expected = [data.Song("Ariana Grande","ordinary things",data.Duration(2,48))]
        result = hw2.song_shorter_than(songs,limit)
        self.assertEqual(len(result),len(expected))

    # Part 4
    def test_running_time_1(self):
        songs = [
            data.Song("Tyler the Creator","St.Chroma",data.Duration(3,17)),
            data.Song("ZAYN","Stardust",data.Duration(3,52)),
            data.Song("Ariana Grande","ordinary things",data.Duration(2,48))
        ]
        #minutes = 3+2+3+3 = 11
        # seconds = 17+48+48+52 = 2 min + 45
        playlist = [5,-1,0,2,1,1]
        expected = data.Duration(13,49)
        result = hw2.running_time(songs,playlist)
        self.assertEqual(expected,result)

    def test_running_time_2(self):
        songs = [
            data.Song("Tyler the Creator","St.Chroma",data.Duration(3,17)),
            data.Song("ZAYN","Stardust",data.Duration(3,52)),
            data.Song("Ariana Grande","ordinary things",data.Duration(2,48))
        ]
        playlist = [0,2,1,1]
        expected = data.Duration(13,49)
        result = hw2.running_time(songs,playlist)
        self.assertEqual(expected,result)

    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
