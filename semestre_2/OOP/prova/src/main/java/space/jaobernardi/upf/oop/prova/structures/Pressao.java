package space.jaobernardi.upf.oop.prova.structures;

import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;

public class Pressao extends Tab {
    private JTabbedPane pane;
    private Integer id;
    private String nome;
    private Double pas;
    private Double pad;

    public Pressao(JTabbedPane pane ,Integer id, String nome, Double pas, Double pad) {
        super(pane);
        this.id = id;
        this.nome = nome;
        this.pas = pas;
        this.pad = pad;
    }

    public Pressao(Integer id, String nome, Double pas, Double pad) {
        super(null);
        this.id = id;
        this.nome = nome;
        this.pas = pas;
        this.pad = pad;
    }

    @Override
    public void addToPane(JTabbedPane tabbedpane) {
        tabbedpane.addTab(getName(), null, makePanel(), getName());
    }

    @Override
    public JPanel makePanel() {
        JPanel panel = new JPanel(false);
        JLabel id = new JLabel("ID: "+String.valueOf(this.id));
        JLabel name = new JLabel("\nNOME: "+this.nome);
        JLabel paspad = new JLabel("\nPAS: "+this.pas+" PAD:"+this.pad);
        JLabel interp = new JLabel("\nINTERPRETAÇÃO: "+getInterpretacao());
        // filler.setHorizontalAlignment(JLabel.CENTER);
        panel.add(id);
        panel.add(name);
        panel.add(paspad);
        panel.add(interp);
        return panel;
    }

    public Double getPAS() {return this.pas;}

    public Double getPAD() {return this.pad;}

    @Override
    public String getName() {return getNome();}

    public String getNome() {return this.nome;}

    public Integer getID() {return this.id;}

    public String getInterpretacao() {
        if (this.pas < 90 || this.pad < 60) 
            return "Baixa";

        if ((this.pas >= 90 && this.pas < 130) || (this.pad >= 60 && this.pad < 85)) 
            return "Normal";
        
        if ((this.pas >= 130 && this.pas < 139) || (this.pad >= 85 && this.pad < 89)) 
            return "Limítrofe";

        return "Pressão Alta";
    }
}
