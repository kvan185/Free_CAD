# HỆ THỐNG TRỐNG RANG: CÁNH ĐẢO LA SẮT CHẠM CÂY TRỤ ĐỂ HÀN VÀO & 10 CÂY CHỐNG XEN KẼ (FREECAD 3D)

---

## 1. Thông Số Kỹ Thuật: Cánh Đảo Trong Chạm Trực Tiếp Cây Trụ Để Hàn Vào

### A. 5 CÁNH ĐẢO TRONG (BẢN RỘNG 10CM, DÀY 0.8CM, DÀI 65CM, KÉO DÀI RA PHÍA SAU)
- **Vật liệu**: Thanh la sắt bản rộng **$10\text{ cm}$ ($100\text{ mm}$)**, dày **$0.8\text{ cm}$ ($8\text{ mm}$)**.
- **Vị trí theo bán kính (Nằm ngay giữa thân 5 cây chống)**:
  - Cây chống dài từ cây láp ($R = 32.5\text{ mm}$) đến thành trống ($R = 392\text{ mm}$), có điểm chính giữa ở $R = 212.25\text{ mm}$.
  - Cánh đảo trong bản $10\text{ cm}$ được đặt đối xứng ngay điểm giữa: **$R_{\text{in}} = 162\text{ mm} \rightarrow R_{\text{out}} = 262\text{ mm}$** (tâm cánh $R = 212\text{ mm}$).
  - **Khoảng cách đến cây láp**: Cách mặt cây láp **$129.5\text{ mm}$ ($\approx 13\text{ cm}$)** $\rightarrow$ **Tuyệt đối KHÔNG áp sát vào cây láp, tạo khoảng trống thông thoáng cực lớn quanh trục.**
  - **Khoảng cách đến vỏ trống**: $130\text{ mm}$ ($13\text{ cm}$) đối xứng hoàn hảo.
  - **Khoảng cách đến cánh ngoài**: Cách mép trong cánh ngoài $60\text{ mm}$ ($6\text{ cm}$).
- **Vị trí dọc trục & Chiều dài (Kéo dài ra phía sau)**:
  - Chiều dài: **$65\text{ cm}$ ($650\text{ mm}$)**.
  - Trải từ tầng 5 cây chống gần đầu ($Y = -400\text{ mm}$), đi xuyên qua và gối hàn lên tầng 5 cây chống giữa ($Y = +100\text{ mm}$), rồi **kéo dài tiếp thêm $15\text{ cm}$ về phía sau** đến $Y = +250\text{ mm}$.
  - Cách miệng sau của trống $25\text{ cm}$ để luồng gió hút khói và cửa cấp hạt thông thoáng hoàn hảo.
- **Bước xoắn & Góc xoắn**: Bước xoắn $P = 1083.3\text{ mm}$, `lefthand = True` $\rightarrow$ Xoắn ngược đúng **$6/10$ vòng ($216^\circ$)**.
- **Tác dụng**: Đón dòng hạt rơi từ đỉnh xuống vùng giữa và hắt ngược lại theo chiều $Y-$, tạo luồng đối lưu tuần hoàn liên tục.
- **Phân bố**: 5 cánh ở các góc **$36^\circ, 108^\circ, 180^\circ, 252^\circ, 324^\circ$**.
- **Màu hiển thị 3D**: Xanh ngọc lục bảo tươi sáng.

---

### B. 5 CÁNH ĐẢO NGOÀI (CHẠM 5 CÂY CHỐNG ĐỂ HÀN & BÁM THÀNH TRỐNG)
- **Vật liệu**: Thanh la sắt bản rộng **$7\text{ cm}$ ($70\text{ mm}$)**, dày **$0.5\text{ cm}$ ($5\text{ mm}$)**.
- **Bán kính làm việc**: Cạnh ngoài bám sát thành trong trống $R = 392\text{ mm}$, cạnh trong $R = 322\text{ mm}$ (cao đứng đúng $7\text{ cm}$).
- **Chiều dài trục**: $H = 960\text{ mm}$ (từ $Y = -480\text{ mm}$ đến $+480\text{ mm}$).
- **Bước xoắn & Độ xoắn**: $P = 1600.0\text{ mm}$ $\rightarrow$ **Giữ nguyên chuẩn xác độ xoắn $6/10$ vòng ($216.0^\circ$)**.
- **Căn chỉnh pha tiếp xúc hàn**:
  - Tại vị trí tầng 5 cây chống bên 1 ($Y = -400\text{ mm}$), quãng đường xoắn từ gốc $Y = -480\text{ mm}$ là $\Delta Y = 80\text{ mm}$.
  - Góc xoắn tích lũy tại $Y = -400\text{ mm}$ là: $\frac{80}{1600} \times 360^\circ = +18.0^\circ$.
  - Bù góc lệch pha ban đầu: **`offset_goc = -18.0°`**.
  - **Kết quả**: Tại $Y = -400\text{ mm}$, cả 5 cánh đảo ngoài đi qua chính xác các góc $0^\circ, 72^\circ, 144^\circ, 216^\circ, 288^\circ$, **chạm khít 100% không còn khe hở vào 5 cây chống để thợ hàn đính/hàn ngấu liên kết chắc chắn!**
