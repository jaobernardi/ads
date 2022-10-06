package space.jaobernardi.upf.ads.oop.swing.structures;

import javax.swing.JComponent;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Menu extends Tab {


    public String getName() {
        return "Adicionar Pessoas";
    }

    @Override
    public JComponent makePanel() {
        JPanel panel = new JPanel(false);
        JLabel filler = new JLabel("Adicionar Pessoas");
        filler.setHorizontalAlignment(JLabel.CENTER);
        panel.add(filler);
        return panel;
    } 
    
}
