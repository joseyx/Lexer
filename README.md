
# Manual de Usuario - Lexer para Programas

Este repositorio contiene un lexer (analizador léxico) implementado en Python utilizando la biblioteca Ply. El lexer se utiliza para analizar y reconocer tokens en programas escritos en un lenguaje de programación personalizado.


## Requisitos

* Python 3.x

* Biblioteca Ply
## Instalacion

* Asegúrate de tener Python 3.x instalado en tu sistema. Si no lo tienes, puedes descargarlo desde el sitio web oficial de Python: python.org/downloads ↗

* Instala la biblioteca Ply ejecutando el siguiente comando en tu terminal:

```bash
  pip install ply
```
    
## Uso

1. Crea un archivo de programa con la extensión .txt y escribe tu programa en él. Asegúrate de seguir las reglas de sintaxis del lenguaje de programación personalizado admitido por este lexer.

1. Abre el archivo lexer.py en tu editor de texto o IDE.

1. En el código fuente de lexer.py, busca la variable file_name y asigna el nombre de archivo de tu programa al que deseas aplicar el lexer. Por ejemplo:

    ```python
    file_name = "programa.txt"
    ```

1. Guarda los cambios en lexer.py.

1. Abre una terminal y navega hasta la ubicación del archivo lexer.py.

1. Ejecuta el siguiente comando para ejecutar el lexer en tu programa:

    ```python
    python lexer.py
    ```

1. El resultado del lexer se mostrará en la terminal, donde cada token reconocido se imprimirá en una nueva línea.

## Tokens soportados

El lexer es capaz de reconocer los siguientes tokens:

* INTEGER: Número entero.
* VARIABLE: Nombre de variable.
* IF: Palabra clave if.
* ELSE: Palabra clave else.
* WHILE: Palabra clave while.
* PLUS: Operador de suma +.
* MINUS: Operador de resta -.
* MULTIPLY: Operador de multiplicación *.
* DIVIDE: Operador de división /.
* LPAREN: Paréntesis izquierdo (.
* RPAREN: Paréntesis derecho ).
* GREATER: Operador de comparación mayor >.
* EXPONENT: Operador de exponenciación ^.
* BREAK: Palabra clave break.

## Manejo de errores

Si el lexer encuentra un carácter inválido en el programa, imprimirá un mensaje de error indicando el carácter inválido.
