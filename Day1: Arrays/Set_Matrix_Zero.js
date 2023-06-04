/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    let row = [];
    let col = [];
    for(let i in matrix){
        for(let j in matrix[i]){
            if (matrix[i][j] === 0){
                if(!row.includes(Number(i)))
                    row.push(i)
                if(!col.includes(j))
                    col.push(Number(j))
            }
        }
    }
    for(let i of row){
        for(let j in matrix[i]){
            matrix[i][j] = 0 ;
        }
    }
    for(let i of col){
        for(let j in matrix){
            matrix[j][i] = 0;
        }
    }
    return matrix;
};
