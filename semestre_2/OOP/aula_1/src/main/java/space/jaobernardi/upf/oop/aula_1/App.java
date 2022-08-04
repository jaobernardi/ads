package space.jaobernardi.upf.oop.aula_1;

import java.util.logging.Logger;

import space.jaobernardi.upf.oop.aula_1.utils.Input;

public class App  {
    public static void main( String[] args ) {
        System.out.println( "Hello World!" );
        String input = Input.getStringInput("Teste: ");
        System.out.println("Input: " + input);
    }
}
