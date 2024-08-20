import art # type: ignore
print(art.logo)

alphabet = [chr(i) for i in range(97, 123)]

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    # If decoding, reverse the shift by multiplying it by -1.
    if encode_or_decode == "decode":
           shift_amount *= -1

    # Looping through each character in the input text.       
    for letter in original_text:
       if letter not in alphabet:
        # If the character is not in the alphabet (like spaces or punctuation)   
           output_text += letter
       else:
        # Calculate the new shifted position within the alphabet.
        shifted_position = alphabet.index(letter) + shift_amount
         # Ensure the position wraps around within the length of the alphabet.
        shifted_position %= len(alphabet) 
        # Append the shifted letter to the output string.
        output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Restarting the cipher program

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Calling the Caesar cipher function with user inputs.
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Asking the user if they want to run the program again.
    restart = input("Type 'yes' if you want to go again, Otherwise, type 'no'. \n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
        


