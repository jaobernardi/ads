package space.jaobernardi.upf.ads.oop.swing;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;

import space.jaobernardi.upf.ads.oop.swing.structures.Menu;
import space.jaobernardi.upf.ads.oop.swing.structures.Person;

public class App {
    private static JFrame jFrame;
    public static JTabbedPane tabbedPane = new JTabbedPane();
    public static JPanel jPanel = new JPanel();
    public static void main( String[] args ) {
        System.out.println( "App Swing  -  @jaobernardi - ADS UPF OOP - 10.2022" );
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                //Turn off metal's use of bold fonts
                UIManager.put("swing.boldMetal", Boolean.FALSE);
                initSwing("title");
            }
        });


    }

    private static void joinComponents() {
        return;
    }

    private static void initSwing(String window_title) {
        jFrame = new JFrame(window_title);
        jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jFrame.setSize(300,300);
        jPanel.add(tabbedPane);
        tabbedPane.setTabLayoutPolicy(JTabbedPane.SCROLL_TAB_LAYOUT);
        Menu menu = new Menu();
        menu.addToPane(tabbedPane);
        jFrame.add(tabbedPane);
        jFrame.pack();
        jFrame.setVisible(true);

    }


    public static JFrame getJFrame() {
        return jFrame;
    }


}
