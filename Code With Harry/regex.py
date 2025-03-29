import re

pattern = r"[A-Z]+bc"
search = "abc hello abc how are you Abc in Cbc or Xbc"

# print(re.search(pattern, search))

matches = re.finditer(pattern, search)

for match in matches:
    word = search[match.span()[0] : match.span()[1]]
    print(word)
