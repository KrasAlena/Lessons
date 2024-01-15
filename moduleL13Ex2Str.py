def get_lower(word):
    result = ''.join([c.upper() if i % 2 != 0 else c for i, c in enumerate(word)])
    return result

if __name__ == '__main__':
    user_string = 'Transcription'
    print(get_lower(user_string))