- **Tác dụng**: Cào sát thành trống, cuốn và xúc hạt cuộn tịnh tiến xuôi liên tục theo chiều $Y+$.
- **Màu hiển thị 3D**: Đỏ cam nổi bật.

---

### C. HỆ THỐNG 10 CÂY CHỐNG BỐ TRÍ XEN KẼ NHAU (VỪA CHẠM CẢ 2 TẦNG ĐỂ HÀN)
- **Vật liệu**: **Ống sắt tròn $\varnothing 20\text{ mm}$, rỗng ruột, dày $2\text{ mm}$** (ĐK trong $\varnothing 16\text{ mm}$).
- **Bên 1 - 5 cây gần đầu** (Cách miệng trống $10\text{ cm}$ $\rightarrow$ $Y = -400\text{ mm}$):
  - Góc ban đầu: Bù góc pha **$-4.5^\circ$** $\rightarrow$ Các góc: **$-4.5^\circ, 67.5^\circ, 139.5^\circ, 211.5^\circ, 283.5^\circ$**.
  - **Tiếp xúc**: Vừa chạm sát sườn mặt bên của 5 cánh ngoài la sắt (khoảng cách $0.687\text{ mm}$), **hoàn toàn giống như 5 cây ở giữa**, không bị cắt xẻ vào lòng ống, tạo góc tiếp xúc lý tưởng để thợ hàn đường hàn ngấu.
- **Bên 2 - 5 cây ở giữa** (Cách miệng lỗ đầu kia $40\text{ cm}$ $\rightarrow$ $Y = +100\text{ mm}$):
  - Góc ban đầu: **$+36.0^\circ$** $\rightarrow$ Các góc: **$36^\circ, 108^\circ, 180^\circ, 252^\circ, 324^\circ$**.
  - **Tiếp xúc**: Vừa chạm sát sườn mặt bên của 5 cánh ngoài (khoảng cách $0.687\text{ mm}$).
- **Tổng kết**: Cả 10 cây chống đều tiếp xúc tiếp tuyến êm ái ("vừa chạm") với 5 cánh ngoài để hàn.

---

### D. HỆ THỐNG TRỐNG RANG 2 LỚP CÁCH KHÍ & CÂY LÁP
- **Vỏ trống trong**: Dài $1\text{ m}$ ($1000\text{ mm}$), đường kính ngoài $80\text{ cm}$ ($800\text{ mm}$), thành dày $0.8\text{ cm}$ ($8\text{ mm}$, $R_{\text{in}} = 392\text{ mm} \rightarrow R_{\text{out}} = 400\text{ mm}$).
- **Lớp áo ngoài cách khí**:
  - Hở **$1\text{ cm}$ ($10\text{ mm}$)** đệm không khí so với vỏ trong ($R_{\text{ao\_in}} = 410\text{ mm}$).
  - Độ dày vỏ ngoài: **$0.5\text{ cm}$ ($5\text{ mm}$)** ($R_{\text{ao\_out}} = 415\text{ mm} \rightarrow \varnothing 830\text{ mm} = 83\text{ cm}$).
  - Chiều dài: $1\text{ m}$ ($1000\text{ mm}$).
  - **Tác dụng**: Tạo lớp đệm khí cách nhiệt chống táp lửa trực tiếp, tránh cháy xém hạt và giữ nhiệt đối lưu hoàn hảo.
- **Cây láp (cây trụ chính)**: Dài tổng $1\text{ m}2$ ($1200\text{ mm}$), thân giữa $\varnothing 65\text{ mm} \times 1000\text{ mm}$ ($R = 32.5\text{ mm}$), 2 đầu tiện bậc $\varnothing 60\text{ mm} \times 10\text{ cm}$ ($100\text{ mm}$).

