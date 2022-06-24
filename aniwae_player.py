# Welcome to aniwae!
# V3
from sys import argv
import os
import subprocess

script, Name, Season, Episode = argv

def anime(name, Season, episode):
    play_anime = '~/Anime/%s/s%s/%s.mp4' % (name, Season, episode)
    subprocess.run(['mpv %s' % play_anime], shell=True)

Watch = True

while Watch == True:
    anime(Name, Season, Episode)
    Controls = True
    while Controls == True:
        control = input('\n[ 1] > +1 Ep\n[-1] > -1 Ep\n[ r] > Restart\n[ q] > Exit\n> ')
        if control != '1' and control != '-1' and control != 'q' and control != 'r':
            print('Please try again')
            continue
        if control == '1':
            Episode = int(Episode) + 1
            Controls = False
            continue
        if control == '-1':
            Episode = int(Episode) - 1
            Controls = False
            continue
        if control == 'r':
            Controls = False
        if control == 'q':
            print('')
            Controls = False
            Watch = False
            exit()
