#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

menu_op = int(input("-----Bienvenido al juego------\n1.rock \n2.paper \n2.scissors:"))

if menu_op == 1:
    print("")

elif menu_op == 2:
    print("")
    exit()
elif menu_op == 3:
    print("")
else:
    print("Opcion invalida")
    exit()