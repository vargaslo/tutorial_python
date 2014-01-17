import os
import sys
import re
import fnmatch


def sorted_nicely(l):
    """ Sort the given iterable in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


def matchingfiles(dir, string):
  # Get all files in a given directory
  where = dir
  filelist = os.walk(where, followlinks=True)

  # Print a series of dashes to fit the terminal size
  rows, columns = os.popen('stty size', 'r').read().split()
  line = '-' * int(columns)
  print line

  # Loop over files to see if they match the string
  matchstring = string
  print 'Recursive list of files in %s that contain "%s":' % (dir, string)
  for root, dirnames, filenames in filelist:
    matchedfiles = fnmatch.filter(filenames, matchstring)
    matchedfiles = sorted_nicely(matchedfiles)

    # If files match the string, output filenames to stdout
    if len(matchedfiles) > 0:
      print '\n%s/' % (root)
      for filename in matchedfiles:
        print filename

  print line
  print 'Done!\n'


matchingfiles('/ws/git/', '*py')
