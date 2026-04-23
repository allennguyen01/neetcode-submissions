class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int secondNum = target - num;

            if (!map.containsKey(num)) {
                map.put(num, i);
            }

            if (map.containsKey(secondNum) && map.get(secondNum) != i) {
                return new int[]{map.get(secondNum), i};
            }
        }

        return new int[] {};
    }
}
