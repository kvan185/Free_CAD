# BẢNG THÔNG SỐ KỸ THUẬT CHI TIẾT: MÁY RANG CỦI 2 LỚP CÁCH KHÍ & KHUNG BỆ ĐẾ

> **Tài liệu kỹ thuật chính thức**  
> *Được trích xuất và tổng hợp toàn bộ từ hệ thống điều khiển mô phỏng FreeCAD 3D.*

---

## 1. Vỏ Trống Rang 2 Lớp (Đệm Khí Cách Nhiệt 1cm & Khe Hở Vận Hành Chuẩn Xác)
* **Vỏ trong**:
  * Chiều dài: Giữ nguyên vẹn **$1000\text{ mm} = 100\text{ cm} = 1\text{ m}$**.
  * Tọa độ trục $Y$: $Y \in [-499.5\text{ mm}, +500.5\text{ mm}]$.
  * **Khe hở đầu trước áp sát mặt máy**: Đúng **$0.5\text{ mm}$** so với mặt trong của Mặt Máy Trước ($Y = -500.0\text{ mm}$), chống cạ quẹt khi trống quay, tuyệt đối không lọt hạt.
  * **Khe hở đầu sau buồng thoát nhiệt**: Đúng **$99.5\text{ mm} = 9.95\text{ cm}$** so với mặt trong của Mặt Máy Sau ($Y = +600.0\text{ mm}$), tạo khoảng không thông thoáng lý tưởng cho luồng khí nóng đối lưu và khói thoát lên ống thu khói.
  * Đường kính ngoài: $\varnothing 800\text{ mm} = 80\text{ cm}$ (Bán kính ngoài $R_{\text{out}} = 400\text{ mm}$).
  * Độ dày thành sắt: $8\text{ mm} = 0.8\text{ cm}$ (Bán kính trong $R_{\text{in}} = 392\text{ mm}$).
* **Vỏ áo ngoài (Áo giữ nhiệt)**:
  * Chiều dài: $1000\text{ mm} = 1\text{ m}$ ($Y \in [-499.5\text{ mm}, +500.5\text{ mm}]$).
  * Bán kính trong: $R_{\text{ao\_in}} = 410\text{ mm}$ (Tạo đệm không khí $10\text{ mm} = 1\text{ cm}$ so với vỏ trong).
  * Độ dày vỏ ngoài: $5\text{ mm} = 0.5\text{ cm}$ (Bán kính ngoài $R_{\text{ao\_out}} = 415\text{ mm} \rightarrow \varnothing 830\text{ mm} = 83\text{ cm}$).
* **Tác dụng nhiệt động**: Lớp không khí tĩnh $1\text{ cm}$ giữa 2 vỏ hoạt động như một lớp đệm nhiệt, ngăn chặn táp lửa trực tiếp từ ngọn lửa củi, chống cháy xém hạt nông sản và giữ nhiệt đối lưu cực tốt.

---

## 1b. Tấm Sắt Tròn Đáy Sau Trống Rang (Hàn Âm Lọt Lòng Vòng Tròn Nhỏ Phi 78.4cm)
* **Ý tưởng thiết kế (Trường hợp 2 được chọn)**: Bịt kín hoàn toàn đuôi sau của **Vòng tròn nhỏ bên trong** (`Trong_Hinh_Tru_Sat`) để hạt cà phê không bị rơi ra ngoài buồng đốt trong quá trình rang, đồng thời giữ nguyên vẹn luồng đệm khí cách nhiệt $1\text{ cm}$ và khoảng hở sau $9.95\text{ cm}$.
* **Quy cách hình học**:
  * **Đường kính ngoài đĩa**: $\varnothing 784.0\text{ mm} = 78.4\text{ cm}$ ($R = 392.0\text{ mm}$), khớp chính xác với đường kính lọt lòng của vỏ trống trong.
  * **Độ dày thép tấm**: **$8.0\text{ mm} = 0.8\text{ cm}$** (đồng bộ chiều dày thành vỏ trống, chống cong vênh nhiệt tối đa).
  * **Lỗ cốt trục xuyên tâm**: $\varnothing 65.0\text{ mm}$ ($R = 32.5\text{ mm}$), xỏ khít vừa vặn qua thân cây láp chính $\varnothing 65\text{ mm}$.
* **Vị trí bố trí dọc trục Y**:
  * Đặt thụt vào trong lòng trống **$5.0\text{ mm}$** so với mép đuôi trống ($Y = +500.5\text{ mm}$):
    * Mặt ngoài đĩa: $Y = +495.5\text{ mm}$.
    * Mặt trong đĩa: $Y = +487.5\text{ mm}$.
  * Mép ngoài ống trống nhô ra $5\text{ mm}$ tạo gờ bảo vệ và rãnh vát chữ V tự nhiên cho đường hàn góc âm.
  * Khoảng hở an toàn đến chóp sau 5 cánh đảo ngoài ($Y = +484.19\text{ mm}$): **$3.31\text{ mm}$** (vận hành quay mượt mà, không va chạm).
* **Kết cấu mối hàn ngấu chịu lực ("Hàn sao cho vừa đủ")**:
  * **Vành hàn cổ trục**: Fillet collar dày $4\text{ mm}$ quanh cốt láp $\varnothing 65\text{ mm}$ ($R = 32.5 \to 38.0\text{ mm}$, $Y = 495.5 \to 499.5\text{ mm}$).
  * **Vành hàn mép chu vi trong**: Fillet seam dày $4\text{ mm}$ bám dọc chu vi trong ống trống ($R = 386.0 \to 392.0\text{ mm}$, $Y = 495.5 \to 499.5\text{ mm}$).
* **Bảo toàn khoảng hở vận hành**:
  * Mép đuôi ống trống vẫn kết thúc tại $Y = +500.5\text{ mm}$.
  * Khoảng hở từ đuôi trống đến mặt trong Mặt Máy Sau ($Y = +600.0\text{ mm}$) giữ **chính xác $99.5\text{ mm} = 9.95\text{ cm}$** theo đúng tiêu chuẩn thông gió lò củi.
* **Đồng bộ chuyển động**: Đĩa đáy sau được hàn dính liền vào cây láp và vỏ trống nên quay đồng bộ 100% khi đảo chiều và đổi tốc độ RPM.

---

## 2. Cây Láp Trục Chính (Trục Bậc Xuyên Tâm Dài 1.3m)
* **Chiều dài tổng thể**: **$1300\text{ mm} = 1.3\text{ m}$** (tăng $10\text{ cm}$ đồng bộ với khoảng cách 2 mặt máy).
* **Thân trục giữa**: $\varnothing 65\text{ mm}$ (Bán kính $R = 32.5\text{ mm}$), dài **$1100\text{ mm} = 110\text{ cm}$** ($Y \in [-500.0, +600.0\text{ mm}]$) xuyên suốt buồng rang giữa 2 mặt máy.
* **Hai đầu tiện bậc lắp bạc đạn & puly**: $\varnothing 60\text{ mm}$, mỗi đầu dài $100\text{ mm} = 10\text{ cm}$:
  * Đầu trước: $Y \in [-600.0, -500.0\text{ mm}]$, nhô ra ngoài Mặt Máy Trước đúng **$82\text{ mm}$**.
  * Đầu sau: $Y \in [+600.0, +700.0\text{ mm}]$, nhô ra ngoài Mặt Máy Sau đúng **$82\text{ mm}$** đối xứng hoàn hảo.

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

