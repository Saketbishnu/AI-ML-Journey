#convert all the odd places with the capital letter
def odd_uppercase(text):
    result =""
    for i in range(len(text)):
        if i%2==0:
            result+=text[i].upper()
        else:
            result+=text[i]
    return result
print(odd_uppercase("hello world"))