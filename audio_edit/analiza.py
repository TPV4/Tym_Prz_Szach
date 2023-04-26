# import numpy as np
import pydub as db
import pydub.playback as pl
# from dataclasses import dataclass
# import os

db.AudioSegment.converter = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
db.AudioSegment.ffmpeg = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
db.AudioSegment.ffprobe ="C:\\ffmpeg\\ffmpeg\\bin\\ffprobe.exe"

class Sciezka:

    def __init__(self, plik) -> None:
        self.plik: str
        self.rozsz=self.rozszezenie(plik)
        self.sciezka=db.AudioSegment.from_file(file=plik, format=self.rozsz)

    def rozszezenie(self, plik):
        k=len(plik)-1
        bat=""
        while(plik[k]!='.'):
            bat+=plik[k]
            k-=1
        tab=bat[::-1]
        return tab
    
    def dlugosc(self):
        return len(self.sciezka)

    def graj(self):
        pl.play(self.sciezka)

    def zapisz(self):
        pass



        