### E. HỆ THỐNG 2 MẶT MÁY GÁ TRỐNG (TRƯỚC & SAU): SẮT TẤM DÀY 1.8CM, VÒNG TRÒN PHI 96CM, HÌNH THANG CHÂN 1.1M
- **Vật liệu & Độ dày**: Sắt tấm kết cấu chịu lực dày **$1.8\text{ cm}$ ($18\text{ mm}$ / 18 ly)** nguyên khối.
- **Bố trí 2 đầu máy đối xứng gá trống**:
  - **Mặt máy trước**: Tọa độ $Y = -518.0\text{ mm} \rightarrow -500.0\text{ mm}$ (ngay miệng trước của trống).
  - **Mặt máy sau**: Tọa độ $Y = +500.0\text{ mm} \rightarrow +518.0\text{ mm}$ (ngay miệng sau của trống).
  - Khoảng cách lọt lòng giữa 2 mặt máy: Đúng **$1000\text{ mm} = 1.0\text{ m}$**, ôm trọn chiều dài thân trống rang.
- **Phía trên hình tròn lớn hơn 10cm cong thắt eo vào 1 tí**:
  - Cung tròn bán kính $R = 480\text{ mm}$ (**$\varnothing 960\text{ mm} = 96\text{ cm}$**, lớn hơn $10\text{ cm}$ so với $\varnothing 86\text{ cm}$ trước đó), bao phủ rộng rãi lớp vỏ áo ngoài ($R_{\text{ao}} = 415\text{ mm}$) với vành gờ che bảo vệ an toàn $65\text{ mm}$ ($6.5\text{ cm}$) mỗi bên.
  - Cung tròn uốn cong qua đường xích đạo ($Z = 0$), tiếp tục thắt cong vào trong 1 tí đến góc $-40^\circ$ ($X = \pm 367.7\text{ mm}, Z = -308.5\text{ mm}$) ôm sát theo sườn dưới của trống.
- **Phía dưới kết hợp liền khối thành hình thang cân (bên dưới dài hơn bên trên)**:
  - **Đáy trên của hình thang**: Chính là eo thắt cong vào của cung tròn, bề rộng $W_{\text{top}} = 735.4\text{ mm} \approx 735\text{ mm}$ tại $Z = -308.5\text{ mm}$.
  - **Đáy dưới của hình thang**: Nằm phẳng trên sàn xưởng tại $Z = -850.0\text{ mm}$, bề rộng **$W_{\text{bottom}} = 1100\text{ mm} = 1.1\text{ m}$** ($X = -550\text{ mm} \rightarrow +550\text{ mm}$).
  - Đúng chuẩn hình thang cân với **đáy dưới ($1100\text{ mm}$) dài hơn đáy trên ($735\text{ mm}$)**.
  - Hai cạnh sườn xiên choãi xuống mặt đất với góc nghiêng $\approx 71.4^\circ$.
  - Tổng chiều cao mặt máy từ đỉnh vòng tròn đến đáy phẳng là **$1330\text{ mm}$ ($1.33\text{ m}$)** (từ $Z = -850\text{ mm}$ đến $Z = +480\text{ mm}$).
  - **Tác dụng**: Cặp chân đế phẳng siêu rộng $1.1\text{ m}$ ở hai đầu tiếp xúc vững chắc trên mặt sàn hoặc dễ dàng bắt bu-lông vào dầm thép bệ máy, chống rung lắc, chống lật tuyệt đối khi trống quay đảo hàng tạ nông sản.
- **Lỗ lọt đầu cốt ở cả 2 mặt máy**: Mỗi mặt có 1 lỗ tròn đường kính **$\varnothing 65\text{ mm}$** ($R = 32.5\text{ mm}$) tại tâm $(0, 0)$, lọt đầu cốt láp $\varnothing 60\text{ mm}$ với khe hở an toàn $2.5\text{ mm}$ đều quanh cốt. Mỗi đầu cốt láp nhô ra ngoài mặt bích đúng **$82\text{ mm}$** để gá lắp gối bi đỡ trục (UCP/UCFL) và puly/nhông xích truyền động.
- **Tính năng cơ học**: Cả 2 mặt máy là chi tiết **tĩnh (cố định vào khung bệ máy)**, đứng yên làm bệ đỡ vững chắc cho toàn bộ trống quay.

---

