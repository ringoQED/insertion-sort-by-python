import os

#Define and initialize index and array
i = 0
j = 0
arr = []
tmpInput = ""

#Define the greeting message
msg_1 = "*******************************"
msg_2 = "*      Sorting Algorithm      *"
msg_3 = "*******************************\n"

os.system('clear')  #Clear the terminal screen. Change to 'cls' if using Windows

print( msg_1 )
print( msg_2 )
print( msg_3 )

#Prompt input and insert into array
while True:
        
    tmpInput = input("Input a no.(Press Enter to sort): ")

    #Force user to input a number
    try:
        arr.append( float( tmpInput ) )
    except ValueError:
        if not(tmpInput == ""):
            print("Please enter a number!")

    if tmpInput == "":
        break

if ( len( arr ) == 0 ):     #Check if there are any numbers to sort. If not, exit the program
    print("No numbers to sort. Exiting...")
    exit()
    
print("Numbers before sorting: ", arr, "\n")

#Loop thru' the array and sort the nos.
while i < len( arr ):
    
    j = 0   #Reset j to 0 to count from the start of array
    while j < len( arr ):
        #Compare the nos. and swap them if not in order
        if ( i < j ) and ( arr[i] > arr[j] ):
            arr.insert(i, arr[j])    #Insert the no. at position j to position i
            arr.pop( j + 1 )             #Remove the original no. after insert

        j += 1
    i += 1

print("Numbers after sorting: ", arr, "\n")

