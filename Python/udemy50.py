score=int(input("Enter your score :"))

if score<60:
    print("Failed")

else:
    if score>=90:
        print("your score is : " + str(score) + "and grade is A")

    else:
        if score >=80:
            print("your score is : " + str(score) + "and grade is B")
        else:
            if score >=70:
                print("your score is : " + str(score) + "and grade is C")
            else:
                print("your score is : " + str(score) + "and grade is D")
                