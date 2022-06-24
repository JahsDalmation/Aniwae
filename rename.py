from sys import argv
import subprocess

script, Anime, Season, File_format, Episodes = argv

#Anime = input('Anime > ')
#File_format = input('File Format, upto first episode digit > ')
#Episodes = int(input("Episodes (no leading 0's > "))

Ep = 1

while Ep <= int(Episodes):
    if Ep < 10:
        subprocess.run(['mv ~/Anime/%s/s%s/%s00%s.mp4 ~/Anime/%s/s%s/%s.mp4' % (Anime, Season, File_format, Ep, Anime, Season, Ep)], shell=True)
    if Ep < 100 and Ep >= 10:
        subprocess.run(['mv ~/Anime/%s/s%s/%s0%s.mp4 ~/Anime/%s/s%s/%s.mp4' % (Anime, Season, File_format, Ep, Anime, Season, Ep)], shell=True)
    if Ep >= 100:
        subprocess.run(['mv ~/Anime/%s/s%s/%s%s.mp4 ~/Anime/%s/s%s/%s.mp4' % (Anime, Season, File_format, Ep, Anime, Season, Ep)], shell=True)
    Ep = Ep + 1

