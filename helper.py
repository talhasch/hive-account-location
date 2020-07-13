IGNORE_LIST = []

def sanitize(x):
    return x.strip().rstrip('"').lstrip('"').lower()


def should_ignore(x):
    return sanitize(x) in IGNORE_LIST 