## 5. Hai Mặt Máy Trước & Sau (Sắt Tấm Dày 1.8cm, Khoảng Cách Lọt Lòng 110cm)
* **Vật liệu**: Sắt tấm kết cấu dày **$1.8\text{ cm} = 18\text{ mm}$** gia công CNC chính xác.
* **Vị trí bố trí dọc trục Y**:
  * **Mặt Máy Trước**: Tọa độ $Y \in [-518.0\text{ mm}, -500.0\text{ mm}]$ (mặt trong tại $Y = -500.0\text{ mm}$).
  * **Mặt Máy Sau**: Tọa độ $Y \in [+600.0\text{ mm}, +618.0\text{ mm}]$ (mặt trong tại $Y = +600.0\text{ mm}$).
  * **Khoảng cách lọt lòng giữa 2 mặt máy**: Đúng **$1100\text{ mm} = 110\text{ cm} = 1.1\text{ m}$** (tăng thêm đúng $10\text{ cm}$ theo yêu cầu).
  * **Phân bố khoảng hở trống bên trong**: Trống dài $100\text{ cm}$ đặt tại $Y = -499.5 \to +500.5\text{ mm}$:
    * Đầu trước áp sát mặt máy trước, chừa khe hở **$0.5\text{ mm}$** chống cạ quẹt khi quay.
    * Mặt sau còn lại đúng **$99.5\text{ mm} = 9.95\text{ cm}$** tạo luồng đối lưu khí nhiệt tuyệt hảo.
* **Hình dáng biên dạng chung**:
  * Phía trên: Cung tròn bán kính $R = 480\text{ mm}$ ($\varnothing 960\text{ mm} = 96\text{ cm}$) bao trọn vỏ ngoài trống ($R = 415\text{ mm}$).
  * Eo thắt: Thắt cong vào tại cao độ $Z = -308.5\text{ mm}$ với bề rộng $73.5\text{ cm}$ ($X = \pm 367.7\text{ mm}$).
  * Chiều cao tổng thể: Giữ nguyên từ đỉnh cung tròn $Z = +480\text{ mm}$ xuống sàn $Z = -850\text{ mm}$ (tổng cao $1330\text{ mm}$).
  * Lỗ tâm trục: Lỗ tròn $\varnothing 65\text{ mm}$ cho đầu cốt láp $\varnothing 60\text{ mm}$ nhô ra $82\text{ mm}$ lắp ổ bi gối đỡ và puly truyền động.
* **Kết cấu chân đồng bộ 2 Mặt Máy Trước & Sau (Phương án C.2 - Vát xéo ra biên + Gờ chân đứng 5.5cm)**:
  * Từ điểm eo thắt ($X = \pm 367.7\text{ mm}, Z = -308.5\text{ mm}$), hai cạnh bên vát chéo một mạch xuôi ra biên ngoài $X = \pm 550\text{ mm}$ tại cao độ $Z = -795\text{ mm}$ (cách mặt sàn/chân máy đúng **$5.5\text{ cm} = 55\text{ mm}$**).
  * Từ điểm $(X = \pm 550\text{ mm}, Z = -795\text{ mm})$, đường biên **bẻ góc vuông thẳng đứng xuống sàn** $Z = -850\text{ mm}$, tạo thành gờ chân đứng cao đúng **$5.5\text{ cm} = 55\text{ mm}$**.
  * Đáy dưới phẳng rộng **$1.1\text{ m} = 1100\text{ mm}$** ($X = \pm 550\text{ mm}$) tiếp xúc phẳng hoàn toàn và êm khít với bệ chân đế máy $111\text{ cm} \times 114.6\text{ cm} \times 0.5\text{ cm}$.
  * Tạo vẻ ngoài đồng bộ, khỏe khoắn, hiện đại và tạo điểm tựa gờ đứng vững chắc cho việc bắt bu-lông/hàn định vị khung bệ máy.

---

## 6. Miệng Ra Hàng & Cụm Máng Xả Hạt Lắp Rời 3 Phần (Góc Tù 120° — Dốc 30° Trong FreeCAD)
* **Vị trí miệng khoét trên mặt máy trước (Sắt 18mm)**:
  * Miệng khoét tại cao độ $Z = -301.9\text{ mm} \rightarrow -201.9\text{ mm}$.
  * Hai bên thành đứng cao **$10\text{ cm} = 100\text{ mm}$** tính từ mép dưới lên.
  * Đỉnh mép trên: Đường thẳng nằm ngang dài **$50\text{ cm} = 500\text{ mm}$** ($X = \pm 250\text{ mm}$).
  * Đáy mép dưới: Đường cong ôm sát chuẩn xác lòng trong của trống ($R = 392\text{ mm}$).
  * Chiều cao thông thủy tại tâm: $19\text{ cm} = 190\text{ mm}$.
* **Cụm máng ra hàng cơ động gồm đúng 3 phần kết cấu (Mô hình hóa 3D Solid 100% trong FreeCAD)**:
  1. **Phần 1: Tấm đáy Inox 1.5mm (`Mieng_Ra_Hang_Day_Inox_1p5mm`)**:
     * **Mép trong giáp trống**: Uốn cong chuẩn xác theo cung tròn $R = 392\text{ mm}$ của phần đáy miệng khoét ($Y = -500.1\text{ mm}$).
     * **Khe hở cách mép quay của vành trống đúng $0.1\text{ mm}$**: Hạt xả trút $100\%$ không bị lọt mép, không kẹt hạt và không bao giờ cạ quẹt vào trống khi quay.
     * **Bẻ góc tù $120^\circ$ chúc dốc xuống đất ($30^\circ$ so với phương ngang)**: Tấm đáy vươn xiên ra ngoài $120\text{ mm}$ (vươn theo phương $Y$ ra $103.92\text{ mm}$ từ $Y = -518.0 \to -621.92\text{ mm}$ và hạ cao độ $60\text{ mm}$ từ $Z = -392.0 \to -452.0\text{ mm}$). Khắc phục triệt để hiện tượng đọng hạt của máng đi ngang; cà phê khi mở cửa sẽ trượt ào ạt rơi tự do thẳng đứng xuống thau làm nguội bên dưới!
     * **Khẩu độ rộng**: **$500\text{ mm}$** ($X = \pm 250\text{ mm}$), thể tích $101,359\text{ mm}^3$.
  2. **Phần 2: Hai tấm Inox vách hông 2 bên (`Mieng_Ra_Hang_2_Vach_Hong_Inox`)**:
     * Dựng đứng ở 2 bên mép máng xả ($X = \pm 250\text{ mm}$), dày $1.5\text{ mm}$, cao $100\text{ mm}$ tại mặt máy và vát xuôi theo độ dốc chúc xuống $30^\circ$ của tấm đáy.
     * Góc trên phía trước được **bo tròn cung lượn mềm mại $R = 30\text{ mm}$ đạt tiếp tuyến $G^1$ mượt mà**: Dẫn hướng dòng hạt, chống văng hạt sang 2 sườn và bảo đảm an toàn tuyệt đối không cấn xước tay người thao tác.
  3. **Phần 3: Hai thanh la gá bắt ốc (`Mieng_Ra_Hang_2_Thanh_La_Bat_Oc` & `Mieng_Ra_Hang_4_BuLong_M8`)**:
     * Thanh la bản rộng **$30\text{ mm}$**, dày **$5\text{ mm}$**, dài **$140\text{ mm}$** hàn liền vào 2 vách hông bên ngoài máng ($X = \pm 250 \to \pm 280\text{ mm}$).
     * Mỗi thanh la **khoan 2 lỗ $\varnothing 10\text{ mm}$** (khoảng cách tâm $70\text{ mm}$) để bắt chặt bằng 4 bu-lông lục giác M8 ren trực tiếp vào mặt máy sắt $18\text{ mm}$.
     * **Ưu điểm cơ khí**: Module lắp rời độc lập bằng 4 con ốc (2 con mỗi bên), tháo lắp cực kỳ nhanh chóng để vệ sinh buồng máy và bảo trì định kỳ.
