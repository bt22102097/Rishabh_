#Answer4
for candies in range(200):
    if (candies % 5 != 2):
        continue
    if (candies % 6 != 3):
        continue
    if (candies % 7 != 2):
        continue

    print(str(candies) + " is the answer!")
    break
x=200

for i in range(x):

    if i % 5 == 2:
       if i % 6 == 3:
          if i % 7 == 2:
             print(i, 'candies are in the bowl!')