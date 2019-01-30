#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


#All the print statements in this function were put in to test the code at strategic locations

def extract_names(filename):
  #print(filename)
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  #initialize your list variable
  names = []

  ####extract all text from file & print(optional)
  text0 = open(filename, "rU")
  text = text0.read()
  #print(text)

  ####find and extract the year and print
  match_year = re.search(r'Popularity\s*in\s*(\d\d\d\d)',text)
  if not match_year:
    #print year not found and then exit
    sys.stderr.write("Year not found!\n")
    sys.exit(1)

  #pick out the year and add it to your list
  year = str(match_year.group(1))
  names.append(year)
  print(year)

  ####extract names and reank no. and print
  #now time for the names and renk extract, using the findall and print
  tuple_list = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
  #print(tuple_list)

  #next is to put the names and rank into a dict. and print
  #this piece of code also checks if the name already exists in the dictionary
  name_and_rank = {}
  for rank, boyname, girlname in tuple_list:
    if boyname not in name_and_rank:
      name_and_rank[boyname] = rank
    if girlname not in name_and_rank:
      name_and_rank[girlname] = rank

  #print rank and names dict
  #print(name_and_rank)

  #now to get the dictionary sorted
  sorted_name_and_rank = {k: name_and_rank[k] for k in sorted(name_and_rank)}  

  #Put it all in one big list
  for name in sorted_name_and_rank:
    names.append(name + " " + sorted_name_and_rank[name])
 

  #return names & print(optional)
  #print(names)
  return names


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = [("C:\\Users\\Dell\\Documents\\data_tutorials\\babynames\\"+nm) for nm in os.listdir() if nm.endswith('.html')]
  #args = sys.argv[1:]
  #print (args)
  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
  for filename in args:
    names = extract_names(filename)

    #turn everything to text with new line seperating each one
    text = '\n'.join(names)
    #print(text)
    
    
    if not summary:
      outfile = open(filename + '.summary', 'w')
      outfile.write(text + '\n')
      outfile.close

    else:
      print (text)

#text = '\n'.join(mylist) + '\n'

  
  
if __name__ == '__main__':
  main()
