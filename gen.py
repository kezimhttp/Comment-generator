def commgen(howmuch,text):
    for i in range(1,howmuch):
        print(i,text)

print("Enter how many comments you need to write")
x = int(input())
print("Enter what you need to enter as content")
y = input()
commgen(x,y)