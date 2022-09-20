# rem = 15 % 4
# Type = type(rem)
# print(Type,rem)


# print("We have {0} small boxes, {1} large boxes, {2} medium boxes".format(10,12,12))



# chars = "[[]]"
# word = "Cool"
# # res = chars[:2]+ word +chars[2:]
# res = chars[:2].join(word)
# # res = .join(chars[2],word)
# print(res)

# word1 = "Computer"
# word2 = "Truck"
# result = word1[1:] + word2[0:1] + word2[2:]
# print(result)

# l = input("Enter the lenght:")
# if(l%2==0):
#     chars = input("Enter Vale:")
chars = "<[<||>]>"
size = len(chars)
index = int(size/2)
word = "mirror"
result = chars[:index]+ word + chars[index:]
print(result)

