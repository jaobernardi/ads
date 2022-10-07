package space.jaobernardi.upf.oop.prova.structures;

import javax.swing.JComponent;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;

public class Tab {

    private JTabbedPane pane;
 
    public Tab(JTabbedPane pane) {
        this.pane = pane;
    }

    public void addToPane(JTabbedPane tabbedpane) {
        tabbedpane.addTab(getName(), null, makePanel(), getName());
    }

    public void register() {
        this.addToPane(pane);
    }

    public JComponent makePanel() {
        JPanel panel = new JPanel(false);
        JLabel filler = new JLabel("Unnamed panel");
        filler.setHorizontalAlignment(JLabel.CENTER);
        panel.add(filler);
        return panel;
    }


    public String getName() {
        return "No name";
    }
    
}