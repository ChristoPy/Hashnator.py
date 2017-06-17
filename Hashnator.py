"""
Copyright 2017 Christopher Ribeiro

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import random, time


class Hashinator ():
	def __init__ (self, HashLevel = 1, HashSize = 16):
		if HashLevel < 1 or HashLevel > 3:
			print "HashLevel must be 1, 2 or 3."
			exit()

		self.HashSize = HashSize

		self.HashLevel = HashLevel
		self.Hash = ""
		self.GenHash ()

	def GenHash (self):
		Final = []
		Hash = []
		Count = 0

		while Count < self.HashSize:
			Final.append(self.RandomNumber ())
			Count += 1

			if self.HashLevel == 1:
				time.sleep(0.1)
				random.shuffle(Final)

			elif self.HashLevel == 2:
				random.shuffle(Final)
				time.sleep(0.3)
				random.shuffle(Final)

			elif self.HashLevel == 3:
				random.shuffle(Final)
				time.sleep(0.5)
				random.shuffle(Final)
				Final.reverse()

		random.shuffle(Final)

		Count = 0

		while Count < self.HashSize:
			Final.append(self.RandomLetter ())
			Count += 1

			if self.HashLevel == 1:
				time.sleep(0.1)
				random.shuffle(Final)

			elif self.HashLevel == 2:
				random.shuffle(Final)
				time.sleep(0.3)
				random.shuffle(Final)

			elif self.HashLevel == 3:
				random.shuffle(Final)
				time.sleep(0.5)
				random.shuffle(Final)
				Final.reverse()

		random.shuffle(Final)

		for Item in Final:
			Hash.append(Item)
			random.shuffle(Final)

		random.shuffle(Hash)

		Final = ""

		for Item in Hash:
			Final += Item

		self.Hash = Final[:self.HashSize]

	def RandomNumber (self):
		Seed = int(str(time.time()).split(".")[-1])

		try:
			Congruent = int(time.time()) ** Seed // 2
			Modulus = Congruent ** (Seed // Congruent ^ 2)
			Iterator = Seed // 2
			Seed = (Seed // Modulus ^ Iterator) + (Iterator * Seed + (Congruent ^ Modulus)) % Modulus
		except:
			pass

		Seed = list(str(Seed))
		random.shuffle(Seed)
		random.shuffle(Seed)
		Seed.reverse()
		random.shuffle(Seed)
		Seed.reverse()

		return Seed[-1]

	def RandomLetter (self):
		Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
					"n","o","p","q","r","s","t","u","v","w","x","y","z",
					"A","B","C","D","E","F","G","H","I","J","K","L","M",
					"N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
		random.shuffle(Letters)

		return Letters[int(self.RandomNumber ())]


