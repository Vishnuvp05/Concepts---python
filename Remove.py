links =["www.google.com","www.wikepedia.in","www.facebook.org","www.instagram.com"]
#lstrip-left rstrip - right  A set of characters to remove as leading characters. By default, it uses space as the character to remove.

for link in links :
    print(link.strip("www."))

# google.com
# ikepedia.in
# facebook.org
# instagram.com

for link in links:
    print(link.removesuffix(".com"))
    print(link.removeprefix("www."))
    # removes specific prefix

