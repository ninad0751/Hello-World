import java.util.*;
import java.io.*;
import java.util.regex.*;
public class Hello {
	
	
	public static void main(String args[]) {
	String word = "abcDeee334326hgf";
	System.out.println(word.replaceAll("abcDee", "x"));
	System.out.println(word.replaceAll("[ab][c]", "x"));
	for(int i=0; i <=5 ; i++)
	{
	Student a = new Student();
	a.start();
	}
	//a.showDetails();
	LinkedList<String> obj = new LinkedList<String>();
	obj.add("India");
	obj.add("Nice");
	obj.addFirst("Pakistan");
	System.out.println(obj);
	
	boolean country = obj.contains("India");
	if(country) {
		
		System.out.println("List contains India");
	}
	else {
		System.out.print("Nope no India in the list");
	}
	
	
	}
	
	
	
	

}
