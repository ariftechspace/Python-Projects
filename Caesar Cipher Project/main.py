alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# This is my Caesar Cipher implementation
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
        
    for letter in original_text:
        if letter in alphabet: 
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:  
            output_text += letter  # ✅ Keep symbols, spaces, numbers unchanged
    print(f"Here is the {encode_or_decode}d result: {output_text}")


want_to_continue = True

while want_to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'y' if you want to continue, or type 'n' if you do not want to:\n").lower()
    if restart == 'n':
        want_to_continue = False
        print("GOODBYE 👋")