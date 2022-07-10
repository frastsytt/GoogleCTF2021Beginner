bakArray = scanArray

function arrayRemove(arr, value) { 
return arr.filter(function(ele){ 
return ele != value; 
});}

scanArray = arrayRemove(scanArray, 0)


left = bakArray.slice(0,7);
left = arrayRemove(left, 0)
center = bakArray[8];
right = bakArray.slice(9);
right = arrayRemove(right, 0)


let unique = scanArray.filter((item, i, ar) => scanArray.indexOf(item) === i);
console.log(unique);


var leftAvg = left.reduce((a, b) => a + b, 0) / left.length;
var rightAvg = right.reduce((a, b) => a + b, 0) / right.length;

if (isNaN(leftAvg)) {
leftAvg = 0}

if (isNaN(rightAvg)) {
rightAvg = 0}


console.log('leftavg' + leftAvg)
console.log('rightavg' + rightAvg)

console.log('left curb' + bakArray[6])
console.log('right curb' + bakArray[10])

longest = Math.max(...unique)

console.log('leftcorner'+bakArray[7])
console.log('rightcorner'+bakArray[9])
/*
if ( [bakArray[7] === bakArray[9] ) {
corners = [bakArray[7], bakArray[9]]
}

console.log(corners);
*/
console.log('longest path is: ' + longest)

if ((longest == bakArray[7]) && (longest == bakArray[9])){
console.log('going straight')
console.log('#######################')
return 0}


if ((leftAvg > rightAvg) && !(bakArray[6]== 0) && true ) {
console.log('i turned left')
console.log('#######################')
return -1}

if ((rightAvg > leftAvg) && !(bakArray[10]== 0) && true ) {
console.log('i turned right')
console.log('#######################')
return 1}