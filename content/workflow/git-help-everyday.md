Title: Xử lý Git trước khi push code lên remote
Date: 2019-01-06 21:20
Category: Workflow
Tags: git
Slug:  git-help-everyday
Authors: HuongNHD
Summary:  `giteveryday` - Một bộ lệnh tối thiểu hữu ích cho `Git` (hơn 20 commands với 4 role cơ bản)

# `git help everyday`

## **NAME(Tên)**

    giteveryday - Một bộ lệnh tối thiểu hữu ích cho `Git`

## **SYNOPSIS(Tóm tắt)**
    Everyday Git với 20 lệnh hoặc hơn

## **DESCRIPTION(Mô tả)**
Người dùng Git có thể được phân nhóm thành bốn loại với mục đích mô tả ở dưới dây, bên cạnh đấy là một tập lệnh git cực kỳ hữu ích được sử dụng hàng ngày.

   ·   `INDIVIDUAL DEVELOPER (STANDALONE)`: Những commands cơ bản cho nhà phát triển độc lập là  nhất cho những ai muốn commit, ngay cả khi  làm việc một mình.

   ·   `INDIVIDUAL DEVELOPER (PARTICIPANT)`: Nếu bạn làm việc với những người khác, bạn sẽ cần những commands được liệt kê trong phần trên (những participant)

   ·   `INTEGRATOR`: Những người đóng vai trò Integrator cần học thêm một số lệnh ngoài những điều trên.

   ·   `REPOSITORY ADMINISTRATION`: Những commands dành cho quản trị viên (system administrators), những người chịu trách nhiệm cho việc quản trị những kho lưu trữ Git.

