import re

email = input("what's your email? ").strip().lower()

# if "@" in email and "." in email:
#     print("Valid")
    
# else:
#     print("Invalid")
    
    
# username,domain = email.split("@")

# # if username and ( "." in domain):
# if username and domain.endswith(".world"):
#     print("Valid")
    
# else :
#     print("Invalid")


if re.search(r"^\w+@\w+\.w+\.edu$",email,re.IGNORECASE):
    
    print("Valid")
else:
    print("Invalid")