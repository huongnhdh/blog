Title: 2018 chuyện giờ mới kể
Date: 2019-02-06 00:00
Category: Tâm sự
Tags: diary
Slug: 2018-chuyen-gio-chua-ke
Author: HuongNHD
Summary: 2018 đã qua, đối với mỗi người đều có những trải nghiệm của riêng mình, tôi cũng thế , và tôi viết bài viết này để lưu lại những trải nghiệm của tôi trong năm 2018 cùng với một số lưu ý, cũng như chia sẻ cho những người có duyên ghé qua blog của tôi.

## Làm việc tại Topica Edtech Group

Đầu năm 2018, sau tết, cụ thể 24-tháng 2-2018, tôi bay ra Hà Nội để bắt đầu công việc mới (tôi vẫn nhớ như in lần đầu tiên đươc đi máy bay, và cũng là lần đầu tiên được vào Hà Nội với cái khí nóng gần 30oC tại TP. HCM, khi đáp máy bay xuống là 18oC, hôm sau tôi bệnh luôn =]] ) tại Topica Edtech Group (trước đó thì tôi làm cho một start up về mảng big data và đã ngủm mất vì không kiếm đcông ược khách hàng, đấy cũng là một trải nghiệm thú vị, khi nào có thời gian tôi sẽ kể lại, hôm nay tôi chỉ kể chuyện chưa kể năm 2018 =]]). Tổng thời gian tôi làm việc ở Topica là 5 tháng thì tôi phải quay về vì tôi không hợp thời tiết của Hà Nội, ở Topica tôi học hỏi được rất nhiều thứ quý giá. Một điều tôi rất ngạc nhiên khi làm việc ở Topica là có rất nhiều nhân sự trẻ ở đây, ở những công ty khác có thể tôi là nhân sự trẻ nhất, nhưng ở Topica có người còn nhỏ hơn tôi những 4 tuổi (thời điểm đấy tôi mới ra trường đi làm khoảng hơn 1 năm thôi), mặc dù đã hoạt động hơn 10 năm nhưng ở đây mọi người vẫn luôn giữ được lửa startup và luôn làm việc hết tôi cho công việc, đến đây, có thể mọi người nghĩ tôi đang PR quá đà cho Topica, nhưng mà mọi việc đều có 2 mặt của nó cả, nhưng ở đây tôi chỉ muốn nói đến mặt tích cực vì đó là một điều làm tôi rất khâm phục đội ngũ lãnh đạo của Topica. Nói thật khi làm ở Topica mức lương họ trả cho tôi cũng không cao lắm, nếu so với giá bình quân của thị trường. nhưng bù lại tôi có được nhiều thứ hơn, ra Hà Nội, một môi trường, cũng như văn hóa hoàn toàn khác biệt với miền Nam đặc biệt tôi còn là dân miền Tây nữa nên sự khác biệt về cách nói chuyện và văn hóa ứng xử là không hề nhỏ, được làm cho một công ty làm products công nghệ lâu năm và đặc biệt họ còn đánh giá tôi ở mức cuối middle (tức là gần senior đấy =]], trong khi tôi làm việc cũng chỉ hơn một năm thôi), thế là lòng ham hư vinh của tôi lên, quyết định vào vào Topica luôn. Thế đấy, nhưng quyết định của tôi thì tôi thấy không uổng phí tí nào, được làm việc cho một môi trường product (một không khí, và cách làm việc hoàn toàn khác) một sản phẩm đã hoạt động gần 3 năm đó là Edumall, phải công nhận rằng môi trường làm việc ở đây rất năng động, sáng tạo, trẻ và nhiệt huyết nữa
Khen đường lối của Topica thế là đủ rồi, Quay lại chủ đề chính là công nghệ thôi, Lúc tôi gia nhập vào sản phẩm Edumall thì sản phẩm đã vào hoạt động gần ba năm, đội ngũ làm sản phẩm đã loanh quanh đâu đó 200 members, riêng IT thì khoảng 40 rồi, đấy cũng là lúc sản phẩm đang gặp rất nhiều khó khăn về việc mở rộng (về business, về multi tenancy, multi location), cần cải tiến, nâng cấp, chuẩn hóa quy trình làm việc (thêm vào QA, tester), kiểm sóat lỗi hệ thống, khả năng chịu tải của hệ thống khi lượng traffic người dùng tăng đột biết (đặc biệt là dịp lễ tết), xây dựng thêm các giải pháp big data để recommendation, để sale, chăm sóc after sale, re-sale, .. vân vân và mây mây, stack công nghệ chính của Edumall lúc đấy là Ruby on Rails (món này thì chuyên dành cho startup vì nó thiết kế chủ yếu dành cho rapid development), lúc mới vô tôi cực kỳ ghét món này vô cùng, may mắn lúc đó tôi chỉ đọc code và viết lại một số service, module bằng Java Spring, song song đó thì hệ thống được triển khai theo mô hình hướng dịch vụ microservice, deploy trên AWS sử dụng k8s thông qua gitlab-ci và cả Jenkin (tùy đặc trưng của từng service). Vì là triển khai theo mô hình hướng dịch vụ microservice nên việc bạn viết bằng ngôn ngữ gì thì tùy thuộc vào leader của bạn thích ngôn ngữ gì, còn việc của bạn là thích leader nào thì xin vào nhóm đó =]]. Túm lại là là mô hình triển khai, và hoạt động khá hiện đại

