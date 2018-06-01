import java.util.Scanner;

public class Student extends Thread
	{
	
	private String name;
	private String address;
	private int percent;
	public void run() {
		/*Scanner sc = new Scanner(System.in);
		System.out.println("Please enter your name: ");
		name = sc.nextLine();
		System.out.println("Please enter your address: ");
		address = sc.nextLine();
		System.out.println("Please enter your percentage ");
		percent = sc.nextInt();
		System.out.println("Thank you for sharing your details :)");*/
		
		try {
			System.out.println(Thread.currentThread().getId());
		}
		catch(Exception e) {
			System.out.println("Exception is caught!");
			
		}
	}
	
	public void showDetails() {
		
		System.out.println("Name :"+name+"\t Address: "+address+"\t Percent :"+percent);
	}

}
