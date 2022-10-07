package space.jaobernardi.upf.oop.prova.structures;

import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;
import javax.swing.JTextField;

import space.jaobernardi.upf.oop.prova.GUI;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Menu extends Tab {

    private JTabbedPane pane;
    private JLabel latest_result = new JLabel("");

    public Menu(JTabbedPane pane) {
        super(pane);
        this.pane = pane;
    }

    @Override
    public String getName() {
        return "Adicionar cálculo";
    }
    
    @Override
    public JComponent makePanel() {
        JPanel panel = new JPanel(false);
        JButton buttonAddPessoa = new JButton("Calcular");

        JPanel input = new JPanel();

        JLabel nameLabel = new JLabel("Informe o nome: ");
        JTextField nameText = new JTextField(5);

        input.add(nameLabel);
        input.add(nameText);

        JLabel idLabel = new JLabel("Informe o ID: ");
        JTextField idText = new JTextField(5);

        input.add(idLabel);
        input.add(idText);
        
        JLabel pasLabel = new JLabel("Informe o PAS: ");
        JTextField pasText = new JTextField(5);

        input.add(pasLabel);
        input.add(pasText);

        JLabel padLabel = new JLabel("Informe o PAD: ");
        JTextField padText = new JTextField(5);

        input.add(padLabel);
        input.add(padText);
        input.add(latest_result);
        buttonAddPessoa.addActionListener(
            new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                Pressao pres = new Pressao(
                    pane,
                    (int) Integer.valueOf(idText.getText()),
                    nameText.getText(),
                    (double) Double.valueOf(pasText.getText()),
                    (double) Double.valueOf(padText.getText())
                );
                GUI.add(pres);
                pres.register();
                latest_result.setText("INTERPRETAÇÃO: "+pres.getInterpretacao());
            }
        });
        panel.add(input);
        panel.add(buttonAddPessoa);
        return panel;
    } 
    
}