* **Cánh Cửa Xả Hạt Sắt 18mm & Ô Kính Thạch Anh Quan Sát Phi 10cm (`Cua_Xa_Hat_Sat_18mm` & `O_Kieng_Quan_Sat_Phi_10cm`)**:
  1. **Cánh cửa sắt 18mm (Tái sử dụng phôi cắt từ miệng xả)**:
     * Tận dụng chính tấm phôi sắt dày **$18\text{ mm}$** cắt ra từ miệng khoét mặt máy trước.
     * Thu nhỏ đều **$1.0\text{ mm}$** xung quanh biên dạng (khe hở lọt lòng $1\text{ mm}$ chống kẹt giãn nở nhiệt, bù trừ mạch cắt plasma/CNC):
       * Chiều ngang: Rộng **$498.0\text{ mm}$** ($X \in [-249.0, +249.0\text{ mm}]$ so với miệng $500\text{ mm}$).
       * Mép trên: $Z = -202.93\text{ mm}$ (hạ thấp $1\text{ mm}$ so với ngưỡng mép $Z = -201.93\text{ mm}$).
       * Đáy uốn cong: Bán kính **$R = 391.0\text{ mm}$** (thu nhỏ $1\text{ mm}$ so với lòng trống $R = 392.0\text{ mm}$), đáy tại $Z = -391.0\text{ mm}$.
       * Thể tích: **$1,290,509.79\text{ mm}^3$**.
  2. **Ô kính quan sát thạch anh chịu nhiệt $\varnothing 10\text{ cm}$ nằm chính giữa cửa**:
     * Vị trí tâm lỗ: Tọa độ **$(X = 0, Z = -296.97\text{ mm})$** — nằm ngay trọng tâm hình học của cánh cửa xả (cách mép trên $94.0\text{ mm}$, cách đáy cong $94.0\text{ mm}$, cách 2 mép bên $249.0\text{ mm}$).
     * Đĩa kính thạch anh chịu nhiệt độ cao ($> 800^\circ\text{C}$): Đường kính **$\varnothing 100\text{ mm} = 10\text{ cm}$**, độ dày **$8\text{ mm}$**, đặt âm chính giữa chiều dày $18\text{ mm}$ của cánh cửa sắt.
     * Độ trong suốt hiển thị: $65\%$, màu lam thạch anh trong trẻo `(0.72, 0.92, 0.96)`. Giúp người thợ rang theo dõi trực tiếp chuyển động cuộn và sắc độ ngả màu của mẻ cà phê/hạt nông sản mà không cần hé mở cửa xả.
  3. **Vành Inox 304 giữ kính & 4 Vít chìm M5**:
     * Mặt bích vành tròn Inox 304 dày $3\text{ mm}$, đường kính ngoài $\varnothing 124\text{ mm}$, lỗ thông quan sát $\varnothing 92\text{ mm}$ giữ ngàm viền kính $4\text{ mm}$ xung quanh kèm gioăng chịu nhiệt.
     * Cố định bằng 4 vít chìm Inox M5 phân bố đều ở góc $45^\circ, 135^\circ, 225^\circ, 315^\circ$ trên đường tròn định vị $\varnothing 108\text{ mm}$.
  4. **Cơ cấu trục láp Ø30mm dài 100cm bẻ cần gạt 30cm sang bên TRÁI & 2 Khâu nối đôi cân bằng 2 bên (Dài 8cm, Rộng 3cm)**:
     * **Cây láp tròn đặc $\varnothing 30\text{ mm}$ (Thép C45)**:
        * Tổng chiều dài phôi: **$100\text{ cm} = 1000\text{ mm}$**.
        * Thân trục ngang: Dài **$70\text{ cm} = 700\text{ mm}$** ($X = +350.0 \to -350.0\text{ mm}$), đầu bên PHẢI có vành chặn cốt collar $\varnothing 45\text{ mm} \times 12\text{ mm}$.
        * **Cần gạt bẻ cong sang BÊN TRÁI NGHIÊNG 45° CHĨA RA PHÍA TRƯỚC**: Bán kính uốn $R = 45\text{ mm}$ tại đầu bên TRÁI ($X = -350\text{ mm}$), cần gạt dài $30\text{ cm} = 300\text{ mm}$ chúc xuống dưới và xoay nghiêng đúng **$45^\circ$ chĩa ra phía trước** ($Y \in [-543.0, -755.1\text{ mm}]$, $Z \in [-171.93, -384.1\text{ mm}]$), đầu cần gắn núm cầu tay nắm $\varnothing 42\text{ mm}$ đầm chắc, cực kỳ thuận tay cho người vận hành đứng trước máy kéo mở cửa xả hạt.
        * Cao độ lắp đặt: Nằm cao hơn mép trên miệng xả đúng **$3\text{ cm} = 30\text{ mm}$** (tọa độ tâm trục $Z = -171.93\text{ mm}$).
        * Khoảng cách trục so với mặt máy: Bề mặt ngoài cây láp cách mặt máy đúng **$1\text{ cm} = 10\text{ mm}$**, tâm trục đặt tại $Y = -543.0\text{ mm}$ ($Y_{\text{mat}} - 10 - 15\text{ mm}$).
     * **2 Gối đỡ bạc đạn rùa UCP206 (Cốt $\varnothing 30\text{ mm}$)**:
       * Vỏ gang đúc hình mai rùa, vòng bi cầu tự lựa 2 nắp chắn bụi, vú mỡ bôi trơn M8 trên đỉnh.
       * Vị trí lắp đặt: Đặt tại $X = \pm 310.0\text{ mm}$ (mép gối đỡ cách mép ngoài máng xả đúng **$1\text{ cm} = 10\text{ mm}$**).
       * Chân đế gối dày $16\text{ mm}$ áp sát mặt máy sắt 18mm, thân gối ôm trọn cây láp tại $Y = -543.0\text{ mm}$.
     * **4 Bu-lông gá M14**:
       * Mỗi bên 2 bu-lông lục giác M14 xuyên qua chân gối, cắm ren ngấu sâu vào mặt máy trước.
     * **2 Khâu nối đôi cân bằng 2 bên (`Hai_Khau_Noi_Cua_Xa_8cm`)**:
       * **Vị trí bố trí đối xứng**: Đặt tại $X = -130.0\text{ mm}$ (Bên Trái) và $X = +130.0\text{ mm}$ (Bên Phải), cách đều tâm máy, hoàn toàn không che khuất ô kính quan sát $\varnothing 10\text{ cm}$ ở giữa ($X \in [-62, +62\text{ mm}]$), tạo lực nâng/hạ cửa xả cân bằng tuyệt đối 2 bên.
       * **2 Nhẫn tròn ôm cây láp**: Chiều dài $L = 3\text{ cm} = 30\text{ mm}$ dọc theo trục X, dày $10\text{ mm}$ ($ID = 30\text{ mm}, OD = 50\text{ mm}$), có lỗ ren vít chí M8 trên đỉnh khóa chặt vào cây láp. Mép sau của nhẫn tròn nằm tại $Y = -518.0\text{ mm}$, trùng khít với mặt máy.
       * **2 Tấm hình chữ nhật đầu nửa tròn**:
         * Chiều dài: **$L = 8\text{ cm} = 80\text{ mm}$** (chuẩn mới theo trục đứng Z từ $Z = -171.93 \to -251.93\text{ mm}$).
         * Chiều rộng: $W = 3\text{ cm} = 30\text{ mm}$ (bằng chiều dài nhẫn tròn).
         * Bề dày: $T = 10\text{ mm}$ (vừa khít khoảng hở 10mm từ cây láp đến mặt máy).
         * **Mặt lưng áp sát mặt máy**: Toàn bộ mặt lưng phẳng của tấm **ÁP SÁT 100% VÀO MẶT MÁY VÀ CÁNH CỬA XẢ SẮT 18MM** tại $Y = -518.0\text{ mm}$ khi cửa đóng kín (phẳng đứng theo trục Z từ $Z = -171.93 \to -251.93\text{ mm}$).
         * Đầu dưới bo nửa tròn bán kính $R = 15\text{ mm}$ ($\varnothing 30\text{ mm}$), tâm nửa tròn khoan lỗ xỏ chốt Pin $\varnothing 10\text{ mm}$ tại cao độ $Z = -236.93\text{ mm}$ (cách mép trên cửa xả $34\text{ mm} = 3.4\text{ cm}$, tạo thế đòn bẩy chắc chắn).
     * **2 Bu-lông Chốt Pin M10 & Ê-cu tự hãm (`Hai_Chot_Pin_M10_Cua_Xa`)**:
       * Bu-lông chốt phi 10mm bắt qua lỗ đầu nửa tròn liên kết chặt khâu nối vào cánh cửa xả sắt 18mm.
     * **Tay khóa gài chữ L bên phải (`Tay_Khoa_Gai_Cua_Xa`)**:
       * Then xoay trục $\varnothing 16\text{ mm}$ tại $X = +229\text{ mm}$, ép tì chặt cánh cửa xả vào mặt máy khi đóng.

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
* **Lỗ khoét mặt máy sau**: Kích thước dài **$50\text{ cm}$** $\times$ cao **$30\text{ cm}$** ($X \in [-250, +250\text{ mm}]$, $Z \in [-800, -500\text{ mm}]$), cách chân máy đúng **$5\text{ cm}$**, đặt tại mặt máy sau mới ($Y = +600 \to +618\text{ mm}$).
* **Cánh cửa sắt 18mm**: Sử dụng lại chính phôi sắt tấm dày $1.8\text{ cm}$ cắt ra (kích thước $49.8\text{ cm} \times 29.8\text{ cm}$, khe cắt CNC $1\text{ mm}$, đặt tại $Y = +600 \to +618\text{ mm}$).
* **2 Bản lề cối chịu lực**: Hàn cố định bên trái mép cửa (nhìn từ sau: $X = +249.5\text{ mm}, Y = +618\text{ mm}$), cối phi $20\text{ mm}$, đệm long đền đồng, tâm xoay tại $Y = +626\text{ mm}$.
* **Góc mở cửa**: **Mở rộng $120^\circ$ về bên trái**, xoay áp sát sườn máy, giải phóng $100\%$ miệng buồng đốt cho thao tác nạp củi lớn và cào tro xỉ trơn tru.
* **Tay khóa**: Then gài dạng chữ L (L-handle) bố trí bên phải cửa kèm núm xoay cách nhiệt.

