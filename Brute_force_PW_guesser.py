import random #random generator
import pyautogui #GUI action

#Characters being used to guess password.
characters="0123456789abcdefghijklmnopqrstuvwxyz" 
#Turning our characters into a list for usage.
guess_list=list(characters) 

#Open GUI for user input.
password=pyautogui.password("Enter password here:") 

#Variable to hold the guessed password for comparsion
guess_password=''

#While loop to cycle through the guess password and compare to the actually password inputted.
while (guess_password!=password):
    #random the guess password through the list created
    guess_password=random.choices(guess_list,k=len(password))
    
    print(">>>>"+str(guess_password)+"<<<<<")
    
    #When the guessed password equals the password inputted, it will output the password.
    if (guess_password==list(password)):
        print("Your Password is: " +"" .join(guess_password))
        break #ending the loop

