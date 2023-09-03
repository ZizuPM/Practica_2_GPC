#!/usr/bin/python3
import cgi

print ("Content-type: text/html")
print

print ("""
Hola Mundo
""")

form=cgi.FieldStorage()
print ("<p>user:", form["user"].value)
print ("<p>pass:", form["pass"].value)

