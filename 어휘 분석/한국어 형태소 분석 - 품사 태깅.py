from konlpy.tag import Okt
from konlpy.tag import Kkma
from konlpy.tag import Hannanum
from konlpy.tag import Komoran
from konlpy.tag import Twitter

okt = Okt()
kkma = Kkma()
hannanum = Hannanum()
komoran = Komoran()
twitter = Twitter()

print("--형태소 분석--")
print("Okt", okt.pos("아버지가 방에 들어가신다."))
print("Kkma", kkma.pos("아버지가 방에 들어가신다."))
print("Hannanum", hannanum.pos("아버지가 방에 들어가신다."))
print("Komoran", komoran.pos("아버지가 방에 들어가신다."))
print("Twitter", twitter.pos("아버지가 방에 들어가신다."))