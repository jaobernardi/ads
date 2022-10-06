package space.jaobernardi.upf.ads.oop.swing.structures;


public class Person extends Tab{
    private String Name;
    private Double Weight;
    private Double Height;


    public Person(String name, Double weight, Double height) {
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
