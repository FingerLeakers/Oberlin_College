
/**
 * @author Trevor Martin 
 * Date of Completion: 19 August 2018
 * Date of Edits: 1 January 2019
 * Language: Java
 */

import java.util.Random;
// To generate a number randomly, this import is required
import java.util.Scanner;
// Formatted input is going to be read so a Scanner is also required

public class HiLo {

    static Scanner scanMePlz = new Scanner(System.in);
    // This first Scanner, scanMePlz, is created outside of the Guesser method based
    // on personal preference

    public static void main(String[] args) 
    { // Main method created to execute the code

	System.out.println("This is a guessing game!" + "\n" + "\n" + "You will guess a number from 1 - 1000." + "\n"
		+ "\n"
		+ "To help you, I will tell you if you the number you guess is farther(colder) or closer(warmer) to the number I am postulating."
		+ "\n" + "\n" + "Good luck my friend!");
	// Introduces the user to the guessing game along with its rules

	Random randyBoi = new Random();
	// Creates a new random object so that a randomly generated integer between the
	// values of 1 and 1000 is created

	int generatedNum = randyBoi.nextInt(1000) + 1;
	// This integer variable holds the randomly generated number
	// The "+ 1" is there because index 1000 is the value 999 and the addition of
	// makes it so that 1000 can be a generated value too

	Guesser(generatedNum);
	// Calls the method that allows the user to guess the number

    }

    public static void Guesser(int generatedNum)
    {

	System.out.println("Please enter your best guess:");
	// Asks the user to enter an initial guess

	int count = 0;
	int trials[] = new int[count];
	// Creates a variable count that marks the user's trials and an array trials to
	// store the trials

	while (scanMePlz.hasNextLine()) 
	{ // Reads the user's input over and
					  // over again until the loop is broken

	    String guess = scanMePlz.nextLine();
	    // Scans and stores the user's input as a string(i.e. "500")

	    Scanner scanBoi = new Scanner(guess);
	    // Creates the second scanner that will be used to verify that the user's string
	    // is also an integer

	    if (scanBoi.hasNextInt()) 
	    { // This sees whether or not the input entered is an integer
		int guesS = scanBoi.nextInt(); // Creates a new variable for the integer that has just been entered
		if (guesS == generatedNum) 
		{ // This outcome breaks the loop and gives the user one of two winning
					     // messages depending on whether or not they cracked the number in 10 tries
					     // or less
		    if (count <= 10)
		    {

			count++;
			System.out.println("\nWow, you are a real madman! Only" + " " + count + " "
				+ "tries, that is true skill. Great job!");
			break;
		    }

		    if (count <= 5) 
		    {
			count++;
			System.out.println("\nYOU ARE A GOD");

		    }

		    count++;
		    System.out.println("Good job! It took you only" + " " + count + " "
			    + "trials to complete this guessing game!");
		    break;
		}

		if (guesS > generatedNum) 
		{ // This is the message for when the entered number is too high
		    System.out.println("\nThat guess is higher than my number.\nPlease try again:");
		    count++;
		    continue;
		}

		if (guesS < generatedNum) 
		{ // This is the message for when the entered number is too low
		    System.out.println("\nThat guess is lower than my number.\nPlease try again:");
		    count++;
		    continue;

		}
		continue;
	    } 
	    else
	    { // If the user did not enter a string that can be converted to an integer, this
		     // message redirects them to go again
		System.out.println("\nThe input entered was not a number, please try again:");
		count++;
		// I counted them not entering a valid input as an attempt because it did that
		// in the example

	    }

	}

    }

}
