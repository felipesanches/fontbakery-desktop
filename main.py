import sys
import resources
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QLabel, QPlainTextEdit
from PyQt5.QtWebChannel import QWebChannel

app = QApplication(sys.argv)

content = QLabel("# Fontbakery-desktop\nv0.0.1")

web = QWebEngineView()
channel = QWebChannel(web.page())
web.page().setWebChannel(channel)
channel.registerObject("content", content)
web.load(QUrl('file:///Users/fsanches/devel/github_felipesanches/fontbakery-desktop/resources/index.html'))
web.show()

def run_fontbakery(fontfile):
  import tempfile
  import os
  import subprocess
  with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
    md_file = os.path.join(tmpdirname, "results.md")
    try:
      fb_cmd = [
          "fontbakery",
          "check-googlefonts",
          "--verbose",
          fontfile,
          "--ghm",
          md_file
      ]
      fb_output = subprocess.check_output(fb_cmd, stderr=subprocess.STDOUT)

    except OSError:
      content.setText("ERROR: fontbakery is not properly installed!")
      return
    except subprocess.CalledProcessError:
      pass

    content.setText(open(md_file, "r").read())
    # delete md_file!

run_fontbakery("/Users/fsanches/devel/github_google/fonts/ofl/lobstertwo/LobsterTwo-Regular.ttf")
sys.exit(app.exec_())
