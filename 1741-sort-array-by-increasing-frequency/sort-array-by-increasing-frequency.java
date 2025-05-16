class Solution {
    public int[] frequencySort(int[] nums) {
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        for(int i:nums)
        {
            if(freqMap.containsKey(i)){
                freqMap.put(i,freqMap.get(i)+1);
            }
            else{
                freqMap.put(i,1);
            }
        }

        // Step 2: Convert int[] to Integer[] using loops
        Integer[] numsArr = new Integer[nums.length];
        for (int i = 0; i < nums.length; i++) {
            numsArr[i] = nums[i];
        }

        // Step 3: Custom sort using comparator
        Arrays.sort(numsArr, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int freqA = freqMap.get(a);
                int freqB = freqMap.get(b);
                if (freqA != freqB) {
                    return Integer.compare(freqA, freqB);  // ascending frequency
                } else {
                    return Integer.compare(b, a);          // descending value
                }
            }
        });

        // Step 4: Convert Integer[] back to int[] using loops
        int[] result = new int[numsArr.length];
        for (int i = 0; i < numsArr.length; i++) {
            result[i] = numsArr[i];
        }

        return result;
    }
}