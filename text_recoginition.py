                   # THIS PROGRAM IS CODED BY SUSHANT KUMAR REG. NO. 12311087

import win32com.client as wincom
def speak():
    speak = wincom.Dispatch("SAPI.SpVoice")
    text = "Welcome to ROBOT PROJECT that is developed by Satyam kumar Singh"
    speak.speak(text)
speak()

try :
    print("               *************************************************************")                   
    print("               *  THIS PROGRAM IS CODED BY SUSHANT KUMAR REG. NO. 12311087 *")
    print("               *************************************************************\n")


    def menu():
       print("""    MENU
     1. Calculator
     2. Number is Prime No. or Not
     3. String is Palindrome or not
     4. Eligibility for voting
     5. Traffic Rules
     6. All Property of any number""")


    def calc():
        print("                       ********* CALCULATOR *********")
        print("")
        def add(a,b):
            print(a," + ",b,' = ',a+b)

        def sub(a,b):
            print(a," - ",b,' = ',a-b)

        def mult(a,b):
            print(a," * ",b,' = ',a*b)

        def div(a,b):
            print(a," / ",b,' = ',a/b)


        ans = "y"
        while ans=="y":
            num_1 = float(input("Enter num_1 : "))
            num_2 = float(input("Enter num_2 : "))
            op = input("Ente any operator (+,-,*,/) : ")
            print("")
            if op=="+":
                add(num_1,num_2)
            elif op=="-":
                sub(num_1,num_2)
            elif op=="*":
                mult(num_1,num_2)
            elif op=="/":
                div(num_1,num_2)
            else:
                print("INVALID INPUT")

            ans = input("Do you want to continue the calcultor program (y/n) : ")



    def fact():
        num = int(input("Enter a integer : "))
        sum1 = 1
        if num>=0:
            for i in range(1,num+1):
                sum1 = sum1*i
            print("Factorial of ",num," = ",sum1)
        elif num<0:
            print("Please enter a positive integer !!!")
        else:
            print("Invalid Input")


    def prime():
        num = int(input("Enter a number : ")) 
        a = True
        for i in range(1,num):
            if num%i==0:
                pass
            else:
                a = False
                break
        if a:
            print(num," is prime number.")
        else:
            print(num," is not prime number.")

    def vote():
        a = int(input("Enter your age : "))
        if a>= 18:
            print("You are eligible to vote \n")
        else:
            print("You are not eligible to vote \n")

    def palin():
        a = input("Enter a string : ")
        b = a[::-1]
        if a==b:
            print("Entered string is a palindrome.")
        else:
            print("Entered string is not a palindrome.")

    def rule():
        print("\t\tPROGRAM OF THE TRAFFIC RULES")
        print("\t MENU FOR TRAFFIC RULES")
        print("\t1. Enter 1 for Red")
        print("\t1. Enter 2 for Yellow")
        print("\t1. Enter 3 for Green\n")
        ac = int(input("Enter the colour : "))
        if ac==1:
            print("Stop \n")
        elif ac==2:
            print("Move Slowly \n")
        elif ac==3:
            print("You Can Move Fast \n")
        else:
            print("Invalid Input \n")





    def speak_1(a):
        speak = wincom.Dispatch("SAPI.SpVoice")
        speak.speak(a)


    def talk():
        a = 'Hii user, What is your name'
        speak_1(a)
        
        name = input("Please Responce : ")

        b = "Nice to meet you {}".format(name)
        speak_1(b)
        speak_1("By the way i am a Robot but as like a human")
        speak_1 ("How are you {}".format(name))
        print("ROBOT : How are you ",name)
        c = input("{} : ".format(name))
        if "fine" in c.lower() or "good" in c.lower() or "well" in c.lower():
            d = 'Good, keep it on'
            speak_1(d)
            print("ROBOT : ",d)
        elif "not" in c.lower():
            e = "no problem take care of your health"
            speak_1(e)
            print("ROBOT : ",e)
        else:
            speak_1("Sorry i can't get you")
            
        



    def task():
        a = "What kind of task you wanted to perform i have some basic task for you."
        b = "You can select any one"
        speak_1(a)
        speak_1(b)
        menu()
        speak_1("Press 1 for calculator")
        speak_1("Press 2 for checking wheather entered number is Prime number or not")
        speak_1("Press 3 for checking wheather entered number is palindrome or not")
        speak_1("Press 4 to check eligibility for voting ")
        speak_1("Press 5 for accessing Traffic rules")
        speak_1("Press 6 for Accessing property of entered number")
        speak_1("Press 7 for accessing factorial of entered number")

        op = input("Enter your response : ")
        if op == "1":
            calc()
        elif op == "2":
            prime()
        elif op == "3":
            palin()
        elif op == "4":
            vote()
        elif op == "5":
            rule()
        elif op == "6":
            prop()
        elif op == "7":
            fact()
        else:
            print("Invalid input !!!")




    def Robo_Project():
        pas = input("Enter the password : ")
        ans = 1
        sum1=1
            
        if pas=="@Sushant":
            print("You have successfully logged in")
            #menu()
            print("Do you want to talk with ROBOT-2.O OR You want to perform any tasks")
            a = "Press 1 for talking with RObot-2.O Or press 2 for performing any tasks"
            speak_1(a)
            var_1 = input("Enter (1 OR 2) : ")
            if var_1=="1":
                talk()
            elif var_1=="2":
                task()
            else:
                print("INVALID INPUT !!!")
            
            

        else:
            while ans<=2:
                print("Incorrect password")
                pas = input("Enter the password : ")
                if pas=="@Sushant":
                    print("\n You have successfully logged in..")
                    
                    print("Do you want to talk with ROBOT-2.O OR You want to perform any tasks")
                    a = "Press 1 for talking with RObot-2.0 Or press 2 for performing any tasks"
                    speak_1(a)
                    var_1 = input("Enter (1 OR 2) : ")
                    if var_1=="1":
                        talk()
                    elif var_1=="2":
                        task()
                    else:
                        print("INVALID INPUT !!!")
                    break
                
                else:
                    ans+=1
                    sum1+=1
        if sum1==3:
            print("!!! You have been denied access....\n")
            
        from datetime import datetime
        now = datetime.now()
        s = now.strftime("%d-%m-%Y  %H:%M:%S")
        print("_________________________________________________________________________________________________")
        print("\t\t\t\t THANKS FOR VISITING MY PROGRAM \n")
        print("         - PROGRAMER SUSHANT KUMAR ","                           Date-Time :",s)
        print("_________________________________________________________________________________________________")

            
        print("_________________________________________________________________________________________________")

    Robo_Project()    
except:
    print("some error ocurred")
    print("Please try again")
