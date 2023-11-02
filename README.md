# participacion #10 de poo 2023/2
Juego de Tetris:
Tu equipo está construyendo un juego de Tetris y tú estás asignado a diseñar los Tetrominós que
son las piezas del juego. Se llaman Tetrominós porque están formados por 4 fragmentos.
Cada tipo de tetrominó se identifica con una letra a la que se parece. Hay siete tipos posibles de
tetrominós.

Funcionalidad
Implementar las siguientes funcionalidades
1. Rotación: Una rotación rota el tetrominó 90 grados en sentido de las manecillas del reloj.
2. Representación: Representar un fragmento de un tetrominó con el carácter @. Imprimir el
estado actual del tetrominó en la consola. El método también debe imprimir un caracter . para
representar los cuadros amarillos en la imagen de arriba.
T después de dos rotaciones
....
..@.
.@@@
....
Z en su estado original
....
.@@.
..@@
....
3. Igualdad: Dos tetrominós son iguales si lucen iguales en su rotación actual. Por ejemplo, una Z
en su estado original es igual a una Z en la rotación 2.
4. Semejanza: Dos tetrominós son semejantes si lucen iguales en al menos una de sus rotaciones.

Adaptación al cambio:

El mecanismo de representación es muy probable que cambie. Diseñe el sistema para que se
pueda cambiar fácilmente a un mecanismo diferente.
Luego implemente el mecanismo de representación para que, en vez de imprimir por consola,
genere un archivo con el estado actual de un tetrominó.

Pruebas:

Debe realizar pruebas unitarias para verificar las funcionalidades implementadas.
