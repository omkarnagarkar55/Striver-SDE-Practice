/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let i = 0;
    let j = 0;
    while(i<nums1.length){
        if(nums1[i] > nums2[j]){
            let aa = nums1.length - 2;
            while(aa>=i){
                nums1[aa+1] = nums1[aa];
                aa--;
            }
            nums1[i] = nums2[j];
            j++;
        }
        i++;

    }
    if(j<n){
        nums1.splice(-(n-j),n-j,...nums2.splice(j,n));
    }
};
