# Create a python program that use Array and Insert each character of your full name and displays each character of your full name in reverse order


# Goal: Ryan Nico Anogante to etnagonA ociN nayR

#Solution 1
myname = ['R','y','a','n','N','i','c','o','A','n','o','g','a','n','t','e']
myname.reverse()
print(myname)

#Solution 2
fullname = str(input("What is your Full name? "))
nm = list(fullname)
nm.reverse()
print("Your name in reversed character is ", nm)