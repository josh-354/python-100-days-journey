import sys


MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'  # Space between words
}

def text_to_morse(text):
    """
    Converts a given text string to Morse Code.
    - Converts input to uppercase.
    - Ignores characters not in the dictionary.
    - Uses '/' for word spaces, single space for letter spaces.
    """
    text = text.upper()
    morse_output = []
    
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_output.append(MORSE_CODE_DICT[char])
    
    # Join with spaces between letters, but replace word spaces
    result = ' '.join(morse_output)
    # Replace ' / ' with '/' for word separation
    result = result.replace(' / ', '/')
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If arguments are provided, join them as input
        input_text = ' '.join(sys.argv[1:])
    else:
        # Otherwise, prompt for input
        input_text = input("Enter text to convert to Morse Code: ")
    
    morse_code = text_to_morse(input_text)
    print(morse_code)
