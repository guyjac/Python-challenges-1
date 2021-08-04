"""
ass1.py
CE151 assignment 1 template
created by sands 30/10/10
modified by sands 28/10/11 - number of exercises changed
modified by sands 28/10/16 - number of exercises changed, example added
"""

from math import sqrt
from math import acos
from math import asin
from math import degrees


def ex0():
    """
    example
    use 8 at exercise selection prompt in my code to select it
    """
    i = int(input("Enter a non-negative integer: "))
    if i<0:
        print("Negative numbers do not have real square roots")
    else:
        root = sqrt(i)
        print("The square root is", round(root, 2))
        
def ex1() :
    """
    exercise 1
    """
    print("This program will calcualte the height of a triangle")
    width = float(input("Please enter a width"))
    length = float(input("Please enter a length"))
    #3=opposite(width) 4=adjacent(length) 5=hypot(height)
    height = float
    hypotenuse = float
    sin = float
                   
    if width > length:
        print("Invalid length detected. The width cannot be greater than the length.")
        ex1()
    else:

        #calculate the hypotenuse by adding together the SQUARE of length AND width
        hypotenuse = ( (length * length) + (width  * width) )

        #calculates the sqrt of the hyp, which is the length of the third side. we use a new var incase we need hyp again
        height = ( sqrt(hypotenuse) )

        #prints the three lengths.. so the user can see what they input
        print (format ("Length","<8s") + format("Width","<8s") + format("Height","<8s") )
        print (format (length, "<8.4") + format(width, "<8.4") + format(height, "<8.4") )
       
        #calculates the sin
        sin = ( asin(width/height) )

        #the last angle is always 90... but it's good practice to calcuate it accuratley...
        
        print (format ("Angle 1","<8s") + format("Angle 2","<8s") + format("Angle 3","<8s") )
        print (format ((degrees(sin) ), "<8.4") + format(90-(degrees(sin)), "<8.4") + format (180- (90- (degrees(sin)) ) -(degrees(sin) ), "<8.4"))
      
def ex2() :
    """
    exercise 2
    """
    print("-- Fibonacci calculator --")
    count = int(input("How many sequences do you want (int)? "))

    #declare fib vars
    fibonacci1 = 0
    fibonacci2 = 1
    fibonacciString=""
	
    while count >= 1:
     
        #concatinate the sequence into a string
        fibonacciString = fibonacciString + str(fibonacci1)+" "
        #easier to use a tuple and more efficient / clean
        fibonacci1, fibonacci2 = fibonacci2, fibonacci1 + fibonacci2

        count = count -1

    print (fibonacciString)
    
def ex3() :
    """
    exercise 3
    """
    rows = int(input("Please enter the desired rows: "))
    columns = int(input("Please enter the desired columns: "))
    highest_value = (rows ** columns)  
    n = 1
    m = 1
    counter_rows = 0
    counter_columns = 1
    output = ""
    max_digits = len(str(highest_value)) + 1
    
    while counter_columns <= columns:
        while counter_rows < rows:
            m = (n * m)         
            #join the string together
            output = output + format(str(m), ">" + str(max_digits) + "s")
            counter_rows += 1
        print(output)
        counter_rows = 0
        counter_columns += 1
        output = ""
        #makes N the same as the column counter (since its 1,2,3,4,5...)
        n = counter_columns
        #M is reset to 1 for multiplication
        m = 1

def ex4() :
    """
    exercise 4
    """
    userWord = input(("Please enter a string: "))
    splitWord = userWord.split()
    longestWord = 0
    longWordVal = ""
    smallestWord = 0
    smallWordVal = ""
	
    for word in splitWord:
        if len(word) > longestWord:
            longestWord = len(word)
            longWordVal = word
        if len(word) <= smallestWord:
            smallestWord = len(word)
            smallWordVal = word
        elif smallestWord == 0:
            smallestWord = len(word)
            smallWordVal = word
        print(word)
        
    print("The longest word,", "'" + longWordVal+ "'," , "was", longestWord, "character(s) long")
    print("The smallest word,", "'" + smallWordVal + "',", "was", smallestWord, "character(s) long")
    
def ex5() :
    """
    exercise 5
    """
    
    vowelSentence = input(("Please enter a sentence: "))
    vowelList = list(vowelSentence.lower())
    charList = ["a","e","i","o","u"]
    charCount = [0,0,0,0,0]
    maxCharIndex = 0
    lettersFound = ""
    n = 0
    p = 0

    #Loop over every letter in a word. 
    #For each letter, loop over the vowels (this can be improved if we just check if its in the vowels, but for now I will leave it as a loop).
    #If a vowel is found, increment its count. 
    #Reset which vowel we are on, when we iterate onto the next letter. (thus we can loop through all the vowels agian for the next letter)
    for letter in vowelList:
            while n <= 4:
                if letter == charList[n]:
                    charCount[n] = charCount[n] + 1
                    n +=1
                else:
                    n +=1  
            n=0

    maxCharCount = max(charCount)
    maxCharIndex = charCount.index(max (charCount) )
    
    if maxCharCount > 0:
        while p <= 4:    
            if charCount[maxCharIndex] == charCount[p]:
                lettersFound = lettersFound  + (charList[p]) + ", "
            p += 1 
        print("The vowel(s) that occurred the most was", lettersFound, "which occurred", maxCharCount, "times")
    else:
        print("No vowels were found")
        
    
