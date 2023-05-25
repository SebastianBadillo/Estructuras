<?php
/*
PHP Data Types
Variables can store data of different types, and different data types can do different things.
PHP supports the following data types:
- String
- Integer
- Float (floating point numbers - also called double)
- Boolean
- Array
- Object
- NULL
- Resource
*/

$string = 'I feel nervious';
echo var_dump($string) . "<br>";

$float = 45.9;
echo var_dump($float) . "<br>";

$answers = array('yes', 'no');
echo var_dump($answers) . "<br>";
print_r($answers);




/** 
 * In PHP, print_r and echo are both used to output text to the screen, but they have some differences in terms of their behavior and syntax:
 *Syntax: echo is used to output a string, while print_r is used to output a variable or an array. So, you can write echo "Hello World";, but you must use print_r with a variable or an array, as in print_r($myArray);.
 *Output format: echo outputs the string as is, while print_r outputs a more readable representation of the variable or array, with each element on a new line and with indentation. This makes print_r especially useful for debugging and understanding complex data structures.
 *Return value: echo does not have a return value, while print_r returns a string representation of the variable or array.
 *In summary, echo and print_r serve different purposes in PHP, with echo being used to output strings and print_r being used to output variables and arrays in a readable format. While they can be used interchangeably in some cases, it's important to choose the right one for the specific situation.
 */
?>