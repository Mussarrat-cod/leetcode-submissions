import java.util.*;
class Solution {
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner (System.in);
        int num= scanner. nextInt();
        int result= addDigits(num);

        System.out.println(result);
    }
    public static int addDigits(int num) {
    while(num>=10)
    {
        int sum=0;
        while(num>0)
        {
            sum+=num%10;
            num=num/10;
        }
        num= sum;
    }
    return num;
    
    }
    
}