calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return length, upper_case, lower_case

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    for item in list_to_search:
        if string_lower == item.lower():
            return True
    return False

print(string_info('Geborgenheit'))
print(string_info('Augsburg'))
print(is_contains('collagen', ['gen', 'GeN', 'collaGeN'])) # Urban ~ urBAN
print(is_contains('gewinn', ['weinen', 'wissen'])) # No matches
print(calls)