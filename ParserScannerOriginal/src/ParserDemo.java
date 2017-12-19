public class ParserDemo {

	public static void main(String[] args) {
		TokenStream tStream = new TokenStream("src/prog2.jay");
		ConcreteSyntax cSyntax = new ConcreteSyntax(tStream);
		Program p = cSyntax.program();
		System.out.println(p.display());
	}
}
