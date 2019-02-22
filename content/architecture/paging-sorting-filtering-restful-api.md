Title: Paging, Sorting, Filtering trong Restful-API
Date: 2019-02-18 10:20
Category: Architecture
Tags: restful-api, analysis, api-design, restful-api-design
Slug: paging-sorting-filtering-restful-api
Authors: HuongNHD
Summary: Paging, sorting, filtering, retrieving fields trong RESTFULL-API

## Paging
> `Use page & per_page query parameter, return x-total-count header`

_( Ngoài việc dùng `page & per_page`, chúng ta cũng có thể sử dụng `offset & limit`  với ý nghĩa tương tự )_

Để phân trang cho kết quả của bạn sử dụng `page` & `per_page` trong query parameter, ví dụ api cần trả về các item từ 50 đến 100 thì, câu lệnh sẽ là

```bash
 GET /item?page=2&per_page=50
```

Một số lưu ý phân trang
1. Trả về  tổng số items thông qua `X-Total-Count` header
2. Nếu muốn cung cấp link to `previous and next page` thì có thể sử dụng Link HTTP header.
3. Trong code mà bạn cài đặt nên set maximum limit, ví dụ 1000 chẳng hạn, để tránh những vấn đề tại server

Ngoài ra còn nhiều cách khác để phân trang chẳng hạn như dùng Range header. Khi nghĩ về end user của bạn, tức client: sẽ dễ dàng phân trang bằng thông số `page` và `per_page` của GET request, hoặc định nghĩa một range header.


## Sorting

> `Using sort parameter with value has prefix is minus (-) sign for desc and no sign for asc`

Cách đơn giản nhất để sort là sử dụng sort query params, cho phép bạn định nghĩa thông qua  minus (-) sign,
For example:
```bash
GET /items?sort=-created_at # desc
GET /items?sort=created_at # asc
```
_(Đây là cách đơn giản nhất, nhưng vẫn cò một số style khác như `sort[desc]=created_at`,`sort:desc=created_at`  or `sort=created_at.desc`)_

## Filtering

>Use a unique query parameter for each of your fields

ex:
```bash
GET /items?first_name=huong
GET /items?title=developer
```

## Searching

> `For fulltext search, should be using q params`

Nếu muốn tìm kiếm một giá trị mà phạm vi full-text search, cách đơn giản nhất là dùng `q` params

Ex: Bạn muốn tìm kiếm mọi thứ liên quan đến "Huong Ngo"

```bash
GET /users?q="Huong Ngo"
```

## Retrieving specific fields
> `Using fields parameter and slit value by ',' `

API nên chỉ cho phép user của bạn chỉ nhận  vào một số fields nhất định thay vì toàn bộ object, khi đó ta nên dùng từ khóa là `fields` và sử dụng dấy chấm phấy ',' để tách các giá trị

Ex:

```bash
GET /users?fields=email,scrore,alias_name
```
## Advanced filtering
> `Using LHS brackets with an operator` for intuitive or `Lucene or ElasticSearch syntax` for flexible issue


Phương thức filtering được nhắc đến ở trên, sử dụng query parameter, làm việc khá ổn nhưng chỉ với các filter là exact match ( chính xác hoàn toàn ). Nhưng nếu bạn cần những filter dạng như:

- 10 <= price <= 100
- status IS NOT past
- user is manager or director

Có nhiều cách để thực hiện:
 1. Using LHS brackets with an operator: `price[lte]=200 status[ne]=past`
 2. Using RHS colon with an operator: `price=lte:200 status=ne:past`
 3. Using Lucene syntax or ElasticSearch Simple Query strings directly: q=price:<200 q=-status:past

Nhìn bảng so sánh dưới đây để có thêm thông tin:

|   | Điểm mạnh  |Hạn chế   |
|---|---|---|
|`LSH Brackets with an operator` | - Người sử dụng (front-end dev) dễ  dàng sử dụng <br> - Tương đối đơn giản để parse ở phía server-side  <br> - Trông khá trực quan| - Không thể  thực hiện OR cho combined filters  |
|`RHS colon with an operator` | - Dễ dàng parser tại server side <br> - Người sử dụng (front-end dev) dễ  dàng sử dụng | - Không thể  thực hiện OR cho combined filters - Ít trực quan hơn `LSH Brackets with an operator`  |
|`Lucene or ElasticSearch syntax` | - Là phương pháp linh hoạt nhất trong các phương pháp trên <br> Gần như không cần parse phía server (có thể đẩy trực tiếp cho `elasticsearch`)  | - Cú pháp không trực quan như các phương pháp trên, cần phải học để sử dụng nhưng không quá khó|

Nếu bạn cần một giải pháp filter linh hoạt nhất có thể dành cho front-end của bạn, cho phép nó query trực tiếp vào DB thông qua API, thì sử dụng trực tiếp `Lucene or ElasticSearch syntax` sẽ hợp lý hơn ngay cả khi nó đòi hỏi người sử dụng phải học để dùng nó.

Tuy nhiên, trong hầu hết các trường hợp phổ biến, thì việc sử dụng `LSH Brackets with an operator` là giải pháp được recomend nhất nếu API của bạn có dùng filter nâng cao

Ref: <br>
https://www.gvj-web.com/blog/paging-sorting-filtering-restful-api <br>
https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination

