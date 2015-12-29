from flask import Flask
app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

import qti_interaction.model
import qti_interaction.view
import qti_interaction.controller