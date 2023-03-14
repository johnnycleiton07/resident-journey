import java.util.ArrayList;

public class ArrayListJava {
	
	public static void main(String[] args) {
		
		
		ArrayList<String> listaDeFrutas = new ArrayList<>();
		
		listaDeFrutas.add("Maça");
		listaDeFrutas.add("Abacaxi");
		listaDeFrutas.add("Mamão");
		
		for (String i : listaDeFrutas) {
			System.out.println(i);
		}
	}

}
