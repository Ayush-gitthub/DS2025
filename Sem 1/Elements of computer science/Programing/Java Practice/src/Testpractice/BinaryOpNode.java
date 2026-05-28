package Testpractice;

public class BinaryOpNode extends ExprNode{
    private  ExprNode n1;
    private  ExprNode n2;
    private char ch;

    public BinaryOpNode(ExprNode n1, ExprNode n2, char ch) {
        this.n1 = n1;
        this.n2 = n2;
        this.ch = ch;
    }

    public ExprNode getN2() {
        return n2;
    }

    public void setN2(ExprNode n2) {
        this.n2 = n2;
    }

    public ExprNode getN1() {
        return n1;
    }

    public void setN1(ExprNode n1) {
        this.n1 = n1;
    }

    public char getCh() {
        return ch;
    }

    public void setCh(char ch) {
        this.ch = ch;
    }

    public double evaluate()
    {
        return switch (ch) {
            case '+' -> n1.evaluate() + n2.evaluate();
            case '-' -> n1.evaluate() - n2.evaluate();
            case '*' -> n1.evaluate() * n2.evaluate();
            case '/' -> {
                if (n2.evaluate() == 0.0)
                    throw new ArithmeticException("Divison by zero not possible");
                yield n1.evaluate() / n2.evaluate();
            }
            default -> 0.0;
        };
    }
}
