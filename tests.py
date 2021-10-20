import time
def assert_equals_string(str1, str2):
    x = time.perf_counter()
    if len(str1) != len(str2):
        return "Runtime: {runtime}s\nFailed: {string1} and {string2} lengths don't match\n-------".format(runtime=x,string1=str1, string2=str2)
    elif type(str1) != type(str2):
        return "Runtime: {runtime}s\nFailed: {string1} and {string2} are different types\n-------".format(runtime=x,string1=str1, string2=str2)
    elif str1 == str2:
        return "Runtime: {runtime}s\nPassed: {string1} is equal to {string2}\n-------".format(runtime=x,string1=str1, string2=str2)
    return "Runtime: {runtime}s\nFailed: undefined \n-------\n".format(runtime=x)

def assert_equals_integer(int1, int2):
    x = time.perf_counter()
    if type(int1) != type(int2):
        return "Runtime: {runtime}s\nFailed: {number1} and {number2} are different types\n-------".format(runtime=x,number1=int1, number2=int2)
    elif int1 == int2:
        return "Runtime: {runtime}s\nPassed: {number1} is equal to {number2}\n-------".format(runtime=x,number1=int1, number2=int2)

    return "Runtime: {runtime}s\nFailed: {number1} is not equal to {number2}\n-------".format(runtime=x,number1=int1,number2=int2)

def assert_equals_boolean(bool1, bool2):
    x = time.perf_counter()
    if type(bool1) != type(bool2):
        return "Runtime: {runtime}s\nFailed: {boolean1} and {boolean2} are different types\n-------".format(runtime=x,boolean1=bool1, boolean2=bool2)
    elif bool1 == bool2:
        return "Runtime: {runtime}s\nPassed: {boolean1} is equal to {boolean2}\n-------".format(runtime=x,boolean1=bool1, boolean2=bool2)
    return "Runtime: {runtime}s\nFailed: {boolean1} is not equal to {boolean2}\n-------".format(runtime=x, boolean1=bool1, boolean2=bool2)
def here():
    x = time.perf_counter()
    return 'Runtime: {runtime}s\nHere!\n-------'.format(runtime=x)

def assert_equals(param1, param2):
    if type(param2) == str:
        return assert_equals_string(param1, param2)
    elif type(param2) == int:
        return assert_equals_integer(param1, param2)
    elif type(param2) == bool:
        return assert_equals_boolean(param1, param2)
    else:
        return "No test matchin type: {type_to_match}\n-------\n".format(type_to_match=type(param2))
