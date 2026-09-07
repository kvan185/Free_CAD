# BẢNG THÔNG SỐ KỸ THUẬT CHI TIẾT: MÁY RANG CỦI 2 LỚP CÁCH KHÍ & KHUNG BỆ ĐẾ

> **Tài liệu kỹ thuật chính thức**  
> *Được trích xuất và tổng hợp toàn bộ từ hệ thống điều khiển mô phỏng FreeCAD 3D.*

---

## 1. Vỏ Trống Rang 2 Lớp (Đệm Khí Cách Nhiệt 1cm)
* **Vỏ trong**:
  * Chiều dài: $1000\text{ mm} = 1\text{ m}$.
  * Đường kính ngoài: $\varnothing 800\text{ mm} = 80\text{ cm}$ (Bán kính ngoài $R_{\text{out}} = 400\text{ mm}$).
  * Độ dày thành sắt: $8\text{ mm} = 0.8\text{ cm}$ (Bán kính trong $R_{\text{in}} = 392\text{ mm}$).
* **Vỏ áo ngoài (Áo giữ nhiệt)**:
  * Chiều dài: $1000\text{ mm} = 1\text{ m}$.
  * Bán kính trong: $R_{\text{ao\_in}} = 410\text{ mm}$ (Tạo đệm không khí $10\text{ mm} = 1\text{ cm}$ so với vỏ trong).
  * Độ dày vỏ ngoài: $5\text{ mm} = 0.5\text{ cm}$ (Bán kính ngoài $R_{\text{ao\_out}} = 415\text{ mm} \rightarrow \varnothing 830\text{ mm} = 83\text{ cm}$).
* **Tác dụng nhiệt động**: Lớp không khí tĩnh $1\text{ cm}$ giữa 2 vỏ hoạt động như một lớp đệm nhiệt, ngăn chặn táp lửa trực tiếp từ ngọn lửa củi, chống cháy xém hạt nông sản và giữ nhiệt đối lưu cực tốt.

---

## 2. Cây Láp Trục Chính (Trục Bậc Xuyên Tâm)
* **Chiều dài tổng thể**: $1200\text{ mm} = 1.2\text{ m}$.
* **Thân trục giữa**: $\varnothing 65\text{ mm}$ (Bán kính $R = 32.5\text{ mm}$), dài $1000\text{ mm}$ nằm trọn trong trống.
* **Hai đầu tiện bậc lắp bạc đạn & puly**: $\varnothing 60\text{ mm}$, mỗi đầu dài $100\text{ mm} = 10\text{ cm}$ nhô ra ngoài 2 mặt máy (nhô ra $82\text{ mm}$ sau khi trừ độ dày mặt máy $18\text{ mm}$).

---

## 3. Hệ Thống 10 Cây Chống Tròn Phi 20mm (Xen Kẽ 36 Độ)
* **Vật liệu**: Ống sắt tròn $\varnothing 20\text{ mm}$, rỗng ruột, độ dày thành ống $2\text{ mm}$ ($\varnothing$ trong $16\text{ mm}$).
* **Tầng 1 (5 cây gần đầu miệng trước - $Y = -400\text{ mm}$)**:
  * Cách miệng trước trống $10\text{ cm}$.
  * Bù góc pha $-4.5^\circ \rightarrow$ Các góc: $-4.5^\circ, 67.5^\circ, 139.5^\circ, 211.5^\circ, 283.5^\circ$.
  * Tiếp xúc tiếp tuyến vừa chạm sát sườn mặt bên của 5 cánh ngoài la sắt để hàn liền.
* **Tầng 2 (5 cây ở giữa - $Y = +100\text{ mm}$)**:
  * Cách miệng sau trống $40\text{ cm}$.
  * Các góc: $36^\circ, 108^\circ, 180^\circ, 252^\circ, 324^\circ$.
  * Tiếp xúc tiếp tuyến vừa chạm sát sườn mặt bên của 5 cánh ngoài để hàn liền.
* **Tổng thể**: 10 cây chống tạo thành nan hoa chữ thập lệch pha đều $36^\circ$ quanh chu vi, triệt tiêu biến dạng xoắn vặn của trống khi quay đảo tải nặng.

---

## 4. Hệ Thống 10 Cánh Đảo La Sắt (Trong & Ngoài)
* **5 Cánh Đảo Trong (Nằm ngay giữa thân cây chống)**:
  * Thanh la sắt bản rộng **$10\text{ cm} = 100\text{ mm}$**, dày **$0.8\text{ cm} = 8\text{ mm}$**.
  * Bán kính làm việc: $R = 162\text{ mm} \rightarrow 262\text{ mm}$ (cách mặt cây láp $\approx 13\text{ cm}$ không chạm láp, cách vỏ trống $13\text{ cm}$).
  * Chiều dài dọc trục: **$65\text{ cm} = 650\text{ mm}$** (từ $Y = -400\text{ mm}$ qua tầng chống giữa đến $Y = +250\text{ mm}$).
  * Bước xoắn $P = 1083.3\text{ mm}$, xoắn ngược đúng **$6/10$ vòng ($216^\circ$)**.
  * Nhiệm vụ: Đón dòng hạt rơi từ đỉnh cao và hắt ngược về phía sau, tạo chu trình đối lưu hạt 3D liên tục.
