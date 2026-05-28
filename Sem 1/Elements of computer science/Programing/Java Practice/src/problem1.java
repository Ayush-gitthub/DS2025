import java.util.*;

public class problem1 {

    public static int virtualArrayGet(int [] base, int [] dim, int []pos)
    {
        int x = 0;
        int []z = new int[dim.length];
        z[0] = 1;
        for(int i = 1; i<dim.length;i++)
        {
            z[i] = z[i-1]*dim[dim.length-i];
        }
        for(int i = 0;i<pos.length;i++)
        {
            int y = z[pos.length-1-i]*pos[i];
            x = x + y;
        }
        return base[x];
    }

    public static String charSort(String input)
    {
        StringBuilder sb = new StringBuilder();
        char [] x = {'a' ,'b', 'c'};
        for (char ch :x)
        {
            sb.append(charSort(input, ch));
        }

        return sb.toString();
    }
    public static String charSort(String input, char ch){
        int count = 0;
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i<input.length();i++){
            if(input.charAt(i) == ch)
                sb.append(ch);
        }
        return sb.toString();
    }

    static String textExtractor(String input){
        StringBuilder sb = new StringBuilder();
        int x = input.length();
        for(int i = 0;i<x;i++)
        {
            if(input.charAt(i) != input.charAt(x-1-i))
            {
                sb.append(input.charAt(i));
            }

        }
        return sb.toString();
    }
    public static String[] predictPrice(String [] products, int [][] harvests)
    {
        String [] res = new String[products.length];
        for(int i = 0; i< harvests.length;i++)
        {
            StringBuilder sb = new StringBuilder(products[i]);
            int avg = 0;
            int curr = harvests[i][0];
            int ind = Math.min(6, harvests[i].length);
            int dem = 0;
            for(int j= 1;j<ind;j++)
            {
                avg+= harvests[i][j];
                dem++;
            }
            avg = avg/(dem);
            if(curr>avg)
            {
                if((curr-avg)*100/avg>=10)
                    sb.append(": drop");
                else
                    sb.append(": same");
            }
            else
            {
                if(((avg-curr)*100/avg)>=10)
                    sb.append(": raise");
                else
                    sb.append(": same");
            }

            res[i] = sb.toString();
        }
        return res;
    }
    public static long g(long [] data, char mode){
        long value = 0;
        int i =0;
        if(mode == '1')
        {
            while(i<data.length)
            {
               value = value + data[i];
               i++;
            }
        }
        else if(mode == '2')
        {
            while(i<data.length)
            {
                value = value + Math.abs(data[i]);
                i++;
            }
        }
        else
        {
            while(i<data.length)
            {
                value++;
                i++;
            }
        }
        return value;
    }
    public static void main() {
        System.out.println("Hello");
        System.out.println(charSort("babacacb"));
        System.out.println(textExtractor("!===(Hello World)===!"));
        String []products = {"Potatoes", "Oranges", "Rice"};

        int [][] harvests = {
                {250, 70, 520, 120, 45, 410, 190, 0, 1050},
                {85, 95, 110, 0, 45},
                {230, 280, 170, 55, 660, 390, 0}
        };
        String []ans = predictPrice(products,harvests);
        for(String x:ans)
            System.out.println(x);

        int [] base = {0 , 1, 2, 3, 4 , 5 , 6 , 7 , 8, 9, 10 , 11 , 12 , 13 , 14 , 15 ,
                16 , 17 , 18 , 19 , 20 , 21 , 22 , 23};
        int [] dim = {4 , 2 , 3};
        int [] pos = {3 , 0 , 1};
        int res = virtualArrayGet( base , dim , pos );
        System.out.println(res);
    }
}
