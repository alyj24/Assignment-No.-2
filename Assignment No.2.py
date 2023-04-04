print("Assignment No.2".center(42, "="))

# number 1
# pseudocode

# ask the user for an input and save the input
input_str = input("\033[92mGood Day! Please enter your input string: ")
output_str = "\033[94m"
# recognize each character of the input
for i in range(len(input_str)):
# if a, change it to *
  if input_str[i] == "a":
      output_str += "*"
# if e, change it to &
  elif input_str[i] == "e":
      output_str += "&"
# if i, change it to #
  elif input_str[i] == "i":
      output_str += "#"
# if o, change it to +
  elif input_str[i] == "o":
      output_str += "+"
# if u, change it to !
  elif input_str[i] == "u":
      output_str += "!"
  else:
      output_str += input_str[i]
# print the output
print(output_str)

print("Assignment No.2".center(42, "="))

# number 2
# pseudocode

# ask the user for an input and save the input
input_str = input("\033[91mGood Day! Please enter your input string: ")
output_str = "\033[95m"
# recognize each character of the input
for i in range(len(input_str)):
# if *, change it to a
  if input_str[i] == "*":
      output_str += "a"
# if &, change it to e
  elif input_str[i] == "&":
      output_str += "e"
# if #, change it to i
  elif input_str[i] == "#":
      output_str += "i"
# if +, change it to o
  elif input_str[i] == "+":
      output_str += "o"
# if !, change it to u
  elif input_str[i] == "!":
      output_str += "u"
  else:
      output_str += input_str[i]
# print the output
print(output_str)

print("Assignment No.2".center(82, "="))

# number 3
# pseudocode

# message: THISISTHELASTTASKHOORDAY 19 7 8 18 8 18 19 7 4 11 0 18 19 19 0 18 10 7 14 14 17 3 0 24
# key: KNIGHTS                      10 13 8 6 7 19 18
# add: 29 20 16 24 15 37 37 7 4 11 0 18 19 19 0 18 10 7 14 14 17 3 0 24
# mod: 3 20 16 24 15 11 11 7 4 11 0 18 19 19 0 18 10 7 14 14 17 3 0 24
# ciphertext: D U Q Y P L L H E L A S T T A S K H O O R D A Y
# define functions
def _pad_key(plaintext, key):
    padded_key = ""
    i = 0
    for char in plaintext:
        if char.isalpha():
            padded_key += key[i % len(key)]
        i += 1
    else:
            padded_key += ""
    return padded_key

def _encrypt_decrypt_char(plaintext_char, key_char, mode= 'encrypt'):
    if plaintext_char.isalpha():
        first_alphabet_letter = 'a'
    if plaintext_char.isupper():
        first_alphabet_letter = 'A'

    old_char_position = ord(plaintext_char) - ord(first_alphabet_letter)
    key_char_position = ord(key_char.lower()) - ord('a')

    if mode == 'encrypt':
        new_char_position = (old_char_position + key_char_position) % 26
    else:
        new_char_position = (old_char_position - key_char_position + 26) % 26
    return chr(new_char_position + ord(first_alphabet_letter))

def encrypt(plaintext, key):
    ciphertext = ""
    padded_key = _pad_key(plaintext, key)
    for plaintext_char, key_char in zip(plaintext, padded_key):
        ciphertext += _encrypt_decrypt_char(plaintext_char, key_char)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    padded_key = _pad_key(ciphertext, key)
    for ciphertext_char, key_char in zip(ciphertext, padded_key):
        plaintext += _encrypt_decrypt_char(ciphertext_char, key_char, mode= 'decrypt')
    return plaintext

# ask the user for an input and save the input
plaintext_input_str = input("\033[93mGreat Day! Please enter in all uppercase letters with no spaces your input message: ")
key_input_str = input("\033[92mOne last thing, Please enter in all uppercase letters with no spaces your input key: ")

# recognize the input by the user
ciphertext = encrypt(plaintext_input_str, key_input_str)
decrypted_plaintext = decrypt(ciphertext, key_input_str)

# print the output
print(f'\033[91mCiphertext: {ciphertext}')
print(f'\033[94mDecrypted Plaintext: {decrypted_plaintext}')