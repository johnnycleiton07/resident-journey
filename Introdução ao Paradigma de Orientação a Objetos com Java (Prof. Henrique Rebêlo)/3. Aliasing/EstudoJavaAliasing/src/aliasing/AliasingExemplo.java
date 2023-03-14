package aliasing;

public class AliasingExemplo {
	
	public static void main(String[] args) {
		int[] array1 = {1, 2, 3};
		int[] array2 = array1;
		
		System.out.println("Valor da primeira posição no Array 1: " + array1[0]);
		System.out.println("Valor da primeira posição no Array 2: " + array2[0]);
		
		array1[0] = 9;
		
		System.out.println("Após alteração:");
		System.out.println("Valor da primeira posição no Array 1: " + array1[0]);
		System.out.println("Valor da primeira posição no Array 2: " + array2[0]);
	}
	
}
