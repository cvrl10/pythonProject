import re

pattern = re.compile(r'[A-Za-z0-9]+')
texts = ['John', 'John_Hunt', '42', 'John42', 'John 42']

for text in texts:
    result = True if pattern.fullmatch(text) else False
    print(text, result)

print('\n', 'Using different methods', '\n', sep='')

for text in texts:
    match = pattern.findall(text)
    print(text, match)


def verify_postcode(postcode):
    if not isinstance(postcode, str):
        return False
    match = re.fullmatch(r'[A-Z]{2}[0-9]{1,2} [0-9]{1,2}[A-Z]{2}', postcode.upper())
    return True if match else False


post_codes = ['SY23 33AA', 'SY23 4ZZ', 'BB1 3PO', 'AA111 NN56', 'AA1 56NN', 'AA156NN', 'AA NN']

print('\n', 'Evoking verify_postcode(post_code)', '\n', sep='')

for post_code in post_codes:
    print(post_code, 'is a UK Postcode: ', verify_postcode(post_code))


def extract_values(text, open='<', close='>'):
    pairs = {
                '<': '>',
                '''"''': '''"''',
                "'": "'",
                '[': ']',
                '{': '}'
            }

    pattern = re.findall('\b'+open+'\b'+close, text)
    return pattern


texts = ['<John>', '<42>', '<John 42>', 'The <town> was in the <valley>']


def extract_values(text, open='<', close='>'):

    pairs = {
                '<': '>',
                '''"''': '''"''',
                "'": "'",
                '[': ']',
                '{': '}'
            }

    if not isinstance(text, str) or close != pairs[open]:
        return None

    pattern = re.findall(open+'[^<]*'+close, text)

    if pattern:
        pattern = [match[1:len(match)-1] for match in pattern]
        return pattern
    else:
        return None

print('\n', 'evoking extract_values(text)', '\n', sep='')

for text in texts:
    print(extract_values(text))


print(extract_values(r"Extracting only the names in single quotes, <Carl>, <Archemetre>"))