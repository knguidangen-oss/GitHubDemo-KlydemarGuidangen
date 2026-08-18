#PLEASE RUN THE CODE TO SEE THE ANSWER CLEARLY AND TRY THE CODES BEFORE READING THE OTHER ANSWERS
#a. If name is “Joseph The Dreamer” and nChar is 5, what will be the output of the code above and why?
print("a.It will print the first five characters of the string on separate lines:")
print("J")
print("A")
print("M")
print("E")
print("S")
print("a.why)The loop for i in range (5) generates indices from 0 to 4. The statement print (name[i]) accesses and prints \
the character at each index one at a time")
#b. Using the same name and nChar is 20, what now is the output and why?
print("b.The code crashed saying IndexError: string index out of range. This is because the index only has 18 characters on \
which nChar = 20 is out of range. .")
#c. If there is an error message encountered in letter b, how will you be able to modify the code so that the error message will not appear.
print("c.I will make the nChad = 0 to 17 only because Joseph The Dreamer only has 18 characters")
print("="*1000)
#a. Find the syntax error and modify it.  Please identify the error and what did you do to fix it?
print("a.The error is that the nChar is not losing a letter quantity = to i in the \
for loop""print(name{0 : nChar]")
print("a.how to fix) Add a -i in the printing part to make the input lose letters per line")
#b. The code should be able to display a given name as an inverted triangle, please fix the code in order for it to do that.  See sample output below if entered name is Joseph
print("b. Try this code for the correct version")
def greet_students(name, nChar):
    for i in range(nChar):

        print(name[0 : nChar - i])

name = input("Enter a Name: ")
greet_students(name, len(name))
print("="*1000)
#a. You are tasked to create the needed function/s that will return the sum of all squared numbers from 1 to n.
print("This code sums of all the squared numbers of your input number")
def sum_of_squared(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

n = 0
while n < 1 or n > 100:
    n = input("Enter a Number from 1 to 100 : ")
    n = int(n)

print("Sum of all squared numbers is", sum_of_squared(n))