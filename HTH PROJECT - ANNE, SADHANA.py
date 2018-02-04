IBcreds = 0
grade = 0
Mcmaster = "Mcmaster University"
Waterloo = "Waterloo University"
Schulich = "Schulich School of Business"
Queens = "Queens University"
finished = 0


global queensinfo
global schulichinfo
global mcmasterinfo
global waterlooinfo
waterlooinfo = False
mcmasterinfo = False
schulichinfo = False
queensinfo = False



print ("************\n" + \
       "INTRODUCTION \n" + \
       "************\n" + \
       " \n" + \
       "Hello! Welcome to the Ontario UniFinder Demo, a simple text-based \n" + \
       "Python program that allows you to enter a field of research in \n" + \
       "university and your current marks and displays the universities in \n" + \
       "Ontario that you're eligible for. Each university also comes with a \n" + \
       "description of its history, housing and food info, as well as \n" + \
       "examples of courses you might take at that university according to\n" + \
       "your field. \n" + \
       " \n" + \
       "************\n" + \
       "INSTRUCTIONS \n" + \
       "************\n" + \
       " \n" + \
       "Type in your answer in the shell, according to the options provided\n" + \
       "to you. The options you have are CAPITALIZED, and are marked by \n" + \
       "double (>>). If you type a response not indicated by the options, \n" + \
       "the program will prompt you to retry with a valid answer. You can \n" + \
       "type FINISH at any time to stop the program, ELIGIBLE to return to \n" + \
       "your list of eligible universities, and RESTART to restart the \n" + \
       "program. Below is your first question."
       " \n" + \
       "************ \n" + \
       " ")

def restartyorn():
    wanttorestart = input ("Would you like to restart the program? \n" + \
                        "   >>YES or NO ").upper()

    if wanttorestart == "YES":
        doyoudoIB()

    elif wanttorestart == "NO":
        print("Ok, have a great day!")

    elif wanttorestart == "FINISHED":
        print("You already stopped the program. You can't do it again!")

    elif wanttorestart == "ELIGIBLE":
        print("You stopped the program, so you can't see your eligible \n" + \
              "universities anymore! Restart it and fill in the info \n" + \
              "again to see your eligible universities once more.")

    else:
        print ("Enter a valid input")
        restartyorn()

def doyoudoIB():
    global IB
    IB = str(input("Did you do IB? \n" + \
                    "   >> Type in YES or NO ")).upper()
              
    if IB == "YES":
        number()

    elif IB == "NO":
        chooseyourgrade()

    elif IB == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        restartyorn()

    elif IB == "ELIGIBLE":
        print("You haven't finished putting in your info yet, so you \n" + \
              "can't find your eligible universities. Answer the \n" + \
              "question again.")
        doyoudoIB()

    else:
        print("Enter in a valid input.")
        doyoudoIB()

def number():
    global chooseanumber
    global IBcreds
    IBcreds = str(input("How many IB credits did you get? ")).upper()

    if IBcreds.isdigit() == True:
        chooseanumber = False
        selectafield()

    elif IBcreds == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        chooseanumber = False
        restartyorn()

    elif IBcreds == "ELIGIBLE":
        print("You haven't finished putting in your info yet, so you \n" + \
              "can't find your eligible universities. Answer the \n" + \
              "question again.")
        chooseanumber=False
        number()

    else:
        print ("Enter a number")
        number()
        
def chooseyourgrade():
    global chooseagrade
    global grade
    grade = str(input("What was your grade percentage as an integer? (ex. 80) ")).upper()

    if grade.isdigit() == True:
        chooseagrade = False
        selectafield()

    elif grade == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        restartyorn()

    elif grade == "ELIGIBLE":
        print("You haven't finished putting in your info yet, so you \n" + \
              "can't find your eligible universities. Answer the \n" + \
              "question again.")
        chooseyourgrade()
        
    else:
        print ("Enter a number")
        chooseyourgrade()
        
def selectafield():
    global field
    global chooseafield
    field = str(input("What field are you going into? \n" + \
                      "    >> ENGINEERING or BUSINESS")).upper()

    if field == "ENGINEERING":
        chooseafield = False
        eligibleuni(IBcreds, grade, field)

    elif field == "BUSINESS":
        chooseafield = False
        eligibleuni(IBcreds, grade, field) ##TODO

    elif field == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        chooseafield = False
        restartyorn()

    elif field == "ELIGIBLE":
        print("You haven't finished putting in your info yet, so you \n" + \
              "can't find your eligible universities. Answer the \n" + \
              "question again.")
        chooseafield=False
        selectafield()

    else:
        print ("Enter a valid input")
        selectafield()

