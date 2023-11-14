def main():
    #Open the file `golf.txt` in read mode and create a file object ('file')
    file = open('golf.txt', 'r')
    #Read the first line from the file into the `name` variable
    name = file.readline()
    while name != '':   #Create a loop that continues as long as the 'Name' is not empty
        #Read the next line from the file into the 'score' variable
        score = file.readline()
        #Remove the newline characters('\n') from 'name' and 'score'       
        name = name.rstrip('\n')
        score = score.rstrip('\n')
        print('Name:', name)  #Print the player name
        print('Score', score) #Print the player score       
        name = file.readline()   #Read the next player`s name and score to the screen     
    file.close()  #Close the file!!!!! 
#Call the main function
main()