Và đây là những điều tôi rút ra được sau khi làm việc tại đây

1. Không phải cứ dựng website bán hàng lên thì sẽ có người mua hàng.
   Khi làm việc ở Edumall, tôi thấy rằng khách hàng chủ yếu của họ đến từ maketing online thông qua các landing page giới thiệu các khóa học là chính, còn việc người dùng đăng ký mua trực tiếp trên hệ thống thì không nhiều (có thể trên trang chủ có quá nhiều sự lựa chọn quá nên họ vô xem xong không biết chọn gì thì đi ra luôn =]])
   Ở đây tôi nhận thấy một điều là chi phí cho IT 3 thì marketing là 4 và sale (kể cả after sale, và chăm sóc khách hàng) là đâu đó khoảng 3 (nếu sản phẩm khác thì có thể là cơ cấu sẽ khác, tùy vào bạn bán sản phẩm gì nữa)

2. Nếu hệ thống bạn xây dựng có kiến trúc tốt ngay từ đầu thì, chi phí dành cho việc maintain sẽ ít đi đáng kể. Cụ thể như tôi đã nói ở trên lúc tôi gia nhập vào vào sản phẩm Edumall thì lúc đấy có khoảng 40IT và gần như 40 IT luôn phải maintain và xử lý điểm nóng của hệ thống,
   các kế hoạch nâng cấp hệ thống luôn phải tạm dừng, mở rộng hệ thống thì luôn dùng giải pháp ngắn hạn là clone mặc dù là có tới 40IT =]], (tôi chỉ đang nói đến thời điểm tôi mới vô), sau đó họ phải tuyển hàng loạt nhân sự mới để vô nâng cấp hệ thống (trong đó có tôi ^^)

Đi sâu hơn vào hệ thống đó chính là bài toán (Đây có lẽ là các bài toán chung của các hệ thống cần mở rộng).

- Distribute transaction
- Muti tenancy
- SSO (single sign on)
- Batch job managerment

Có lẽ đau đầu nhất là bài toán về `Distribute transaction`, Khi nào có thời gian tôi sẽ chém gió tiếp về các bài toán trên

## Sau 2 tháng thất nghiệp

Ôi đời không như là mơ, như đã kể ở trên ở Topica được xem như là một môi trường rất thích hợp cho những người trẻ như tôi, làm việc và rèn luyện chính tôi, thế nhưng tôi lại không phù hợp với không khí ở Hà Nội, tôi buộc phải quay lại HCM sau 5 tháng ở Hà Nội, trong hơn một tháng đầu về tôi không đi đâu cả chỉ ở trong phòng dưỡng lại nhan sắc (bầu không khí tại HN đã hủy hoại nhan sắc của tôi, ôi đê mê !) trong một tháng đó tôi chỉ nhận làm 2 cái landing page để kiếm sống, không có gì đặc biệt cả. Một tháng sau tôi lên linked In và topCV mở trạng thái tìm việc (thời điểm đó là khoảng tháng 8, thị trường chuyển nhượng chưa được sôi động lắm =]] ). Thế là tôi lại phải ôn bài vở để đi phỏng nhiều công ty tây, ta có, lớn, nhỏ có và đó cũng là cơ hội để tôi nhìn lại chính về định hướng, đam mê, điểm mạnh, điểm yếu của bản thân cũng như việc liệu tôi có nên làm công ăn lương suốt đời không, và đấy cũng là lúc tôi manh nha ý định về kinh doanh, nhưng muốn kinh doanh thì đối với người ngoại đạo như tôi (cha mẹ làm ruộng, bản thân lại là dân kỹ thuật) cần phải biết các khái niệm về đầu tư, và kinh doanh, thế là tôi lại kiếm các cuốn sách về kinh doanh để đọc, với sự hướng dẫn của bạn bè thì cuốn sách đầu tiên mà tôi đọc là "Cha Giàu, Cha nghèo", đây là một serial sách về kinh doanh, được xem là best seller. Chưa chắc đọc xong cuốn sách này bạn sẽ trở thành nhà kinh doanh tốt, nhưng chắc chắn bạn sẽ có một tư duy tốt hơn về tài chính, đấy là cảm nhận của tôi. Quay lại việc đi phỏng vấn, sau khi phỏng vấn qua nhiều công ty, nhưng kết quả không làm tôi hài lòng lắm (kiểu như `theo tình thì tình chạy, chạy tình theo` đó mà ^~^, hazz ), Và sau 2 ngày về quê để thoải mái tinh thần, tôi đi lên và phỏng vấn lại vào công ty đang làm hiện tại và đi làm luôn vào đầu tháng 9 ^^.