* **5 Cánh Đảo Ngoài (Bám thành trống & chạm cả 10 cây chống để hàn)**:
  * Thanh la sắt bản rộng **$7\text{ cm} = 70\text{ mm}$**, dày **$0.5\text{ cm} = 5\text{ mm}$**.
  * Bán kính làm việc: $R = 322\text{ mm} \rightarrow 392\text{ mm}$ bám sát bề mặt thành trong trống.
  * Chiều dài: $960\text{ mm}$ ($Y = -480\text{ mm} \rightarrow +480\text{ mm}$).
  * Bước xoắn $P = 1600\text{ mm}$, xoắn xuôi đúng **$6/10$ vòng ($216^\circ$)**.
  * Nhiệm vụ: Cào sát thành trống, cuốn và đẩy dòng hạt tịnh tiến xuôi về miệng xả hàng.

---

## 5. Hai Mặt Máy Trước & Sau (Sắt Tấm Dày 1.8cm)
* **Vật liệu**: Sắt tấm kết cấu dày **$1.8\text{ cm} = 18\text{ mm}$** gia công CNC chính xác.
* **Hình dáng biên dạng**:
  * Phía trên: Cung tròn bán kính $R = 480\text{ mm}$ ($\varnothing 960\text{ mm} = 96\text{ cm}$) bao trọn vỏ ngoài trống ($R = 415\text{ mm}$).
  * Eo thắt: Thắt cong vào tại cao độ $Z = -308.5\text{ mm}$ với bề rộng $73.5\text{ cm}$ ($X = \pm 367.7\text{ mm}$).
  * Phía dưới: Chân hình thang cân mở rộng xuống đáy phẳng rộng **$1.1\text{ m} = 1100\text{ mm}$** ($X = \pm 550\text{ mm}$) tại cao độ $Z = -850\text{ mm}$.
  * Lỗ tâm trục: Lỗ tròn $\varnothing 65\text{ mm}$ cho đầu cốt láp $\varnothing 60\text{ mm}$ nhô ra $82\text{ mm}$ lắp ổ bi gối đỡ và puly truyền động.

---

## 6. Miệng Ra Hàng Mặt Trước (Cửa Xả Nông Sản)
* **Vị trí**: Nằm ở mặt máy trước tại cao độ $Z = -301.9\text{ mm} \rightarrow -111.9\text{ mm}$.
* **Biên dạng hình học**:
  * Hai bên thành đứng cao **$10\text{ cm} = 100\text{ mm}$** tính từ mép dưới lên.
  * Đỉnh mép trên: Đường thẳng nằm ngang dài **$50\text{ cm} = 500\text{ mm}$** ($X = \pm 250\text{ mm}$).
  * Đáy mép dưới: Đường cong ôm sát chuẩn xác lòng trong của trống ($R = 392\text{ mm}$).
  * Chiều cao thông thủy tại tâm: $19\text{ cm} = 190\text{ mm}$.
* **Ưu điểm**: Hạt xả trút sạch $100\%$ không bị đọng mép, khoảng cách đến cốt trục $17\text{ cm}$ đảm bảo độ cứng vững kết cấu.

---

## 7. Cây Thăm Hàng (Trier / Sampler) & Lỗ Thăm Phi 30mm
* **Lỗ thăm**: Hình tròn $\varnothing 30\text{ mm}$ nằm trên mặt máy trước, ngang cao độ cây láp bên trái ($X = -200\text{ mm}, Z = 0\text{ mm}$).
* **Cây thăm hạt Inox**:
  * Ống inox $\varnothing 28\text{ mm}$, dài $45\text{ cm}$, tay cầm gỗ phi $34\text{ mm}$ dài $12\text{ cm}$.
  * Góc xiên: Nằm ngang cao độ cốt láp ($Z = 0$), xiên góc $16.7^\circ$ hướng vào tâm.
  * Vị trí mũi thăm: Dừng tại $Y = -427.6\text{ mm}$.
  * Khoảng hở an toàn: Cách cánh ngoài $14.6\text{ cm}$, cách cây chống $1.8\text{ cm}$, cách cánh trong $2.8\text{ cm}$, cách cốt láp $14.3\text{ cm}$ $\rightarrow$ **Tuyệt đối không cấn cánh đảo hay cây chống khi máy đang quay!**

---

