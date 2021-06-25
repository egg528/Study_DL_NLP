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
print("Okt", okt.morphs("아버지가방에들어가신다."))
print("Kkma", kkma.morphs("아버지가방에들어가신다."))
print("Hannanum", hannanum.morphs("아버지가방에들어가신다."))
print("Komoran", komoran.morphs("아버지가방에들어가신다."))
print("Twitter", twitter.morphs("아버지가방에들어가신다."))