import string
var=string.ascii_lowercase

list=[char for char in var]

ml="".join(list)
print("")
p = input("Enter primer: ")

pr = p.replace(" ","")
primer = pr.lower()

primer_list=[char for char in primer]
c = input("Enter ciphertext: ")

cr = c.replace(" ","")
cipher = cr.lower()
cipher_list=[char for char in cipher]
mega_list=primer_list

lenvar=len(cipher_list)

# for range and loop
# need primer+ciphertext
# length is length of ciphertext
# all of key will be used to decipher, the beginning of the ciphertext will be appended to the key
print("Decoded text is: ")
for r in range(0,lenvar):
    j = ml.index(mega_list[r])
    # This gets the nth position of the primer to determine which row should be consulted
    #print("Row number is: "+str(j))
    ciphertext = (' '.join(ml[+j:]+ml[:+j]))
    # This is the code that shifts the letters to obtain the correct row
    #print(ciphertext+"  Row: "+str(j))
    #print("Cipherlist character is: "+cipher_list[r])
    #
    # find 'n' in ciphertext
    pos=ciphertext.index(cipher_list[r])
    f=(int(pos)/2)
    dc=ml[int(f)]
    mega_list.append(dc)
    print(dc, end='')
print("")
print("")