## 8. Cửa Buồng Đốt Mặt Sau & 2 Bản Lề Cối Mở 120 Độ
* **Lỗ khoét mặt máy sau**: Kích thước dài **$50\text{ cm}$** $\times$ cao **$30\text{ cm}$** ($X \in [-250, +250\text{ mm}]$, $Z \in [-800, -500\text{ mm}]$), cách chân máy đúng **$5\text{ cm}$**.
* **Cánh cửa sắt 18mm**: Sử dụng lại chính phôi sắt tấm dày $1.8\text{ cm}$ cắt ra (kích thước $49.8\text{ cm} \times 29.8\text{ cm}$, khe cắt CNC $1\text{ mm}$).
* **2 Bản lề cối chịu lực**: Hàn cố định bên trái mép cửa (nhìn từ sau: $X = +249.5\text{ mm}, Y = +518\text{ mm}$), cối phi $20\text{ mm}$, đệm long đền đồng.
* **Góc mở cửa**: **Mở rộng $120^\circ$ về bên trái**, xoay áp sát sườn máy, giải phóng $100\%$ miệng buồng đốt cho thao tác nạp củi lớn và cào tro xỉ trơn tru.
* **Tay khóa**: Then gài dạng chữ L (L-handle) bố trí bên phải cửa kèm núm xoay cách nhiệt.

---

## 9. Buồng Đốt Củi Gạch Sa Mốt Nằm Gọn Dưới Trống
* **Quy cách viên gạch sa mốt**: $30\text{ cm} \times 10\text{ cm} \times 5\text{ cm}$ (Dài $\times$ Rộng $\times$ Dày), mạch vữa xây chịu nhiệt $1.5\text{ mm}$.
* **Sàn đáy buồng đốt**:
  * Lát 7 hàng gạch nằm dày **$5\text{ cm}$** ($Z = -850 \rightarrow -800\text{ mm}$).
  * Kích thước sàn: Rộng **$70\text{ cm}$** ($X = \pm 350\text{ mm}$), Dài **$1\text{ m}$** ($Y = \pm 500\text{ mm}$).
  * Bằng phẳng khít ngang ngưỡng mép dưới cửa sau ($Z = -800\text{ mm}$).
* **Hai vách hông lò**:
  * Bao **đúng 1 lớp gạch nằm** dày **$10\text{ cm}$** mỗi bên: Vách trái ($X = -350 \rightarrow -250\text{ mm}$), Vách phải ($X = +250 \rightarrow +350\text{ mm}$).
  * Lòng trong thông thủy buồng đốt: Rộng đúng **$50\text{ cm}$** ($X = \pm 250\text{ mm}$) khớp chuẩn với cửa sau $50\text{ cm}$.
  * Tổng bề rộng lò gạch phủ bì: Đúng **$70\text{ cm}$**, lọt hoàn toàn trong eo thắt mặt máy ($73.5\text{ cm}$), dư an toàn $1.8\text{ cm}$ mỗi bên $\rightarrow$ **Nằm gọn lọt thỏm dưới gầm trống, không hề bị lòi ra ngoài**.
  * Chiều cao vách: Xây **9 hàng gạch** ($45\text{ cm}$ từ sàn lò, tổng cao $50\text{ cm}$ từ chân máy) lên tới cao độ **$Z = -350\text{ mm}$ vừa chạm tới đáy trống**.
  * Cưa gọt vòm cong $R_{\text{cut}} = 425\text{ mm}$ ôm cách vỏ áo ngoài ($R_{\text{ao}} = 415\text{ mm}$) đúng **$1\text{ cm} = 10\text{ mm}$** đồng đều giữ nhiệt tuyệt đối.
* **Vách chắn trước**: Dày $10\text{ cm}$, rộng $50\text{ cm}$, cao 8 lớp (đến $Z = -400\text{ mm}$), gọt vòm $R425\text{ mm}$ cách trống $1\text{ cm}$, nằm hoàn toàn dưới miệng xả hạt.

---

## 10. Chân Đế Máy Hình Chữ Nhật (Sắt Tấm Dày 0.5cm)
* **Vật liệu**: Thép tấm dày **$0.5\text{ cm} = 5\text{ mm}$**.
* **Kích thước mặt bằng**: **$1110\text{ mm} \times 1046\text{ mm}$** ($111\text{ cm} \times 104.6\text{ cm}$).
* **Độ dư tiêu chuẩn**: Dư mỗi bên trước sau đúng **$0.5\text{ cm} = 5\text{ mm}$** và trái phải đúng **$0.5\text{ cm} = 5\text{ mm}$**.
* **Vị trí**: Đặt phẳng dưới mặt sàn xưởng tại $Z = -855\text{ mm} \rightarrow -850\text{ mm}$, đỡ trọn chân 2 mặt máy và lò gạch, liên kết chống rung lật tuyệt đối.
