calls = 0
def count_calls():
    global calls
    calls += 1

def string_info (string):
    print(len(string), (string.upper()), (string.lower()))
    count_calls()

def is_contains(string, list_to_search):
    if string.upper() in (list(map(str.upper, list_to_search))):
        print(True)
    else:
        print(False)
    count_calls()

print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
