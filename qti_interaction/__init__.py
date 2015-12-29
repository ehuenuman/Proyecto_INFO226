from flask import Flask
app = Flask(__name__)

import qti_interaction.model
import qti_interaction.controller