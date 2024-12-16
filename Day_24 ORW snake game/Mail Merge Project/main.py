#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Day_24 ORW snake game/Mail Merge Project/Input/Letters/starting_letter.txt") as file:
    letter_lines = file.readlines()

with open("Day_24 ORW snake game/Mail Merge Project/Input/Names/invited_names.txt") as names:
    list_names = names.readlines()

for name in list_names:    
    clear_name = name.strip('\n')
    with open(f"Day_24 ORW snake game/Mail Merge Project/Output/ReadyToSend/letter_for_{clear_name}.docx", mode="a") as letter:
        for line in letter_lines:
            line_ok = line.replace("[name]",clear_name)
            letter.write(line_ok)





