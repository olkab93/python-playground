# 1. Converting Radians into Degrees
# 1 rad to deg
# degree = 57.2957795
#
#
# def radian_to_deg(angle_radian):
#     angle_degree = angle_radian * degree
#     return angle_degree
#
#
# angle_to_convert = int(input("Type angle value in radian: "))
# print(radian_to_deg(angle_to_convert))
#
#
# # --------------------------------------------------------------------------------------------
# # 2. Sort a List
#
# user_list = input("Pass me items to sort separated by a comma: ").split(",")
# sort = input("How should I sort the list? Type: asc, desc or none: ").lower()
#
#
# def format_user_input(user_input):
#     formatted_list = []
#     for item in user_input:
#         no_space = item.strip()
#         formatted_list.append(int(no_space))
#     return formatted_list
#
#
# def sort_a_list(list_to_sort, sort_type):
#     if sort_type == "asc":
#         list_to_sort.sort()
#         return list_to_sort
#     elif sort_type == "desc":
#         list_to_sort.sort(reverse=True)
#         return list_to_sort
#     elif sort_type == "none":
#         return list_to_sort
#     else:
#         print("I don't know how to sort your list.")
#
#
# print(sort_a_list(format_user_input(user_list), sort))
#
#
# # --------------------------------------------------------------------------------------------
# # 3. Convert Decimal Numbers to Binary
#
# def convert_decimal_to_binary(num_to_convert):
#     reminders = []
#     while num_to_convert >= 1:
#         reminders.append(str(int(num_to_convert % 2)))
#         num_to_convert = num_to_convert / 2
#
#     reminders.reverse()
#     binary = "".join(reminders)
#     return binary
#
#
# print(convert_decimal_to_binary(125))

# --------------------------------------------------------------------------------------------
# 4. Count Vowels in a String

def count_vowels_in_a_string(string_to_count):
    vowels = ["A", "E", "I", "O", "U"]
    vowels_count = 0
    for letter in string_to_count.upper():
        if letter in vowels:
            vowels_count += 1
    return vowels_count


print(count_vowels_in_a_string("COCONUT"))
