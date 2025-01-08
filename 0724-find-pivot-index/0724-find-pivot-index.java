class Solution {
    public int pivotIndex(int[] nums) {
        boolean done = false;
        int leftSum = 0;
        int rightSum = 0;
        int index = 0;
        for(int i = 0; i < nums.length; i++) {
            for(int j = 0; j < nums.length; j++) {
                if(j < i)
                    leftSum += nums[j];
                else if(j > i)
                    rightSum += nums[j];
            }
            if(leftSum == rightSum)
                return i;
            else {
                leftSum = 0;
                rightSum = 0;
            }
        }
        return -1;
    }
}