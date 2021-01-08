import sys

print(sys.version)
print(sys.platform)

if (sys.platform == "win32"):
    print(sys.getwindowsversion())
print("바이트 순서 :", sys.byteorder)
print("모듈 경로 :", sys.path)
sys.exit(0)


"""
pip install

pip install pyinstaller

pyinstaller -F p282.py
"""