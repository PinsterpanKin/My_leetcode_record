#classic, showcasing good logic
def isPalindrome(x):
    if x<0:
        return False
    x=str(x)
    for i in range(int(ceil(len(x)/2))):
        if x[i]!=x[len(x)-i-1]:
            return False
        return True

#This new solution is more concise and efficient, as it uses string slicing to reverse the string and compare it with the original string.
def isPalindrome(x):
    if x<0:
        return False
    x=str(x)
    return x==x[::-1]