Title: How cookies track you around the web and how to stop them
Date: 2019-03-06 10:20
Category: Security
Tags: privacy, security
Slug: stop-cookies-tracking
image: cookies.svg
opengraph_image: cookies.svg
Authors: HuongNHD
Summary: How cookies track you around the web and how to stop them
# How cookies track you around the web and how to stop them

Ref: https://privacy.net/stop-cookies-tracking
Translated by: HuongNHD
---

![cookies](../images/cookies.svg){:height="80vw" min-height="300px"}
Nếu lướt web bằng các loại browser phổ biển như Chrome, Firefox, Internet Explorer, Edge, hoặc Safari, thì chắc là trong túi cookies của chúng ta đã có khá nhiều bánh cookies rồi. Cookies được sử dụng để ghi lại những thông tin cơ bản của website mà chúng ta lướt qua (ví dụ: thông tin login, thông tin giỏ hàng, ngôn ngữ trên giao diện web, ...). Nó được tạo ra bởi website và tồn tại bên phía browser cho đến khi nó expire (hết hạn đó) .

Nhiều Cookies là vô hại, trong khi có những cookies vẫn hoạt động trên những website không sinh nó, dùng để thu thập các thông tin về hành vi cũng như từng cú click của bạn. Ở đây tôi muốn nó đến các `third-party persistent cookies` hay với một cách dễ hiểu hơn thì nó là `tracking cookies`.

**Tracking cookies** can thiệp sâu vào sự riêng tư của người duyệt web nhiều đến nỗi nhiều chương trình diệt virus liệt chúng vào spyware (nghĩa là phần mềm gián điệp). Mặc dù nó mang tiếng xấu là thế  nhưng chúng lại phổ biến đến nỗi mà chúng ta không thể nào tránh khỏi chúng. Trong bài viết này chúng ta sẽ đi tìm hiểu chi tiết và giải thích cách các tracking cookies theo dõi `web activity` của chúng ta như thế nào, tại sao chúng lại phổ biến đế thế và làm thế nào để ngừng chúng lại


## Types of cookies explained - Một số thể  loại cookies

Đầu tiên, cần lướt qua các loại cookies chính là session cookies và persistent cookies. Có bao giờ bạn đi đến browser setting và xóa mọi cookies thì đó cũng chính là việc bạn đang xóa các persistent cookies.

### 1. Session cookies
Loại cookies cơ bản nhất là session cookie. Session cookie chỉ tồn tại trong bộ nhớ tạm (temporary memory) và sẽ được xóa ngay khi bạn đóng trình duyệt. Bất kỳ cookies nào được tạo ra mà không có hạn sử dụng (expiration date) thì tự động hiểu đó là session cookie. Một trong những cách sử dụng phổ biến của `session cookie` là để ghi nhớ giỏ hàng trên một site thương mại điện tử  (Mặc dù ngày nay đa số họ sẽ lưu trên database hay server )

### 2. First-party persistent cookies
`Persisten cookies` được viết trên bộ nhớ thiết bị (memory device) cũng với một hạn sử dụng. và nó chỉ được sử dụng bởi website tạo ra nó  và it can `last however long the website dictates`. Nó được để lại trên device ngay cả khi đã đóng trình duyệt. Trình duyệt sẽ sử dụng `first-party persistent cookie` để có nhiều cải tiến về  chất lượng phục vụ, như việc nhớ bạn đã đăng nhập và không cần đăng nhập lại mỗi khi quay trở lại một trang web. 

### 3. Third-party persistent cookies
`Third party persistent cookies`, như đã biết về  `tracking cookie` cũng là ý chính trong bài viết này. Cũng giống như `first-party persistent cookie` những cookies này được lưu trong bộ nhớ của thiết bị và có một hạn sử dụng. Không giống như sự đa dạng của `first-party persistent cookie`, tuy nhiện những cookies này được phép truy cập trên những web site không tạo ra chúng. Điều này cho phép người tạo ra cookie này có thể thu thập và nhận về bất kì dữ liệu nào về  thời gian cũng như resource của chúng khi truy cập 1 page.

## Where do tracking cookies come from? - Tracking cookie đến từ đâu?
Những website ngày nay thì hiếm khi chỉ tạo ra được từ mã code và nội dung từ chủ trang web hay người quản trị, thay vào đó họ sử  dụng các resource có sẵn để  xây dựng và thêm các chức năng cần thiết để  hoạt động. Những resource này rất hữu ích đôi khi là cần thiết cho sự cạnh tranh. Nhưng thật không may, chính những resource này lại thường là những thủ phạm chính cho việc online tracking. Một số resource phổ biến và có sử dụng `tracking cookie` là: 
- Advertisements - dịch vụ quảng caó
- Social media widgets (Like and Share buttons, comments sections, etc - nút like, share, vùng bình luận) 
- Web analytics - Các dịch vụ phân tích web site

Ngay cả khi bạn không click vào quảng cáo, click nút share hay bình luận thì các thông tin của tracking cookies vẫn sẽ được gửi về  server của người tạo các cookie này. Ngay khi bạn load trang thì thông tin cookie đã được giửi đến server nơi mà nó được tạo, nếu cookie không tồn tại thì resource vẫn có thể  tạo 1 cái khác.