def ex6() :
    """
    exercise 6
    """
    
    encryptString = input(("Please enter a string to be encrypted or decrypted: "))
    key = int(input("Please enter a key (int): "))
    encryptArray = []
    cryptCounter = 0
    asciiChar = 0
    cryptedStr = ""

    #check to make sure its only CAPS letters
    if len( [chars for chars in encryptString if not (chars.isalpha() or chars.isspace() ) ] ):
        print("Please enter a string with only capital letters")
    elif len ([chars for chars in encryptString if (chars.islower() or chars.isdigit())]):
        print("Please enter a string with only capital letters")
    else:

        #make the string into an array
        charList = list(encryptString)
        
        for letters in charList:
            if (ord(letters)) != 32:
                #32 is a space which we dont care about encrypting.
                asciiChar = (((ord(letters)) - 65 + key)%26)+65
            else:
                asciiChar = (ord(letters))
            encryptArray.append(asciiChar)
            cryptCounter +=1
            
        for i in range(0, len(encryptArray)):
            cryptedStr =cryptedStr+chr(encryptArray[i])

        print(cryptedStr)
        
def uprightTriangle(char1,uWidth,listed,line,arr) :
	#character, width of base triangle, output to list?, additional lines(force line down),list
        spacer = 0
        #height of triangle (counter is width+1 /2)
        counter1 = (uWidth+1)/2
        listCtr = 0
        pyramidStr = ""
        
        while counter1 >= 1:
            pyramidStr = (char1 * (uWidth - spacer))
            spacer += 2
            counter1 -=1
            if listed == True:
                try:
                    arr[listCtr+int(line)] = arr[listCtr+int(line)] + pyramidStr
                except:
                     arr.append(pyramidStr)
                listCtr += 1
            else:
                pyramidStr = pyramidStr.center(uWidth)
                print (pyramidStr)

def downsideTriangle(char2,width,listed,line,arr):
    #character, width of base triangle, output to list?, additional lines(force line down), list
    spacer = 1
    counter1 = 0
    listCtr = 0
    pyramidStr = ""
    
    while counter1 < width:
        pyramidStr = char2 * (spacer)
        counter1 += 2
        spacer += 2

        if listed == True:
            try:
                arr[listCtr+int(line)] = arr[listCtr+int(line)]+ pyramidStr
            except IndexError:
                arr.append(pyramidStr)
            listCtr += 1
        else:
            pyramidStr = pyramidStr.center(width)
            print (pyramidStr)    
def ex7() :
    """
    exercise 7
    """
    char1 = input(("Please specify a char: "))
    char2 = input(("Please specify a 2nd char: "))
    uWidth = int(input("Please specify a width"))
    level2 = []
    trianglePrint = ""

    #level 1
    if uWidth %2 == 0:
        print("You must enter an odd number")
    else:
        #level1
        print ("level 1")
        uprightTriangle(char1,uWidth,False,0,level2)

        #level2
        print("Level 2")
        downsideTriangle(char2,uWidth,True,0,level2)
        downsideTriangle(char2,uWidth,True,(uWidth/2)+1,level2)
        uprightTriangle(char1,uWidth,True,(uWidth/2)+1,level2)
        downsideTriangle(char2,uWidth,True,(uWidth/2)+1,level2)

        #print the level2 triangle
        for i in range(len(level2)):
            trianglePrint = level2[i]
            trianglePrint = trianglePrint.center((uWidth*2)+1)
            print (trianglePrint,sep="")

        #print("Level 3")
        level2 = []
        print("Level 3")
        #character, width of base triangle, output to list?,(triangles per line), additional lines, list
        uprightTriangle(char1,(uWidth*2)+1,True,0,level2)
        downsideTriangle(char2,uWidth,True,0,level2)
        downsideTriangle(char2,uWidth,True, ((uWidth+1)/2),level2)
        uprightTriangle(char1,uWidth,True,((uWidth+1)/2),level2)
        downsideTriangle(char2,uWidth,True, ((uWidth+1)/2),level2)
        uprightTriangle(char1,(uWidth*2)+1,True,0,level2)
        uprightTriangle(char1,(uWidth*2)+1,True,(uWidth*2),level2)    
            
        for i in range(len(level2)):
            trianglePrint = level2[i]
            trianglePrint = trianglePrint.center((uWidth*5))
            print (trianglePrint,sep="")
            

# modify the following line so that your name is displayed instead of Lisa's
print("CE151 assignment 1 - Guy Jacobs")

# do not modify anything beneath this line
exlist = [None, ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex0]
running = True
while running :
    line = input("Select exercise (0 to quit): ")
    if line == "0" : running = False
    elif len(line)==1 and "1"<=line<="8": exlist[int(line)]()
    else : print("Invalid input - try again")


