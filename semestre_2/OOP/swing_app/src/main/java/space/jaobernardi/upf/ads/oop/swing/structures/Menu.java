package space.jaobernardi.upf.ads.oop.swing.structures;

import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;
import javax.swing.JTextField;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Menu extends Tab {

    private JTabbedPane pane;

    public Menu(JTabbedPane pane) {
        super(pane);
        this.pane = pane;
    }

    @Override
    public String getName() {
        return "Adicionar Pessoas";
    }
    
    @Override
    public JComponent makePanel() {
        JPanel panel = new JPanel(false);
        JButton buttonAddPessoa = new JButton("Adicionar pessoa");

        JPanel input = new JPanel();

        JLabel nameLabel = new JLabel("Informe o nome: ");
        JTextField nameText = new JTextField("                             ");

        input.add(nameLabel);
        input.add(nameText);

        buttonAddPessoa.addActionListener(
            new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                Person p = new Person(pane, nameText.getText(), null, null);
                p.register();
            }
        });
        panel.add(input);
        panel.add(buttonAddPessoa);
        return panel;
    } 
    
}
