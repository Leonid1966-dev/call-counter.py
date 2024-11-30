calls = 0

def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for item in list_to_search:
        if string == item.lower():
            return True
    return False


print(string_info("the North Caucasus"))
print(string_info("America"))
print(is_contains("port", ["Port", "import", "export"]))
print(is_contains("Clothes", ["shirt", "trousers", "jacket"]))

print(calls)

