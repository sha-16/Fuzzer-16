# fuzzer-16

Este es un fuzzer que nació con la idea de crear un programa en Python3 que enviará peticiones HTTP de una forma un tanto más rápida. El proyecto lleva 8 horas de código aprox, lo cual no es nada, así que aún hay mucho por hacer...

## Instalación y ejecución
```bash
$ git clone https://github.com/sha-16/fuzzer-16.git
$ cd fuzzer-16/
$ pip3 install <library> -> Ejecuta esto por cada librería que necesites (ya que no he añadido aún el fichero requirements.txt)
$ chmod +x fuzzer-16.py
$ ./fuzzer-16.py
```

## Problemas
El script a la hora de terminar su ejecución deja muchos procesos corriendo por detras, los cuales 
podemos mirar ejecutando, en bash, la sentencia: 

```bash 
$ ps -eo pid,cmd
```

Si te molesta demasiado el hecho de que queden corriendo, los puedes matar ejecutando: 

```bash 
$ for pid in $(ps -eo pid,cmd | grep "fuzzer-16" | grep -v "grep" | awk '{print $1}'); do kill -9 $pid; done
```

**Por ahora esta es la única forma que se me ocurre para solucionar este problema.** 

**PD**: Perdón si tienes que instalar librerías de Python3 de forma manual, pronto añadiré el ```requeriments.txt```.

**Nota**: si pruebas el script y encuentras fallos, me los podrías hacer saber por favor 🤞

