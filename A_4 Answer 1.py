#answer 1
marks=int(input("enter your marks"))
print(marks)
if marks<25 :
    print("F")
elif marks>25 and marks<45 :
    print("E")
elif marks>45 and marks<50:
    print("D")
elif marks>50 and marks<60:
    print("C")
elif marks>60 and marks<80:
    print ("B")
elif marks>80:
    print ("A")