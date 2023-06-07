/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let size = nums.length;
    let ans;
    nums.sort((a,b)=> a-b);
    for(let i=0;i<size-1;i++){
        if(nums[i]===nums[i+1])
            return nums[i];
    }
};
