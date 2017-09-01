// String.prototype.DoSelectHack = function(num) {
//     if (num % 2 == 0)
//         return this.toUpperCase()
//     else
//         return this.toLowerCase()
// }


// function exists(arr, number)
// true false

function exists() {
    var myArray = [3, 4, 5, 6, 11];
    var i = 0
    while (i < myArray.length) {
        if (myArray[i] === 33) {
            console.log(true);
            return;
        }
        i += 1;
    }
    console.log(false);
}














exists();


// var myArray = [3, 4, 5, 6, 11];