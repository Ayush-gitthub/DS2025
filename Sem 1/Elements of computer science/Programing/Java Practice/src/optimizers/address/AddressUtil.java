package optimizers.address;
import java.util.regex.*;

public class AddressUtil {
    static String [] splitAddress(AddressOptimizer ao)
    {
        String s = ao.s;
        if (s == null) return null;
        String regex = "^(\\d{5})\\s(.+)$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(s);
        if (matcher.matches()) {
            return new String[] { matcher.group(1), matcher.group(2) };
        }
        return null;
    }
}