def eligibleuni (IBcreds, grade, field):
    global fie 
    if (int(IBcreds) >= 26 or int(grade) >= 85) and field == "ENGINEERING":
        fie = False
        print ("Here are your eligible universities: " + str(Mcmaster) + str(Waterloo))
        learnaboutuni()
        
    elif (int(IBcreds) >= 26 or int(grade) >= 75) and field == "BUSINESS":
        fie = False
        print ("Here are your eligible universities: " + str(Queens) + str(Schulich))
        learnaboutuni()

    elif (int(IBcreds) <= 25 or int(grade) <= 74) and field == "BUSINESS" or field == "ENGINEERING":
        fie = False
        print ("Sorry, your grade is too low, so you're not eligible for any universities.")

    else:
        print("Enter in a valid input.")
        eligibleuni(IBcreds, grade, field)

    return;

def learnaboutuni():
    
    uni = str(input("Type in the name of the university you want to learn more about. ")).upper()

    if uni == ("QUEENS" or "QUEENS UNIVERSITY"):
        queensinfo = True
        print("Queens University is located in Kingston, Ontario, and is \n" + \
              "currently headed by Dean David Saunders. Established in 1919, \n" + \
              "Queens offers a wide array of business courses for any young \n" + \
              "entreprenur, marketer or accountant hoping to prove their worth.\n" + \
              " \n" + \
              "RANKING: \n" + \
              "4th in Canada \n" + \
              "80th in the world")
        housing()
        queensinfo = False

    if uni == ("SCHULICH" or "SCHULISH SCHOOL" or "SCHULISH SCHOOL OF BUSINESS"):
        schulichinfo = True
        print("Despite its rather peculiar name, the Schulish School of Business is \n" + \
              "known for its incredible achievments. Located in North York, Ontario, \n" + \
              "its current dean is Dezso J, Horvat. The school has been standing \n" + \
              "since it was established in 1966. \n" + \
              "\n" + \
              "RANKING: \n" + \
              "1st in Canada for business schools \n" + \
              "24th in the world for business schools")
        housing()
        schulichinfo = False
    if uni == ("MCMASTER UNIVERSITY" or "MCMASTER"):
        
        mcmasterinfo = True
        print ("Mcmaster University was established in 1887, and is led today by \n" + \
               "President Patrick Deane. Located in Hamilton, Ontario, it has \n" + \
               "remained a center of innovation for talented young minds \n" + \
               "around the globe for centuries. \n" + \
               " \n" + \
               "RANKING: \n" + \
               "3rd in Canada \n" + \
               "66th in the world")
        housing()
        mcmasterinfo = False

    if uni == ("WATERLOO" or "WATERLOO UNIVERSITY" or "UNIVERSITY OF WATERLOO"):
        waterlooinfo = True
        print("Founded in 1956, the University of Waterloo is known across \n" + \
              "Canada and the world for its incredible achievements in public \n" + \
              "research, mathematics and computer sciences. Its current president \n" + \
              "Feridun Hamdullahpur. \n" + \
              " \n" + \
              "RANKING: \n" + \
              "7th in Canada \n" + \
              "162nd in the world")
        housing()
        waterlooinfo = False

    elif uni == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        restartyorn()

    elif uni == "ELIGIBLE":
        print("Sending you back to your list of eligible universities...")
        eligibleuni(IBcreds, grade, field)

    else:
        print ("Enter in a valid input.")
        learnaboutuni()

