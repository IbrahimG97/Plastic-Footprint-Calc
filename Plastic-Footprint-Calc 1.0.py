#.... This program is designed to input various plastic items such as plastic straws, cups and bags and how much you use
# of each item. For example I used 15 straws this week and I created this many grams of plastic waste for the week.
# the goal is to have the program be able to calculate multiple items at once instead of one at a time.
# for example it will tell you your combined total of plastic waste based on how many straws bags and cups used etc.
# The program will take that data and compare it to the national average in the USA
# The Program will also take monetary savings into account if you curretly visit a place that offers it
# Starbucks and whole foods are one of the places that offer a discount based on using reusable items
# If the user does visit one of theses places then a monenetary savings for the week month and year will be displayed.

#Start of project

plastic_straws= .42 #this is the weight in grams of a plastic straw
plastic_bags= 3 #this is the weight in grams of a plastic bag
plastic_cup= 8 #this is the weight in grams of a pastic cup
def starbucks_savings(): # this is a function used to calculate the monetary savings of using a reusable cup at starbucks for a week, year, and month
    numofcups = input('Enter the number of cups used this week\n')
    numofcups = float(numofcups)
    savings = float(0.10)
    savings = float(savings)
    print('By switching to a reusable cup you could save,','In one week',numofcups*savings, 'Cents', 'In one month', numofcups*savings*4,'Cents','In one year', numofcups*savings*52, 'Cents')



def wholefoods_savings(): # this is a function used to calculate the monetary savings of using a reusable bag at whole foods for a week, year, and month
    numofbags = input('Enter the number of bags used this week\n')
    numofbags = float(numofbags)
    savings = float(0.05)
    savings = float(savings)
    print('By switching to a reusable bag you could save,','In one week',numofbags*savings, 'Cents', 'In one month', numofbags*savings*4, 'Cents', 'In one year', numofbags*savings*52, 'Cents')

#need to work on being able to calculate exact decimal values and possibly converting cents to dollar amounts.
#See if its possible to have a currency placeholder and have the value typed into the sentence instead of the sentence right next to it
#work on making verything that needs to be calculated into a fucntion.
#Work on for or while loops to have program choose which function is best
National_average = ['Insert calc for national average'] # add this at the end of the straw, bags and cup function instead as a single one.
print('Welcome to the plastic footprint calc')
print()
print('This program is designed to show you how many Grams of plastic you consume Yearly, Monthly, Weekly')
print('This program can also show any monetary and planetary savings based on reusable choices.')
print()
print('Please select an item by typing its name. You can select straws, cups or bags.')
#put for or while loop to have the program select a function











































print('Do you use Starbucks or Wholefoods?')

def choosesavings(): #this function allows you to choose between monetary savings for starbucks or wholefoods
    if input() == 'Starbucks':
        starbucks_savings()
    elif input() == 'Wholefoods':
        wholefoods_savings()
    else:
        print('Please select either Starbucks or Wholefoods, Answer is case sensitive!')
        print()
        choosesavings() #

choosesavings()



