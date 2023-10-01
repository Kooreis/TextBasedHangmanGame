Random randGen = new Random();
var idx = randGen.Next(0, 9);
string mysteryWord = listwords[idx];
char[] guess = new char[mysteryWord.Length];
Console.Write("Please enter your guess: ");