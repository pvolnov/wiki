```
curl -s https://aerokube.com/cm/bash | bash
sudo ./cm selenoid start --vnc -g "--limit 8"

./cm selenoid-ui start
```

Смотрим: `http://localhost:4444/status`
Админка: `http://localhost:8080/`


Python Example

```
capabilities = {
    "browserName": "chrome",
    "version": "78.0",
    "platform": "LINUX"
}

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=capabilities
)

```