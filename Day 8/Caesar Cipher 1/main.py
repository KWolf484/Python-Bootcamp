alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs.
#  You should be able to test the code and encrypt a message.

def encrypt(original_text, shift_amount):
    holder = ""
    for char in original_text:
        alpha_pos = alphabet.index(char)+shift_amount
        alpha_pos %= len(alphabet)
        holder += alphabet[alpha_pos]
    print(holder)

encrypt(original_text=text, shift_amount=shift)
# ### Merge block with encrypt(), rename func to caesar(),
# ### add third parameter encode_decode=direction ###
#
# def decrypt(original_text, shift_amount):
#     for char in original_text:
#         alpha_pos = alphabet.index(char)-shift_amount
#         alpha_pos %= len(alphabet)
#         holder.append(alphabet[alpha_pos])
#     list_to_string(items=holder)

# ### Redundant list_to_string() func ###
#
# def list_to_string(items):
#     placement = ""
#     for item in items:
#         placement += item
#     print(placement)

# ### Redundant block, integrate within caesar() ###
#
# if direction == "encode" or direction == "e":
#     print("Encrypting message")
#     encrypt(original_text=text, shift_amount=shift)
# elif direction == "decode" or direction == "d":
#     print("Decrypting message")
#     decrypt(original_text=text, shift_amount=shift)
# else:
#     print("Function unavailable.")





