def result(marks):
    per=sum(marks)/5
    if per>=90:
        gr="A"
    elif per>=80:
        gr="B"
    elif per>=70:
        gr="C"
    elif per>=60:
        gr="D"
    else:
        gr="F"
    return per,gr

marks=[]
for i in range(5):
    marks.append(float(input("Enter marks: ")))

per,gr=result(marks)
print("Percentage:",per)
print("Grade:",gr)
