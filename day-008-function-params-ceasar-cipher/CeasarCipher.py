def encrypt(text, shift):

    text_list = list(text.lower())

    for i in range(len(text_list)):
        char_code = ord(text_list[i])

        if ord('a') <= char_code <= ord('z'):
            coded = char_code + shift if char_code + shift <= 122 else char_code + shift - 26
            text_list[i] = chr(coded)

    return "".join(text_list)

def decrypt(code, shift):
    
    code_list = list(code.lower())

    for i in range(len(code_list)):
        char_code = ord(code_list[i])

        if ord('a') <= char_code <= ord('z'):
            decoded = char_code - shift if char_code - shift >= 97 else 26 + char_code - shift
            code_list[i] = chr(decoded)

    return "".join(code_list)

print(encrypt('hellozeh', 9))
print(decrypt(encrypt('hellozeh', 9), 9))