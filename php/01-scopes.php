<?php
echo 'Hello world';

$color = 'red';
$example2 = 'lets go';

function hola()
{
  global $color; /*with this statement we can access a global variable
    from within a function, [WHIOUT THIS STATEMENT WE WILL HAVE AN ERROR]*/
  echo $color . "<br>";

  echo $GLOBALS['example2']; /*Another way to access a global variable */
}

/*Static Scope*/
function myTest()
{
  static $number = 0; /*the static variable will mantain the value of the variable from the last
      time*/
  echo $number . "<br>";
  $number++;
}
myTest();
myTest();
myTest();
myTest();



hola();


?>