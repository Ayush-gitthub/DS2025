package Testpractice;

public class generics <a, b, c>{
    private a vara;
    private b varb;
    private c varc;

    public generics(a vara, b varb, c varc) {
        this.vara = vara;
        this.varb = varb;
        this.varc = varc;
    }

    public a getVara() {
        return vara;
    }

    public void setVara(a vara) {
        this.vara = vara;
    }

    public b getVarb() {
        return varb;
    }

    public void setVarb(b varb) {
        this.varb = varb;
    }

    public c getVarc() {
        return varc;
    }

    public void setVarc(c varc) {
        this.varc = varc;
    }

    @Override
    public String toString() {
        return "generics{" +
                "vara=" + vara +
                ", varb=" + varb +
                ", varc=" + varc +
                '}';
    }
}
