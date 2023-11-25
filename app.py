#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

print("-----Bienvenido al juego------. \nDe las siguientes opciones: \nRock \nPaper \nScissors")
menu_op = input("Elija una: ")

if menu_op.lower() == "rock":
    print("rock")

elif menu_op.lower() == "paper":
    print("paper")

elif menu_op.lower() == "scissors":
    print("scissors")

else:
    print("Opción incorrecta")