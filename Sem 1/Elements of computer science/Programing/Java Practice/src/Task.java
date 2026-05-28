import com.sun.source.tree.Tree;

import java.util.*;
import java.util.HashMap;

public class Task {
    private HashMap<Integer,Members> coll = new HashMap<Integer, Members >();
    public Task(Collection<Members> members)
    {
        for(Members m :members)
        {
            int x = m.getId();
            if(coll.containsKey(x))
                throw new IllegalArgumentException();
            coll.put(x, m);
        }

    }
    public void removeDuplicates()
    {
        HashSet<Members> x = new HashSet<Members>(coll.values());
        for(Members m :x) {
            int y = m.getId();
            coll.put(y, m);
        }
    }
    public void addMember(Members m)
    {
        int x = m.getId();
        if(coll.containsKey(x))
            throw new IllegalArgumentException();
        coll.put(x, m);
    }
    public Map<Integer, List<Members>> getBirthYearMap(){
        TreeMap<Integer, List<Members>> x = new TreeMap<>();
        for(Members m: coll.values())
        {
            int y = m.getBirthYear();
            if(x.containsKey(y)){
                List<Members> z = x.get(y);
                z.add(m);
            }
            else{
                List<Members> z = new ArrayList<>();
                z.add(m);
                x.put(y,z);
            }
        }
        return x;
    }
}
