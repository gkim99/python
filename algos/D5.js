/*
    Generate Coin Change

    Given a number of U.S. cents, return an object with the optimal 
    configuration of coins.

    EXAMPLE:

    var input = 173;
    var output = {
        quarters: 6,
        dimes: 2,
        nickels: 0,
        pennies: 3
    }

    A couple of different approaches:

    Option 1: Keep decrementing by the highest coin value possible, adding to that 
    key value pair each time, making your way down the hierarchy of coins

    Option 2: Our old friend modulo (i.e. the % operator)

    Modulo example:
    42 % 25 would give us 17, because 25 x 1 is 25, and there's 17 left to get us to 42

    Because (6 x 25) + (2 x 10) + (0 x 5) + (3 x 1) 
    is 150 + 20 + 0 + 3 = 173.
*/

function generateCoinChangeObject(cents){
    
}