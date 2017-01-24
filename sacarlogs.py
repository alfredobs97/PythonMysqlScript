#!/usr/bin/python
from fabric.decorators import task, hosts
from fabric.api import run
from fabric.api import *
env.key_filename = 'llaveBautista'
@task
@hosts('root@192.168.8.16')
def deploy():
    result = prompt("Introducir ruta del log de error: ")
    get(result, ".")
    result = prompt("Introducir ruta del log de acceso: ")
    get(result, ".")