---

## 9. Buồng Đốt Củi Gạch Sa Mốt Nằm Gọn Dưới Trống (Dài 110cm)
* **Quy cách viên gạch sa mốt**: $30\text{ cm} \times 10\text{ cm} \times 5\text{ cm}$ (Dài $\times$ Rộng $\times$ Dày), mạch vữa xây chịu nhiệt $1.5\text{ mm}$.
* **Sàn đáy buồng đốt**:
  * Lát 7 hàng gạch nằm dày **$5\text{ cm}$** ($Z = -850 \rightarrow -800\text{ mm}$).
  * Kích thước sàn: Rộng **$70\text{ cm}$** ($X = \pm 350\text{ mm}$), Dài **$110\text{ cm} = 1.1\text{ m}$** ($Y \in [-500.0, +600.0\text{ mm}]$) ôm kín khít từ Mặt Máy Trước đến Mặt Máy Sau.
  * Bằng phẳng khít ngang ngưỡng mép dưới cửa sau ($Z = -800\text{ mm}$).
* **Hai vách hông lò**:
  * Bao **đúng 1 lớp gạch nằm** dày **$10\text{ cm}$** mỗi bên: Vách trái ($X = -350 \rightarrow -250\text{ mm}$), Vách phải ($X = +250 \rightarrow +350\text{ mm}$).
  * Chiều dài vách hông: **$110\text{ cm}$** ($Y = -500 \rightarrow +600\text{ mm}$).
  * Lòng trong thông thủy buồng đốt: Rộng đúng **$50\text{ cm}$** ($X = \pm 250\text{ mm}$) khớp chuẩn với cửa sau $50\text{ cm}$.
  * Tổng bề rộng lò gạch phủ bì: Đúng **$70\text{ cm}$**, lọt hoàn toàn trong eo thắt mặt máy ($73.5\text{ cm}$), dư an toàn $1.8\text{ cm}$ mỗi bên $\rightarrow$ **Nằm gọn lọt thỏm dưới gầm trống, không hề bị lòi ra ngoài**.
  * Chiều cao vách: Xây **9 hàng gạch** ($45\text{ cm}$ từ sàn lò, tổng cao $50\text{ cm}$ từ chân máy) lên tới cao độ **$Z = -350\text{ mm}$ vừa chạm tới đáy trống**.
  * Cưa gọt vòm cong $R_{\text{cut}} = 425\text{ mm}$ ôm cách vỏ áo ngoài ($R_{\text{ao}} = 415\text{ mm}$) đúng **$1\text{ cm} = 10\text{ mm}$** đồng đều giữ nhiệt tuyệt đối.
* **Vách chắn trước**: Dày $10\text{ cm}$, rộng $50\text{ cm}$, cao 8 lớp (đến $Z = -400\text{ mm}$), gọt vòm $R425\text{ mm}$ cách trống $1\text{ cm}$, nằm hoàn toàn dưới miệng xả hạt.

---

## 10. Chân Đế Máy Hình Chữ Nhật (Sắt Tấm Dày 0.5cm, 111cm x 114.6cm)
* **Vật liệu**: Thép tấm dày **$0.5\text{ cm} = 5\text{ mm}$**.
* **Kích thước mặt bằng**: **$1110\text{ mm} \times 1146\text{ mm}$** ($111\text{ cm} \times 114.6\text{ cm}$).
* **Độ dư tiêu chuẩn**: Dư mỗi bên trước sau đúng **$0.5\text{ cm} = 5\text{ mm}$** ($Y \in [-523.0, +623.0\text{ mm}]$ so với 2 mặt máy tại $Y = -518\text{ mm}$ và $Y = +618\text{ mm}$) và trái phải đúng **$0.5\text{ cm} = 5\text{ mm}$** ($X \in [-555.0, +555.0\text{ mm}]$).
* **Vị trí**: Đặt phẳng dưới mặt sàn xưởng tại $Z = -855\text{ mm} \rightarrow -850\text{ mm}$, đỡ trọn chân 2 mặt máy và lò gạch, liên kết chống rung lật tuyệt đối.