def housing():
    house = input("DO you want to learn about the housing at this university? \n" + \
                  " >> YES or NO ").upper()
    
    #if house == "YES" and waterlooinfo == True:
    #    print ("With 9 different student residence sites, Waterloo boasts \n" + \
    #           "a comfortable surplus of places for students to stay on \n" + \
    #           "campus.")
    #    waterlooinfo = False
    #    choice()

    if house.upper() == "YES" and mcmasterinfo == True:
        print ("ON CAMPUS ROOM TYPES:  \n" + \
                "Bunk & Loft Triple Room - $5,600 \n" + \
                "Lofted Triple/Quad - $5,800  \n" + \
                "Lofted Triple Room with Access to Single-User Washroom - $5,950 \n" + \
                "Triple Room - $6,300 \n" + \
                "Quad Room - $6,300 \n" + \
                "Double Room - $6,400 \n" + \
                "Double Room with Access to Single-User Washroom - $6,600 \n" + \
                "Double Room with Ensuite Washroom - $6,900 \n" + \
                "Single Room - $7,200 \n" + \
                "Single Room with Access to Single-User Washroom - $7,400 \n" + \
                "Single Room with Ensuite Washroom - $7,700 \n" + \
                "Apartment – 2 Person (Double Room) - $7,850 \n" + \
                "Apartment – 4/6 Person (Single Room) - $7,950 \n" + \
                "Suite – 4 person (Single Room) - $8,400")
        mcmasterinfo == False
        choice()

    if house == "YES" and queensinfo == True:
        print ("With 17 student residences, Queens University is home to \n" + \
               "more than 4500 students pursing higher education, with many \n" + \
               "more living off campus. Most residences are a 10 minute \n" + \
               "walk to classes, the gym and other campus facilities. On \n" + \
               "campus, the cost for 1 student paying for 1 full academic \n" + \
               "year ranges from $13284 to $15009, whereas off campus costs \n" + \
               "are approximately $500-$800 monthly.")
        queensinfo == False
        choice()

    if house == "YES" and schulichinfo == True:
        print ("On  Schulish campus, rooms cost approximately $5000 for 1 term \n" + \
               "(a 4 month period), whereas off campus rooms cost \n" + \
               "approximately $500-$1200 per month. The total expenses \n" + \
               "for most students amounts to $8700.")
        schulichinfo == False
        choice()

    elif house == "NO":
        choice()

    elif house == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        restartyorn()

    elif house == "ELIGIBLE":
        print("Sending you back to your list of eligible universities...")
        eligibleuni(IBcreds, grade, field)

    else:
        print ("Enter a valid input")

def choice():
    donext = input ("What do you want to do next? \n" + \
                    "   >>GO BACK or MEAL INFO ").upper()

    if donext == "GO BACK":
        eligibleuni(IBcreds, grade, field)

    elif donext == "MEAL INFO":
        mealinfo()

    elif donext == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        restartyorn()
        
    elif donext == "ELIGIBLE":
        print("Sending you back to your list of eligible universities...")
        eligibleuni(IBcreds, grade, field)

    else:
        print("Enter a valid input.")
        choice()

def mealinfo():

    if waterlooinfo == True:
        waterloofood()

    elif mcmasterinfo == True:
        mcmasterfood()

    elif queensinfo == True:
        queensfood()

    elif schulishinfo == True:
        schulishfood()


def anothermeal():
    picknewmeal = input ("Do you want to learn about another meal plan? \n" + \
                         "  >> YES or NO ").upper()
    if picknewmeal == "YES":
        mealinfo()

    elif picknewmeal == "NO":
        mealmenu()

    elif picknewmeal == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        restartyorn()
        
    elif picknewmeal == "ELIGIBLE":
        print("Sending you back to your list of eligible universities...")
        eligibleuni(IBcreds, grade, field)

    else:
        print("Enter a valid input")
        anothermeal()


def mealmenu():
    donextmeals = input ("What do you want to do next? \n" + \
                        "   >>GO BACK or HOUSING INFO ").upper()

    if donextmeals == "GO BACK":
        eligibleuni(IBcreds, grade, field)

    elif donextmeals == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        restartyorn()
        
    elif donextmeals == "ELIGIBLE":
        print("Sending you back to your list of eligible universities...")
        eligibleuni(IBcreds, grade, field)

    elif donextmeals == "HOUSING INFO":
        housing()

    else:
        print ("Enter a valid input")
        mealmenu()
#################
def queensfood():
    mealchoice = input ("Choose a meal plan to learn about. \n" + \
                        " >> MANDATORY MEAL PLAN or OPTIONAL MEAL PLAN ").upper()

    if mealchoice == "MANDATORY MEAL PLAN":
        print ("For students living in Village 1, the new REZ or REV, the \n" + \
               "mandatory meal plan is perfect for them. It comes in 3 types: \n" + \
               "lite, regular and hearty. The average regular mandatory meal \n" + \
               "plan costs $2505.")
        anothermeal()

    elif mealchoice == "OPTIONAL MEAL PLAN":
        print ("For those who live in Mackenzie King Village, UW Place, \n" + \
               "Columbia Lake Village, Minota Hagey Residence or off \n" + \
               "campus. It comes in 3 plans: casual, saver and super \n" + \
               "saver. The most common plan, the saver plan, costs \n" + \
               "$1450.")
        anothermeal()

    elif mealchoice == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        restartyorn()

    elif mealchoice == "ELIGIBLE":
        print("Sending you back to your list of eligible universities...")
        eligibleuni(IBcreds, grade, field)

    else:
        print ("Enter a valid input")
        mealinfo()

