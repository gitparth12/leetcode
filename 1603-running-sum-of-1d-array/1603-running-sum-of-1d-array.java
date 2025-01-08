class Solution {
    public int[] runningSum(int[] nums) {
        int toReturn[] = new int[nums.length];
        toReturn[0] = nums[0];
        for(int i = 1; i < toReturn.length; i++) {
            toReturn[i] = toReturn[i-1] + nums[i];
        }
        return toReturn;
    }
}