---

## 11. Hộp Vô Hàng Inox 3mm & Cơ Cấu Van Gạt Láp Ø20mm (Tab 2)
* **Kiểu dáng**: Hình thang vuông dựng đứng, đầu nhọn dốc hướng xuống đáy trước ($Z = 0$).
  * **Kích thước mặt bằng**: Đáy vuông $30\text{ cm} \times 30\text{ cm}$, vách trước cao $65\text{ cm}$, vách sau cao $30\text{ cm}$ (từ $Z = 35\text{ cm} \rightarrow 65\text{ cm}$).
  * **Máng trượt dốc**: Tấm inox $300 \times 461\text{ mm}$, nghiêng $49.4^\circ$ giúp hạt cà phê trôi tự nhiên không đọng góc.
  * **Thể tích buồng chứa**: $\sim 62.6\text{ Lít}$ ($\sim 25 - 35\text{ kg}$ hạt cà phê nhân tươi).
* **Cửa xả & Cửa nạp**:
  * **Cửa xả hạt đáy trước**: Khoảng trống $20\text{ cm} \times 30\text{ cm}$ ở phía dưới chân vách trước ($Z = 0 \rightarrow 200\text{ mm}$).
  * **Lỗ khoét tròn $\varnothing 20\text{ cm}$ vách trước**: Khoét ở phần trên của tấm vách trước, mép trên chừa lại đúng $1\text{ cm} = 10\text{ mm}$.
  * **Lỗ nắp đỉnh $\varnothing 20\text{ cm}$**: Khoét chính giữa tấm nắp đỉnh vuông $30\text{ cm} \times 30\text{ cm}$ tại $Z = 650\text{ mm}$.
* **Ống nạp liệu $\varnothing 19.9\text{ cm}$ dài $30\text{ cm}$**:
  * Đặt từ nắp đỉnh ($Z = 650\text{ mm}$) đâm thẳng xuống ($Z = 350\text{ mm}$).
  * Khe hở lọt lỗ: $0.5\text{ mm}$ đều quanh chu vi lỗ $\varnothing 200\text{ mm}$.
  * **Trục xoay láp tròn đặc $\varnothing 20\text{ mm}$**: Dài $428\text{ mm}$, xuyên qua 2 lỗ tròn $\varnothing 20\text{ mm}$ tại $(X = 10.5, Z = 353.9\text{ mm})$, **dư nhô dài ra đúng $10\text{ cm} = 100\text{ mm}$ về bên phải** (mặt ngoài hông phải $Y = +153\text{ mm} \rightarrow +253\text{ mm}$) để gắn cần gạt và tay nắm thao tác.
  * **Hệ thống 4 vòng tròn bạc chặn (Mỗi bên 2 vòng, ID $\varnothing 20\text{ mm}$ vừa khít cây láp, OD $\varnothing 32\text{ mm}$ thành dày 6mm)**:
    - **Vòng dày ($10\text{ mm}$) hàn vào hộp**: Hàn dính cố định vào mặt ngoài 2 tấm hông hộp, làm gối bạc trượt tăng cứng vững và chống mài mòn cho lỗ thành hộp.
    - **Vòng ngoài ($8\text{ mm}$) hàn vào cây láp**: Hàn dính trực tiếp vào cây láp $\varnothing 20\text{ mm}$, đóng vai trò cữ chặn định vị chống trượt dọc trục (axial stop) và xoay đồng bộ cùng cây láp khi đóng mở van.
  * **Lá van inox 3mm**: Đúng **1 tấm Inox 304 dày 3mm bo tròn đẹp mắt** ($W = 220\text{ mm}$, dài $249.5\text{ mm}$ từ tim láp đến đỉnh, đầu trước uốn cong bán nguyệt $R = 110\text{ mm}$ đồng tâm hoàn hảo với ống $\varnothing 19.9\text{ cm}$, chừa mép đều $10.5\text{ mm}$ xung quanh không còn góc nhọn thừa) hàn cố định trực tiếp vào trục láp tròn $\varnothing 20\text{ mm}$.
  * **Cơ cấu góc tọa độ 3 góc vuông (1 Ra Ngoài, 1 Xuống Dưới - 3 cây láp tròn Ø20mm trực giao tại đầu láp nhô ra)**:
    - **Vị trí gốc tọa độ**: Nằm ngay chỗ giao vuông góc ở đầu cây láp nhô ra $10\text{ cm}$ bên sườn máy tại $(X = -240, Y = -807.5, Z = 508.9\text{ mm})$.
    - **3 Trục trực giao tạo đúng 3 góc vuông tuyệt đối ($90^\circ$)**:
      1. **Trục láp ngang Ø20mm**: Dài $428\text{ mm}$, là trục xoay chính của cụm van gạt (trên máy nằm ngang sườn tại $X = -240\text{ mm}$, nhô ra $10\text{ cm}$).
      2. **Cây vuông góc 1 (Cần ngang Ø20mm quay ra ngoài)**: Dài $220\text{ mm}$ ($22\text{ cm}$), vươn ngang ra phía ngoài (hướng $-Y$ trên máy rang từ $Y = -807.5 \to -1027.5\text{ mm}$, hướng thẳng về phía người vận hành đứng trước máy).
      3. **Cây vuông góc 2 (Cần đứng Ø20mm quay xuống dưới)**: Dài $220\text{ mm}$ ($22\text{ cm}$), chúc thẳng đứng xuống dưới $-Z$ ($Z = 508.9 \to 288.9\text{ mm}$ trên máy), vuông góc tuyệt đối với cây láp ngang và cần gạt ngoài.
    - **Cặp góc vuông hình thành**:
      - Góc 1: Trục Láp $\perp$ Cần Ra Ngoài ($90^\circ$).
      - Góc 2: Cần Ra Ngoài $\perp$ Cần Chúc Xuống ($90^\circ$).
      - Góc 3: Cần Chúc Xuống $\perp$ Trục Láp ($90^\circ$).
      $\rightarrow$ Tạo thành khung **3 góc vuông: 1 ra ngoài, 1 chúc xuống**, cực kỳ thẩm mỹ, gọn gàng, đầm chắc, hạ thấp trọng tâm cụm điều khiển và cho phép người vận hành chọn 2 cách thao tác (nâng cần ngoài lên hoặc kéo cần dưới về phía mình).
  * **Góc vận hành**: $0^\circ$ (đóng kín chặn đáy ống) $\rightarrow 45^\circ$ (mở thông hạt trôi xuống trống rang).
* **Bảng điều khiển tích hợp 2 Tab GUI (Dual-Tab Controller)**:
  * **Tab 1: 🏭 Máy Rang Củi (Trống 2 Lớp)**: Tốc độ quay $5 - 120\text{ RPM}$, đảo chiều, tạm dừng, xuyên thấu vỏ trống, ẩn/hiện vỏ trống, bệ đế, lò gạch sa mốt, nút Ẩn/Hiện Hộp Vô Hàng Mặt Trước, mở cửa sau $120^\circ$, đổi tư thế đứng/ngang, góc nhìn Isometric/Sau/Trước.
  * **Tab 2: 📥 Hộp Vô Hàng & Van Gạt (Ống Ø20)**: Điều khiển góc mở van gạt live ($0^\circ \rightarrow 45^\circ$), nút đóng/mở 1-click, **nút Ẩn/Hiện thùng bên ngoài** (ẩn toàn bộ các tấm vỏ ngoài để nhìn rõ ống nạp và van gạt như ẩn vỏ trống), xuyên thấu vỏ hộp, mở/đậy nắp đỉnh, ẩn/hiện khối tham chiếu, góc nhìn nhanh (Isometric, Cạnh, Mặt Trước) và Bảng kê cắt phôi Inox 3mm (BOM).
  * **Đồng bộ FreeCAD 3D View**: Tự động kích hoạt đúng tài liệu 3D tương ứng khi người dùng click chuyển tab trên giao diện điều khiển.

