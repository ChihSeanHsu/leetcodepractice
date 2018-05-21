class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int Maxnum = 0;
        int Maxin;
        int max=0;
        int temp;
        for(int i=0;i<nums.size();i++){
            if(nums[i] > max){
                max = nums[i];
                if(nums[i] > Maxnum) {
                    max = Maxnum;
                    Maxnum = nums[i];
                    Maxin = i;               
                }
            }     
        }
        if(Maxnum >= max*2){
            return Maxin;
        }
        return -1;
        
    }
};
