# script rápido pra baixar videos do youtube.
from pytube import YouTube

link = input('Qual o link para o video? ')

yt = YouTube(link)
print(yt.title)
yt = yt.streams.get_highest_resolution()
try:
    yt.download()
except: 
    print('Alguma coisa deu errada no download... Checa a url ou ')
