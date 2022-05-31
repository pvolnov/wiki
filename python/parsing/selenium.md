
### browsermob proxy
```python
server = Server("/home/neafiol/browsermob-proxy-2.1.4/bin/browsermob-proxy", {"port": 9031})
server.start()
self.proxy_mob = server.create_proxy()
self.proxy_mob.new_har("bmbets", options={"captureContent": True, "captureBinaryContent": True,
                                            'captureHeaders': True, 'captureCookies': True})

profile = webdriver.FirefoxProfile()
profile.set_proxy(self.proxy_mob.selenium_proxy())
```


### Add proxy to profile
```python
 profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", proxy.split("@")[1].split(":")[0])
profile.set_preference("network.proxy.socks_port", int(proxy.split("@")[1].split(":")[1]))
profile.set_preference("network.proxy.socks_version", 5)
profile.update_preferences()

```

### Selenoid
```python
self.driver = webdriver.Remote(
    command_executor=f"http://{selenoid}:4444/wd/hub",
    desired_capabilities={
        "browserName": "firefox",
        "sessionTimeout": "5m"
    },
    browser_profile=profile
)
```