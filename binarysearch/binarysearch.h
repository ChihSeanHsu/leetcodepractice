int search(int* nums, int numsSize, int target) {
    int mid = numsSize/2;
    return loop(nums, numsSize, target, mid);
}


int loop(int* nums, int numsSize, int target, int mid){
        if(nums[mid] == target) return mid;
        else 
        {
            if(nums[mid] < target) {
                mid += 1;
                if(mid > numsSize) return -1;
                else{
                    if(nums[mid] > target) return -1;
                    else return loop(nums, numsSize, target, mid);
                }
            }
            else{
                mid -= 1;
                if(mid < 0) return -1;
                else{
                    if(nums[mid] < target) return -1;
                    else return loop(nums, numsSize, target, mid);
            
                }
            }
        }
}
