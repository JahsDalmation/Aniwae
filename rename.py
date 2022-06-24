import subprocess

Anime = input('Anime > ')
File_format = input('File Format, upto first episode digit > ')
Episodes = int(input("Episodes (no leading 0's > "))

Ep = 1

while Ep <= Episodes:
    if Ep < 10:
        subprocess.run(['mv ~/Anime/%s/%s00%s.mp4 ~/Anime/%s/%s.mp4' % (Anime, File_format, Ep, Anime, Ep)], shell=True)
    if Ep < 100 and Ep >= 10:
        subprocess.run(['mv ~/Anime/%s/%s0%s.mp4 ~/Anime/%s/%s.mp4' % (Anime, File_format, Ep, Anime, Ep)], shell=True)
    if Ep >= 100:
        subprocess.run(['mv ~/Anime/%s/%s%s.mp4 ~/Anime/%s/%s.mp4' % (Anime, File_format, Ep, Anime, Ep)], shell=True)
    Ep = Ep + 1

