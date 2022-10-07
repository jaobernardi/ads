package space.jaobernardi.upf.oop.prova;

import java.util.ArrayList;
import java.util.Random;
import java.util.logging.Logger;

import space.jaobernardi.upf.oop.prova.structures.Pressao;

public class Console  {
    private static ArrayList<Pressao> data = new ArrayList<Pressao>();

    public static void imagineData() {
        Random rand = new Random();
        for (int i = 0; i < 3; i++) {
            data.add(
                new Pressao(
                    rand.nextInt(1000),
                    "Pressao Imaginária",
                    (double) rand.nextInt(140),
                    (double) rand.nextInt(90)
                )
            );
        }
    }
    public static boolean add(Pressao pres) {
        return data.add(pres);
    }
    public static void main( String[] args ) {
        imagineData();
        for(Pressao pres : data) {
            System.out.println("[!] ID: "+pres.getID()+" Nome: "+pres.getNome()+" PAD: "+ pres.getPAD()+" PAS: "+pres.getPAS()+" Interpetacao: "+pres.getInterpretacao());
        }
        
    }
}
