Title: Python Setup development 2020
Date: 2020-08-03 10:20
Category: Tools
Tags: python, dev-env, mac-osx
Slug: python-setup-dev-environment
Authors: HuongNHD
Summary: Setup môi trường cho lập trình Python python cơ bản

# Setup môi trường development for Python
1. Python3
2. Pip3
3. Quản lý môi trường (virtualenv, virtualenvwrapper )
4. Các IDE or Editor phổ biến

### 1. Install python3

Vì sao chúng ta phải cài python3 trong khi hầu hết các OS đều support sẵn python2 ?

Dựa trên thông báo của [python.org](https://www.python.org/doc/sunset-python-2/) thì Python2 sẽ ngưng phát triển (support, maintain) từ ngày 1 tháng 1 năm 2020

Do đó chúng ta cần phải cài và nâng cấp lên python3

```zsh
## MAC OSX
brew install python3
python3 ––version

## LINUX DEBIAN
sudo apt update
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
python3 ––version

## LINUX RETHAT/CENTOS-7
yum update -y
yum install -y python3
python3 ––version
```

### 2. Pip3

Để quản lý các thư viện được sử dụng mỗi ngôn ngữ đề có các bộ tool khác nhau ( yarn hoặc npm cho nodejs,  gem + bundler cho ruby, maven hoặc gradle cho Java).

Trong python thì dùng `pip` là đơn giản nhất (ngoài ra vẫn còn 1 tool khác là easy_install, tuy nhiên do pip được sinh sau nên có nhiều cải tiến hơn)

```zsh
pip3 --version
```

### 3. Quản lý môi trường bằng virtualenv, virtualenvwrapper

Khi 1 nhà phát triển phần mềm cần làm việc trên nhiều project python trên cùng 1 máy tính, rất dễ xảy ra hiện tượng xung đột version  của thư viện, Ví dụ như project A cũ hơn cần django==2.1.14 còn project B mới hơn cần dùng django==3.0.9, Khi đó việc chuyển qua lại khi làm việc cho 2 project này thì Omg!

Vì để hạn chế các lỗi xảy ra do dùng nhầm version của thư viện hay thậm chí version của python (python2.7, python3.4, python 3.5,...) thì bộ đôi `virtualenv`, `virtualenvwrapper` được xử dụng nhiều cho việc tạo ra các môi trường phát triển biệt lập cho các dự án khác nhau, phát triển song song với nhau.

#### Install

```zsh
pip3 install virtualenv
pip3 install virtualenvwrapper
```

```bash
echo "VIRTUALENVWRAPPER_PYTHON=`which python3`" >>  ~/.profile
echo "WORKON_HOME=\$HOME/.virtualenvs" >> ~/.profile
echo "VIRTUALENVWRAPPER_VIRTUALENV=`which virtualenv`" >> ~/.profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
```

#### Example

```bash
# Tạo một môi trường mới
mkvirtualenv blog-env

# Vị trí của môi trường blog-env sau khi được tạo
(blog-env)  ls $WORKON_HOME/blog-env
bin        lib        pyvenv.cfg

# Thoát khỏi blog environment
(blog-env) deactive

# Vào lại blog-env để tiếp tục công việcj
workon blog-env
(blog-env)
```


## 4. Các IDE or Editor phổ biến
- IDE: [Pycharm](https://www.jetbrains.com/pycharm/download/)
- Editor: [VSCode](https://code.visualstudio.com/)
