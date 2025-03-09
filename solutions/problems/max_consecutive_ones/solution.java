import java.util.Scanner;

public class Solution {
   
    public static int findMaxConsecutiveOnes(int[] nums) {
        int maxcnt=0;
        int currentcnt=0;
        for(int num:nums)
        {
            if(num==1)
            {
                currentcnt++;
                if(currentcnt>maxcnt)
                {
                    maxcnt=currentcnt;
                }
            }
            else
            {
                currentcnt=0;
            }
        }
        return maxcnt;

    }

    public static void main(String[] args)
    {
        int [] nums= new int[5];
        Scanner scanner=new Scanner(System.in);
        for (int i=0;i<nums.length;i++)
        {
            nums[i]=scanner.nextInt();

        }
        int result= findMaxConsecutiveOnes(nums);
        System.out.println(result);
    
}
}
