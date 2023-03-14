
public class ArraysEmJava {
	public static void main(String[] args) {
		int[] valores = new int[10];
		
		valores[0] = 10;
		valores[1] = 22;
		valores[2] = 30;
		valores[3] = 40;
		valores[4] = 50;
		valores[5] = 60;
		valores[6] = 70;
		valores[7] = 80;
		valores[8] = 90;
		valores[9] = 100;
		
		System.out.println("O elemento 7 do Array é o número " + valores[6]);
		
		valores[6] = 700;
		System.out.println("O elemento 7 do Array é o número " + valores[6]);
		
		
		for (int i: valores) {
			System.out.print(i + " ");
		}
		
		
	}
}