### G. MIỆNG RA HÀNG TẠI MẶT TRƯỚC: DÀI 50CM, 2 BÊN THÀNH CAO ĐÚNG 10CM (TỪ MÉP DƯỚI LÊN), ĐÁY CONG THEO TRỐNG R392MM
- **Vị trí gia công**: Cắt xuyên thủng qua tấm thép dày **$1.8\text{ cm}$ ($18\text{ mm}$)** của Mặt máy trước (`obj_mat_truoc`, $Y = -518\text{ mm} \rightarrow -500\text{ mm}$). Mặt máy sau giữ liền khối kín 100% để chống lọt khí.
- **Biên dạng hình học chuẩn xác**:
  - **2 bên thành đứng**: Cao đúng **$10\text{ cm} = 100\text{ mm}$** tính từ mép dưới của cung tròn lòng trống ($Z = -301.9\text{ mm}$) thẳng đứng lên ($Z = -201.9\text{ mm}$) tại hai bên biên $X = -250.0\text{ mm}$ và $X = +250.0\text{ mm}$.
  - **Cạnh trên (Đường thẳng)**: Đường thẳng nằm ngang dài đúng **$50\text{ cm} = 500\text{ mm}$** (từ $X = -250\text{ mm}$ đến $X = +250\text{ mm}$) tại cao độ $Z = -201.9\text{ mm}$.
  - **Cạnh dưới (Đường cong theo trống)**: Cung tròn uốn cong ôm sát thành trong của trống rang với bán kính **$R = 392\text{ mm}$** (từ $X = -250\text{ mm}, Z = -301.9\text{ mm}$ qua đáy thấp nhất $X = 0, Z = -392.0\text{ mm}$ đến $X = +250\text{ mm}, Z = -301.9\text{ mm}$).
  - **Chiều cao lớn nhất tại tâm (từ đáy lên đỉnh)**: Đạt **$190\text{ mm} = 19.0\text{ cm}$** (từ $Z = -392.0\text{ mm}$ lên $Z = -201.9\text{ mm}$), mở rộng khẩu độ đón luồng hạt trút ra cực kỳ thông thoáng.
- **Ưu điểm cơ khí & Công năng vận hành**:
  - **Xả sạch 100% không đọng hạt**: Đáy miệng xả trùng khớp hoàn hảo với thành trong lòng trống ($R = 392\text{ mm}$), không có bất kỳ gờ hay bậc cản nào $\rightarrow$ Nông sản/cà phê sau khi rang chín được các cánh đảo ngoài xúc trút trơn tru ra ngoài không hề bị sót hay vướng cháy khét.
  - **Đảm bảo độ cứng vững kết cấu**: Khoảng "thịt" thép nguyên khối chịu lực giữa cạnh trên miệng xả ($Z = -201.9\text{ mm}$) và mép dưới lỗ cốt trục $\varnothing 65\text{ mm}$ ($Z = -32.5\text{ mm}$) còn tới **$169.4\text{ mm} \approx 17\text{ cm}$**. Tấm thép 18 ly siêu dày giữ vững độ cứng chịu tải rung động mà không hề bị võng hay biến dạng.
  - **Khoảng sáng xả liệu thoáng rộng**: Từ đáy miệng xả ($Z = -392\text{ mm}$) xuống mặt tấm chân đế ($Z = -850\text{ mm}$) có khoảng cách tĩnh lên đến **$458\text{ mm} \approx 46\text{ cm}$**, cực kỳ thuận tiện để bố trí máng hứng, phễu rót và đưa bàn làm nguội/thau hứng cà phê vào bên dưới.

---

### H. LỖ THĂM HÀNG PHI 30MM & CÂY THĂM HÀNG NẰM NGANG CÂY LÁP (KHÔNG CẤN CÁNH ĐẢO)
- **Vị trí gia công trên Mặt máy trước**:
  - Tọa độ tâm lỗ: **Nằm ngang cây láp ($Z = 0.0\text{ mm}$)**, bố trí phía bên trái tại **$X = -200.0\text{ mm}, Z = 0.0\text{ mm}$** (vị trí góc 9 giờ đón trọn dòng hạt cuộn trút xuống).
  - Đường kính lỗ: **$\varnothing 30\text{ mm}$ ($R = 15\text{ mm}$)**, khoan xát xiên qua tấm sắt dày $1.8\text{ cm}$ ($18\text{ mm}$) của mặt máy trước.
- **Cấu tạo Cây thăm hàng (Trier / Sampler spoon)**:
  - **Thân ống & Máng xúc mẫu (Inox)**: Ống inox $\varnothing 24\text{ mm}$, có bích chặn $\varnothing 38\text{ mm}$ tì lên mặt ngoài. Chiều sâu đút vào trống $7.2\text{ cm}$ (đầu tip tại $Y = -427.6\text{ mm}$), phay rãnh lòng máng ngửa lên trên ($+Z$) hứng trọn hạt rơi.
  - **Tay cầm cách nhiệt**: Gỗ tiện công thái học $\varnothing 32\text{ mm}$, dài $11\text{ cm}$, nhô ngang sang bên trái phía trước mặt máy tại cao độ $Z = 0$, chống nóng an toàn tuyệt đối khi rút/xoay lấy mẫu thử.
