class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int size = nums.size();
        int lsum = 0, rsum = accumulate(nums.begin(), nums.end(), 0); //or use for loop to sum
        for(int i=0; i<size; i++){
            if(rsum - nums[i] == 2* lsum){
                return i;
            }
            lsum += nums[i];
        }
        return -1;
        
    }
};
