Title: Dùng Docker trên Window 10
Date: 2019-05-11 14:49
Category: Tools
Tags: docker,install-guide
Slug: docker-docker-composer-in-Window-10
Authors: HuongNHD
image: https://s3-ap-northeast-1.amazonaws.com/huongnhdh.blog/docker-windows.png
credit_image: internet
language: vi
Summary: Dùng Doker trên Window 10 cơ bản, cách cài đặt, lỗi hay gặp, command hay dùng


# Dùng Docker in Window 10 cơ bản

Đây là hướng dẫn cho việc cài đặt Docker desktop phục vụ cho việc development trên Window, post này mình cài đặt cho Docker version 18.09.2. (Version cũ thì cách cài đặt cũng sẽ khác)

## Hướng dẫn cài đặt
1. Yêu cầu hệ thống chạy Docker trên Window

    - CPU: CPU cần phải hỗ trợ virtualization, và phải 64 bit
    - OS
    - Window 10 Professtional 64 bit 
    - Window 10 Enterprise 64 bit
    - Windown 10 Education (1607 Anniversary Update, Build 14393 or later)

    Thông tin này được trên thông báo trên trang [hướng dẫn cài đặt của Docker](https://docs.docker.com/docker-for-windows/install/#what-to-know-before-you-install)

2. Download Docker CE (community edition)

    Docker có 2 phiên bản là Docker CE (Community Edition) sẽ khác với Docker EE (Enterprise Edition)
    
    - CE thì dùng cho developer các nhân hoặc các nhóm nhỏ để tìm hiểu và build môi trường development
    - EE là phiên bản dành cho doanh nghiệp, có các tính năng đặc biệt 1 trong số đó là hỗ trợ scale ứng dụng. 
    
    Tìm hiểu thêm sự khác nhau về tính năng giữa 2 phiên bản tại [đây](https://docs.docker.com/install/overview/)

    Download Docker CE cho Window trên docker hub tại đây [link download](https://hub.docker.com/editions/community/docker-ce-desktop-windows) (Để download được thì cần đăng nhập vào docker hub)

3. Sau khi cài đặt xong "Docker for Windows Installer". 

    Mở ứng dụng docker và xác nhận lại Docker đã hoạt động chưa.
    - Đầu tiên nếu OS chưa active Hyper-V, thì sẽ tự động restart lại Window
    - Tiếp theo là login vào tài khoản DockerHub
    - Mở cmd test lại bằng câu lệnh `docker run hello-world`

    Nếu gặp lỗi 
    ```
    Error response from daemon: Get https://registry-1.docker.io/v2/: 540 net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
    ```
    Chỉ cần `docker login` rồi restart lại Window là ok 
    - Tiếp theo kiểm tra docker-compose (Quản lý docker containers khi một ứng dụng cần nhiều docker. vd một ứng dụng blog cần 1 container run nginx, 1 container apache, 1 container mySQL chẳng hạn) : 
    
    `docker-compose --vesion`
    - Tiếp theo kiểm tra (trình quản lý tập trung cho các container ):

    `docker-machine --version`

## Cách dùng
Vì là trên Window nên việc dùng `bash shell` hơi bất tiện nên mình dùng luôn `docker-cli`
```sh
# list all image
 docker images

# list all image zombies(dangling)
 docker images --filter "dangling=true"

# remove all image zombies(dangling)
# -q will only number 
 docker rmi $(docker images -f "dangling=true" -q)
 
```
Và còn rất nhiều command tại đây https://docs.docker.com/engine/reference/commandline/docker/

## Tool for monitor
Mặc định có 1 công cụ trong `Docker Toolbox on Windows` ta có [Kitematic](https://kitematic.com/). Tuy nhiên có không có sẵn ta phải download thêm về tại 
[Kimatic release page](https://github.com/docker/kitematic/releases) (chọn platform là Window)
rồi extract to `C:\Program Files\Docker\Kitematic`. 

![open kitematic](https://s3-ap-northeast-1.amazonaws.com/huongnhdh.blog/OpenKitematic.png)

Đây là 1 tool open source hỗ trợ các thao tác cơ bản nhất khi dùng Docker tuy nhiên nó còn nhiều hạn chế, cụ thể là, các chức năng chính của Kitematic hỗ trợ: 
- Quản lý container(remove, stop, start).
- xem log của container (nếu container có setting log ra stdout)
- Xem setting của container 
- Mở termnal cho container 

Còn các chức năng khác khả cần thiết nhưng Kitematic chưa hỗ trợ, ví dụ như monitor resource (CPU, ram, disk, network), hỗ trợ lauching một container, quản lý image trên local, lệnh dọn tất cả các container rác, ....

## Link tham khảo
- https://docs.docker.com/docker-for-windows/
- https://awesome-docker.netlify.com/
- https://docs.docker.com/engine/reference/commandline/docker/