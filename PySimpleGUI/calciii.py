import math

Cal=input("Enter which type of calculations you want to do: ") 

if Cal=='Basic':  

    def Basic(n1,n2):
        operand=input("Enter operand : ")

        if operand == '+':
            return n1+n2
        elif operand == '-':
            return n1-n2
        elif operand == '*':
            return n1*n2
        elif operand == '/':
            return n1/n2
        elif operand == '%':
            return n1%n2

    Number1=float(input("Enter Number 1:"))

    Number2=float(input("Enter Number 2:"))

    print(Basic(Number1,Number2))

if Cal == 'Trig': 

    CM=input("Enter what do you need to perform : ")
 
    def Trig(Func_): 

        if CM == 'sin_':
            angle=math.radians(float(input("Enter the angle: ")))
            sin_=math.sin(angle)
            print(sin_)

        else:
            if CM == 'tan_':
                angle=math.radians(float(input("Enter the angle: ")))
                try:
                    tan_=math.tan(angle)
                    print(tan_)
                except Exception as E:
                    print(E)
            else:
                if CM == 'cos_':
                    angle=math.radians(float(input("Enter the angle: ")))
                    cos_=math.cos(angle)
                    print(cos_)
                
                else:
                    if CM == 'cosec_':
                        angle=math.radians(float(input("Enter the angle:")))

                        try:
                            cosec_=1/math.sin(angle)
                            print(cosec_)
                        except Exception as E:
                            print(E)

                    else:
                        if CM == 'sec_':
                            angle=math.radians(float(input("Enter the angle:")))

                            try:
                                sec_=1/math.cos(angle)
                                print(sec_)
                            except Exception as E:
                                print(E)

                        else:
                            if CM == 'cot_':
                                angle=math.radians(float(input("Enter the angle :")))
                                
                                try:
                                    cot_=math.cos(angle)/math.sin(angle)
                                    print(cot_)
                                except Exception as E:
                                    print(E)
    
    Trig(CM)

if Cal == 'square':
    Num=float(input("Enter number: "))
    def square(Num):
         
        return math.sqrt(Num)
    
    print(square(Num))





