import csv
import numpy as np
import pandas as pd
from sklearn import preprocessing,cross_validation,metrics
from sklearn.linear_model import LogisticRegression
class HashMap:
	def __init__(self):
		self.size = 6
		self.map = [None] * self.size
		
	def _get_hash(self, key):
		hash = 0
		for char in str(key):
			hash += ord(char)
		return hash % self.size
		
	def add(self, key, value):
		key_hash = self._get_hash(key)
		key_value = [key, value]
		
		if self.map[key_hash] is None:
			self.map[key_hash] = list([key_value])
			return True
		else:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					pair[1] = value
					return True
			self.map[key_hash].append(key_value)
			return True
			
	def get(self, key):
		key_hash = self._get_hash(key)
		if self.map[key_hash] is not None:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		return None
			
	
				
h = HashMap()
h.add('slapped', 'true')
h.add('slap', 'true')
h.add('hate', 'true')
h.add('blood', 'true')
h.add('shoot', 'true')
h.add('kill', 'true')
h.add('killed', 'true')
h.add('killing', 'true')
h.add('dead', 'true')
h.add('death', 'true')
h.add('saala', 'true')
h.add('pussy', 'true')
h.add('bitch', 'true')
h.add('bastard', 'true')
h.add('shag', 'true')
h.add('faggot', 'true')
h.add('cock', 'true')
h.add('dipshit', 'true')
h.add('fuck', 'true')
h.add('chuda', 'true')
h.add('bsdk', 'true')
h.add('bhosadike', 'true')
h.add('gaand', 'true')
h.add('gand', 'true')
h.add('chutiya', 'true')
h.add('stupid', 'true')
h.add('asses', 'true')
h.add('asshole', 'true')
h.add('boob', 'true')
h.add('boobs', 'true')
h.add('cunt', 'true')
h.add('fuckk', 'true')
h.add('shit', 'true')
h.add('chutiye', 'true')
h.add('dog', 'true')
h.add('kutte', 'true')
h.add('kutta', 'true')
h.add('piss', 'true')
h.add('sex', 'true')
h.add('sexy', 'true')
h.add('nanga', 'true')
h.add('nangi', 'true')
h.add('bhenchod', 'true')
h.add('behnchodd', 'true')
h.add('behnnchod', 'true')
h.add('bhenchhod', 'true')
h.add('madarchhod', 'true')
h.add('madarchodd', 'true')
h.add('madarchod', 'true')
h.add('randi', 'true')
h.add('anarchist', 'true')
h.add('ape', 'true')
h.add('arse', 'true')
h.add('arselicker', 'true')
h.add('butthead', 'true')
h.add('doofus', 'true')
h.add('dickhead', 'true')
h.add('dick', 'true')
h.add('gangster', 'true')
h.add('terrorist', 'true')
h.add('motherfucker', 'true')
h.add('MILF', 'true')
h.add('milf', 'true')
h.add('freak', 'true')
h.add('pig', 'true')
h.add('retard', 'true')
h.add('son of a bitch', 'true')
h.add('swine', 'true')
h.add('idiot', 'true')
h.add('chut', 'true')
h.add('choot', 'true')
h.add('chutt', 'true')
h.add('slut','true')
h.add('rand','true')
h.add('chudai','true')
h.add('lund','true')
h.add('chudogi','true')
h.add('chudoge','true')
h.add('chodenge','true')
h.add('phuddi','true')
h.add('bekar','true')
h.add('phategi','true')
h.add('bc','true')
h.add('bsdk','true')
h.add('hoes','true')
h.add('randiyan','true')
h.add('bakchodi','true')
h.add('saale','true')
h.add('fuckboi','true')
h.add('chutia','true')
h.add('bhenchodo','true')
h.add('FUCK','true')
h.add('porn','true')
h.add('booty','true')
h.add('penis','true')
h.add('vagina','true')
h.add('Lesibian','true')
h.add('chutar','true')
h.add('Randi','true')
h.add('chodna','true')
h.add('chut','true')
h.add('lund','true')
h.add('chusne','true')
h.add('kuttiya','true')
h.add('clitoris','true')
h.add('doggy style','true')
h.add('fucking hot','true')
h.add('dick','true')
h.add('underwear','true')
h.add('muaaaahhhhhhhh','true')
h.add('Aaaaaahhhhhhh','true')
h.add('chod','true')
h.add('suck','true')
h.add('horny','true')
h.add('randiyo','true')
h.add('loda','true')
h.add('randipana','true')
h.add('suwar','true')
h.add('bhosda','true')
h.add('mdrjat','true')
h.add('matherchod','true')
h.add('chutiyapa','true')
h.add('mc','true')
h.add('madrjat','true')
h.add('benchod','true')
h.add('saloo','true')
h.add('gaandu','true')
h.add('ahh','true')
h.add('ass','true')
h.add('breast','true')
h.add('butt','true')
h.add('buttocks','true')
h.add('naked','true')
h.add('nude','true')
h.add('tits','true')
h.add('ooooooohhh','true')
h.add('sexual','true')
h.add('hips','true')
h.add('lick','true')
h.add('nipple','true')
h.add('bobs','true')
h.add('bikni','true')
h.add('bra','true')
h.add('seductive','true')
h.add('xxx','true')
h.add('Booooobs','true')
h.add('sucky','true')
h.add('chodunga','true')
h.add('chuut','true')
h.add('cum','true')
h.add('oral','true')
h.add('dicks','true')
h.add('lesbian','true')
h.add('fack','true')
h.add('saxey','true')
h.add('fuking','true')
h.add('whore','true')
h.add('saala','true')
h.add('saale','true')
h.add('bhadve','true')
h.add('lavde','true')
h.add('bc','true')
h.add('bhencho','true')
h.add('bkl','true')
h.add('bhosda','true')
h.add('bhosdwaale','true')
h.add('lund','true')
h.add('chudwa','true')
h.add('bhenchod','true')
h.add('milf','true')
h.add('asssss','true')
h.add('chutiyo','true')
h.add('chutiyapa','true')
h.add('chutiyes','true')
h.add('lowda','true')
h.add('booby','true')
h.add('jerk', 'true')


p=pd.read_csv("FINAL DOC CHANGED - Sheet1.csv")

badCount = 0
k = 0

Y=np.array(p["bad_word_count"])
comments = np.array(p["COMMENTS"])

for comment in comments:
    data = comment.split()
    for word in data: 
        if h.get(word) == 'true':    
            badCount = badCount+1 
    Y[k] = badCount
    k = k+1
    badCount = 0

Z = np.array(p["RATING"])
X = np.array(p.drop(["RATING","URATING","COMMENTS"],1))

i = 0
for item in X:
    item[3] = Y[i]
    i = i+1

X_train, X_test, Z_train, Z_test = cross_validation.train_test_split(X, Z, test_size = 0.2)
model=LogisticRegression()
model.fit(X_train,Z_train)

predicted=model.predict(X_test)
predicted=np.round(predicted)

accu=model.score(X_test,Z_test)
print(accu)
print(metrics.classification_report(Z_test,predicted))
