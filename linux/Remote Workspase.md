sudo apt update -y
sudo apt install xfce4 xfce4-goodies tigervnc-standalone-server -y

vncpasswd

nano ~/.vnc/xstartup
```bash
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec startxfce4 
```

chmod u+x ~/.vnc/xstartup

nano ~/.vnc/config
```
geometry=1920x1080
dpi=96
```

vncserver

vncserver -list
vncserver -kill :1


docker run -d -p 6080:80 -p 5900:5900 -e USER=doro -e PASSWORD=password -e VNC_PASSWORD=g87g2f97g6  -e RESOLUTION=1920x1080 -v /dev/shm:/dev/shm dorowu/ubuntu-desktop-lxde-vnc
