package Testpractice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Recursionq3 {
    static int[] flattenDigits(int n) {
        List<Integer> x = new ArrayList<Integer>();
        int r = 67;
        String ra = Integer.toString(r);
        String rb = String.valueOf(r);
        System.out.println(ra + rb);
        if(n ==0)
            return new int[]{0};
        flattenDigits(x, n);
        Collections.reverse(x);
        int []z =new int[x.size()];
        int[] za = x.stream().mapToInt(Integer::intValue).toArray();
        for(int i =0;i<x.size();i++)
            z[i] = x.get(i);
        Arrays.sort(z);
        System.out.println(Arrays.binarySearch(z, 9));
        return za;
    }
    static  void flattenDigits(List<Integer> x, int n)
    {
        if(n== 0)
        {
            return ;
        }

        int y = n%10;
        x.add(y);
        flattenDigits(x, n/10);
    }
    public static void main(String[] args)
    {
        System.out.println(Arrays.toString(flattenDigits(69069)));
        int [] input = flattenDigits(123);
        assert Arrays.equals(flattenDigits(0),    new int[]{0});
        assert Arrays.equals(flattenDigits(7),    new int[]{7});
        assert Arrays.equals(flattenDigits(123),  new int[]{1,2,3});
        assert Arrays.equals(flattenDigits(5080), new int[]{5,0,8,0});
        assert Arrays.equals(flattenDigits(100),  new int[]{1,0,0});

    }
}

