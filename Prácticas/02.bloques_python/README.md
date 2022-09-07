# Tema 03. De la programación de bloques a Python
## Solución de las prácticas

**Programación**: automatización de tareas cuya salida depende de la entrada del programa.

Se pueden realiza programas por varias motivaciones recogidas en las siguientes prácticas.

### Programa #1: Programación imperativa básica
**Secuencializar o agrupar tareas manuales para que sean ejecutadas en un orden concreto**
- Al hacer clic en la bandera verde...
- El gato debe decir "Hola" durante 1 segundo.
- A continuación se va hacer grande fijando su tamaño a 200%.
- Esperaremos 1 segundo.
- Ocultaremos el gato.
- Esperaremos 1 segundo.
- Mostraremos el gato.
- Lo dejaremos en su tamaño original, 100%.
- Dirá (de forma pensativa) "Uy, ¿qué ha pasado?" durante 1 segundo.

### Programa #2: Condicionales
**Generar distintas salidas en función de la información de entrada**
- Al hacer clic en la bandera verde...
- El gato debe decir "¡Hola, soy el gato IA!" durante 1 segundo.
- Preguntará "Dime una palabra en español y la traduciré al inglés"
- Se evaluará la palabrá introducida (almacenada en la variable respuesta). Si su contenido es igual a Hola:
   + El gato debe decir "Hola se dice en inglés: hello" durante 2 segundo.
- Si no...
   + El gato debe decir "¡Vaya! Ahí me has pillado" durante 2 segundo.

### Programa #3: Condicionales anidados
**Generar distintas salidas en función de la información de entrada - Avanzado**

Se creará un sistema inteligente basado en reglas:
- Al hacer clic en la bandera verde...
- Preguntará "¿Qué temperatura hace hoy?"
- Si la temperatura es inferior a 0 grados el gato dirá: "Hace mucho, pero que mucho frío" durante 2 segundos.
- Si la temperatura está entre [0, 9] el gato dirá: "Hace frio, pero se puede soportar" durante 2 segundos.
- Si la temperatura está entre [10, 19] el gato dirá: "La temperatura es agradable" durante 2 segundos.
- Si la temperatura está entre [20, 29] el gato dirá: "Empieza el calorcito" durante 2 segundos.
- Si la temperatura es superior a 30 grados el gato dirá: "Hace mucho, pero mucho calor" durante 2 segundos.

### Programa #4: Bucles
**Automatizar y optimizar la repetición de una serie de tareas**

Se creará un programa, similar al desarrollado en Scratch, en el cuál se diga en primer lugar "¡Hola!", a continuación se mostrará un "\*" por cada paso hasta dar 8 y se mostrárá el texto "¡Llegué!". Se mostrará el texto "Volviendo" y de vuelta se mostrará un "-" por cada paso de vuelta. Al finalizar se mostrará el texto "¡Volví!".

Algo como lo siguiente:
```
¡Hola!********¡Llegué! Volviendo --------¡Volví!
```
