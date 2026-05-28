package Testpractice;

import java.util.*;

public class dataconversion {
    static int[] runLengthEncode(int[] input){
        if(input.length == 0)
            throw new IllegalArgumentException("Input must not be empty");
        List<Integer> x  = new ArrayList<Integer>();
        TreeSet<Integer> y = new TreeSet<>();
        for(int z: input)
        {
            x.add(z);
            y.add(z);
        }
        List<Integer> ans = new ArrayList<>();
        int [] ans1 = new int[y.size()*2];
        int i = 0;
        System.out.println(x);
        System.out.println(y);
        for(int p: y)
        {
            ans1[i] = p;
            i++;
            ans1[i] = Collections.frequency(x, p);
            i++;
        }
        return ans1;
    }

    public static void main(String[] args){
        System.out.println(Arrays.toString(runLengthEncode(new int[]{1, 1, 1, 2, 3, 3})));
    }
}
