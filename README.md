# VtuberSuperChat Dashboard

## 項目簡介
這個項目旨在爬取Vtuber的SuperChat數據，並通過Redash展示在Dashboard上。項目使用Python、RabbitMQ和Celery進行分散式爬蟲，將清洗後的數據存儲在MySQL數據庫中，並使用Docker Swarm進行管理。

## 主要技術
- Python
- RabbitMQ
- Celery
- MySQL
- Redash
- Docker Swarm
- GitLab CI/CD

## 功能
- 爬取直播主的SuperChat相關數據
- 清洗並存儲數據至MySQL
- 使用Redash建立Dashboard
- Docker Swarm管理
- GitLab CI/CD，自動化測試及部署

## 安裝步驟

### 前置需求
- Ubuntu 22.04
- Docker
- Linode雲端機器(兩台)

### SSH到其中一台機器部署
1. 安裝Docker、poetry：
    ```bash
    sudo apt-get update
    sudo apt-get install -y docker.io
    sudo apt install make
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH=$PATH:$HOME/.local/bin
    sudo apt install git
    ```

2. clone程式碼、安裝套件：
    ```bash
    git clone https://gitlab.com/sss96437/username.git
    cd ~/username/poetry-demo
    poetry lock
    poetry install
    ```

3. 安裝Gitlab-Runner：
    ```bash
    sudo curl -L --output /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64

    sudo chmod +x /usr/local/bin/gitlab-runner

    sudo useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash

    sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner

    sudo gitlab-runner start

    sudo usermod -aG docker gitlab-runner

    sudo gitlab-runner register --url https://gitlab.com/ --registration-token <YourToken>

    sudo rm /home/gitlab-runner/.bash_logout
    ```

4. 部署Docker Swarm的UI介面：
    ```bash
    docker swarm init
    docker stack deploy -c portainer.yml por
    ```

5. 建立Mysql volume及Network：
    ```bash
    docker volume create mysql
    docker network create --scope=swarm --driver=overlay my_network
    ```

6. SSH到另一台機器重複一、二步驟，並加入worker：
    ```bash
    docker swarm join --token <YourToken>
    ```

7. 部屬的前置步驟：
    ![步驟一](https://gitlab.com/sss96437/username/-/blob/e3735ccd7a34421f7acbed8a426cb138a4235673/step1.png)
    ![步驟二](https://gitlab.com/sss96437/username/-/blob/e3735ccd7a34421f7acbed8a426cb138a4235673/step2.png)
    - [建立mysql的table](poetry-demo/create_table.sql)

8. SSH到manager機器部屬Mysql、Rabbitmq、Redash：
    ```bash
    docker stack deploy --with-registry-auth -c mysql.yml mysql
    docker stack deploy --with-registry-auth -c rabbitmq.yml rabbitmq
    docker stack deploy -c redash.yml redash
    ```

## 使用說明
- 在本機或測試機push程式碼以及建立新的tag後，便會觸發CICD
- 自動部屬爬蟲和schedular
- schedular每周一下午三點自動爬最新的資料下來

## 相關文檔
- [數據架構](./data-architecture.md)
- [數據轉換過程](./data-transformation.md)

## 聯繫方式
如果有任何問題，請通過sss96437@gmail.com聯繫。