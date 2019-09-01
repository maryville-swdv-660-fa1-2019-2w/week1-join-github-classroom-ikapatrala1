import camelcase
from clint.textui import colored

name = input("Please enter your name: ")
c = camelcase.CamelCase()

txt = "Hello {0} !!".format(c.hump(name))

print(colored.green(txt))

print(colored.red("Welcome to Week 1 Package Managed Project!!!!!!!!!"))