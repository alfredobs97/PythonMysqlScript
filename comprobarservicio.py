#!/usr/bin/python
from fabric.decorators import task, hosts
from fabric.api import run
from fabric.api import *
env.key_filename = 'llaveBautista'
@task
@hosts('root@192.168.8.16')
def deploy():
    result = run('service mysql status')
    if result == "mysql stop/waiting":
        print("Error Mysql no activado")
        result = prompt('Quiere arrancar el servidor?[s/n]')
        if result == 's':
            run('service mysql restart')
