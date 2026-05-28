package optimizers.address;
import optimizers.*;

import java.util.ArrayList;
import java.util.List;

public class AddressOptimizer implements optimizers{
    protected String s;
    public AddressOptimizer(String s)
    {
        this.s = s;
    }

    public List<String> optimize(){
        String [] x = AddressUtil.splitAddress(this);
        if(x.length == 0)
            return new ArrayList<String>();

        return new ArrayList<String>(List.of(x));

    }
}
