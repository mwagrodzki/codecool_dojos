import random

attacker = []
defender = []

for i in range(3):
    attacker.append(random.randrange(1,7))

attacker.sort(reverse=True)
att = str(attacker).replace('[','').replace(', ','-').replace(']','')

for i in range(2):
    defender.append(random.randrange(1,7))

defender.sort(reverse=True)
dfn = str(defender).replace('[','').replace(', ','-').replace(']','')

print("Dice:")
print("  Attacker: "+ att)
print("  Defender: "+ dfn)