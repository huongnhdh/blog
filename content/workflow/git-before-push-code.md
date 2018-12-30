Title: Xử lý Git trước khi push code lên remote
Date: 2010-12-03 10:20
Category: Workflow
Tags: git
Slug:  workflow-git-before-push-code
Authors: HuongNHD
Summary: Cần làm gì trước khi đẩy git lên remote mà tránh conflict tại local

# Trước khi commit code 
## Bước 1: Devloper nên nhớ lấy code về từ remote trước

```
git pull --rebase upstream master # git fork
```
hoặc 

```
git pull --rebase origin master 
```

## Bước 2: Thực hiện kiểm tra code conflict ngay tại local trước khi push code lên remote

```
git stash 
git pull --rebase upstream master or  git pull --rebase origin master
git stash apply 
```