- **Tư thế lắp đặt: ĐỂ XÉO TRONG MẶT PHẲNG NẰM NGANG ($Z = 0$)**:
  - Góc xiên vào tâm: $\approx 16.7^\circ$ trong mặt phẳng nằm ngang ($Z = 0.0\text{ mm}$, vector $\vec{V} = (30, 100, 0)$) hướng chếch vào lòng trống.
  - Hướng miệng xúc mẫu: Ngửa thẳng lên trên ($+Z$) để dòng nông sản/hạt cà phê đảo cuộn từ đỉnh trống rơi tự nhiên lọt đầy máng.
- **Tính toán cơ khí: TUYỆT ĐỐI KHÔNG CẤN CÁNH ĐẢO**:
  - **Với 5 Cánh đảo ngoài ($R = 322 - 392\text{ mm}$)**: Cây thăm nằm ở bán kính $R = 175.6\text{ mm}$, cách xa mép trong cánh ngoài tới **$146.4\text{ mm} \approx 14.6\text{ cm}$** $\rightarrow$ Tuyệt đối an toàn.
  - **Với 10 Cây chống tròn ($\varnothing 20\text{ mm}$ tại $Y = -400\text{ mm}$)**: Đầu tip cây thăm dừng tại $Y = -427.6\text{ mm}$, cách mép cây chống tới **$17.6\text{ mm}$** khoảng hở an toàn.
  - **Với 5 Cánh đảo trong (bắt đầu tại $Y = -400\text{ mm}$)**: Cây thăm cách đầu cánh trong tới **$27.6\text{ mm}$**.
  - **Với Cốt trục chính / Cây láp ($\varnothing 65\text{ mm}$, $R = 32.5\text{ mm}$)**: Cách mặt trục láp tới **$143.1\text{ mm} \approx 14.3\text{ cm}$**.
  - **Kết luận**: Cây thăm hàng nằm ngang trục láp đạt độ tiện dụng tối ưu, đứng yên hoặc xoay rút lấy mẫu trơn tru khi máy đang vận hành mà không hề va quẹt vào bất kỳ chi tiết quay nào!

---

### I. CỬA BUỒNG ĐỐT MẶT SAU: LỖ 50x30CM, TẬN DỤNG TẤM SẮT ĐÃ CẮT LÀM CỬA, KHE CẮT 1MM, 2 BẢN LỀ MỞ VỀ BÊN TRÁI
- **Vị trí gia công**: Cắt bằng máy CNC xuyên thủng qua tấm thép dày **$1.8\text{ cm}$ ($18\text{ mm}$)** của Mặt máy sau (`obj_mat_sau`, $Y = +500.0\text{ mm} \rightarrow +518.0\text{ mm}$).
- **Kích thước lỗ khoét khung**:
  - **Chiều dài (bề rộng theo phương ngang)**: **$50\text{ cm} = 500\text{ mm}$**, cân đối chính giữa từ $X = -250.0\text{ mm}$ đến $X = +250.0\text{ mm}$.
  - **Chiều cao (theo phương đứng)**: Giảm còn đúng **$30\text{ cm} = 300\text{ mm}$** (từ $Z = -800.0\text{ mm}$ lên $Z = -500.0\text{ mm}$).
  - **Khoảng cách tới chân máy**: Đáy mép dưới đặt tại **$Z = -800.0\text{ mm}$**, cách chân đế máy ($Z = -850.0\text{ mm}$) đúng **$5\text{ cm} = 50\text{ mm}$**.
- **Cấu tạo cánh cửa tận dụng phôi sắt đã cắt (Kerf cắt 1mm)**:
  - **Dùng lại tấm sắt 18mm đã cắt**: Tiết kiệm vật tư tối đa, vừa khít hoàn hảo vào khung cửa.
  - **Đường cắt (kerf) chuẩn CNC**: Chừa khe hở đều **$1.0\text{ mm}$** cả 4 cạnh xung quanh:
    - Kích thước cánh cửa: Rộng **$49.8\text{ cm} = 498\text{ mm}$** x Cao **$29.8\text{ cm} = 298\text{ mm}$** x Dày **$1.8\text{ cm} = 18\text{ mm}$**.
- **Hệ thống 2 bản lề cối & Khóa cửa (Mở về bên trái)**:
  - **2 Bản lề cối hàn bên trái**: Hàn dọc mép bên trái ($X = +249.5\text{ mm}$, $Y = 518\text{ mm}$ khi đứng nhìn từ phía sau), bố trí tại cao độ $Z = -560\text{ mm}$ và $Z = -740\text{ mm}$. Cối đường kính $\varnothing 20\text{ mm}$ chịu lực siêu bền, cho phép **cánh cửa mở xoay mượt mà về bên trái** góc từ $0^\circ$ đến $120^\circ$.
  - **Tay khóa then gài L-handle bên phải**: Bố trí tại $X = -210\text{ mm}, Z = -650\text{ mm}$, có lưỡi gài giữ chặt cánh cửa khi đóng kín buồng đốt.
