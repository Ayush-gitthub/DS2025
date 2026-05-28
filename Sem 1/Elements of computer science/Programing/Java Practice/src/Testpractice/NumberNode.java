package Testpractice;

public class NumberNode extends ExprNode{

    public double getValue() {
        return value;
    }

    public void setValue(double value) {
        this.value = value;
    }

    public NumberNode(double value) {
        this.value = value;
    }

    private double value;

    public double evaluate()
    {
        return this.value;
    }

}
