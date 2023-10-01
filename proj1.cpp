#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

//library inclusions

void printMap(char arr[20][20]);

bool game();

int randomLocation();

int guessLocation(int a);

bool cordCompare(int xGuess, int yGuess, int xCords, int yCords);

//prototypes

void printMap(char arr[20][20])
/*
    Prints the 20x20 grid the balloon will appear on.
    did not show up for class into a list.
    :param: char arr[20][20]: a 2d array with a set size of 20 for both the rows and columns 
*/
{
  cout << "      "; //spacing for start of grid
  for(int i = 0; i < 20; i++) //the for loop runs for 19 lines to print a 20x20 grid (counting zero)
  {
    if(i >= 9)
    {
      cout << i << " ";
    }
    //the space is one less for values 9 and below so the $ signs match the single digits
    else
    {
      cout << i << "  ";
    }
    //the space is one more for values above 9 so the $ signs match the double digits
  }
    
  cout << endl;
  //spacing for new line
  for(int i = 0; i < 20; i++) //the for loop runs for 19 lines to print a 20x20 grid (counting zero)
  {
    if(i > 9)
    {
      cout << " " << i << " ";
    }
    //the space is one less for values more than 9 so the spacing matches the double digits
    else
    {
      cout << "  " << i << " ";
    }
    //the space is one more for values less than 9 so the spacing matches the single digits
    for(int j = 0; j < 20; j++)
    {
      cout << "  " << arr[i][j];
    }
    //finally each coordinate is printed for the array
    cout << endl;
    //more spacing stuff for grid to match sample
  }
}

bool cordCompare(int xGuess, int yGuess, int xCords, int yCords)
/*
    Compares the guessed coordinates by the user to the random generated coordinates by the program and tells the direction
    :param: int xGuess: the x coordinate guessed by the user
    :param: int yGuess: the y coordinate guessed by the user
    :param: int xCords: the random x coordinate generated in randomLocation
    :param: int yCords: the random y coordinate generated in randomLocation
*/
{
  if(xGuess == xCords and yGuess == yCords)
  {
    cout << "You have found the balloon" << endl;
    return true;
  }
  //returns true if the coordinates match with the guess and ends the game
  else if (yGuess < yCords and xGuess == xCords)
  {
    cout << "You didn't find the balloon" << endl;
    cout << "The balloon is east of your guess" << endl;
    return false;
  } 
  //returns false if the coordinates do not match and thus continues the game. in this case the direction would be east because the x values match while the guess is less than the random coordinate for y
  else if (yGuess > yCords and xGuess == xCords)
  {
    cout << "You didn't find the balloon" << endl;
    cout << "The balloon is west of your guess" << endl;
    return false;
  } 
  //in this case the direction would be east because the x values match while the guess is more than the random coordinate for y
  else if (xGuess > xCords)
  {
    cout << "You didn't find the balloon" << endl;
    cout << "The balloon is north of your guess" << endl;
    return false;
  }
  //in this case the direction would be north because the guess is more than the random coordinate for x
  else if (xGuess < xCords)
  {
    cout << "You didn't find the balloon" << endl;
    cout << "The balloon is south of your guess" << endl;
    return false;
  } 
  //in this case the direction would be north because the guess is less than the random coordinate for x
  return 0;
}

int randomLocation(){
/*
    Generates a random number for the coordinates of the balloon
    :return: cords, the randomly generated coordinates
*/
  int cords = rand() % 20;
  //sets 2 coordinates to random numbers from 0-20
  return cords;
  
}

int guessLocation(int a){
/*
    Takes the guess inputted by the user and stores them into x and y values
    :param: int a, an integer used in the call to get the x and y coordinates to run through the switch case 
    :return: x, the x coordinate guessed by the user
    :return: y, the y coordinate guessed by the user
*/
  int x;
  int y;
  //basic declarations
  
  switch(a)
  {
    case 1:
    {
      cout << "Where would you like to look for the balloon?" << endl;
      cout << "Enter the X coordinate (0-19): " << endl;
      cin >> x;
  
      return x;
      break;
    } //if int is 1, case 1 runs and the X value is asked for
    case 2:
    {
      cout << "Enter the Y coordinate (0-19): " << endl;
      cin >> y;
  
      return y;
      break;
    } //if int is 2 the case 2 runs and the Y value is asked for
  }
 return 0;
}

bool game(){
/*
    This program runs the game and essentially also serves as a reset for when the user wants to play again
*/
  int prompt;
  int xGuess;
  int yGuess;
  bool game = false;
  char arr[20][20];
  //declarations

  for(int i = 0; i < 20; i++)
  {
    for(int j = 0; j < 20; j++)
    {
      arr[i][j] = '$';
    }
  }
  //filling the array to make $ signs print

  srand(time(NULL));
  //setting a random time so both coordinates don’t have the same value

  int xCords = randomLocation();
  int yCords = randomLocation();
  //generates the random coordinates

  cout << "Welcome to the Surveillance Balloon Tracker" << endl;
  cout << "You are searching for the surveillance balloon" << endl;
  //welcome message 
  
  while(not game) //the while loop only runs while game is false
  {
    cout << "What would you like to do?" << endl;
    cout << "1. Display Map" << endl;
    cout << "2. Guess location of Balloon" << endl;
    cout << "3. Exit" << endl;
    cin >> prompt;
    //basic input
    if(prompt == 1)
    {
      printMap(arr);
    }
    //prints map by calling the declared array into the function
    else if(prompt == 2)
    {
      do
      {
        xGuess = guessLocation(1);
        yGuess = guessLocation(2);
      }while(xGuess > 19 or xGuess < 0 or yGuess > 19 or yGuess < 0);
      //runs the guesses simultaneously by calling with a number, which then goes to the switch case, also has input validation for the check 
      game = cordCompare(xGuess, yGuess, xCords, yCords);
      //checks the coordinates and the guesses to see if they match
      if(game == false)
      {
        arr[yGuess][xGuess] = 'G';
      }
      //if the coordinates dont match, the above return would change the map to a G by setting the specific coordinates in the array
    }
    else if (prompt == 3)
    {
      game = true;
      return 1;
    }
    //causes the game to end, and the return 1 prevents the would you like to play again prompt from reappearing
    else
    {
      cout << "Please choose again." << endl;
    }
    //input validation
  }
  return 0;
}


int main() {
  
  bool done = game(); //setting done to game so that if exit is prompted the game does not run and would you like to play again is not asked
  char replay = 'a';
  //setting a char for the input of the replay prompt
  while (not done){ //once the game has ended, this prompt stops the game from continuing on
    cout << "Would you like to play again? (y/n)" << endl;
    cin >> replay;
    //basic input
    if (replay == 'n')
    {
      done = true;
    } 
    //if input is no, the program ends as done is true
    else if (replay == 'y')
    {
      game();
    
    }
    //if input is yes, the game continues
    else 
    {
      cout << "Please choose again" << endl;
      cout << "Would you like to play again? (y/n)" << endl;
      cin >> replay;
    }
    //input validation
  }
  cout << "Thank you for using the Surveillance Balloon Tracker." 
        << endl; //end of program message
  }