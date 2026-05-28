package Testpractice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class longestpalindrome {

    static String longestPalindrom(String input){
        String x = "";
        for(int i = 0;i<input.length();i++){
            for(int j = i;j<=input.length();j++)
            {
                String sb = (input.substring(i, j));
                StringBuilder b1 = new StringBuilder(input.substring(i, j));
                String sb1 = b1.reverse().toString();
                if(sb.equals(sb1)&& sb.length()>x.length())
                    x = sb;
            }
        }
        return  x;

    }
    public static int[] computeAlt(int[] arr, int threshold) {
        int count = 0;
        List<Integer> x = new ArrayList<Integer>();
        int i = 0;
        while(i<arr.length)
        {
            if(arr[i]>threshold)
            {
                x.add(arr[i]);
            }
            i++;
        }
        int [] ans = x.stream().mapToInt(Integer::intValue).toArray();
        return  ans;

    }
    public static void main(String[] args){
        System.out.println(longestPalindrom("racecar"));
        System.out.println(Arrays.toString(computeAlt(new int[]{1, 5, 3, 8, 2}, 4)));
    }
}
