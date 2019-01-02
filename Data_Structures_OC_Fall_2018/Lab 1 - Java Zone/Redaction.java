/**
 * @author Trevor Martin 
 * Date of Completion: 19 August 2018
 * Date of Edits: 1 January 2019
 * Language: Java
 */
import java.util.Arrays; //I converted the String array args into a list using .asList, which requires this package
import java.util.Scanner; //Formatted input is going to be read so a Scanner is also required

public class Redaction 
{// class name

    public static void main(String[] args)
    {// main function so that the code can be run or executed

	Scanner scanner1 = new Scanner(System.in);// the first scanner reads from system in and will read the text file
						  // <text file that you provide it

	while (scanner1.hasNextLine()) 
	{// this loop keeps going through the text file until there are no lines left to
					// go through
	    String line = new String(scanner1.nextLine()); // nextLine, or the next line, is assigned the String
							   // variable "line"

	    Scanner scanner2 = new Scanner(line);// this new scanner takes in the input of each "line"

	    while (scanner2.hasNext())// this loop keeps going through the String line until there are no words left.
				      // It uses hasNext() as opposed to hasNextLine() because it does not need to
				      // jump a line each time it scans
	    {
		String word = new String(scanner2.next());// the String variable "word" is used to capture each word in
							  // the file

		if (Arrays.asList(args).contains(word)) 
		{// the args array is converted to a list of words to be
							 // redacted and if the text file words is one of those words an
							 // "XXXXXX" is printed
		    System.out.print("XXXXXX ");
		} 
		else 
		{// if the text file word is not one to be redacted it simply gets printed as is
		    System.out.print(word + " ");
		}

	    }
	    System.out.println();

	}

    }
}