Chẳng hạn như khi viết bài post này và tôi đã sử dụng hình ảnh được host trên một trang web khác, Trang web kia có thể đã tạo cookie ngay khi tôi vừa truy cập vào bài post này trên browser này của mình (ngay cả khi tôi không thực sự truy cập vào trang web đó mà tôi chỉ load resource từ nó).

Tương tự, hầu như mọi ads và wigets không được host bởi trang web mà nó đang hiển thị. Nó chỉ sử dụng resource được kéo về  từ bên thứ 3 và rồi ... tất cả chúng đều sử dụng cookies.

Theo một báo các của [the Guardian năm 2012](https://www.theguardian.com/technology/2012/apr/23/cookies-and-web-tracking-intro), một số công ty lớn sử dụng trackingcookie bao gồm :

- AddThis
- Adnxs
- Doubleclick
- Facebook
- Google
- Quantserve
- Scorecard Research
- Twitter
- Yieldmanager
## What do tracking cookies know about me? - Tracking cookies lấy đi những thông tin gì?
Tracking cookies thường được sử  dụng cho mục đích quảng cáo, retargeting là chính, `retarget` là một chiến thuật dựa vào thông tin của tracking cookies để hiển thị quảng cáo cho người đẫ  từng  truy cập vào một trang web cụ thể hay thể hiện sự quan tâm đến một sản phẩm cụ thể . Nếu bạn đã mua hoặc thậm chí chỉ nhìn sản phẩm ấy trên Amazon, sau đó bạn thấy các quảng cáo cho các  sản phẩm tương tự trên trang web khác mà bạn ghé qua, thì tức là bạn đã được retargeted. 

Dưới đây là những bước cơ bản để giải thích retargeting làm việc:

1. Bạn đã nhận 1 tracking cookies từ một trang blog yêu thích hoặc một trang web mua sắm nào đó. Cookies này sẽ chứa 1 unique ID  không phải để  định danh bạn hay một cá nhân nào mà là dùng để định dạnh web browser của bạn.

2. Chủ của 1 web site shopping nào đó đăng ký và trả tiền cho các nền tảng quảng cáo ví dụ như Google.

3. Google ads không cứng nhắc, khi bạn ghé vào 1 web site sử dụng google ads để kiếm tiền, thì website này sẽ cho thấy cookies và gửi về  Google thông qua ads. Google lúc này sẽ thấy được ID của bạn được lưu trong cookies và nhận ra rằng nó đến từ một shoping site yêu thích của bạn.

4. Và sau đó thì Google sẽ hiển thị một quảng cáo phù hợp cho shopping site

Tương tự như thế , các ads khác của Google cũng có thể sử dụng cookies của bạn nếu cookies này đáp ứng được một số tiêu chí của retargeting.Như thế có thể thấy cookie này của bạn  không chỉ có lợi với mỗi trang web nơi bạn nhận nó.

Nó có thể vô hại trong những lần đầu, nhưng những tracking cookies này có thể  thu thập rất nhiều thông tin về cách bạn duyệt web. Khi đó thì google ads có ở mọi nơi. Đó là những công ty quảng cáo online lớn nhất thế giới, và ở đây có rất nhiều, rất nhiều công ty như thế. Bởi vì đó, những công ty quảng cáo này có thể cùng nhau tìm hiểu lịch sử  duyết web của bạn theo 1 trình tự nào đó và trong bao lâu. Khi mà cookies được gửi đến server của họ nó thường chứa các thông tin về những website mà bạn đã truy cập

## What makes a cookie? - Cookies có gì?
Nếu kiểm tra cookie file tại một trang web bất kỳ bằng [EditThisCookies](http://www.editthiscookie.com), ta thấy, Cookies chỉ có 3 component là chủ yếu là: name, value, attribute 
![alt text](https://www.editthiscookie.com/images/posts/edit-cookie-2.png)

- Name được sử dụng bởi website và ads để nhận dạng cookie và mục đích sử dụng của nó.
- The value là thành phần chưa unique ads ID lưu trữ nhờ đó tracker creator có thể nhận diện bạn khi bạn truy cập vào những website khác. Nó thường là một chuỗi số và ký tự được sinh ra ngẫu nhiên, hoặc không là một chuỗi mã hóa các thông tin nêu trên
- The attribute chứa thông tin về đặc tính của cookie như: HSD của cookie, nếu cookie không được set HSD thì cookie đó sẽ bị hủy khi browser đóng. Tracking cookies bắt buộc phải có hạn sử dụng.
- Nếu cookies có thể  được sử  dụng từ domain khác
- Liệu rằng cookies có thể  được gửi đi trong insecure connection hay không. Đơn giản là kiểm tra nó với HTTPs
- Liệu rằng cookies có thể  bị truy cập bằng JavasScript hay không. Tắt nó đi để ngăn cản các XSS attack mà có thể sử dụng đánh cắp thông tin đăng nhập sửa đổi cookies cho mục đích bất chính. 

--- tobe continue ....
## How to stop tracking cookies
## Do not track
## Privacy Badger
## Disconnect
## Adblock Plus
## Other tracking methods
## Referrer URLs
## Web beacons
## Browser fingerprinting
## Cookie syncing
## Supercookies

