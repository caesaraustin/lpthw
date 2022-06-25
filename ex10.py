#What Was That?
print("I am 6'2\" tall.") #escape double-quote inside string
#it's like saying, whatever comes after this \, consider as part of printed text, not as ending the string.
print('I am 6\'2" tall.') #escape single-quote inside string

#tab, clearly
tabby_cat = "\tI'm tabbed in."
# \n seems to divide between two lines
persian_cat = "I'm split\non a line."
#once again, it looks like whatever comes after the \ is being considered part of the string text
#escapes the next character set
backslash_cat = "I'm \\ a \\ cat."

#putting it all together
#just tried to put the # a line below the """ and it didn't make it a comment, interesting...
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

cats = 800
print(f"There are the following varietals of cats:\n{cats:28}")
#printed 800 on a line that has :28 characters


print(f"There are the following varietals of cats:\n{cats}")

print(f"There are the following varietals of cats:\n{8*'cats'}")

print(f"There are the following varietals of cats:\n\t{8*cats}")

print(f"There are the following varietals of cats:\n\t{8*'{cats}'}")

print(f"There are the following varietals of cats:\n\t 8 * {cats}")

#print(f"There are the following varietals of cats:\n\t {8} * '{cats}'")
numcats = f'{cats} ' * 8
print(f'There are the following varietals of cats:\n\t{numcats}')