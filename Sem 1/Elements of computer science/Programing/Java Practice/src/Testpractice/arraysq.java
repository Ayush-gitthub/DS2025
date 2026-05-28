package Testpractice;

import java.util.Arrays;

public class arraysq {
    static String[] gradeStudents(String[] names, int[][] scores){
        String[] x = new String[names.length];
        for(int i = 0;i< names.length;i++)
        {
            String y = names[i];
            int z = 0;
            for(int j = 0;j<scores[i].length;j++)
            {
                z = z + scores[i][j];
            }
            z = z/scores[i].length;
            if(z>=90)
            {
                y = y + ": A";
                x[i] = y;
                continue;
            }
            if(z>=75)
            {
                y = y + ": B";
                x[i] = y;
                continue;
            }
            if(z>=60)
            {
                y = y + ": C";
                x[i] = y;
                continue;
            }
            if(z>=50)
            {
                y = y + ": D";
                x[i] = y;
                continue;
            }
            y = y + ": F";
            x[i] = y;
        }

        return x;
    }

    public static void main(String[] args){
        String[] names = {"Alice", "Bob", "Carol"};
        int[][] scores = {{95,88,92}, {60,55,70}, {40,45}};
        String[] res = gradeStudents(names, scores);

        System.out.println(Arrays.toString(res));
    }
}
