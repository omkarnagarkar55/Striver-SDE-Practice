/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let low = 0;
    let mid = 0;
    let high = nums.length - 1;
    while(mid<=high){
        if(nums[mid]=== 0){
            swap(nums,low,mid);
            low++;
            mid++;
        }else if(nums[mid]=== 1)
            mid++;
        else{
            swap(nums,high,mid);
            high--;
        }
    }
};

var swap = (arr,index1,index2)=>{
    let temp = arr[index1];
    arr[index1] = arr[index2];
    arr[index2] = temp;
}
