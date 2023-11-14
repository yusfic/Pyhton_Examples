3#Golf Scores
#Create main function
#Collecting data and writing it to a file for each player.
def main():
    #Prompt the user to enter the number of players
    number = int(input('Enter a number of players: '))
    #Open a file name 'golf.txt' in write mode('w')
    file = open('golf.txt', 'w')
    #Create a loop and repear the following steps for each player
    for i in range(1,number + 1):
        print('Enter data for player: ',i)
        #Enter player`s name and assign `name` variable
        name = input('Enter name: ')
        #Enter player`s score and assign `score` variable
        score = input('Enter the score: ')
        #Write the player`s name and score to the `golf.txt` file
        file.write(name + '\n')
        file.write(score + '\n')
    #Close the file!!!!!    
    file.close()
    #Display records have been written to the file
    print('Records are written to the file golf.txt')  
#Call the main function
main()


                    
    
    
