print("Enter marks Obtained in 5 subjects")
m1=float(input())
m2=float(input())
m3=float(input())
m4=float(input())
m5=float(input())
tot=m1+m2+m3+m4+m5
a=tot/5
if a>=91 and a<=100:
    print("Your grade is A+")
elif a>=81 and a<=90:
    print("Your grade is A")
elif a>=71 and a<=80:
    print("Your grade is B+")
elif a>=61 and a<=70:
    print("Your grade is B")
elif a>=51 and a<=60:
    print("Your grade is C+")
elif a>=41 and a<=50:
    print("Your grade is C")
elif a>=31 and a<=40:
    print("Your grade is D+")
elif a>=21 and a<=30:
    print("Your grade is D")
elif a>=11 and a<=20:
    print("Your grade is E")
elif a>=0 and a<=10:
    print("Your grade is F")
else:
    print("Invalid input, check that it is out of 100")