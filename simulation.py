import sys

#this is my funtion to check if the type of the variable you entered is correct
def type_validation(type, variable):
    if type == "string":
        try:
            variable = str(variable)
            return variable
        except:
            print("float, float, int, filename.txt")
            exit()
    elif type == "integer":
        try:
            variable = int(variable)
            return variable
        except:
            print("float, float, int, filename.txt")
            exit()
    elif type == "float":
        try:
            variable = float(variable)
            return variable
        except:
            print("float, float, int, filename.txt")
            exit()


#taking my initial values from the command line, validating, and organizing them into type set variables
initial_population = type_validation("float", sys.argv[1])

#checking to see if "initial_population" is greater than 0 and less than 1
if 0 > initial_population or initial_population > 1:
    print("enter a value between 0 and 1 for the first argument")
    exit()

growth_rate = type_validation("float", sys.argv[2])

#checking to see if "growth_rate" is greater than 0 and less than 4
if 0 > growth_rate or growth_rate > 4:
    print("enter a value between 0 and 4 for the second argument")
    exit()

iterations = type_validation("integer", sys.argv[3])

#checking to see if "iterations" is positive
if iterations < 0:
    print("you need to have a positive number of iterations for the thrid argument")
    exit()

output_file = type_validation("string", sys.argv[4])

#setting up my variable for chekcing the strings filetype
length = len(output_file)
output_file_checker = output_file[length - 4:]

while output_file_checker != ".txt":
    print("make sure its a .txt file for the fourth argument")
    exit()
#done checking variables

#initializing other variables and lists that don't need to be validated
current_population = initial_population
population_counter = []

#setting my output file object
file1 = open(output_file, "w")

#inserting the initial value into my list with correct formatting
population_counter.insert(0, "0\t" + str(f"{initial_population:.3f} \n"))

#logistic equation function 
def logistic_equation(current_population) :
    current_population = growth_rate * current_population * (1- current_population)
    return current_population

#my main for loop to run through all the iterations
for x in range(1, iterations + 1):

    current_population = logistic_equation(current_population)

    population_counter.insert(x, str(x) + "\t" + str(f"{current_population:.3f} \n"))

#writing my list "population_counter" to my file
file1.writelines(population_counter)
file1.close