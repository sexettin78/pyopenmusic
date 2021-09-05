import os
try:
  print("Müziği durdurmak için ctrl+c ")
  mzk = input("Müzik Yolu Giriniz > ")
  os.system("mpv --no-video "+mzk)
except:
  os.system("pip install mpv")
  
