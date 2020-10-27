
## 1. Install

```bash
 sudo apt-get install vsftpd
 sudo service vsftpd start
 sudo apt-get install xinetd

 nano  /etc/xinetd.d/vsftpd
 ```

## 2. Put there:
```
service ftp
{
        disable                 = no
        socket_type             = stream
        wait                    = no
        user                    = root
        server                  = /usr/sbin/vsftpd
        per_source              = 5
        instances               = 200
        no_access               = 10.1.1.10
        banner_fail             = /etc/vsftpd.busy
        log_on_success          += PID HOST DURATION
        log_on_failure          += HOST
}
```

## 3. Put `nano /etc/vsftpd.conf `:
```
listen=NO
userlist_file=/etc/vsftpd.userlist
userlist_enable=YES
userlist_deny=NO
```

## 4. Add user for conect and restart:
```
echo neafiol > /etc/vsftpd.userlist
sudo service xinetd restart
```
