package space.jaobernardi.upf.ads.oop.swing.structures;

import javax.swing.JComponent;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;

public class Tab {
    
    public void addToPane(JTabbedPane pane) {
        pane.addTab(getName(), null, makePanel(), getName());
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