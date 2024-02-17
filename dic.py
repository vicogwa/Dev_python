hubbies = {'cooking': 'rice', 'reading': 'novie', 'gaming': 'candycrush'}
# print("Sarah's hubby is reading " + hubbies['reading'].title() +".")
# print("Sarah's hubby is cooking " + hubbies['cooking'].title() +".")
# print("Sarah's hubby is playing " + hubbies['gaming'].title() +".")

for key, value in hubbies.items():
    print(key.title(),  value.title()  + " is sarah's favorite hubby")

# for hubby in hubbies:
    # print(hubby.title(), hubbies[hubby] + " is sarah's favorite hubby.")