- **Tính toán cơ khí & Khoảng cách an toàn**:
  - **Khoảng thịt thép lên cốt trục láp**: Từ đỉnh lỗ ($Z = -500.0\text{ mm}$) lên tới lỗ cốt láp $\varnothing 65\text{ mm}$ ($Z = -32.5\text{ mm}$) tăng lên tới **$467.5\text{ mm} \approx 47\text{ cm}$** thép tấm 18 ly nguyên khối $\rightarrow$ Cực kỳ cứng vững, chống rung lắc hoàn toàn.
  - **Khoảng cách tới gầm trống rang**: Cách đáy vỏ ngoài trống ($Z = -415\text{ mm}$) tới **$85\text{ mm} = 8.5\text{ cm}$** dải thép liền khối bảo vệ.
- **Công năng vận hành thực tế**:
  - Đóng vai trò là **Cửa buồng đốt củi / nạp nhiệt / thông gió**: Dễ dàng mở cửa về bên trái để đưa củi lửa hoặc đầu đốt gas vào, đóng kín cửa khi rang để giữ nhiệt, và mở ra vệ sinh cào tro xỉ định kỳ cực kỳ tiện lợi.

---

### J. BUỒNG ĐỐT CỦI & LÒNG MÁNG GẠCH SA MỐT CAO 50CM ÔM TRỐNG CÁCH 1CM GIỮ NHIỆT TUYỆT ĐỐI (KT 30x5x10CM)
- **Yêu cầu thiết kế**: "tôi chỉ cần gạch cao lên 50cm thôi".
- **Kích thước từng viên gạch sa mốt tiêu chuẩn**:
  - Chiều dài: **$30\text{ cm} = 300.0\text{ mm}$**
  - Chiều rộng: **$10\text{ cm} = 100.0\text{ mm}$**
  - Chiều dày: **$5\text{ cm} = 50.0\text{ mm}$**
  - Mạch vữa xây chịu nhiệt: $1.5\text{ mm}$ sắc nét mô phỏng chân thực kết cấu xây lò.
