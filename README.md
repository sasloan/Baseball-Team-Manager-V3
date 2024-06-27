# Baseball-Team-Manager-V3


Team Management Program: Part 3
Convert the Baseball Team Manager program from procedural to object-oriented. This doesn’t change what the code does; it makes the code more modular, reusable, and easier to maintain. Follow the three tier architecture design principles of separating presentation, business logic, and data functionality . 
Sample Console Output

================================================================
                   Baseball Team Manager

CURRENT DATE:    2022-07-12
GAME DATE:       2022-07-19
DAYS UNTIL GAME: 7

MENU OPTIONS
1 – Display lineup
2 – Add player
3 – Remove player
4 – Move player
5 – Edit player position
6 – Edit player stats
7 - Exit program

POSITIONS
C, 1B, 2B, 3B, SS, LF, CF, RF, P
================================================================ 
Menu option:  1
   Player                                POS    AB     H     AVG
----------------------------------------------------------------
1  Dominick Gilbert                       1B   545   174   0.319
2  Craig Mitchell                         CF   533   127   0.238
3  Jack Quinn                             RF   535   176   0.329
4  Simon Harris                            C   485   174   0.359
5  Darryl Moss                            3B   532   125   0.235
6  Grady Guzman                           SS   477   122   0.256
7  Wallace Cruz                           LF   475   138   0.291
8  Cedric Cooper                          2B   215    58   0.270
9  Alberto Gomez                           P   103    21   0.204

Menu option:

Specifications
•	Use a Player class that provides attributes that store the first name, last name, position, at bats, and hits for a player. The class constructor should use these five attributes as parameters. This class should also provide a method that returns the full name of a player and a method that returns the batting average for a player.
•	Use a Lineup class to store the lineup for the team as a private list attribute. This class must include the following methods (with parameters) to modify the private list attribute:  add player (player object), remove player (lineup number), get player(lineup number), and move player(old lineup number, new lineup number).  The add method will add a new player to the end of the list. The remove and get methods require the lineup location of the targeted player as a parameter and both methods will return the player object at the specified location; the only difference is that the get method will not delete the object from the list attribute. In addition the class must include an iterator so that the lineup object can be used in a for loop.
•	Use a file named objects to store the code for the Player and Lineup classes.
•	Use a file named ui to store the code for the user interface. This is the existing code from the main module in projects #1 and #2. Rename the existing module and refactor the code to use a Lineup object instead of a list of dictionaries (project #2) or a list of lists (project #1). Modify the code to separately ask the user for both the first name and last so that the two inputs can be used when creating a player object.
•	Use a file named db to store the two functions that read from and write to the file that stores the data. These functions should use the same names used in the previous project. The function that reads the file does not use a parameter and returns a lineup object which holds the player objects that are created when the data is read from the given players.txt file. A lineup object is used as the parameter for the function that writes the data to the file. 



Submission details
Projects can require the use of material from any of the previous chapters covered in the textbook.
Create a Team Management Python program that satisfies the specifications above. 
Put General Comments at the beginning of the project that includes (1) your name, (2) the project name, (3) the date, and (4) a description of the project. 
Turn in a ZIP file of the final version of the program. Include a Word document which contains output of the testing done on the program. The Word document must be inside the ZIP file.
In the Comments section on the Assignment webpage, report (A) an estimate of the time it took to complete the project. Report a single value in minutes, and (B) a single rating of the project, on an ordinal scale, as either (1) Easy, (2) Moderate, (3) Hard, OR (4) Challenging. 
