# url = input("URL:").strip()

# username = url.replace("https://twitter.com/","")
# print(f"username: {username}")

# url = input("URL:").strip()

# username = url.removeprefix("https://twitter.com/")
# print(f"username: {username}")

# import re
# url = input("URL: ").strip()
# username = re.sub(r"^(https://)?(www\.)?twitter\.com/",'',url)
# print(f"Username: {username}")

# import re 

# url = input("URL: ").strip()
# matchs = re.search(r"https?://(www\.)?twitter\.com/(.+)$",url,re.IGNORECASE)
# if matchs:
#     print(f"Username:",matchs.group(2))

# import re 

# url = input("URL: ").strip()
# if matchs := re.search(r"https?://(?:www\.)?twitter\.com/(.+)$",url,re.IGNORECASE):
#     print(f"Username:",matchs.group(1))

import re 

url = input("URL: ").strip()
if matchs := re.search(r"https?://(?:www\.)?twitter\.com/([a-z0-9_]+)",url,re.IGNORECASE):
    print(f"Username:",matchs.group(1))