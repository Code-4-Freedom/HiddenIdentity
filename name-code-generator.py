import random
print("Username-code Generator")
print("Project Library")
print(" ")
print("Your username-code suggestion:")
print(" ")

i1 = ['1','2','3','4','5','6','7','8','9','0']
random.shuffle(i1)
x1 = random.choice(i1)

i2 = ['1','2','3','4','5','6','7','8','9','0']
random.shuffle(i2)
x2 = random.choice(i2)

i3 = ['1','2','3','4','5','6','7','8','9','0']
random.shuffle(i3)
x3 = random.choice(i3)

ia = ['a','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','J','K','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
random.shuffle(ia)
xa = random.choice(ia)

ib = ['a','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','J','K','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
random.shuffle(ib)
xb = random.choice(ib)

ic = ['a','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','J','K','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
random.shuffle(ic)
xc = random.choice(ic)

ie = ['a','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','J','K','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
random.shuffle(ie)
xd = random.choice(ie)

ig = ['a','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','J','K','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
random.shuffle(ig)
xe = random.choice(ig)

ih = ['a','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','J','K','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
random.shuffle(ih)
xf = random.choice(ih)

print(xa+xb+xc+xd+xe+xf+x1+x2+x3)
