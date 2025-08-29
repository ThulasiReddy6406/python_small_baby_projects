# def love_calculator(name_1,name2):
#     mix_name = name_1+name2
#     t ="true"
#     l = "love"

#     true_love=0
#     love=0

#     for char in mix_name:
#         if char in t:
#             true_love+=1
#         else:
#             true_love+=0

#     for letter in mix_name:
#         if letter in l:
#             love+=1
#         else:
#             love+=0
#         return f"True Love score: {true_love + love}"

# resuly= love_calculator("rakshitha ishwar patel","ganthi thulasi nadha reddy")
# print(resuly)




def calculate_love_score(name1, name2):
    love1 = 0
    love2 = 0
    combined_names = (name1 + name2).lower()

    for char in combined_names:
        if char in "true":
            love1 += 1
        if char in "love":
            love2 += 1

    love_score = int(str(love1) + str(love2))
    print(love_score)

calculate_love_score("rakshitha ishwar patel", "ganthi thulasi nadha reddy")
