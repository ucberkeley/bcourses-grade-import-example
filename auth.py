TOKEN_FILE = 'token'

try:
    with open(TOKEN_FILE) as f:
        token = f.read()
except IOError:
    print('bCourses token file not found:', TOKEN_FILE)
