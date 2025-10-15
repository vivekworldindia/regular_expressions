# import re 

# text = "The rain in spane"

# if re.search(r"^The.*spane",text): 
#     print("result found!")
# else :
#     print("result not found!")


# import re
# result = re.findall(r'\d+', " User Id: user1, user2, user3")
# print(result)

# import re

# result = re.findall(r'(user)(\d+)', "User IDs: user1, user2, user3,")
# print(result)


# import re

# text = "User IDs: user1, user2, user3"

# # "user" और उसके बाद आने वाले नंबर को पकड़ना
# matches = re.findall(r'(user)(\d+)', text)

# # हर match को अच्छे से print करना
# for user, num in matches:
#     print(f"Username = {user}{num}")


# import re

# text = "User IDs: u-001, u-002, u-100"

# # नया regex pattern
# matches = re.findall(r'(u-)(\d+)', text)

# for prefix, num in matches:
#     print(f"Username = {prefix}{num}")


# import re 

# text = "The rane in spain "

# match = re.findall("in",text)
# print(match)

# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt,2)

# print("The first white-space character is located in position:", x.start())

# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)

# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)


# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())