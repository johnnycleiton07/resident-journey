
public class IncrementoEDecrementoEmJava {
	public static void main(String[] args) {
		
		int variavel = 10;
		
		/* adiciona 1 ao valor de x, armazena o resultado em x, e retorna o valor original*/
		System.out.println(variavel++); 
	    System.out.println(variavel);
		
	    /* adiciona 1 ao valor de x, armazena o resultado em x, e retorna o novo valor incrementado*/
		System.out.println(++variavel); 
	    System.out.println(variavel);
	    
	    
	    /* subtrai 1 do valor de x, armazena o resultado em x, e retorna o valor original*/
	    System.out.println(variavel--); 
	    System.out.println(variavel);

	    /* subtrai 1 do valor de x, armazena o resultado em x, e retorna o novo valor decrementado*/
	    System.out.println(--variavel); 
	    System.out.println(variavel);
	}

}