Dù nhiều lý do nhưng đây là khoảng thời gian thất nghiệp đầu tiên tôi có từ khi đi làm (không có thu nhập hàng tháng là thất nghiệp rồi), để chuẩn bị tránh cho việc thất nghiệp trong tương lai chúng ta cần chuẩn bị hành trang đầy đủ:

- Nên có một công việc mới trước khi nghỉ làm ở chỗ cũ.
- Nếu bạn nghỉ việc trong trạng thái chưa biết trước thì sao (ví dụ công ty phá sản và bạn mất việc) nên có một công việc kinh doanh để tài chính luôn được đảm bảo ^~^

## Một công việc mới

Thế là đầu tháng chín tôi đã bắt đầu làm việc taị công ty mới, mọi thứ đều tốt, nhưng có một điều tôi phải công nhận là ... `ghét của nào trời trao của ấy`, ở đoạn thời gian làm ở Topica tôi có nói là không thể thích nổi phong cách của `Ruby On Rails`, thế nhưng khi qua đây tôi lại gắn bó với RoR =]], tuy nhiên không phải thế mà tôi nhàm chán với công việc, tôi đi tìm kiếm và khám phá những điều thú vị từ RoR, hiểu hơn về nó, làm cho nó hoạt động hiệu quả hơn. Hơn nữa tại đây tôi có thể gặp được những người lãnh đạo mới với những tầm nhìn mới, quan điểm mới (hãy nhớ rằng đồng nghiệp có thể chỉ gắn bó trong thời gian ngắn, nhưng lãnh đạo là người có thể gắn bó với bạn cho đến lúc bạn nghỉ việc luôn)về việc xây dựng asset, quan điểm về tầm quan trọng của security, cách quản lý member trong team, ...

Một công việc mới chính là một khởi đầu mới, nó như thế nào phụ thuộc vào bạn nhìn nó như thế nào, nhưng nếu bạn đã chọn thì hãy hết tôi với nó! Nếu bạn có một mục tiêu tốt cho tương lai, thì chắc chắn bạn sẽ không bị lạc lõng giữa dòng đời

## Lời cuối cùng, mối quan hệ giữa người lao động và doanh nghiệp

Lời cuối cùng của bài viết, tôi muốn chia sẻ một chút quan điểm giữa người lao động và chủ doanh nghiệp.

Trong cuộc sống luôn luôn có biến số và kết quả phương trình toán học đó luôn tùy thuộc vào bạn gán cho biến số đó giá trị bao nhiêu.
Quan hệ giữa người chủ doanh nghiệp và người lao động cũng như một phương trình vậy, nếu chủ doanh nghiêp đã đưa sẵn kết quả cho bạn, và bạn tự tìm ra giá trị cuả mình và đặt các biến số của phương trình đó sao cho phương trình cân bằng, vậy thì quá ổn rồi, còn gì phải nói, thế nhưng có nếu người lao động đạt các giá trị vào các biến cao hơn, hoặc thấp hơn, vậy thì chủ doanh nghiệp sẽ phải có một kết quả khác để cho phương trình được cân bằng (Kết quả ở đây không hẳn là tiền bạc, đó có thể là danh vọng, địa vị, hay tình cảm 0_0). Vậy nếu phương trình không cân bằng thì sao?

- Trường hợp 1: Chủ doanh nghiệp đưa ra kết quả `cao hơn`: Vậy thì người lao động đó sẽ bị đuổi, hoặc giảm lương, hoặc có thể không bị gì, nhưng dù là kết quả nào thì giá trị con người đó cũng sẽ giảm.

- Trường hợp 2: Chủ doanh nghiệp đưa ra kết quả `thấp hơn`, vậy thì sớm hay muộn người lao động đó cũng sẽ ra đi. Tôi hay nghe người khác nói ràng anh ta / cô ta chăm chỉ làm việc vô cùng nhưng vẫn không được lên lương hay lên chức, đó thường là những lời ngụy biện. Nếu người đó thật sự có bản lĩnh và có cống hiến lớn với doanh nghiệp mà bị đối xử bất công thì chắc chắn đã có doanh nghiệp khác, hoặc người khác mời đi để cống hiến cho họ rồi, không còn ở đó mà than trách đâu =]]. Bởi thế hãy tỉnh thức nhé ^^

Tôi không đồng ý với quan điểm rằng người làm lâu năm ở một công ty thì trung thành hơn, còn người hay nhảy việc là người có phẩm cách không tốt. Điều đó còn phụ thuộc vào họ làm gì, và doanh nghiệp thuê họ đối đãi với họ thế nào nữa.

Đây chỉ là chút quan điểm cá nhân của tôi về mối quan hệ giữa người lao động và doanh nghiệp, là quan điểm nên có thể đúng hoặc sai tùy vào từng cá nhân (tôi không nói đó là chân lý nhé). Có thể ngày này năm sau quan điểm của tôi sẽ thay đổi, tất cả đều phụ thuộc vào trải nghiệm mà bạn trải qua.

Năm mới 2019 sang, chắc chắn cũng sẽ là một năm đầy hứa hẹn với nhiều sự kiện diễn ra, hãy chào đón nó trong một tâm trạng vui vẻ, tràn đầy nhé ^^
