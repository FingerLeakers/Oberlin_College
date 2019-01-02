/**
 * @author Trevor Martin 
 * Date of Completion: 19 August 2018
 * Date of Edits: 1 January 2019
 * Language: Java
 */

import java.util.ArrayList;
import java.util.Scanner;

public class BenfordAnalysis 
{// our class is Benford Analysis, let's go!

    public static void main(String[] args)
    {// make the main to execute some code baby
	System.out.println("This is my Benford Analysis Program. Unrelated, but I hope you are having a nice day.");// tells
														    // the
														    // user
														    // what
														    // we're
														    // about
														    // to
														    // do
	Scanner scanner1 = new Scanner(System.in);// declare the first scanner that will read the file
	ArrayList<Integer> firstDigitCounter = new ArrayList<Integer>();// declare our digit counter array list
	for (int i = 0; i < 10; i++)
	{// let's give this ArrayBoi some digits, from 0-9
	    firstDigitCounter.add(0);
	}
	System.out.print("\nBefore the analysis here is the current digit counter\n" + firstDigitCounter + "\n" + "\n");
//show the user that their array list is empty
	int totalCount = 0;// we gotta make a total count for later when we find the F R E Q U E N C Y

	while (scanner1.hasNextLine()) 
	{// this loop goes through the file, see how it calls scanner1
	    String line = scanner1.nextLine();// this string "line" will capture each line of the file that goes through
					      // the scanner
	    Scanner scanner2 = new Scanner(line);// this new scanner...scanner2, you're probably thinking how original,
						 // but this helps me out...reads the words in each lines

	    while (scanner2.hasNext())
	    {// let's loop loop loop lopp through those words
		String word = new String(scanner2.next());// capture the words!
		char firstThing = word.charAt(0);// let's make the first letter or number a character called firstThing
		if (Character.isDigit(firstThing)) 
		{// if that firstThing character is a digit...
		    String firstNum = new String(word.substring(0, 1));// then we call that digit firstNum and cut it
								       // out into a string using substring
		    int firstDigit = Integer.parseInt(firstNum);// we need that number as a int so then let's parse that
								// shit

		    int count = firstDigitCounter.get(firstDigit);// create a count variable and set it equal to that
								  // digit that was entered
		    int countNew = count + 1;// increase the count of that digit by 1 for each occurrence of it
		    firstDigitCounter.set(firstDigit, countNew);// set that new number in the digit holder
		    totalCount++;// total count goes up by 1 for each count

		}

	    }

	}

	System.out.print("\nAfter the analysis here is the current digit counter\n" + firstDigitCounter + "\n" + "\n");// show
														       // them
														       // how
														       // the
														       // counter
														       // changes

	int maxCount = 0;// make our maxCOunt for finding the star number later

	for (int j = 0; j < firstDigitCounter.size(); j++)
	{// go through the array list

	    int digit = firstDigitCounter.get(j);// a digit is equal to the count at a slot in the list

	    if (digit > maxCount) {// if that count is greater than 0 or the previous maxCOunt
		maxCount = firstDigitCounter.get(j);// set that slot as the maxCounter
	    }

	}

	float frequencyMax = (((float) maxCount / totalCount) * 100);// use your new maxCount to find the max Frequency
								     // for the stars later on

	for (int i = 0; i < firstDigitCounter.size(); i++)
	{// go through each slot in the array list

	    int digit2 = firstDigitCounter.get(i);// get the value in single slot

	    int number2 = i; // get the slot index

	    float frequency = (((float) digit2 / totalCount) * 100); // get the individual frequency for an index

	    System.out.printf(" %d: %8d %4.3f%% : ", number2, digit2, frequency); // print that out girl

	    if (digit2 > 0) // if we got some counts on a digit
	    {
		int relFreq = ((50 * Math.round(frequency)) / Math.round(frequencyMax));// modulate the stars relative
											// to the max frequency
		for (int k = 0; k < relFreq; k++) 
		{// print the number of stars for that relative frequency
		    System.out.print("*");

		}

	    }
	    else if (digit2 == 0)
	    {
		System.out.print("No Stars");
	    }

	    System.out.println();// get me a new line!
	}

    }

}
