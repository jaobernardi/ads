package space.jaobernardi.upf.ads.oop.swing;

import javax.swing.JFrame;
import javax.swing.JTabbedPane;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;

import com.formdev.flatlaf.FlatLightLaf;

import space.jaobernardi.upf.ads.oop.swing.structures.Menu;

public class App {
    private static JFrame jFrame;
    public static JTabbedPane tabbedPane;
    public static void main( String[] args ) {
        System.out.println( "App Swing  -  @jaobernardi - ADS UPF OOP - 10.2022" );
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                //Turn off metal's use of bold fonts
                //UIManager.put("swing.boldMetal", Boolean.FALSE);
                try {
                    initSwing("Test swing app @jaobernardi");
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });


    }


    private static void initSwing(String window_title) throws ClassNotFoundException, InstantiationException, IllegalAccessException, UnsupportedLookAndFeelException  {
        //Setup 
        FlatLightLaf.setup();
        //UIManager.setLookAndFeel(new FlatLightLaf());
        tabbedPane = new JTabbedPane();
        jFrame = new JFrame(window_title);
        jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        tabbedPane.setTabLayoutPolicy(JTabbedPane.SCROLL_TAB_LAYOUT);
        Menu menu = new Menu(tabbedPane);
        menu.register();
        
        jFrame.add(tabbedPane);
        jFrame.setSize(700,500);
        //jFrame.pack();
        jFrame.setVisible(true);

    }


    public static JFrame getJFrame() {
        return jFrame;
    }


}
