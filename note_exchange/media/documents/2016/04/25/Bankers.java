import java.util.Arrays;
import java.util.Scanner;

public class Bankers {

	static int numberOfCustomers = 3;
	static int numberOfResources = 4;
	static int[] available = new int[numberOfResources];
	static int[][] maximum = new int[numberOfCustomers][numberOfResources];
	static int[][] allocation = new int[numberOfCustomers][numberOfResources];
	static int[][] need = new int[numberOfCustomers][numberOfResources];


	public static void main(String[] args) {
	}


	public static void Input() {
		Scanner input = new Scanner(System.in);

		System.out.println("Enter allocation matrix: ");

		// Allocation Matrix
		for (int i = 0; i < numberOfCustomers; i++) {
			for (int j = 0; j < numberOfResources; j++) {
				allocation[i][j] = input.nextInt();
			}
		}

		System.out.println(Arrays.deepToString(allocation));
		System.out.println("Enter maximum matrix: ");

		// Maximum Matrix
		for (int i = 0; i < numberOfCustomers; i++) {
			for (int j = 0; j < numberOfResources; j++) {
				maximum[i][j] = input.nextInt();
			}
		}

		System.out.println(Arrays.deepToString(maximum));
		System.out.println("Enter available matrix: ");

		// Available Matrix
			for (int j = 0; j < numberOfResources; j++) {
				available[j] = input.nextInt();
			}

		System.out.println(Arrays.deepToString(allocation));

	}


	private static int[][] Need() {
		for (int i = 0; i < numberOfCustomers; i++) {
			for (int j = 0; j < numberOfResources; j++) {
				need[i][j] = maximum[i][j] - allocation[i][j];
			}
		}
		return need;
	}


	private static boolean Check(int j, int[][] array) {

		for (int i = 0; i < numberOfResources; i++) {
			if (available[i] < array[j][i])
				return false;
		}
		return true;
	}


	public static void Safe(int index, int[][] array) {

		int counter = 0;
			boolean allocated = false;
				System.out.println(Check(index, array));
				if (Check(index, array)) { // trying to allocate
					for (int k = 0; k < numberOfResources; k++)
						available[k] = available[k] - need[index][k] + maximum[index][k];
					System.out.println("Allocated process : " + index);
					counter++;
					System.out.println("\nSafely allocated");
				} else{
					System.out.println("All proceess cant be allocated safely");
				}
	}


	static void print(String string){
		System.out.println(string);
	}
}
