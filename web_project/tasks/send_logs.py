#!/home/OBud/hexagone/Linux_B2/web_project/venv/bin/python3

from datetime import datetime
import os

basedir = os.path.dirname(__name__)
now = datetime.now()

open(f"{basedir}/{now}", 'w').close()
