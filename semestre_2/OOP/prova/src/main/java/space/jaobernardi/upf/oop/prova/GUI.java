package space.jaobernardi.upf.oop.prova;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;

import space.jaobernardi.upf.oop.prova.structures.Menu;


public class GUI extends Console {
    private static JFrame frame;
    private static JTabbedPane tabbed;

    public static void createGUI() {
        frame = new JFrame("Calculadora de Pressão");
        frame.setSize(850,350);
        tabbed = new JTabbedPane();
        frame.add(tabbed);
        Menu menu = new Menu(tabbed);
        menu.register();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        
    }
    public static void main(String[] args) {
        imagineData();
        createGUI();
    }
    
}