## 1. `INDIVIDUAL DEVELOPER (STANDALONE)`
   Một developer cá nhân độc lập thì không phải trao đổi  patches với những người khác,  làm việc một mình với một kho lưu trữ, Họ thường sử dụng những commands sau:

  ·   `git-init(1)` để tạo mới một  kho lưu trữ

  ·   `git-log(1)` để xem lịch sử những thay đổi trong kho lưu trữ

  ·   `git-checkout(1) and git-branch(1)`để chuyển qua các nhánh khác nhau.

  ·   `git-add(1)` để quản lý các index file

  ·   `git-diff(1)` và `git-status(1)` để xem những gì bận đang làm

  ·   `git-commit(1)` để  lưu những thay đổi vào  nhánh hiện tại.

  ·   `git-reset(1)` và `git-checkout(1)` (with pathname parameters) để hủy bỏ những thay đổi.

  ·   `git-merge(1)` để tích hợp thay đổi của các nhánh local

  ·   `git-rebase(1)` kết quả giống như git-merge(1) nhưng làm với cơ chế khác. có thể tìm hiểu thêm tại đây [git-rebase](https://git-scm.com/book/vi/v1/Ph%C3%A2n-Nh%C3%A1nh-Trong-Git-Rebasing)

  ·   `git-tag(1)` để tag một điểm đặc biết (vd realease)

#### Examples (Ví dụ)

Dùng 1 file nén tarball như là một điểm bắt đầu khi tạo  một kho lưu trữ mới

```bash
    $ tar zxf frotz.tar.gz
    $ cd frotz
    $ git init
    $ git add . (1)
    $ git commit -m "import frotz vào source tree."
    $ git tag v2.43 (2)

# 1. Thêm vào tất cả mọi thứ dưới thư mục hiện tại.
# 2. Đánh dấu một tag để quản lý dễ dàng.
```

Tạo 1 nhánh topic/feature và nhánh develop.

``` bash
$ git checkout -b alsa-audio (1)
$ edit/compile/test
$ git checkout -- curses/ux_audio_oss.c (2)
$ git add curses/ux_audio_alsa.c (3)
$ edit/compile/test
$ git diff HEAD (4)
$ git commit -a -s (5)
$ edit/compile/test
$ git diff HEAD^ (6)
$ git commit -a --amend (7)
$ git checkout master (8)
$ git merge alsa-audio (9)
$ git log --since='3 days ago' (10)
$ git log v2.43.. curses/ (11)

# 1. Tạo mới một topic branch.
# 2. Loại bỏ tất cả thay đổi trên file curses/ux_audio_oss.c.
# 3. Nếu thêm vào một file mới; bạn có thể lọai bỏ và sửa đổ  khi thực hiện git commit -a sau đó.
# 4. Để xem những gì thay đổi khi bạn commit.
# 5. Viết tắt của (git commit --amend --squash ) commit mọi thứ, as you have # tested, with your sign-off.
# 6. Xem tất cả thay đổi bao gồm cả các commit trước đó.
# 7. sửa commit trước đó, thêm vào những thay đổi mới, sử dụng message gốc.
# 8. chuyển qua master branch.
# 9. tích hợp nhánh topic vào  nhánh master.
# 10. xem lại lịch sử commit; các công thức để  giới hạn đầu ra có thể  # combined and include -10 (để  show ra 10 commits), --until=2005-12-10, vv.
# 11. chỉ nhìn những thay đổi của thư mục curses, từ thời điểm tại v2.43 tag.
```

### 2. `INDIVIDUAL DEVELOPER (PARTICIPANT)`

Một developer làm việc như một thành viên trong một nhóm dự án cần học cách làm sao để giao tiếp với các thành viên còn lại, và sử dụng những commands này  bên cạnh những command mà developer độc lập hay  dùng
  
·   `git-clone(1)` tạo một bản sao của kho lưu trữ trên upstream về local của bạn.

·   `git-pull(1)` and `git-fetch(1)` từ **origin**  để  giữ up-to-date với the upstream.

·   `git-push(1)` làm kho lưu trữ được chia sẻ, khi áp dụng  flow kiểu CVS

·   `git-format-patch(1)` để chuẩn bị đăng kí email, nếu bạn chấp nhận qui trình làm việu kiểu `Linux kernel-style forum workflow`.

·   `git-send-email(1)` để gửi e-mail submission mà không corruption bằng MUA.

·   `git-request-pull(1)` để  tạo một tóm tắt cho sự thay đổi từ upstream mà  bạn pull về

#### Examples (Ví dụ) 

Clone the upstream and work on it. Feed changes to upstream.
Tạo bản sao từ repo để làm việc trên đó. Và đưa những sự thay đổi lên upstream.

```bash
$ git clone git://git.kernel.org/pub/scm/.../torvalds/linux-2.6 my2.6
$ cd my2.6
$ git checkout -b mine master (1)
$ edit/compile/test; git commit -a -s (2)
$ git format-patch master (3)
$ git send-email --to="person <email@example.com>" 00*.patch (4)
$ git checkout master (5)
$ git pull (6)
$ git log -p ORIG_HEAD.. arch/i386 include/asm-i386 (7)
$ git ls-remote --heads http://git.kernel.org/.../jgarzik/libata-dev.git (8)
$ git pull git://git.kernel.org/pub/.../jgarzik/libata-dev.git ALL (9)
$ git reset --hard ORIG_HEAD (10)
$ git gc (11)

# 1. checkout a new branch mine from master. Branch ở local tên là `mine` được trỏ tới branch master
# 2. repeat as needed. lặp lại những gì cần thiết tại bước 1
# 3. extract patches from your branch, relative to master, (Trích xuất những sửa đổi từ nhánh của bạn so với nhánh master),
# 4. and email them.  (set author bằng email cho chúng)
# 5. return to master, ready to see what’s new (Trở về nhánh master cũng như xem những gì mới cập nhật từ đồng đội)
# 6. git pull fetches from origin by default and merges into the current branch. (lấy tất cả những thay đổi từ origin và tích hợp(merge) chúng vào nhánh master)
# 7. immediately after pulling, look at the changes done upstream since last time we checked, only in the area we are interested in. (Ngay sau khi pull về, nhìn những thây đổi đã làm trên upstream kể từ thời gian cuối cùng chúng ta check, chỉ trong những khu vực chúng ta quan tâm )
# 8. check the branch names in an external repository (if not known).(Kiểm tra một branch names trong một kho lưu trữ bên ngoài)
# 9. fetch from a specific branch ALL from a specific repository and merge it. (Fetch all branch từ 1 kho lưu trữ chỉ định vaqf merge chúng)
# 10. revert the pull. (undo thao tác pull)
# 11. thu thập những đối tượng là rác còn lại sau quá trình `reverted pull`
```

Đẩy lên vào một repository khác.

```bash
satellite$ git clone mothership:frotz frotz (1)
satellite$ cd frotz
satellite$ git config --get-regexp '^(remote|branch)\.' (2)
remote.origin.url mothership:frotz
remote.origin.fetch refs/heads/*:refs/remotes/origin/*
branch.master.remote origin
branch.master.merge refs/heads/master
satellite$ git config remote.origin.push \
            +refs/heads/*:refs/remotes/satellite/* (3)
satellite$ edit/compile/test/commit
satellite$ git push origin (4)

mothership$ cd frotz
mothership$ git checkout master
mothership$ git merge satellite/master (5)

# 1. mothership machine có kho lưu trữ tên là  `frotz`; copy kho lưu trữ này về để làm việc với satellite machine.
# 2. copy nguyên một bộ biến config mặc định. Nó sắp xếp Git pull để fetch và lưu trữ các nhánh của  mothership machine đến local remotes/origin/* remote-tracking nhánh.
# 3. arrange git push to push all local branches to their corresponding branch of the mothership machine. Sắp xếp việc git push từ nhánh local đến nhánh remote tương ứng
# 4. push will stash all our work away on remotes/satellite/* remote-tracking branches on the mothership machine. You could use this as a back-up method. Likewise, you can pretend that mothership "fetched" from you (useful when access is one sided). Hành động __push__ sẽ stash tất cả công việc của the mothership machine lên nhánh remotes/satellite/* remote-tracking. Đây là một cách dùng đê backup. Tương tự thếm bạn cần giả  lập rằng. mothership lấy từ bạn (Và điều này sẽ hữu ích khi việc truy cập là từ một phía)
# 5. on mothership machine, merge the work done on the satellite machine into the master branch. Trên branch mothership machine, tích hợp những công việc đã hoàn thành trên `satellite machine` lên trên branch master.

```

Branch off of a specific tag.
Kết thúc nhánh với một tah cụ thể

```bash
$ git checkout -b private2.6.14 v2.6.14 (1)
$ edit/compile/test; git commit -a
$ git checkout master
$ git cherry-pick v2.6.14..private2.6.14 (2)

# 1. create a private branch based on a well known (but somewhat behind) tag. Tạo một nhánh riêng từ tên tag đã biết.

# 2. chuyển tất cả những thay đổi trong  private2.6.14 branch đến master branch mà không phải thông qua format "merging" nào. Hoặc làm bằng tay.

# git format-patch -k -m --stdout v2.6.14..private2.6.14 | git am -3 -k

# An alternate participant submission mechanism is using the git request-pull or pull-request mechanisms (e.g as used on GitHub (www.github.com) to notify your upstream of your contribution. Một cơ chế cho viêc cập nhật các participant là sử dụng cơ chế git request-pull, hoặc pull-request để thông báo việc contribuition của bạn lên upstream.

```

__Tuần sau chúng ta sẽ tiếp tục với part 2 nhé ^^_

## 3. `INTEGRATOR`

A fairly central person acting as the integrator in a group project receives changes made by others, reviews and integrates them and publishes the result for others to use, using these commands
in addition to the ones needed by participants.

This section can also be used by those who respond to git request-pull or pull-request on GitHub (www.github.com) to integrate the work of others into their history. A sub-area lieutenant for a
repository will act both as a participant and as an integrator.

·   `git-am(1)` to apply patches e-mailed in from your contributors.

·   `git-pull(1)` to merge from your trusted lieutenants.

·   `git-format-patch(1)` to prepare and send suggested alternative to contributors.

·   `git-revert(1)` to undo botched commits.

·   `git-push(1)` to publish the bleeding edge.

Examples
       A typical integrator’s Git day.

               $ git status (1)
               $ git branch --no-merged master (2)
               $ mailx (3)
               & s 2 3 4 5 ./+to-apply
               & s 7 8 ./+hold-linus
               & q
               $ git checkout -b topic/one master
               $ git am -3 -i -s ./+to-apply (4)
               $ compile/test
               $ git checkout -b hold/linus && git am -3 -i -s ./+hold-linus (5)
               $ git checkout topic/one && git rebase master (6)
               $ git checkout pu && git reset --hard next (7)
               $ git merge topic/one topic/two && git merge hold/linus (8)
               $ git checkout maint
               $ git cherry-pick master~4 (9)
               $ compile/test
               $ git tag -s -m "GIT 0.99.9x" v0.99.9x (10)
               $ git fetch ko && for branch in master maint next pu (11)
                   do
                       git show-branch ko/$branch $branch (12)
                   done
               $ git push --follow-tags ko (13)

           1. see what you were in the middle of doing, if anything.
           2. see which branches haven’t been merged into master yet. Likewise for any other integration branches e.g.  maint, next and pu (potential updates).
           3. read mails, save ones that are applicable, and save others that are not quite ready (other mail readers are available).
           4. apply them, interactively, with your sign-offs.
           5. create topic branch as needed and apply, again with sign-offs.
           6. rebase internal topic branch that has not been merged to the master or exposed as a part of a stable branch.
           7. restart pu every time from the next.
           8. and bundle topic branches still cooking.
           9. backport a critical fix.
           10. create a signed tag.
           11. make sure master was not accidentally rewound beyond that already pushed out.
           12. In the output from git show-branch, master should have everything ko/master has, and next should have everything ko/next has, etc.
           13. push out the bleeding edge, together with new tags that point into the pushed history.

       In this example, the ko shorthand points at the Git maintainer’s repository at kernel.org, and looks like this:

           (in .git/config)
           [remote "ko"]
                   url = kernel.org:/pub/scm/git/git.git
                   fetch = refs/heads/*:refs/remotes/ko/*
                   push = refs/heads/master
                   push = refs/heads/next
                   push = +refs/heads/pu
                   push = refs/heads/maint

## 4. `REPOSITORY ADMINISTRATION`
A repository administrator uses the following tools to set up and maintain access to the repository by developers.

·   git-daemon(1) to allow anonymous download from repository.

·   git-shell(1) can be used as a restricted login shell for shared central repository users.

·   git-http-backend(1) provides a server side implementation of Git-over-HTTP ("Smart http") allowing both fetch and push services.

·   gitweb(1) provides a web front-end to Git repositories, which can be set-up using the git-instaweb(1) script.

update hook howto[1] has a good example of managing a shared central repository.

In addition there are a number of other widely deployed hosting, browsing and reviewing solutions such as:

·   gitolite, gerrit code review, cgit and others.

Examples
We assume the following in /etc/services

        $ grep 9418 /etc/services
        git             9418/tcp                # Git Version Control System

Run git-daemon to serve /pub/scm from inetd.

        $ grep git /etc/inetd.conf
        git     stream  tcp     nowait  nobody \
            /usr/bin/git-daemon git-daemon --inetd --export-all /pub/scm

    The actual configuration line should be on one line.

Run git-daemon to serve /pub/scm from xinetd.

        $ cat /etc/xinetd.d/git-daemon
        # default: off
        # description: The Git server offers access to Git repositories
        service git
        {
                disable = no
                type            = UNLISTED
                port            = 9418
                socket_type     = stream
                wait            = no
                user            = nobody
                server          = /usr/bin/git-daemon
                server_args     = --inetd --export-all --base-path=/pub/scm
                log_on_failure  += USERID
        }

    Check your xinetd(8) documentation and setup, this is from a Fedora system. Others might be different.

Give push/pull only access to developers using git-over-ssh.
    e.g. those using: $ git push/pull ssh://host.xz/pub/scm/project

        $ grep git /etc/passwd (1)
        alice:x:1000:1000::/home/alice:/usr/bin/git-shell
        bob:x:1001:1001::/home/bob:/usr/bin/git-shell
        cindy:x:1002:1002::/home/cindy:/usr/bin/git-shell
        david:x:1003:1003::/home/david:/usr/bin/git-shell
        $ grep git /etc/shells (2)
        /usr/bin/git-shell

    1. log-in shell is set to /usr/bin/git-shell, which does not allow anything but git push and git pull. The users require ssh access to the machine.
    2. in many distributions /etc/shells needs to list what is used as the login shell.

CVS-style shared repository.

        $ grep git /etc/group (1)
        git:x:9418:alice,bob,cindy,david
        $ cd /home/devo.git
        $ ls -l (2)
            lrwxrwxrwx   1 david git    17 Dec  4 22:40 HEAD -> refs/heads/master
            drwxrwsr-x   2 david git  4096 Dec  4 22:40 branches
            -rw-rw-r--   1 david git    84 Dec  4 22:40 config
            -rw-rw-r--   1 david git    58 Dec  4 22:40 description
            drwxrwsr-x   2 david git  4096 Dec  4 22:40 hooks
            -rw-rw-r--   1 david git 37504 Dec  4 22:40 index
            drwxrwsr-x   2 david git  4096 Dec  4 22:40 info
            drwxrwsr-x   4 david git  4096 Dec  4 22:40 objects
            drwxrwsr-x   4 david git  4096 Nov  7 14:58 refs
            drwxrwsr-x   2 david git  4096 Dec  4 22:40 remotes
        $ ls -l hooks/update (3)
            -r-xr-xr-x   1 david git  3536 Dec  4 22:40 update
        $ cat info/allowed-users (4)
        refs/heads/master       alice\|cindy
        refs/heads/doc-update   bob
        refs/tags/v[0-9]*       david

    1. place the developers into the same git group.
    2. and make the shared repository writable by the group.
    3. use update-hook example by Carl from Documentation/howto/ for branch policy control.
    4. alice and cindy can push into master, only bob can push into doc-update. david is the release manager and is the only person who can create and push version tags.

## GIT
       Part of the git(1) suite

## NOTES
...

    _Git 2.19.1   10/05/2018  GITEVERYDAY(7)_