import os
is_windows = os.name == 'nt'
def shutdown():
    if is_windows:
        os.system("shutdown /s /t 0")
    else:
        os.system("shutdown -h now")
def restart():
    if is_windows:
        os.system("shutdown /r /t 0")
    else:
        os.system("shutdown -r now")
def logout():
    if is_windows:
        os.system("shutdown /l")
    else:
        os.system("pkill -KILL -u $USER")