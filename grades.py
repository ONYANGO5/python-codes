subject_1=int(input("marks for subject 1:"))
subject_2=int(input("marks for subject 2:"))
subject_3=int(input("marks for subject 3:"))
subject_4=int(input("marks for subject 4:"))
average=(subject_1+subject_2+subject_3+subject_4)/4
print(average)
if average>=70<=100:
    print("A")
elif average>=60<70:
    print("B")
elif average>=50<60:
    print("C")
elif average>=40<50:
    print("D")
elif average>=0<40:
    print("FAIL")