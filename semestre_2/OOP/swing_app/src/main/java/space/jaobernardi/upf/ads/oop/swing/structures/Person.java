package space.jaobernardi.upf.ads.oop.swing.structures;

import javax.swing.JTabbedPane;

public class Person extends Tab{
    private String Name;
    private Double Weight;
    private Double Height;
    private JTabbedPane pane;


    public Person(JTabbedPane pane, String name, Double weight, Double height) {
        super(pane);
        this.pane = pane;
        this.Name = name;
        this.Height = height;
        this.Weight = weight;

    }

    public Person(String name, Double weight, Double height) {
        super(null);
        this.Name = name;
        this.Height = height;
        this.Weight = weight;
    }

    @Override
    public String getName() {
        return this.Name;
    }

    public Double getWeight() {
        return this.Weight;
    }

    public Double getHeight() {
        return this.Height;
    }
}
