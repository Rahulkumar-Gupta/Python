'''str=input("Enter the String: ")
print(str.center(100,'*'))
sub=input("What you want?")
print("String Count",str.count(sub))
print("String Find",str.find(sub))
'''


'''
str1=input("Enter String :")
print("Is ALNUM",str1.isalnum())
print("IS DIGIT",str1.isdigit())
print("IS ALPHA",str1.isalpha())
print("IS LOWER",str1.islower())
print("IS UPPER",str1.isupper())
print("IS TITLE",str1.istitle())
print("LOWER",str1.lower())
print("UPPER",str1.upper())
print("TITLE",str1.title())
'''
str2=input("Enter First String :")
str3=input("Enter Second String :")
sub=input("Enter Any Symbol :")
seq=[str2,str3]
print("Addition ",seq)
print("Joint ",sub.join(seq))
print("MAX ",max(str2))
print("Swap ",str2.swapcase())