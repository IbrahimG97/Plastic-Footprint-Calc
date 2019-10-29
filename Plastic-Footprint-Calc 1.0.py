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
    numofcups = int(numofcups)
    savings = int(10)
    savings = int(savings)
    print(numofcups*savings, 'In one week this is how much you could have saved in cents if you switched to a resusable option. "The Last zero is ignored" .')
    print(numofcups*savings*4, 'In one month this is how much you could have saved in cents.')
    print(numofcups*savings*52, 'In one year this is how much you could have saved in cents.')#since im calculating per week 52 weeks are in one year


def wholefoods_savings(): # this is a function used to calculate the monetary savings of using a reusable bag at whole foods for a week, year, and month
    numofbags = input('Enter the number of bags used this week\n')
    numofbags = int(numofbags)
    savings = int(5)
    savings = int(savings)
    print(numofbags*savings, 'In one Week this is how much you could have saved in cents if you switched to a resusable option. "The Last zero is ignored" .')
    print(numofbags*savings*4, 'In one Month this is how much you could have saved in cents if you switched to a resusable option. "The Last zero is ignored" .')
    print(numofbags*savings*52, 'In one Year this is how much you could have saved in cents if you switched to a resusable option. "The Last zero is ignored" .')

#need to work on being able to calculate exact decimal values and possibly converting cents to dollar amounts.
#See if its possible to have a currency placeholder and have the value typed into the sentence instead of the sentence right next to it
#work on making verything that needs to be calculated into a fucntion.
#Work on for or while loops to have program choose which function is best
National_average = ['Insert calc for national average'] # add this at the end of the straw, bags and cup function instead as a single one.
print('Welcome to the plastic footprint calc')
print()
print('This program is designed to show you how many pounds of plastic you can save yearly, monthly and weekly.')
print('This program can also show any monetary and planetary savings based on reusable choices.')
print()
print('Please select an item by typing its name. You can select straws, cups or bags.')
#put for or while loop to have the program select a function











































print('Do you use Starbucks or Wholefoods?')

def choosesavings(): #this function allows you to choose between monetary savings for starbucks or wholefoods
    if input() == 'starbucks':
        starbucks_savings()
    elif input() == 'wholefoods':
        wholefoods_savings()
    else:
        print('please select either Starbucks or Wholefoods')
        print()
        choosesavings() #





