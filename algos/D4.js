/*
    Given a sorted array of page numbers where a term appears,
    produce an index string.

    Consecutive pages should form ranges separated by a hyphen

    BONUS: Only use the hyphen IF there are 3 or more consecutive pages.

    EXAMPLE:

    var input = [1, 5, 6, 7, 8, 9, 10, 14, 22, 23, 24, 25, 27];

    var output = "1, 5-10, 14, 22-25, 27";

    var input2 = [2, 3, 4, 7, 8, 10, 12, 14, 15, 16, 17];

    BASIC:
    var output2 = "2-4, 7-8, 10, 12, 14-17";
    BONUS:
    var output2 = "2-4, 7, 8, 10, 12, 14-17";
*/

function bookIndex(pages){
    var pages_string = [];
    for(var i=0; i<pages.length; i++){
        if(pages[i]+1 == pages[i+1]){
            var start = pages[i];
            while(pages[i]+1 == pages[i+1]){
                i++;
            }
        var end = pages[i];
        pages_string.push(start + "-" + end);
        } else{
            pages_string.push(pages[i]);
        }
    }
    var newstring = pages_string.join(",");
    return newstring
}

var input = [1, 5, 6, 7, 8, 9, 10, 14, 22, 23, 24, 25, 27];
var input2 = [2, 3, 4, 7, 8, 10, 12, 14, 15, 16, 17];

console.log(bookIndex(input2));