# Welcome to aniwae!
# V3
# What to watch?

import subprocess

local_anime = ['baki', 'jujutsu-kaisen', 'mushoku-tensei']

def anime_player(Name, Season, Episode):
    subprocess.run(['python ./aniwae_player.py %s %s %s' % (Name, Season, Episode)], shell=True)

def local_anime_titles():
    s = 0
    for i in local_anime:
        print('[%s] > %s' % (s, i))
        s = s + 1

def hello():
    print('Welcome to Aniwae!')

Hello = True

while Hello == True:
    source = input('[l]ocal\n[e]xternal\n[r]ename\n[q]uit\n> ') 

    if source != 'l' and source != 'e' and source != 'q' and source != 'r':
        print('Try again.\n') 

    if source == 'l':
        print('')
        local_anime_titles()
        X = input('[ ]> ')
        Name = local_anime[int(X)]
        subprocess.run(['ls -1 ~/Anime/%s/' % Name], shell=True)
        Season = int(input("Season Number > "))
        subprocess.run(['ls -1 ~/Anime/%s/s%s/' % (Name, Season)], shell=True)
        Ep = input('\n[Ep] > ')        
        anime_player(Name, Season, int(Ep))

    if source == 'r':
        print('\nPlease choose title:')
        local_anime_titles()
        Y = input('[ ]> ')
        Anime = local_anime[int(Y)]
        subprocess.run(['ls -1 ~/Anime/%s/' % Anime], shell=True)
        Season = int(input("Season Number > "))
        subprocess.run(['ls -1 ~/Anime/%s/s%s/' % (Anime, Season)], shell=True)
        File_format = input('File Format, upto first episode digit > ')
        Episodes = int(input("Episodes (no leading 0's) > "))
        subprocess.run(['python ./rename.py %s %s %s %s' % (Anime, Season, File_format, Episodes)], shell=True)

    if source == 'q':
        Hello = False


#while Hello == True:
#local_anime_titles()
    
    
