#printing, printing, printing
#Here's some strange stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"
#\n splits the string text between lines
months = "Jan\r\nFeb\r\nMar\r\nApr\r\nMay\r\nJun\r\nAug"

#\r is adding a space when I do \n
# this little guy is 

print("Here are the days:", days)
print("Here are the months:", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

print('''
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
''')
#would this be useful when my string needs to include a "", because then I could use it instead of the \ to escape?