- **Cấu tạo không gian 3 thành phần & Kỹ thuật cưa gọt gạch ôm sát trống (Nằm gọn dưới trống)**:
  1. **Sàn đáy buồng đốt (Hearth Floor)**:
     - Lát kín trực tiếp trên mặt tấm sắt chân máy từ $Z = -850.0\text{ mm}$ đến $Z = -800.0\text{ mm}$ (dày đúng $5\text{ cm} = 50\text{ mm}$, 1 viên gạch nằm).
     - **Bảo vệ cách nhiệt $100\%$**: Ngăn chặn hoàn toàn nhiệt độ cực cao của than hồng ($800 - 1000^\circ\text{C}$) truyền xuống tấm sắt chân máy $5\text{ mm}$ và sàn xưởng, chống cong vênh bệ máy.
     - **Bằng phẳng khít mép dưới cửa sau**: Mặt sàn gạch ở cao độ $Z = -800.0\text{ mm}$, trùng khớp $100\%$ với ngưỡng dưới của cửa sau ($Z = -800.0\text{ mm}$), giúp thao tác đưa củi vào và cào tro xỉ ra trơn tru tuyệt đối, không có gờ cản trở.
     - Kích thước sàn: Rộng **$700\text{ mm} = 70\text{ cm}$** ($7$ hàng gạch $\times 100\text{ mm}$, $X \in [-350, +350\text{ mm}]$), Dài **$1000\text{ mm} = 1\text{ m}$** ($Y \in [-500, +500\text{ mm}]$) xây so le các hàng.
  2. **Hai vách hông bao đúng 1 lớp gạch dày $10\text{ cm}$, chừa lòng ngang $50\text{ cm}$, cao 9 hàng đến đáy trống**:
     - **Lòng trong chừa đúng ngang $50\text{ cm} = 500\text{ mm}$**: $X \in [-250, +250\text{ mm}]$, khớp hoàn hảo $100\%$ với chiều rộng cửa sau $50\text{ cm}$.
     - **Bao quanh đúng 1 lớp gạch (dày $10\text{ cm} = 100\text{ mm}$)**: Vách trái từ $X \in [-350, -250\text{ mm}]$, vách phải từ $X \in [+250, +350\text{ mm}]$.
     - **Tổng bề rộng phủ bì chỉ $70\text{ cm} = 700\text{ mm}$**: Nhỏ hơn bề rộng eo thắt hẹp nhất của mặt máy ($73.5\text{ cm}$, $X = \pm 367.7\text{ mm}$) $\rightarrow$ Dư an toàn ít nhất $1.8\text{ cm}$ mỗi bên, **lọt thỏm hoàn toàn dưới gầm trống và bên trong mặt máy, tuyệt đối không bị lòi ra ngoài!**
     - **Chiều cao xây đến đáy trống**: Xây **9 hàng gạch** ($45\text{ cm}$ từ sàn gạch, $50\text{ cm}$ từ chân máy) lên tới $Z = -350.0\text{ mm}$.
     - **Kỹ thuật cưa gọt gạch tạo hình ($R_{\text{cắt}} = 425.0\text{ mm}$)**: Cắt vát vòm cong trụ tròn bán kính **$R_{\text{cut}} = 425.0\text{ mm}$** dọc theo trục $Y$.
     - **Khe hở giữ nhiệt tuyệt đối $1\text{ cm} = 10\text{ mm}$**: So với bán kính vỏ áo ngoài $R_{\text{ao}} = 415.0\text{ mm}$, khoảng hở tròn đều là **$425 - 415 = 10.0\text{ mm} = 1\text{ cm}$** ôm sát quanh đáy trống.
     - **Hiệu quả nhiệt động học**: Khí nóng và bức xạ từ than củi bị bẫy kín trong khe hở $1\text{ cm}$ ôm quanh thân trống, không cho nhiệt lượng thoát sang hai bên hông máy, giúp tiết kiệm củi tối đa và tăng tốc độ gia nhiệt trống rang.
  3. **Vách chắn nhiệt phía trước (Front Wall)**:
     - Xây chắn ở đầu trước: $Y \in [-500, -400\text{ mm}]$ (dày $10\text{ cm}$), $X \in [-250, +250\text{ mm}]$ (rộng $50\text{ cm}$).
     - Đỉnh vách được gọt vòm cong $R_{\text{cut}} = 425\text{ mm}$ ôm cách đáy trống ngoài $1\text{ cm}$ (đỉnh tại $X=0$ đạt $Z = -425\text{ mm}$).
     - **Hoàn toàn không cấn miệng ra hàng**: Miệng ra hàng mặt trước nằm từ $Z = -302\text{ mm}$ lên $Z = -202\text{ mm}$, cao hơn đỉnh vách trước tới $123\text{ mm} \approx 12.3\text{ cm}$ $\rightarrow$ Hạt xả trút $100\%$ không bị vướng.
- **Kích thước lòng buồng đốt**: Rộng **$50\text{ cm}$** $\times$ Chiều dài buồng đốt **$90\text{ cm}$** ($Y \in [-400, +500\text{ mm}]$), chứa thoải mái củi dài $60 - 80\text{ cm}$.
- **Cào tro và nạp củi thuận tiện qua cửa sau 50x30cm**: Đáy cửa sau phẳng lì tiếp nối mặt sàn gạch sa mốt, cào tro xỉ ra ngoài dễ dàng trong 1 nốt nhạc.

---

### F. HỆ THỐNG CHÂN ĐẾ MÁY HÌNH CHỮ NHẬT: SẮT TẤM DÀY 0.5CM (5MM), DƯ MỖI BÊN 0.5CM (5MM)
- **Vật liệu & Độ dày**: Thép tấm kết cấu dày chuẩn **$0.5\text{ cm} = 5.0\text{ mm}$ (5 ly)** nguyên tấm.
- **Kích thước bao chuẩn xác tuyệt đối**:
  - **Bề ngang máy (Trục $X$ - Trái & Phải)**:
    - Đáy chân 2 mặt máy có bề rộng $1100.0\text{ mm} = 1.1\text{ m}$ ($X = -550.0\text{ mm} \rightarrow +550.0\text{ mm}$).
    - Dư ra mỗi bên trái và phải đúng **$0.5\text{ cm} = 5.0\text{ mm}$** $\rightarrow$ Biên $X = -555.0\text{ mm} \rightarrow +555.0\text{ mm}$.
    - **Tổng chiều rộng chân đế**: **$W = 1110.0\text{ mm} = 111.0\text{ cm} = 1.11\text{ m}$**.
  - **Chiều dọc máy (Trục $Y$ - Trước & Sau)**:
    - Mặt ngoài mặt máy trước tại $Y = -518.0\text{ mm}$, mặt ngoài mặt máy sau tại $Y = +518.0\text{ mm}$ (khoảng bao phủ $1036.0\text{ mm}$).
    - Dư ra mỗi bên trước và sau đúng **$0.5\text{ cm} = 5.0\text{ mm}$** $\rightarrow$ Biên $Y = -523.0\text{ mm} \rightarrow +523.0\text{ mm}$.
    - **Tổng chiều dài chân đế**: **$L = 1046.0\text{ mm} = 104.6\text{ cm} = 1.046\text{ m}$**.
  - **Chiều cao & Cao độ lắp đặt (Trục $Z$)**:
    - Độ dày tấm: $H = 5.0\text{ mm}$.
    - Đáy 2 mặt máy tựa khít lên mặt trên của chân đế tại $Z = -850.0\text{ mm}$.
    - Mặt dưới chân đế tiếp xúc mặt sàn tại $Z = -855.0\text{ mm}$ (Điểm gốc: $X = -555.0, Y = -523.0, Z = -855.0\text{ mm}$).
