# import stuff
import csv
import os

### TAGS ###
# All tags will be fed into the function getSongs, which can be called multiple times.
# If multiple arguments are given to getSongs, the intersect of those arguments will be returned.
# If getSongs is called multiple times, the union of those calls will be played.
# Make sure to list all sets in tags.
# Choose tags from following list (may not be complete):
# <insert list of tags from csv file>
set1 = ['popular', 'polished']
set2 = ['country']
tags = [set1, set2]

# define lists as empty
global playlist
playlist = []

# import taglist
with open('Tags.csv', 'rb') as csvfile:
	songlist = csv.reader(csvfile, delimiter=',', quotechar='|')
	songs = []
	for row in songlist:
		i = 0
		attrib = []
		while (i < len(row)):
			attrib.append(row[i])
			i += 1
		songs.append(attrib)

# change directories
os.chdir('../Music')

# Inputs complete list of songs (songs), the current playlist (playlist), and a list of tags to match (*args).
def getSongs(songs, playlist, *args):
	for row in songs:
		# Sees if this song is already on playlist.
		skip = 0
		if (len(playlist) > 0) & (len(row) > 0):
			for song in playlist:
				if song == row[0]:
					skip = 1
		# If the song isn't on the playlist already
		if skip == 0:
			# And it matches all the tags given.
			if set(args[0]).intersection(row) == set(args[0]):
				# Add to playlist
				playlist.append(row[0])
				print "appending",row[0]
	return playlist

# goes through tags, calls getSongs
for tagset in tags:
	playlist = getSongs(songs, playlist, tagset)


# go through playlist
s = 0
while (s < len(playlist)):
        print 'Playing %s' % playlist[s]
	command = 'mplayer %s' % playlist[s]
	os.system(command)
	s += 1 
 

