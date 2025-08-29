# lis = [1,2,3,"nani",2,"sur",6,1]


# ex = set()
# du = set()

# for words in lis:
#     if words in ex:
#         du.add(words)
#     else:
#         ex.add(words)
# print(du)


# para = "iam nani from india and how are you nani iam ok and iam from haridwar."
# s = para.lower().split()

# ex = set()
# re = set()

# for words in s:
#     if words in ex:
#         re.add(words)
#     else:
#         ex.add(words)

# print(re)

# def count_unique_vowels(sentence):
#     vowels = {'a', 'e', 'i', 'o', 'u'}
#     sentence_chars = set(sentence.lower())  # convert to lowercase and extract unique characters
#     found_vowels = sentence_chars.intersection(vowels)  # find common vowels
#     print(f"Unique vowels found: {found_vowels}")
#     print(f"Total unique vowels: {len(found_vowels)}")

# # Example
# user_input = input("Enter a sentence: ")
# count_unique_vowels(user_input)

all = []
i = 0
for students in range(2):
    student = input("ENTER YOUR SUBJECTS :-  ").lower().split()
    i+=1
    all.append(set(student))
    print(f"student{i} == {student}")
    
common =set.intersection(*all)
print(common)
for com in all:
    if com == common:
        print(all[com])
    