- **Tác dụng cơ khí**:
  - Khóa cứng và liên kết 2 mặt máy trước - sau thành một khối khung giằng chassi hoàn chỉnh.
  - Phân bổ đều trọng lượng máy (hàng trăm kg) xuống mặt nền xưởng, triệt tiêu hoàn toàn ứng suất rung lắc khi trống quay đảo nông sản tải nặng.
  - Vành gờ dư $5\text{ mm}$ đều 4 phía tạo đường rãnh chuẩn cho thợ cơ khí chạy đường hàn góc liên kết bệ máy hoặc khoan lỗ bắt bu-lông neo chân đế (anchor bolts).

---

## 2. Bảng Điều Khiển Thông Minh (Smart Control Dashboard)
- **Auto-Clean**: Tự động đóng tất cả tab cũ trong FreeCAD trước khi mở mới.
- **Giao diện tinh gọn, thông minh**: Xóa bỏ toàn bộ khối văn bản thừa rườm rà trên hộp thoại, chuyển toàn bộ thông số kỹ thuật chi tiết vào tài liệu markdown [`THONG_SO_KY_THUAT.md`](file:///c:/VAN/CAD/THONG_SO_KY_THUAT.md).
- **Nút "📖 Thông Số (MD)"**: Đặt ngay thanh tiêu đề, 1-click mở ngay tài liệu kỹ thuật đầy đủ.
- **Thanh trạng thái sống (Live Status)**: Hiển thị thời gian thực trạng thái quay động cơ (`🟢 Đang quay` / `🔴 Đã tạm dừng`), góc xoay độ, chiều quay (Thuận / Nghịch) và trạng thái cửa sau (Đóng / Mở 120°).
- **Preset tốc độ thông minh (1-Click Speed)**: Thanh trượt 5 - 120 RPM kèm các nút chọn nhanh `20 RPM (Chậm)`, `40 RPM (Chuẩn)`, `60 RPM (Nhanh)`.
- **Nút "🚪 Mở Cửa Sau (120°)"**: Cơ cấu cửa xoay mở rộng **$120^\circ$** về bên trái, áp sát sườn máy, giải phóng $100\%$ miệng cửa để nạp củi và cào tro phẳng đáy sàn gạch.
- **Nhóm Quan sát**: `👁 Xuyên Thấu Vỏ Trống` (transparency 50%), `📦 Ẩn/Hiện Vỏ Trống`, `🛡 Ẩn/Hiện Khung Bệ Máy`, `🧱 Ẩn/Hiện Lò Gạch Sa Mốt`.
- **Góc nhìn camera thông minh 1-Click**:
  - `📐 Isometric`: Căn góc nhìn phối cảnh 3D tiêu chuẩn.
  - `🔙 Mặt Sau (Lò Gạch)`: Tự động căn góc nhìn thẳng vào cửa sau và lòng buồng đốt.
  - `🔜 Mặt Trước (Miệng Xả)`: Tự động căn góc nhìn thẳng vào miệng xả hàng và cây thăm inox.
  - `🔄 Đổi Tư Thế Đứng / Ngang`.

---

## 3. Cách Khởi Chạy Ngay Trong FreeCAD
1. Mở phần mềm **FreeCAD**.
2. Trên thanh menu, vào **Macro** $\rightarrow$ **Macros...**
3. Chọn file **`trong_hinh_tru.FCMacro`** $\rightarrow$ Bấm **Execute**.
4. Toàn bộ mô hình máy rang với **buồng đốt củi lót gạch chịu lửa 30x5x10cm nằm gọn dưới gầm trống, cửa buồng đốt mở rộng 120 độ, miệng xả 50x10cm đáy cong, cây thăm hàng inox ngang cốt láp, 2 mặt máy trước sau 1.8cm, trống 2 lớp cách khí 1cm và hệ thống 10 cánh đảo** sẽ xuất hiện cùng **bảng điều khiển thông minh mới** sẵn sàng vận hành!


