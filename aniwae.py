# Welcome to aniwae!
# V3
# What to watch?

import subprocess

local_anime = ['baki-2018', 'jujutsu-kaisen', 'mushoku-tensei']

def anime_player(Name, Episode):
    subprocess.run(['python ./aniwae_player.py %s %s' % (Name, Episode)], shell=True)

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
        Ep = input('\n[Ep] > ')        
        anime_player(Name, int(Ep))
    if source == 'r':
        subprocess.run(['python ./rename.py'], shell=True)
    if source == 'q':
        Hello = False


#while Hello == True:
#local_anime_titles()
    
    
