/**
 * @author Trevor Martin 
 * Date of Completion: 19 August 2018
 * Date of Edits: 1 January 2019
 * Language: Java
 */

// A scanner is not necessary given that the height is a command-line argument

public class Pyramids 
{

    // This is our class - Pyramids - and is where everything is going to occur

    public static void main(String[] args)
    {
	// The main method allows the "*" pyramid to be executed

	System.out.println("The height you entered is:" + args[0]);
	// This just tell the user the height they entered so they remember it

	if (args[0].length() > 3) 
	{
	    System.out.println("Please enter a value for the height that does not exceed a length of 3");
	    System.exit(1);
	}
	// This if statement stops the program if a value with a length > 1 was entered
	// as a command line argument
	// and informs the user that the value they entered was too long

	int userHeight = Integer.parseInt(args[0]);

	// This creates a new variable userHeight that convert the String command-line
	// argument into an integer

	Egyptian(userHeight);

	// Here the method Egyptain is called with the parameter of the height that the
	// user entered

    }

    public static void Egyptian(int userHeight)
    {
	// This name suits this method well; Egyptians were excellent Pyramid builders.
	// Also, this method take in the parameter that is the height entered by the
	// user

	for (int i = 0; i < userHeight; i++) 
	{
	    // This first for loop goes over each of the rows in the pyramid-to-be

	    for (int space = 0; space <= (userHeight - (i + 1)); space++)
	    {
		System.out.print(" ");
		// This second for loop is for generating spaces before each *; the range for
		// the number of spaces was found in PreLab
	    }
	    for (int stars = 0; stars < ((i * 2) + 1); stars++) 
	    {
		System.out.print("*");
		// This third for loop is for generating the *'s for each row and uses another
		// equation from PreLab 1
	    }

	    System.out.print("\n");
	    // Finally, we want there to actually be distinct rows instead of a list of *'s,
	    // this can be done by \n which makes a new line
	}

    }
}
