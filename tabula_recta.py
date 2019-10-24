import string
var=string.ascii_lowercase

list=[char for char in var]

ml="".join(list)
print("")
print("                  tabula  recta")
print("")
for i in range(0,26):
     print(' '.join(ml[+i:]+ml[:+i]))
print("")
print("")
print("Spaces will be stripped from input")
print("Case will be converted to lowercase")
print("")
pr = input("Enter the primer: ")
#pr = "queenly"
pr2 = pr.replace(" ","")
primer = pr2.lower()

primer_list=[char for char in primer]

p = input("Enter the plaintext: ")
#p = "attackatdawn"
p2 = p.replace(" ","")
plaintext = p2.lower()

plaintext_list=[char for char in plaintext]

key=primer+plaintext
key_list=[char for char in key]
print("")
print("Primer is:    "+primer)
print("Plaintext is: "+plaintext)
print("Key:          "+primer+plaintext)
kl=len(plaintext_list)
#print("Plaintext length is: "+str(kl))
print("")
print("Ciphertext: ")
for r in range (0,kl):
    #j = row value (why didn't I name it r?)
    j = ml.index(key[r])
    ciphertext = (' '.join(ml[+j:]+ml[:+j]))
    po = ml.index(plaintext[r])
    #print(ciphertext[po*2]+" :ciphertext", end=' ')
    print(ciphertext[po*2], end='')
    #total = (ciphertext[po*2])
print("")
print("")
