<?php

/*
1. En la universidad se efectuó la elección del representante de los estudiantes ante el Consejo Superior. Se presentaron 30 candidatos y cada uno se identificó con un número del 1 al 30. Asumiendo que los 5000 estudiantes de la universidad votaron, elabore un programa donde:
Imprima un listado de mayor a menor, según el número de votos obtenidos por cada candidato
*/
$candidatos = array();
for ($x = 0; $x < 30; $x++) {
    $candidatos['Candidato' . $x + 1] = 0;
}

for ($y = 0; $y < 5000; $y++) {
    $votado = rand(1, 30);
    $candidatos['Candidato' . $votado]++;
}


print_r($candidatos);
echo '<br>';

arsort($candidatos);
print_r($candidatos);
for ($x = 0; $x < 30; $x++) {
    echo $candidatos['Candidato' . $x + 1] . '<br>';
}



?>