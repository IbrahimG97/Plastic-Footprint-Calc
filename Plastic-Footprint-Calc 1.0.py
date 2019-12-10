#.... This program is designed to input various plastic items such as plastic straws, cups and bags and how much you use
# of each item. For example I used 15 straws this week and I created this many grams of plastic waste for the week.
# the goal is to have the program be able to calculate multiple items at once instead of one at a time.
# for example it will tell you your combined total of plastic waste based on how many straws bags and cups used etc.
# The program will take that data and compare it to the national average in the USA
# The Program will also take monetary savings into account if you curretly visit a place that offers it
# Starbucks and whole foods are one of the places that offer a discount based on using reusable items
# If the user does visit one of theses places then a monenetary savings for the week month and year will be displayed.

#Start of project
print('Welcome to the Plastic Consumption Calc')
print('This program is designed to show you how many Grams of plastic you consume Yearly, Monthly, Weekly')
print('This program can also show any monetary and planetary savings based on reusable choices.')
print('Lets start by finding out your plastic usage')
boolean=False

def plastic_straws():     #Function used to run straw consumption in grams.
    numofstraws = input('Enter number of Straws used this week.\n')
    numofstraws = float(numofstraws)
    consumed = float(.43)
    consumed = float(consumed)
    print('By using disposable plastic straws for the week you have used:', numofstraws*consumed, 'Grams', '\n' 'If you continue to use plastic straws you will have used,',numofstraws*consumed*4, 'Grams in one month', numofstraws*consumed*52,'Grams in one year' )

def plastic_bags(): #Function for plastic bag consumption
    numofbags = input('Enter number of bags used this week.\n')
    numofbags = int(numofbags)
    consumed = int(3)
    consumed = int(consumed)
    print('By using disposable plastic bags for the week you have used:', numofbags*consumed, 'Grams' '\n' 'If you continue to use disposable plastic bags you will have used,',numofbags*consumed*4, 'Grams in one month', numofbags*consumed*52, 'Grams in one year')

def plastic_cup():#Function for plastic cup consumption
    numofcups = input('Enter number of plastic cups used this week. \n')
    numofcups = int(numofcups)
    consumed = int(8)
    consumed = int(consumed)
    print('By using disposable plastic cups for the week you have used:', numofcups*consumed, 'Grams' '\n' 'If you continue to use disposable plastic cups you will have used,' ,numofcups*consumed*4, 'Grams in one month', numofcups*consumed*52, 'Grams in one year')


def starbucks_savings(): # this is a function used to calculate the monetary savings of using a reusable cup at starbucks for a week, year, and month
    numofcups = input('Enter the number of cups used this week\n')
    numofcups = float(numofcups)
    savings = float(0.10)
    savings = float(savings)
    print('Starbucks offers 10 cents off any order if you use a reusable mug!')
    print('By switching to a reusable cup you could save,','In one week',numofcups*savings, 'Cents', 'In one month', numofcups*savings*4,'Cents','In one year', numofcups*savings*52, 'Cents')

def wholefoods_savings(): # this is a function used to calculate the monetary savings of using a reusable bag at whole foods for a week, year, and month
    numofbags = input('Enter the number of bags used this week\n')
    numofbags = float(numofbags)
    savings = float(0.05)
    savings = float(savings)
    print('Wholefoods offers 5 cents off any purchase with use of a reusable bag!')
    print('By switching to a reusable bag you could save,','In one week',numofbags*savings, 'Cents', 'In one month', numofbags*savings*4, 'Cents', 'In one year', numofbags*savings*52, 'Cents')

def choosesavings(): #this function allows you to choose between monetary savings for starbucks or wholefoods
        if input() == 'Starbucks':
            starbucks_savings()
        elif input() == 'Wholefoods':
             wholefoods_savings()
        else:
            print('Please select either Starbucks or Wholefoods, Answer is case sensitive!')
            choosesavings()





#need to work on being able to calculate exact decimal values and possibly converting cents to dollar amounts.
#See if its possible to have a currency placeholder.





def maincalc():  # This is what allows the user to select which calculation they would like to do.
    boolean = False

    while boolean == False: #For some reason If I used a regular while loop without boolean it would only consider the first option and nothing else. This method I got from Stack overflow
        item = input('Please select an item by typing its name. You can select straws, cups or bags.\n')
        if 'straws' in item:
            plastic_straws()
            boolean = True
        if 'bags' in item:
            plastic_bags()
            boolean = True
        if 'cups' in item:
            plastic_cup()
            boolean = True
        if boolean == False:
            print('Please select straws, cups or bags.')


maincalc()
print('The second part of this calculator allows you to see how much money you would save if you used reusable bags or cups at specific locations that offer discounts')
print('Starbucks and Wholefoods offer discounts for using a reusable bag or cup. Please type in Starbucks or Wholefoods to being the 2nd part of the calculator.')
choosesavings()

print('Thank you for using the Plastic Foot Print calculator. The goal is to inspire users to use less plastic waste and use more reusable items!')








#i = False Tried to fix the loop for wholefoods
# while i == False:
    #if input() == 'Starbucks':
        #starbucks_savings()
        #i = True
    # if input() == 'Wholefoods':
    #     wholefoods_savings()
    #     i = True
    # if i == False:
    #     print('Please type either Starbucks or Wholefoods. Answer is case sensitive!')

