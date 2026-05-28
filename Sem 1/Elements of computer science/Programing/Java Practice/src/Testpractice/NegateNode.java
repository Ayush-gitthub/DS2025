package Testpractice;

public class NegateNode extends ExprNode{
    ExprNode b1;

    public NegateNode(ExprNode b1) {
        this.b1 = b1;
    }
    public  double evaluate(){
        return b1.evaluate()*(-1.0);
    }
}
