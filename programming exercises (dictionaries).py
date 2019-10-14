# exercise 6
# text = str(input('tip your text to convert: '))
# rot13 = str.maketrans(
#     "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
#     "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
# print(str.translate(text, rot13))
# text = str(input("enter your text to convert:"))
# rot13 = str.maketrans(
#     "0123456789",
#     "ABCDEFGHIJ")
# print(str.translate(text, rot13))


# exercise 1
# mydict = {"Animal":1,"Fruit":2,"Vegetables":3}
# keylist = ["Animal", "Fruit", "Vegetables"]
# def remove_keys(mydict,keylist):
#     for i in keylist:
#         del mydict[i]
# print(remove_keys(mydict,keylist))
# exercise 2
# def accept_login(users,username,password):
#     users = {}
#     username = "sunny.jo"
#     password = "hahahaha"
#     users[username] = password
#     x = input("Enter username :")
#     if x in users:
#         y = input("Enter password :")
#         if y == users[x]:
#             print("hello",x)
#         else:
#             print("sorry wrong password")
#     else:
#         print("sorry wrong username")
#  exercise 3
# val = int(input("Input a number range 1-3:"))
# mydict = {"a":1, "b":2, "c":3, "d":4}
# def find_value(mydict,val):
#     for keys,values in mydict.items():
#         if val == values:
#             print(keys)
# print(find_value(mydict,val))

# exercise 4
# def letter_frequencies(mylist):
#     dict = {}
#     for i in (range(len(mylist))):
#         if (mylist[i] in dict):
#             dict[mylist[i]] = int(dict.get(mylist[i])) + 1
#         else:
#             dict[mylist[i]] = 1
#     return dict
# x = input("Enter any string :")
# print(word_frequencies(x))

# exercise 4
# dict = {}
# def word_frequencies(text):
#     for word in text.split():
#         dict[word] = dict.get(word,0)+1
#     for key in dict:
#         print(dict[key],key)
# word_frequencies("welcome to binus")

# exercise 5
# def count_kmers(DNA, k):
#     counts = {}
#     num_kmers = len(DNA) - k + 1
#     for i in range(num_kmers):
#         kmer = DNA[i:i+k]
#         if kmer not in counts:
#             counts[kmer] = 0
#         counts[kmer] += 1
#     return counts
# print(count_kmers("ATGATG",3))