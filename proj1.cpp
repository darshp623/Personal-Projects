#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;

//library inclusions                                                                                                                       

const int WORDSINFILE = 9578;
const int MINGUESSLETTERS = 3;
const int ASCII = 256;
const int MINSTARTLETTERS = 8;
const string PROJ1_DATA = "proj1_data.txt";
//declaring constants                                                                                                                      


void loadFile(string fileArray[WORDSINFILE]);
string startingWord(string fileArray[WORDSINFILE]);
bool checkGuess(string fileArray[WORDSINFILE], string word);                                                                                                            
string getInput(string word);
bool isAnagram(string word, string input);
bool checkValid(string fileArray[WORDSINFILE], string input);
int totalAnagrams(string fileArray[WORDSINFILE], string input);
//prototypes                                                                                                                               

void loadFile(string fileArray[WORDSINFILE])
{
  int count = 0;
  //basic declarations                                                                                                                     
  ifstream file;
  //allows for the reading of the data in the file                                                                                         
  file.open(PROJ1_DATA);
  //opens the data file containing the ingredients and their recipes                                                                       
  if (file.is_open())
  //only executes IF the file opens                                                                                                        
  {                                                                                                                                                                                                                                             
    while(file >> fileArray[count])
    {                                                                                                       
      count++;                                                                                                                             
    }                                                                                                                                      
  }
  file.close();
  //closes the file                                                                                                                        
}

string startingWord(string fileArray[WORDSINFILE]){

  int randomWord = 0;
  randomWord = rand() % WORDSINFILE;
  string start = fileArray[randomWord];
  if(start.length() < MINSTARTLETTERS)
  {
    while (start.length() < MINSTARTLETTERS)
    {
      randomWord = rand() % WORDSINFILE;
      start = fileArray[randomWord];
    }
  }
  //sets a word using the value assigned from 0-9578                                                                                       
  return start;

}

string getInput(string word)
{
  string input;
  //int anagrams_full;                                                                                                                     
  int counter = 0;
  cout << "Welcome to UMBC Anagrammer!" << endl;
  cout << "There are blank anagrams available in this puzzle" << endl;
  cout << "Startng word is:" << word << endl;
  cout << "What word would you like to try?" << endl;
  cin >> input;
  if(word.length() > MINGUESSLETTERS)
  {
    counter++;
  }
  else if(word.length() < MINGUESSLETTERS)
  {
    while(word.length() < MINGUESSLETTERS or counter != totalAnagrams(fileArray, input))                                                                 
    {
      cout << "Minimum of 3 characters." << endl;
      cout << "You have guessed" << counter << "of blank" << "anagrams available." << endl;
      cout << "What word would you like to try?" << endl;
    }
  }
  return input;
}

bool isAnagram(string word, string input)
{
  int asciiTable[ASCII];
  // Initialize the array with values from 0 to 255                                                                                        
  for (int i = 0; i < ASCII; i++)
  {
    asciiTable[i] = i;
  }
  if (input.length() > word.length())
  {
    return false;
  }
  for (int i = 0; i < word.length(); i++)
  {
    char holder = word.at(i);
    asciiTable[holder]++;
  }
  for (int i = 0; i < input.length(); i++)
  {
    char holder = input.at(i);
    if(asciiTable[holder] <= 0)
    {
      return false;
    }
  }
  return true;
}

int totalAnagrams(string fileArray[WORDSINFILE], string input)
{
  int counter = 0;
  for (int i = 0; i < WORDSINFILE; i++)
  {
    if(isAnagram(input, fileArray[i]))
    {
      counter++;
    }
  }
  return counter;
}


bool checkValid(string fileArray[WORDSINFILE], string input)
{
  int anagrams_full = 70;
  int counter = 0;
  string checkWord[anagrams_full];
  for (int i = 0; i < anagrams_full; i++)
  {
    if(input == fileArray[i])
    {
      checkWord[counter] = input;
      counter++;
      return true;
    }
  }
  return false;
}

bool checkGuess(string fileArray[WORDSINFILE], string word)                                                                                                             
{                                                                                                                                          
  int anagrams_total = totalAnagrams(fileArray, word);
  int counter = 0;
  string checkWord[anagrams_total];
  for (int i = 0; i < WORDSINFILE; i++)
  {
    if(input == fileArray[i])
    {
      checkWord[counter] = input;
      counter++;
    }
  }
  for (int i = 0; i < anagrams_total; i++)
  {
    if (input == checkWord[i])
    {
      cout << "You already guessed that word" << endl;
      return true;
    }
  }              
  return false;                                                                                                                                                                                                                                                         
}                                                                                                                                          

// check if the word is in the list, if it is add it to a new array, then if they guess it again and its already in the array, say its alr\
esdy been guessed                                                                                                                          
int main(){
  srand(time(NULL));
  string fileArray[WORDSINFILE];
  loadFile(fileArray);
  string startWord = startingWord(fileArray);
  string guess = getInput(startWord);
  checkValid(fileArray, startWord);
  checkGuess(guess);                                                                                                                   
}