---

## 12. Lỗ Nạp Liệu Chữ Nhật 20x30cm Đẩy Lên Cao Tối Đa Trên Mặt Máy Trước & Máng Dẫn Hướng Chống Rớt Hạt
* **Khôi phục Mặt Máy Sau ($Y = +500 \to +518\text{ mm}$)**:
  * Loại bỏ hoàn toàn lỗ nạp phía sau, mặt máy sau nguyên bản phẳng liền khối ở nửa trên, chỉ giữ lại lỗ cốt tâm $\varnothing 65\text{ mm}$ và cửa buồng đốt $50\times 30\text{ cm}$ phía dưới.
* **Lỗ khoét chữ nhật $20\text{ cm} \times 30\text{ cm}$ trên Mặt Máy Trước ($Y = -518 \rightarrow -500\text{ mm}$) — Tối Ưu Lên Cao Nhất Có Thể**:
  * **Chiều ngang (trục X)**: $W = 300\text{ mm} = 30\text{ cm}$ ($X \in [-150.0, +150.0\text{ mm}]$ đối xứng qua trục tâm máy).
  * **Chiều cao (trục Z)**: $H = 200\text{ mm} = 20\text{ cm}$ ($Z \in [+155.0\text{ mm}, +355.0\text{ mm}]$ — nâng cao lên sát kịch trần vòm trống).
  * **Kiểm tra lọt lòng đường tròn trống ($R_{\text{in}} = 392\text{ mm}$)**:
    - Tại 2 góc trên cùng ($X = \pm 150\text{ mm}, Z = 355\text{ mm}$):
      $$R_{\text{góc}} = \sqrt{150^2 + 355^2} \approx 385.39\text{ mm} < R_{\text{in}} = 392.0\text{ mm}$$
    - Chừa lại đúng **$6.61\text{ mm}$** thành sắt dày dặn so với mép trong trống, vừa vặn tuyệt đối không lẹm vào thành trống, vừa đạt độ cao tối đa về mặt hình học!
    - Ngưỡng đáy lỗ nâng lên cao độ $Z = +155\text{ mm}$, cách đỉnh cốt trục giữa ($\varnothing 65\text{ mm}$) tới **$122.5\text{ mm} = 12.25\text{ cm}$** (khoảng không gian cực kỳ thoáng đãng).
    - Cách miệng ra hàng phía dưới ($Z \le -202\text{ mm}$) hơn **$35.7\text{ cm}$** và không chạm lỗ cắm que thăm hàng ($X = -200\text{ mm}, Z = 0$).
* **Máng trượt dẫn hướng Inox 304 đâm sâu vào lòng trống từ Mặt Trước (Độ Dốc Cực Đại $50.6^\circ$)**:
  * **Vượt qua khe hở quay $2\text{ mm}$**: Máng trượt đâm xuyên qua tấm mặt máy trước dày $1.8\text{ cm}$ và **vươn sâu $60\text{ mm}$ vào lòng trống** (tới $Y = -440\text{ mm}$), triệt tiêu hoàn toàn nguy cơ hạt rơi vào khe hở giữa mép trống và mặt máy.
  * **Độ dốc trượt cực đại $\alpha = 50.6^\circ$**: Nhờ nâng lỗ nạp lên cao nhất ($Z_{\text{bot}} = +155\text{ mm}$), sàn máng nghiêng dốc từ $Z = +155\text{ mm}$ ($Y = -518$) xuống $Z = +60\text{ mm}$ ($Y = -440$), tạo góc dốc **$50.6^\circ$** (tương đương độ dốc thành phễu $49.4^\circ$). Cà phê nhân trượt xả lao như thác cuốn vào sâu trong lòng trống, không bao giờ lo đọng hạt.
  * **2 Thành be chắn hai bên (Side Baffles)**: Cao $60\text{ mm}$ ($Z \in [155, 215\text{ mm}]$), ngăn tuyệt đối không cho hạt bị văng tạt sang hai bên khi gặp luồng khí nóng đối lưu.
* **Gắn cụm Hộp Vô Hàng Inox 3mm vào Mặt Trước Máy Rang**:
  * Cửa xả hạt đáy $20\times 30\text{ cm}$ của Hộp Vô Hàng khớp kín khít $100\%$ với cửa nạp liệu trên mặt máy trước tại cao độ tối ưu $Z = 155 \rightarrow 355\text{ mm}$, vị trí $Y \in [-818.0, -518.0\text{ mm}]$.
  * Đỉnh nắp hộp vươn lên cao độ $Z = +805\text{ mm} \approx 80.5\text{ cm}$, đứng đổ bao hạt ngay trước máy vô cùng thuận tiện, không cần đi vòng ra sau.
  * Cụm tay gạt 3 góc vuông $\varnothing 20\text{ mm}$ (1 ra ngoài, 1 chúc xuống) hướng trực diện về phía người vận hành, thao tác nâng/kéo mở $0^\circ \to 45^\circ$ cực kỳ nhẹ nhàng, đồng bộ live trên cả 2 Tab mô hình 3D.

---

## 13. Cụm Cây Láp Tròn Phi 30mm Dài 100cm Bẻ Cần Gạt Sang Trái 30cm Nghiêng 45° Ra Trước & 2 Gối Đỡ Bạc Đạn Rùa UCP206
* **Cây láp tròn đặc $\varnothing 30\text{ mm}$**:
  * **Tổng chiều dài phôi**: $100\text{ cm} = 1000\text{ mm}$.
  * **Thân trục ngang**: Dài $70\text{ cm} = 700\text{ mm}$ ($X \in [-350.0, +350.0\text{ mm}]$).
  * **Cần gạt bẻ cong sang bên TRÁI nghiêng 45° chĩa ra trước**: Tại $X = -350.0\text{ mm}$, uốn bán kính lượn $R = 45\text{ mm}$, cần gạt vươn dài $30\text{ cm} = 300\text{ mm}$ chúc xuống dưới và xoay nghiêng đúng **$45^\circ$ chĩa ra phía ngoài** ($Y \in [-543.0, -755.1\text{ mm}]$, $Z \in [-171.93, -384.1\text{ mm}]$), gắn núm cầu kim loại $\varnothing 42\text{ mm}$ cầm nắm công thái học.
  * **Vòng chặn định vị bên phải**: Vòng chặn $\varnothing 45\text{ mm}$, dày $12\text{ mm}$ tại đầu phải $X = +350\text{ mm}$ khóa chống dịch chuyển dọc trục.
* **Vị trí lắp ráp**:
  * **Cao hơn mép trên miệng xả đúng $3\text{ cm} = 30\text{ mm}$**: Cao độ tâm trục $Z_{\text{shaft}} = -171.93\text{ mm}$ (mép trên miệng xả ở $Z = -201.93\text{ mm}$).
  * **Tọa độ trục $Y$**: $Y_{\text{shaft}} = -543.0\text{ mm}$ (khoảng hở từ bề mặt cây láp đến mặt máy trước đúng $1\text{ cm} = 10\text{ mm}$).
