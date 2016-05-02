import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Customers implements Runnable {

	static Bankers bank = new Bankers();
	static List<Customers> workers;
	public boolean isRunning = false;
	static Random random = new Random();
	static int[][] request;

	public Customers() {
		Thread thread = new Thread(this);
		thread.start();
	}

	public static void main(String[] args) throws InterruptedException {

		Bankers.Input();
		workers = new ArrayList<Customers>();
		request = new int[bank.numberOfCustomers][bank.numberOfResources];

		for (int i = 0; i < bank.numberOfCustomers; i++) {
			workers.add(new Customers());
		}

		for (Customers worker : workers) {
			while (worker.isRunning) {
				Thread.sleep(100);
			}
		}
	}


	@Override
	public void run() {

		System.out.println("Current thread id: " + Thread.currentThread().getId());

		this.isRunning = true;
		this.isRunning = false;

		int counter = 0;
		boolean complete[] = new boolean[bank.numberOfCustomers];

		while (counter < 1)
			if (Thread.currentThread().getId() == 11) {
				int process = 0;
				boolean allocated = false;
				for (int i = 0; i < bank.numberOfCustomers; i++) {
					for (int k = 0; k < bank.numberOfResources; k++) {
						request[i][k] = random.nextInt(3 - 1) + 1;
					}
				}
				try {
					if (request_resources(process, request) == 0) {
						allocated = complete[process] = true;
					} else {
					}
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				counter++;
			} else if (Thread.currentThread().getId() == 12) {
				int process = 1;
				boolean allocated = false;
				for (int i = 0; i < bank.numberOfCustomers; i++) {
					for (int k = 0; k < bank.numberOfResources; k++) {
						request[i][k] = random.nextInt(3 - 1) + 1;
					}
				}
				try {
					if (request_resources(process, request) == 0) {
						allocated = complete[process] = true;
					} else {
					}
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				counter++;
			} else {
				int process = 2;
				boolean allocated = false;
				for (int i = 0; i < bank.numberOfCustomers; i++) {
					for (int k = 0; k < bank.numberOfResources; k++) {
						request[i][k] = random.nextInt(3 - 1) + 1;
					}
				}
				try {
					if (request_resources(process, request) == 0) {
						allocated = complete[process] = true;
					} else {
					}
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				counter++;
			}

		try {
			// Sleep zzzzzzzz
			Thread.sleep(1000);
		} catch (InterruptedException e) {
		}
	}


	Mutex mutex = new Mutex();


	@SuppressWarnings("finally")
	public int request_resources(int p, int[][] array) throws InterruptedException {

		if(mutex.available == true){
			mutex.acquire();
			try {
				Bankers.Safe(p, array);
			} finally {
				mutex.release();
				return 0;
			}
		}else{

		}
		return -1;
	}
}
