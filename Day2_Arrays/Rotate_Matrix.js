/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    let size = matrix.length;
    for(let i = 0;i< size;i++){
        for(let j = 0;j<=i;j++){
            if(i!==j){
                swap(matrix,i,j);
            }
        }
        
    }
    for(let i = 0;i< size;i++){
        matrix[i] = matrix[i].reverse();
    }
};

var swap = function(matrix,a,b){
    let temp = matrix[a][b];
    matrix[a][b] = matrix[b][a];
    matrix[b][a] = temp;
};