* **2 Gối đỡ bạc đạn rùa UCP206 cốt $\varnothing 30\text{ mm}$**:
  * **Vị trí**: Đặt tại $X = \pm 310\text{ mm}$ (cách mép ngoài thanh la máng xả $1\text{ cm}$).
  * **Tấm đệm sắt kê chân gối dày đúng $1\text{ cm} = 10\text{ mm}$**: Kê giữa mặt máy sắt 18mm và chân gối đỡ gang UCP206 để đưa tâm trục ra đúng khoảng cách vận hành.
  * **Bu-lông gá**: 4 bu-lông M14 cắm ren vào mặt máy sắt 18mm.
* **Cánh cửa xả sắt 18mm có ô kính quan sát $\varnothing 10\text{ cm}$**:
  * Cắt từ phôi mặt máy thu nhỏ $1\text{ mm}$ đều 4 cạnh: Rộng $398\text{ mm}$, Cao $198\text{ mm}$, Dày $18\text{ mm}$.
  * Ô kính thạch anh chịu nhiệt $\varnothing 100\text{ mm}$ dày $8\text{ mm}$ nằm chính giữa cánh cửa.
  * Vành Inox 304 kẹp giữ kính và 4 vít chìm M5.
  * Cụm tay khóa then gài L bên phải ($X = +229\text{ mm}$) giữ cửa đóng kín khít.

---

## 14. Tích Hợp Trực Tiếp 2 Khâu Nối Đôi Cân Bằng Cửa Xả Vào Mô Hình Chính (`Hai_Khau_Noi_Cua_Xa_8cm`)
* **Tích hợp mô hình & Dọn dẹp macro phụ**:
  * Đã tích hợp trực tiếp và đồng bộ 100% vào **4 tệp mô hình máy chính**: `mo_phong_may_rang_cui.py`, `mo_phong_may_rang_cui.FCMacro`, `trong_hinh_tru.py`, `trong_hinh_tru.FCMacro`.
  * Đã **xóa bỏ hoàn toàn** các tệp macro phụ tạm thời (`macro_thiet_ke_khau_noi_cua_xa.*`) theo yêu cầu, đảm bảo cấu trúc dự án tinh gọn, tập trung duy nhất vào file mô hình hoàn chỉnh.
* **Kích thước hình học chuẩn của Khâu nối đôi cân bằng (Dài mặc định 8cm, ÁP SÁT MẶT MÁY 100%)**:
  1. **2 Nhẫn tròn ôm cây láp $\varnothing 30\text{ mm}$**:
     * Đường kính trong: $ID = 30\text{ mm}$ (vừa khít cây láp tròn $\varnothing 30\text{ mm}$).
     * Bề dày thành nhẫn: $T = 10\text{ mm} \rightarrow$ Đường kính ngoài $OD = 50\text{ mm}$.
     * Chiều dài nhẫn: $L = 30\text{ mm}$ (đúng $3\text{ cm}$ dọc theo chiều trục láp X).
     * Có lỗ ren vít chí M8 trên đỉnh nhẫn siết chặt khóa then vào cây láp.
     * Mép sau cùng của nhẫn tròn: Nằm tại $Y = -518.0\text{ mm}$, phẳng khít với mặt máy trước.
  2. **2 Tấm hình chữ nhật đầu nửa tròn (Dài 8cm, Áp sát mặt máy)**:
     * Kích thước: Rộng $3\text{ cm} = 30\text{ mm}$ (bằng chiều dài nhẫn), Dài **$8\text{ cm} = 80\text{ mm}$** (chuẩn mới theo trục đứng Z từ $Z = -171.93 \to -251.93\text{ mm}$), Dày $10\text{ mm}$ (vừa khít khoảng hở 10mm từ cây láp đến mặt máy).
     * **Mặt lưng áp sát mặt máy**: Toàn bộ mặt lưng phẳng của tấm **ÁP SÁT 100% VÀO MẶT MÁY VÀ CÁNH CỬA XẢ SẮT 18MM** tại $Y = -518.0\text{ mm}$ khi cửa đóng kín. Mặt trước tại $Y = -528.0\text{ mm}$ tiếp xúc phẳng khít với bề mặt cây láp.
     * Đầu dưới bo tròn hình bán nguyệt: Bán kính $R = 15\text{ mm}$ (đường kính ngoài $30\text{ mm}$).
     * Khoan lỗ chốt xoay ở tâm nửa tròn: Đường kính $\varnothing 10\text{ mm}$ dùng cho bu-lông / chốt Pin M10 tại $Z = -236.93\text{ mm}$ (cách mép trên cánh cửa xả $34\text{ mm} = 3.4\text{ cm}$, truyền lực đòn bẩy vững chắc).
  3. **Nhân bản thành 2 bên cân bằng đối xứng ($X = \pm 130\text{ mm}$)**:
     * **Vị trí bố trí**: Đặt cân xứng tại $X = -130.0\text{ mm}$ (Bên Trái) và $X = +130.0\text{ mm}$ (Bên Phải), cách đều tâm máy.
     * **Bảo vệ ô kính quan sát**: Ô kính thạch anh tròn $\varnothing 10\text{ cm}$ ở giữa cửa xả ($X \in [-62, +62\text{ mm}]$) hoàn toàn thông thoáng, mỗi khâu nối cách mép kính tới $68\text{ mm}$, tầm nhìn không bị cản trở.
     * **Cân bằng động lực học**: Khi người vận hành gạt cần 30cm bên trái, lực kéo/ép được truyền đồng thời qua 2 cánh tay đòn song song, triệt tiêu hoàn toàn momen vặn vẹo cánh cửa sắt 18mm nặng và phân bố áp lực đóng kín đều trên toàn bộ gioăng miệng xả.
  4. **2 Chốt Pin M10 & Ê-cu tự hãm (`Hai_Chot_Pin_M10_Cua_Xa`)**:
     * 2 Bu-lông chốt phi 10mm xuyên qua lỗ đầu nửa tròn bắt trực tiếp vào cánh cửa xả sắt 18mm, giữ chặt khâu nối áp khít cánh cửa vào mặt máy khi đóng.

---

## 15. Bộ Chỉnh Gối Bi Trục Phi 60mm - Kiểu Phương Ân (Thiết Kế Chi Tiết Chuẩn 100%)

