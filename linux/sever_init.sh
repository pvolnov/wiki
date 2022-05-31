sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install python3-pip


sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common -y

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update 
sudo apt-get upgrade -y

sudo apt-get install docker-ce docker-ce-cli containerd.io -y

curl -s https://aerokube.com/cm/bash | bash
sudo ./cm selenoid start --vnc -g "--limit 8"

sudo ./cm selenoid-ui start

docker run -d --name socks5 -p 1080:1080 -e PROXY_USER=neafiol -e PROXY_PASSWORD=nef441 serjs/go-socks5-proxy

timedatectl set-timezone Europe/Moscow



#опрочитанном
"Пиши, сокращай" - Максим Ильяхов.

Книга посвещана трем темам: как писать, что писать и о чем писать.
Авторы приводят множество приемов отжима воды, как из отдельных предложений так и из текста вцелом. После редакции по советам из книги пропадают почти все длинные предложения, причастные обороты и шампы. 2 листа превращаются в 2 абзатса совершенно без потери смысла,  а шанс дочтения и благодарность читателя возрастают кратно. 
Помимо общих правил, если довольно много советов по продающим текстам, составлению резюме, написанию обращений. Я начал задумыватся перед тем как что-то написать о том зачем кто-то будет это читать, что люди хотят получить и как не потратить зря их время. Текст из возможности высказать мысль становится инструментом чтобы ее донести. 

Минусы: много примеров на одну идею, бумажное издание портится при сильном разгибе. Довольно много воды (в книге о том как ее избежать кек).

Итог: Рекомендую к прочтению
Страниц: 430
Скорость чтения: быстрая, много примеров
Я прочитал за: 4 дня
Оценка: 7/10