def queensfood():
    mealchoice = input ("Choose a meal plan to learn about. \n" + \
                        " >> ON CAMPUS or OFF CAMPUS").upper()

    if mealchoice == "ON CAMPUS":
        print ("On campus, Queens students get 19 meals a week, 200 \n" + \
               "Trade-A-Meals, and 150 Flex dollars, as well as 3 dining \n" + \
               "halls and 21 retail locations to buy food from.")
        anothermeal()

    elif mealchoice == "OFF CAMPUS":
        print ("The off campus meal plan is made to fit the lives of \n" + \
               "Queens students living off of the school's campus. \n" + \
               "Designed to be flexible and simple, it includes 3 options: \n" + \
               "the Dining Hall Lover, the Weekly 10 or the Annual 320, with \n" + \
               "Plus versions for each one. The costs range from $835 \n" + \
               "to $4040.")
        anothermeal()

    elif mealchoice == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        restartyorn()

    elif mealchoice == "ELIGIBLE":
        print("Sending you back to your list of eligible universities...")
        eligibleuni(IBcreds, grade, field)

    else:
        print ("Enter a valid input")
        mealinfo()
##################
def schulishfood():
    mealchoice = input ("Choose a meal plan to learn about. \n" + \
                        " >> MANDATORY MEAL PLAN or OPTIONAL MEAL PLAN ").upper()

    if mealchoice == "MANDATORY MEAL PLAN":
        print (" \n" + \
               "mandatory meal plan is perfect for them. It comes in 3 types: \n" + \
               "lite, regular and hearty. The average regular mandatory meal \n" + \
               "plan costs $2505.")
        anothermeal()

    elif mealchoice == "OPTIONAL MEAL PLAN":
        print ("For those who live in Mackenzie King Village, UW Place, \n" + \
               "Columbia Lake Village, Minota Hagey Residence or off \n" + \
               "campus. It comes in 3 plans: casual, saver and super \n" + \
               "saver. The most common plan, the saver plan, costs \n" + \
               "$1450.")
        anothermeal()

    elif mealchoice == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        restartyorn()

    elif mealchoice == "ELIGIBLE":
        print("Sending you back to your list of eligible universities...")
        eligibleuni(IBcreds, grade, field)

    else:
        print ("Enter a valid input")
        mealinfo()

def waterloofood():
    mealchoice = input ("Choose a meal plan to learn about. \n" + \
                        " >> MANDATORY MEAL PLAN or OPTIONAL MEAL PLAN ").upper()

    if mealchoice == "MANDATORY MEAL PLAN":
        print ("For students living in Village 1, the new REZ or REV, the \n" + \
               "mandatory meal plan is perfect for them. It comes in 3 types: \n" + \
               "lite, regular and hearty. The average regular mandatory meal \n" + \
               "plan costs $2505.")
        anothermeal()

    elif mealchoice == "OPTIONAL MEAL PLAN":
        print ("For those who live in Mackenzie King Village, UW Place, \n" + \
               "Columbia Lake Village, Minota Hagey Residence or off \n" + \
               "campus. It comes in 3 plans: casual, saver and super \n" + \
               "saver. The most common plan, the saver plan, costs \n" + \
               "$1450.")
        anothermeal()

    elif mealchoice == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        restartyorn()

    elif mealchoice == "ELIGIBLE":
        print("Sending you back to your list of eligible universities...")
        eligibleuni(IBcreds, grade, field)

    else:
        print ("Enter a valid input")
        mealinfo()

def mcmasterfood():
    mealchoice = input ("Choose a meal plan to learn about. \n" + \
                        " >> RESIDENTIAL or OFF CAMPUS ").upper()

    if mealchoice == "RESIDENTIAL":
        print ("All students living on Mcmaster's campus must get this food plan. \n" + \
               "There are two types, group A and B. The one you will be assigned \n" + \
               "depends on where you're staying on campus. The most common meal plan, \n" + \
               "a group A regular plan, costs about $4,355 per academic year.")
        anothermeal()

    elif mealchoice == "OFF CAMPUS":
        print ("There are 2 off-campus meal plans: Freedom and Term. The Freedom \n" + \
               "plan is designed to be risk-free and flexible, whereas the Term \n" + \
               "one is designed to last over a long period of time. The costs of \n" + \
               "each one vary from student-to-student.")
        anothermeal()

    elif mealchoice == "FINISH":
        finished = 1
        print("Thank you for using the Ontario UniFinder Demo! See you soon!")
        restartyorn()

    elif mealchoice == "ELIGIBLE":
        print("Sending you back to your list of eligible universities...")
        eligibleuni(IBcreds, grade, field)

    else:
        print ("Enter a valid input")
        mealinfo()

doyoudoIB()
