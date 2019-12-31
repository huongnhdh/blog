Title: ORM: mapping from database to OOP languages (ngôn ngữ hướng đối tượng)
Date: 2019-12-31 12:30
Category: Architecture
Tags: orm, memo, database
Slug: orm-mapping
Authors: HuongNHD
Summary: ORM mapping như thế nào từ database qua object trong ngôn ngữ hướng đối tượng.

## ORM: mapping from database to OOP languages (ngôn ngữ hướng đối tượng)

**ORM** (Object Relational Mapping) là một kỹ thuật dùng để mapping dữ liệu của các Database SQL (cơ sở dữ liệu có quan hệ "_") qua các object, class của các ngôn ngữ hướng đối tượng. Do đó ta sẽ có bảng mapping sau.

| Database |     OOP languages(ngôn ngữ hướng đối tượng)      |
|----------|-------------|
| Tables|  classes |
| columns |object attributes|
| rows |   object |


- In Rails: ActiveRecord.
- In Python: SQlAlchemy.
- In Java: Hibernate-JPA.