### 15.1. Khái Niệm & Vai Trò Thực Tế Của Bộ Chỉnh Máy Rang
* **Bộ chỉnh máy rang** là cụm cơ cấu định vị cơ khí chính xác dọc theo trục quay ($Y$), bắt trực tiếp vào mặt máy trước/sau bằng 4 bu-lông lớn:
  1. **Căn chỉnh khe hở nhiệt độ & chống cạ quẹt**: Giữ khe hở đầu trước giữa vành trống và mặt máy trước đúng chuẩn **$0.5\text{ mm}$**, không để trống bị bó kẹt khi giãn nở vì nhiệt ở $250^\circ\text{C} - 300^\circ\text{C}$ và triệt tiêu nguy cơ cạ kim loại làm mòn thành trống hoặc rớt hạt cà phê.
  2. **Bù trừ độ rơ dọc trục & căn chỉnh đồng trục**: Khi lắp ráp thực tế, dung sai cơ khí của mối hàn bệ máy và thân vỏ có thể sai lệch. Bộ chỉnh cho phép người thợ vặn nhẹ cổ siết lục giác $S=105\text{ mm}$ để dịch chuyển ổ bi tịnh tiến mượt mà $\pm 15\text{ mm}$ dọc trục.
  3. **Khóa chống rung cực nhanh (Quick-Lock Clamp)**: Cần gạt công thái học tại góc $-150^\circ$ siết chặt rãnh kẹp ôm cổ ren, triệt tiêu hoàn toàn hiện tượng rung lắc và tự tháo lỏng ốc khi máy chạy liên tục $40\text{ RPM}$.
  4. **Đỡ tải trọng tâm trống rang**: Chịu toàn bộ tải trọng tĩnh của trống ($>150\text{ kg}$) cộng thêm $30 - 60\text{ kg}$ hạt cà phê khi rang và lực quán tính quay.
  5. **Kín bụi tuyệt đối**: Bịt kín đầu cốt trục láp $\varnothing 60\text{ mm}$ bằng nắp tròn $\varnothing 86\text{ mm}$ và 3 vít M4, ngăn $100\%$ vỏ lụa và bụi cà phê lọt vào phá hỏng bạc đạn.

---

### 15.2. Danh Mục 7 Chi Tiết Cấu Tạo Bộ Chỉnh (BOM Chuẩn Thực Tế)

| STT | Mã Chi Tiết | Tên Chi Tiết | Quy Cách Kỹ Thuật & Kích Thước | Vật Liệu Chế Tạo |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `1_Than_Goi_Gang` | **Thân Bệ Bích Vuông Gang** | Vuông $165 \times 165\text{ mm}$, dày $16\text{ mm}$, bo góc $R15$. Cổ tròn $\varnothing 125\text{ mm}$ cao $60\text{ mm}$, có tai kẹp xẻ rãnh góc $-150^\circ$, vú mỡ tra bi góc $+35^\circ$. | Gang xám đúc FC250 |
| **2** | `2_4_BuLong_M14` | **4 Bu-lông Bắt Mặt Máy** | 4 bộ bu-lông M14 $\times 45\text{ mm}$, kèm long đền phẳng $\varnothing 14\text{ mm}$, tâm 4 lỗ vuông $\pm 65\text{ mm}$ bắt chắc vào mặt máy. | Thép cấp bền 8.8 mạ kẽm |
| **3** | `3_Bac_Dan_UC212` | **Bạc Đạn Đỡ Trục UC212** | Ổ bi lòng cầu tự lựa: Lỗ trong $\varnothing 60\text{ mm}$, đường kính ngoài $\varnothing 110\text{ mm}$, bề rộng $24\text{ mm}$, 8 viên bi cầu thép, 2 phớt cao su chắn bụi kép. | Thép ổ lăn cao cấp GCr15 |
| **4** | `4_Cot_Lap_Phi60` | **Đoạn Cốt Láp Bậc $\varnothing 60$** | Đầu trục $\varnothing 60\text{ mm} \times 110\text{ mm}$, mài bóng cấp chính xác h6, phay rãnh then cavet $18 \times 11\text{ mm}$ dài $50\text{ mm}$ truyền lực puly. | Thép hợp kim C45 tôi cứng |
| **5** | `5_Co_Luc_Giac_Ren` | **Cổ Siết Lục Giác Ren Ngoài** | Lục giác ngoài $S=105\text{ mm}$, ống ren ngoài M100 tịnh tiến tiến/lùi định vị khe hở trống rang. | Thép chế tạo máy C45 |
| **6** | `6_Can_Khoa_Nhanh` | **Cần Gạt Khóa Nhanh** | Tay gạt công thái học dài $65\text{ mm}$ kèm núm tròn $\varnothing 24\text{ mm}$ tại góc $-150^\circ$, siết chặt tai kẹp chống xoay tuột ren. | Thép mạ Chrome & Núm bọc nhựa |
| **7** | `7_Nap_Tron_Va_3_Vit_M4` | **Nắp Tròn Bịt Đầu & 3 Vít M4** | Nắp tròn $\varnothing 86\text{ mm}$ có gờ định tâm, siết bằng 3 vít chìm M4 bố trí đều $120^\circ$, bảo vệ kín khít trục. | Thép dập nguội mạ kẽm |

---

### 15.3. Bố Trí Lắp Ráp Trên 2 Mặt Máy (Tab 1: `1_May_Rang_Cui_Hoan_Chinh`)
* **Cụm Trước ($Y = -518.0\text{ mm}$)**: Bích phẳng áp khít mặt trước của tấm mặt máy trước $18\text{ mm}$, vươn nhô về phía trước (hướng $-Y$), ôm trọn đầu cốt láp trước $\varnothing 60\text{ mm}$.
* **Cụm Sau ($Y = +618.0\text{ mm}$)**: Bích phẳng áp khít mặt sau của tấm mặt máy sau $18\text{ mm}$, vươn nhô về phía sau (hướng $+Y$), ôm trọn đầu cốt láp sau $\varnothing 60\text{ mm}$.
* **Bảng điều khiển GUI tích hợp**:
  * Nút `⚙️ Ẩn/Hiện Bộ Chỉnh Trên Máy`: Bật/tắt nhanh tầm nhìn bộ chỉnh trên cả 2 mặt máy.
  * Nút `🔍 Xuyên Thấu Vỏ Gang (Soi Bi)`: Làm trong suốt thân gang $65\%$ để soi rõ bạc đạn UC212, cốt trục và then cavet đang lắp bên trong.
  * Nút `🔬 Soi Chi Tiết (Tab 3)`: Chuyển thẳng sang Tab 3 để soi kỹ 2 phần.

---

### 15.4. Tổ Chức Tab 3 Riêng Biệt (`3_Bo_Chinh_Goi_Bi_Truc_Phi60`)
* **Phần 1: Tháo Rời 7 Chi Tiết (Exploded View - Bên Trái $X = -280\text{ mm}$)**:
  * Tách rời toàn bộ 7 linh kiện theo trình tự tháo lắp dọc trục $Y$ với khoảng giãn hợp lý:
    * Thân bệ gang đúc $\rightarrow$ 4 Bu-lông M14 $\rightarrow$ Bạc đạn UC212 $\rightarrow$ Cốt láp $\varnothing 60 \rightarrow$ Cổ siết lục giác $S105 \rightarrow$ Cần khóa nhanh $\rightarrow$ Nắp tròn 3 vít M4.
* **Phần 2: Cụm Lắp Ráp Hoàn Chỉnh (Assembled View - Bên Phải $X = +280\text{ mm}$)**:
  * Toàn bộ 7 chi tiết được lắp ăn khớp chính xác $100\%$ theo đúng kích thước hình học và tương tác cơ học thực tế.
* **Hệ thống nút góc nhìn chuyên dụng**:
  * `📐 Phối Cảnh Toàn Bộ`: Quan sát toàn diện cả cụm tháo rời và cụm lắp ráp.
  * `💥 Phần 1: Tháo Rời 7 Chi Tiết`: Tự động zoom đặc tả cụm tháo rời ($X = -280\text{ mm}$).
  * `⭐ Phần 2: Cụm Lắp Ráp Hoàn Chỉnh`: Tự động zoom đặc tả cụm lắp ráp ($X = +280\text{ mm}$).
  * `👁️ Chiếu Đứng (Front)`, `🔝 Chiếu Bằng (Top)`, `👉 Chiếu Cạnh (Right)`.






