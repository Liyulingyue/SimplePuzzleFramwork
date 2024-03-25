import os
ernie_access_token = "**************"
os.environ["ERNIE_ACCESS_TOKEN"] = ernie_access_token

from GameTools.GradioTools.gr_main import demo

demo.launch()