#data
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#taking data from user
direction = input(
  """
  Type 1 for 'encode' to encrypt, type 2 'decode' to decrypt:
    
    1. encode
    2. decode
  """)

#initial messages  
if(direction == "1"):
  print(
    """
      Encode your private data here. 
    """
  )
elif(direction == "2"):
  print(
    """
      Do you need your private data back, yes it is here. 
    """
  )

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Encryption starts here

def encrypt(plainText, shiftText):
  cipher_text = ''
  for letter in text:
    #print(letter)
    position = alphabet.index(letter)
    #print(position)
    newPosition = position + shiftText
    #print(newPosition)
    newLetter = alphabet[newPosition]
    cipher_text += newLetter
  print(f"The encrypted text is ->: {cipher_text}")

#Decryption starts here

def decrypt(plainText, shiftText):
  cipher_text = ''
  for letter in text:
    #print(letter)
    position = alphabet.index(letter)
    #print(position)
    newPosition = position - shiftText
    #print(newPosition)
    newLetter = alphabet[newPosition]
    cipher_text += newLetter
  print(f"The decrypted text is ->: {cipher_text}")

#Handling options
if(direction == "1"):
  print(
    """
      Encoded succesfully. Now sleep tight. 
    """
  )
  encrypt(text, shift)

elif(direction == "2"):
  print(
    """
      Decoded succesfully. Remember us in Good words 
    """
  )
  decrypt(text, shift)