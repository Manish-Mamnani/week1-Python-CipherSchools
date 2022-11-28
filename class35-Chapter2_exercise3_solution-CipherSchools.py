name, single_character = input("enter your name and a character: ").split(",")
print(f"length of your name is: {len(name)}")
print(f"character count: {name.lower().count(single_character.lower())}")
#"  Manish  "--->"Manish"--->"manish"
#"  H  "--->"H"--->"h"
print(f"character count: {name.strip().lower().count(single_character.strip().lower())}")