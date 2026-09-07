# -*- coding: utf-8 -*-
"""
========================================================================================
 Tên file : trong_hinh_tru.py / trong_hinh_tru.FCMacro
 Mô tả    : Macro FreeCAD mô hình hóa & mô phỏng xoay hoàn chỉnh:
            1. TRỐNG HÌNH TRỤ SẮT RỖNG 2 ĐẦU:
               - Chiều cao (dài) : 1m (1000mm)
               - Đường kính ngoài: 80cm (800mm) -> Bán kính ngoài R = 400mm
               - Độ dày thành sắt: 0.8cm (8mm)  -> Bán kính trong r = 392mm
            2. CÂY LÁP (TRỤC BẬC) XUYÊN TÂM CHÍNH GIỮA (CÂY TRỤ):
               - Chiều dài tổng  : 1m2 (1200mm)
               - Thân giữa       : phi 65mm (bán kính R = 32.5mm, dài 1000mm)
               - 2 đầu tiện bậc  : phi 60mm, mỗi đầu dài 10cm (100mm) nhô ra ngoài
            3. HỆ THỐNG 10 CÂY CHỐNG BỐ TRÍ XEN KẼ NHAU (LỆCH PHA 36 ĐỘ):
               - Vật liệu: Ống sắt tròn phi 20mm, rỗng ruột, dày 2mm (phi trong 16mm)
               - Bên 1 (Cách miệng trống 10cm - Y = -400mm): 5 cây ở góc 0°, 72°, 144°, 216°, 288°
               - Bên 2 (Cách miệng lỗ đầu kia 40cm - Y = +100mm): 5 cây ở góc 36°, 108°, 180°, 252°, 324°
               -> 10 cây chống tạo thành ngôi sao 10 cánh xen kẽ đều 36 độ quanh chu vi!
            4. HỆ THỐNG 10 CÁNH ĐẢO LA SẮT 7CM X 0.5CM - CHẠM CÂY TRỤ ĐỂ HÀN VÀO:
               - 5 CÁNH ĐẢO TRONG (HÀN LIỀN TRỰC TIẾP VÀO CÂY TRỤ PHI 65MM):
                 Thanh la sắt bản rộng 7cm (70mm), dày 0.5cm (5mm), chân cánh chạm trực tiếp
                 vào bề mặt cây trụ giữa (R = 32.5mm) để hàn ngấu chắc chắn, đỉnh cánh vươn ra R = 102.5mm.
                 Ngắn 300mm ở khoảng giữa trống (Y = -300 đến 0mm), xoắn ngược đúng 6/10 vòng (216°).
               - 5 CÁNH ĐẢO NGOÀI: Thanh la sắt bản 7cm (70mm), dày 0.5cm (5mm),
                 bước xoắn P = 1600mm, uốn xoắn ĐÚNG 6/10 VÒNG (216°) dọc theo chiều dài trống,
                 bám sát thành trong của trống (R = 392mm -> 322mm), xúc hạt cuộn tịnh tiến xuôi.
            6. MẶT MÁY TRƯỚC ĐỂ GÁ TRỐNG (SẮT TẤM DÀY 1.8CM):
               - Chi tiết tĩnh cố định vào bệ máy để gá miệng trống và đỡ bạc đạn
               - Vật liệu: Sắt tấm dày 1.8cm (18mm), vị trí Y = -500mm đến -518mm
               - Phía trên: Hình tròn R = 430mm (D86cm) bao phủ trọn vẹn lớp vỏ áo ngoài R = 415mm
               - Phía dưới: Chân hình thang cân mở rộng ra đáy phẳng 1m (X = ±500mm tại Z = -800mm) giữ thăng bằng vững chãi
               - Ở giữa phía trên: Lỗ tròn phi 65mm lọt đầu cốt láp phi 60mm (cốt nhô 82mm lắp puly)
            13. BUỒNG ĐỐT CỦI LÓT GẠCH SA MỐT NẰM GỌN DƯỚI TRỐNG (CHỪA NGANG 50CM, CAO ĐẾN TRỐNG, BAO 1 LỚP GẠCH):
                - Kích thước gạch sa mốt chịu lửa: 30cm x 10cm x 5cm (mạch vữa xây 1.5mm)
                - Sàn đáy lát gạch dày 5cm (Z = -850 đến -800mm, rộng 70cm x dài 100cm) nằm gọn gàng khít mép dưới cửa sau
                - Lòng trong chừa thông thủy đúng ngang 50cm (X = -250 đến +250mm) khớp chuẩn miệng cửa đốt củi
                - Bao quanh đúng 1 lớp gạch (dày 10cm, X = -350..-250 và +250..+350mm), tuyệt đối không lòi ra ngoài sườn máy (lọt hoàn toàn trong eo mặt máy R36.8cm)
                - Vách hông xây cao 9 hàng gạch (đến Z = -350mm) vừa chạm đến đáy trống, cưa gọt lòng máng R=425mm ôm cách vỏ trống đúng 1cm giữ nhiệt tuyệt đối
                - Vách trước dày 10cm ngăn táp lửa trực tiếp vào mặt máy trước
            * TỰ ĐỘNG ĐÓNG SẠCH TẤT CẢ TÀI LIỆU CŨ TRƯỚC KHI MỞ MỚI *
            * BẢNG ĐIỀU KHIỂN XOAY ĐỒNG BỘ 360° + BẬT/TẮT XUYÊN THẤU & ẨN/HIỆN MẶT MÁY / VỎ TRỐNG / LÒ GẠCH *
 Tác giả  : Kỹ Sư Thiết Kế Cơ Khí & CAD Tự Động Hóa
 Phiên bản: 15.0 - Firebrick Chamber Compact Under Drum (50cm Clear, 1 Brick Layer, 1cm Gap Edition)
========================================================================================
"""

import sys
import math
import FreeCAD as App
import Part

# Cấu hình UTF-8 an toàn cho console Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Nhập thư viện Qt hỗ trợ đa phiên bản (PySide6 cho FreeCAD 1.0+, PySide2 cho 0.20/0.21)
try:
    from PySide6 import QtCore, QtWidgets, QtGui
except ImportError:
    try:
        from PySide2 import QtCore, QtWidgets, QtGui
    except ImportError:
        from PySide import QtCore, QtWidgets, QtGui

try:
    import FreeCADGui as Gui
except ImportError:
    Gui = None

# Biến toàn cục giữ tham chiếu cửa sổ điều khiển
_TRONG_DIEU_KHIEN_WINDOW = None


def kiem_tra_co_gui():
    """Kiểm tra môi trường FreeCAD có đang chạy đồ họa GUI hay không."""
    if Gui is None:
        return False
    try:
        if callable(getattr(Gui, "getMainWindow", None)):
            return Gui.getMainWindow() is not None
    except Exception:
        return False
    return False


def dong_sach_tat_ca_tai_lieu_cu():
    """Đóng sạch sẽ 100% tất cả các tài liệu và cửa sổ mô phỏng cũ đang mở."""
    global _TRONG_DIEU_KHIEN_WINDOW

    if _TRONG_DIEU_KHIEN_WINDOW is not None:
        try:
            _TRONG_DIEU_KHIEN_WINDOW.close()
        except Exception:
            pass
        _TRONG_DIEU_KHIEN_WINDOW = None

    try:
        app = QtWidgets.QApplication.instance()
        if app:
            for w in list(app.topLevelWidgets()):
                if isinstance(w, QtWidgets.QDialog):
                    try:
                        if hasattr(w, "timer") and hasattr(w.timer, "stop"):
                            w.timer.stop()
                        w.close()
                    except Exception:
                        pass
    except Exception:
        pass

    for doc_name in list(App.listDocuments().keys()):
        try:
            App.closeDocument(doc_name)
        except Exception:
            pass


def gan_mau(obj, mau_rgb, line_color=(0.2, 0.2, 0.2), line_width=1.5, do_trong_suot=0):
    """Gán màu sắc và thuộc tính hiển thị trực quan cho chi tiết 3D."""
    if kiem_tra_co_gui() and hasattr(obj, "ViewObject") and obj.ViewObject:
        vo = obj.ViewObject
        vo.ShapeColor = mau_rgb
        vo.LineColor = line_color
        vo.Transparency = do_trong_suot
        if hasattr(vo, "LineWidth"):
            vo.LineWidth = line_width


def tao_mo_hinh_chi_tiet(doc):
    """
    Tạo mô hình 3D hoàn chỉnh gồm:
    1. Trống hình trụ sắt rỗng 2 đầu: Dài 1000mm (1m), phi 800mm (80cm), dày 8mm (0.8cm).
    2. Cây láp xuyên tâm: Dài 1200mm (1m2), thân giữa phi 65mm, 2 đầu phi 60mm x 100mm (10cm).
    3. Hệ thống 10 cây chống XEN KẼ NHAU (Lệch pha 36 độ):
       - Ống tròn phi 20mm, rỗng ruột, dày 2mm (phi trong 16mm).
       - Bên 1: Cách miệng trống 10cm (Y = -400mm), góc 0°, 72°, 144°, 216°, 288°.
       - Bên 2: Cách miệng lỗ đầu kia 40cm (Y = +100mm), góc 36°, 108°, 180°, 252°, 324°.
    4. 5 Cánh đảo ngoài: La sắt bản 7cm (70mm), dày 0.5cm (5mm), xoắn 6/10 vòng (216°) dọc thành trống.
    5. 5 Cánh đảo trong: La sắt bản 7cm (70mm), dày 0.5cm (5mm), CHẠM TRỰC TIẾP VÀO CÂY TRỤ ĐỂ HÀN VÀO!
    """
    # -------------------------------------------------------------
    # 1. VỎ TRỐNG TRONG HÌNH TRỤ SẮT (D80cm x L1m x Dày 0.8cm)
    # -------------------------------------------------------------
    chieu_dai = 1000.0   # 1m
    r_ngoai = 400.0      # Ngang 80cm -> R = 400mm
    do_day = 8.0         # Dày 0.8cm = 8mm
    r_trong = r_ngoai - do_day  # 392mm

    cyl_out = Part.makeCylinder(r_ngoai, chieu_dai, App.Vector(0, -chieu_dai / 2.0, 0), App.Vector(0, 1, 0))
    cyl_in = Part.makeCylinder(r_trong, chieu_dai + 20.0, App.Vector(0, -chieu_dai / 2.0 - 10.0, 0), App.Vector(0, 1, 0))
    hinh_trong = cyl_out.cut(cyl_in)

    obj_trong = doc.addObject("Part::Feature", "Trong_Hinh_Tru_Sat")
    obj_trong.Shape = hinh_trong
    obj_trong.Label = "1. Vỏ Trống Trong (D80cm x L1m x Dày 0.8cm)"
    # Mặc định để trong suốt nhẹ 45% để nhìn thấu các cánh đảo bên trong
    gan_mau(obj_trong, (0.76, 0.79, 0.84), do_trong_suot=45)

    # -------------------------------------------------------------
    # 1b. LỚP ÁO TRỐNG NGOÀI: DÀY 0.5CM, HỞ 1CM CÁCH KHÍ
    #    - Hở 1cm cách khí: R_in = 400mm + 10mm = 410mm (Phi trong 820mm)
    #    - Dày 0.5cm (5mm): R_out = 410mm + 5mm = 415mm (Phi ngoài 830mm = 83cm)
    #    - Chiều dài: 1000mm (1m) bằng chiều dài trống
    # -------------------------------------------------------------
    khoang_cach_khi = 10.0  # Hở 1cm cách khí
    do_day_ao = 5.0        # Dày 0.5cm = 5mm
    r_ao_in = r_ngoai + khoang_cach_khi  # 410.0mm
    r_ao_out = r_ao_in + do_day_ao       # 415.0mm

    cyl_ao_out = Part.makeCylinder(r_ao_out, chieu_dai, App.Vector(0, -chieu_dai / 2.0, 0), App.Vector(0, 1, 0))
    cyl_ao_in = Part.makeCylinder(r_ao_in, chieu_dai + 20.0, App.Vector(0, -chieu_dai / 2.0 - 10.0, 0), App.Vector(0, 1, 0))
    hinh_ao = cyl_ao_out.cut(cyl_ao_in)

    obj_ao_ngoai = doc.addObject("Part::Feature", "Lop_Ao_Trong_Ngoai_Cach_Khi")
    obj_ao_ngoai.Shape = hinh_ao
    obj_ao_ngoai.Label = "1b. Lớp Áo Trống Ngoài (D83cm x Dày 0.5cm, Hở Khí 1cm)"
    # Để độ trong suốt 55% để nhìn rõ lớp đệm khí 1cm và vỏ trống trong
    gan_mau(obj_ao_ngoai, (0.70, 0.75, 0.82), do_trong_suot=55, line_color=(0.15, 0.20, 0.30), line_width=1.5)

    # -------------------------------------------------------------
    # 2. CÂY LÁP (TRỤC BẬC) DÀI 1M2, THÂN PHI 65MM, 2 ĐẦU PHI 60MM X 10CM
    # -------------------------------------------------------------
    shapes_lap = []
    # Đầu 1: phi 60mm (R = 30mm), dài 100mm (10cm) tại Y: -600 đến -500
    dau_1 = Part.makeCylinder(30.0, 100.0, App.Vector(0, -600.0, 0), App.Vector(0, 1, 0))
    # Thân giữa (Cây Trụ Chính): phi 65mm (R = 32.5mm), dài 1000mm tại Y: -500 đến +500
    than_giua = Part.makeCylinder(32.5, 1000.0, App.Vector(0, -500.0, 0), App.Vector(0, 1, 0))
    # Đầu 2: phi 60mm (R = 30mm), dài 100mm (10cm) tại Y: +500 đến +600
    dau_2 = Part.makeCylinder(30.0, 100.0, App.Vector(0, 500.0, 0), App.Vector(0, 1, 0))

    shapes_lap.extend([dau_1, than_giua, dau_2])
    hinh_lap = Part.makeCompound(shapes_lap)

    obj_lap = doc.addObject("Part::Feature", "Cay_Lap_Truc_Bac")
    obj_lap.Shape = hinh_lap
    obj_lap.Label = "2. Cây Láp Trục Bậc (L1m2, Thân D65mm, 2 Đầu D60mm x 10cm)"
    gan_mau(obj_lap, (0.90, 0.72, 0.22), line_color=(0.35, 0.25, 0.05), line_width=2.0)

    # -------------------------------------------------------------
    # 3. HỆ THỐNG 10 CÂY CHỐNG BỐ TRÍ XEN KẼ NHAU (LỆCH PHA 36 ĐỘ)
    #    - Ống sắt phi 20mm, rỗng ruột, dày 2mm (phi trong 16mm)
    #    - Bên 1: Y = -400mm (Cách miệng trống 10cm), góc 0°, 72°, 144°, 216°, 288°
    #    - Bên 2: Y = +100mm (Cách miệng lỗ đầu kia 40cm), góc 36°, 108°, 180°, 252°, 324°
    # -------------------------------------------------------------
    shapes_chong = []
    r_chong_ngoai = 10.0   # phi 20mm -> R = 10mm
    r_chong_trong = 8.0    # dày 2mm -> r = 8mm
    r_start = 30.0         # Cắm từ bề mặt cây láp
    r_end = 392.0          # Chạm thành trong của trống
    chieu_dai_chong = r_end - r_start

    vi_tri_chong = [
        (-400.0, -4.5, "Bên 1 (Cách miệng trống 10cm - 5 Cây Gần Đầu) - Góc bù -4.5° để vừa chạm sát sườn cánh ngoài hàn liền"),
        (100.0,  36.0, "Bên 2 (Cách miệng lỗ đầu kia 40cm - 5 Cây Ở Giữa) - Vừa chạm 5 cánh ngoài chuẩn xác")
    ]

    for y_pos, offset_goc, mo_ta in vi_tri_chong:
        # Vòng cổ bích hàn ôm trục cây láp
        co_truc_out = Part.makeCylinder(38.0, 30.0, App.Vector(0, y_pos - 15.0, 0), App.Vector(0, 1, 0))
        co_truc_in = Part.makeCylinder(32.5, 34.0, App.Vector(0, y_pos - 17.0, 0), App.Vector(0, 1, 0))
        co_truc = co_truc_out.cut(co_truc_in)
        shapes_chong.append(co_truc)

        # 5 cây chống mỗi bên, lệch pha 36 độ
        for i in range(5):
            goc_do = offset_goc + (i * 72.0)

            ong_ngoai = Part.makeCylinder(
                r_chong_ngoai,
                chieu_dai_chong,
                App.Vector(r_start, y_pos, 0),
                App.Vector(1, 0, 0)
            )
            ong_trong = Part.makeCylinder(
                r_chong_trong,
                chieu_dai_chong + 4.0,
                App.Vector(r_start - 2.0, y_pos, 0),
                App.Vector(1, 0, 0)
            )
            cay_chong_ong = ong_ngoai.cut(ong_trong)

            cay_chong_ong.Placement = App.Placement(
                App.Vector(0, 0, 0),
                App.Rotation(App.Vector(0, 1, 0), goc_do)
            )
            shapes_chong.append(cay_chong_ong)

    hinh_chong = Part.makeCompound(shapes_chong)
    obj_chong = doc.addObject("Part::Feature", "He_Thong_10_Cay_Chong_Xen_Ke")
    obj_chong.Shape = hinh_chong
    obj_chong.Label = "3. Hệ Thống 10 Cây Chống Xen Kẽ Nhau 36° (Ống D20mm Dày 2mm)"
    gan_mau(obj_chong, (0.16, 0.48, 0.78), line_color=(0.10, 0.25, 0.45), line_width=1.8)

    # -------------------------------------------------------------
    # 4. HỆ THỐNG 5 CÁNH ĐẢO NGOÀI: LA SẮT BẢN 7CM, DÀY 0.5CM, XOẮN 6/10 VÒNG (216°)
    #    - Vật liệu: Thanh la sắt bản rộng 7cm (70mm), dày 0.5cm (5mm)
    #    - Cạnh ngoài bám sát thành trong trống: R = 392mm
    #    - Cạnh trong: R = 322mm (bản rộng đúng 7cm)
    #    - Chiều dài trục: H = 960mm (Y = -480 đến +480)
    #    - Bước xoắn pitch = H / 0.6 = 1600.0mm -> XOẮN ĐÚNG 6/10 VÒNG = 216 ĐỘ!
    #    - 5 cánh phân bố đều: 0°, 72°, 144°, 216°, 288°
    # -------------------------------------------------------------
    H_out = 960.0
    pitch_out = H_out / 0.6   # 1600.0mm -> Xoắn ĐÚNG 6/10 vòng (216 độ)
    R_out_wall = 392.0        # Sát thành trong trống
    R_out_edge = 392.0 - 70.0 # 322mm -> Bản rộng đúng 7cm (70mm)

    h_wall = Part.makeHelix(pitch_out, H_out, R_out_wall, 0, False)
    h_edge = Part.makeHelix(pitch_out, H_out, R_out_edge, 0, False)
    loft_out = Part.makeLoft([Part.Wire(h_wall.Edges), Part.Wire(h_edge.Edges)], False, False)
    # Độ dày thanh la đúng 0.5cm = 5mm
    base_outer = loft_out.makeOffsetShape(5.0, 0.01, fill=True)
    base_outer.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -90.0)
    base_outer.translate(App.Vector(0, -H_out / 2.0, 0))

    # Căn chỉnh góc xoay ban đầu:
    # Tại Y = -400mm (vị trí 5 cây chống tầng 1 ở các góc 0°, 72°, 144°, 216°, 288°):
    # Cánh đảo dài 960mm bắt đầu từ Y = -480mm đến Y = -400mm (đi được ΔY = 80mm).
    # Với bước xoắn pitch = 1600mm, góc xoắn tích lũy tại Y = -400mm là: (80 / 1600) * 360° = +18.0°.
    # Để cánh đảo chạm khít 100% vào đúng 5 cây chống để hàn ngấu liên kết:
    # Cần bù góc lệch pha ban đầu: offset_goc_canh = -18.0°.
    # Khi đó góc cánh tại Y = -400mm = (i * 72° - 18°) + 18° = i * 72° (TRÙNG KHÍT HOÀN TOÀN VỚI 5 CÂY CHỐNG!)
    offset_goc_canh = -18.0

    shapes_canh_ngoai = []
    for i in range(5):
        angle = i * 72.0 + offset_goc_canh
        c_ngoai = base_outer.copy()
        c_ngoai.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), angle)
        shapes_canh_ngoai.append(c_ngoai)

    hinh_canh_ngoai = Part.makeCompound(shapes_canh_ngoai)
    obj_canh_ngoai = doc.addObject("Part::Feature", "5_Canh_Dao_Ngoai_LaSat_7cm_6_10_Vong_216")
    obj_canh_ngoai.Shape = hinh_canh_ngoai
    obj_canh_ngoai.Label = "4. 5 Cánh Đảo Ngoài (La Sắt Bản 7cm, Dày 0.5cm, Xoắn 6/10 Vòng 216°)"
    # Màu đỏ cam nổi bật
    gan_mau(obj_canh_ngoai, (0.95, 0.35, 0.10), line_color=(0.60, 0.15, 0.05), line_width=1.6)

    # -------------------------------------------------------------
    # 5. HỆ THỐNG 5 CÁNH ĐẢO TRONG: LA SẮT BẢN 10CM, DÀY 0.8CM, DÀI 50CM
    #    - VỊ TRÍ: NẰM NGAY GIỮA CỦA 5 CÂY CHỐNG, KHÔNG ÁP SÁT VÀO CÂY LÁP!
    #    - Vật liệu: Thanh la sắt bản rộng 10cm (100mm), dày 0.8cm (8mm)
    #    - Bán kính làm việc (nằm ngay giữa thân cây chống):
    #      + Cây chống dài từ R = 32.5mm (cây láp) đến R = 392mm (thành trống), tâm giữa R = 212mm
    #      + Cánh đảo trong bản 10cm đặt đúng vị trí giữa: R_in = 162mm -> R_out = 262mm
    #      + Cách cây láp: 162 - 32.5 = 129.5mm (~13cm thông thoáng, TUYỆT ĐỐI KHÔNG áp sát cây láp)
    #      + Cách thành trống: 392 - 262 = 130mm (13cm)
    #    - Chiều dài: H = 650mm (65cm) - kéo dài thêm 15cm về phía sau (từ Y = -400mm đến Y = +250mm)
    #    - Bước xoắn pitch = H / 0.6 = 1083.3mm, lefthand=True -> XOẮN NGƯỢC 6/10 VÒNG (216°)
    #    - 5 cánh bố trí ở góc: 36°, 108°, 180°, 252°, 324°
    # -------------------------------------------------------------
    H_in = 650.0
    pitch_in = H_in / 0.6     # 1083.3mm -> Xoắn ngược ĐÚNG 6/10 vòng (216 độ)
    R_in = 162.0              # Cách cây láp ~13cm (KHÔNG áp sát vào cây láp)
    R_out = R_in + 100.0      # 262.0mm -> Bản rộng đúng 10cm (100mm), nằm ngay giữa cây chống
    thick_in = 8.0            # Độ dày thanh la đúng 0.8cm = 8mm

    hi_inner = Part.makeHelix(pitch_in, H_in, R_in, 0, True)   # Cạnh trong ở giữa cây chống
    hi_outer = Part.makeHelix(pitch_in, H_in, R_out, 0, True)  # Cạnh ngoài ở giữa cây chống
    loft_in = Part.makeLoft([Part.Wire(hi_inner.Edges), Part.Wire(hi_outer.Edges)], False, False)
    # Độ dày thanh la đúng 0.8cm = 8mm
    base_inner = loft_in.makeOffsetShape(thick_in, 0.01, fill=True)
    base_inner.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -90.0)
    base_inner.translate(App.Vector(0, -400.0, 0))

    shapes_canh_trong = []
    for i in range(5):
        angle = 36.0 + i * 72.0
        c_trong = base_inner.copy()
        c_trong.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), angle)
        shapes_canh_trong.append(c_trong)

    hinh_canh_trong = Part.makeCompound(shapes_canh_trong)
    obj_canh_trong = doc.addObject("Part::Feature", "5_Canh_Dao_Trong_LaSat_10cm_Day_08cm_Dai_65cm")
    obj_canh_trong.Shape = hinh_canh_trong
    obj_canh_trong.Label = "5. 5 Cánh Đảo Trong (La Sắt Bản 10cm, Dày 0.8cm, Dài 65cm, Giữa Cây Chống)"
    # Màu xanh lục ngọc tươi sáng tương phản với cánh ngoài
    gan_mau(obj_canh_trong, (0.10, 0.78, 0.52), line_color=(0.05, 0.40, 0.25), line_width=1.8)

    # -------------------------------------------------------------
    # 6. MẶT MÁY TRƯỚC ĐỂ GÁ TRỐNG: SẮT DÀY 1.8CM, VÒNG TRÒN LỚN HƠN 10CM (PHI 96CM)
    #    - CÓ MIỆNG RA HÀNG (CỬA XẢ NÔNG SẢN/CÀ PHÊ):
    #      + Cao 10cm (100mm) tại điểm thấp nhất của lòng trống
    #      + Phía trên là đường thẳng nằm ngang dài 50cm (500mm, từ X = -250mm đến +250mm)
    #      + Phía dưới là đường cong ôm sát vách trong của trống rang R = 392mm
    #      + Đáy tiếp xúc trơn tru phẳng khít với đáy lòng trống trong, hạt xả trút 100% không bị đọng
    #      + Khoảng thịt thép đỡ cốt trục phi 65mm còn tới 259.5mm (~26cm) siêu cứng vững
    # -------------------------------------------------------------
    R_mat = 480.0
    T_mat = 18.0
    Y_mat = -518.0

    # Góc thắt eo cong vào: -40 độ (tương ứng 320° bên phải và 220° bên trái)
    theta_neck = math.radians(-40.0)
    x_tR = R_mat * math.cos(theta_neck)      # +367.70mm (Đáy trên bên phải)
    z_tR = R_mat * math.sin(theta_neck)      # -308.53mm
    x_tL = -x_tR                             # -367.70mm (Đáy trên bên trái)
    z_tL = z_tR                              # -308.53mm

    W_half_bot = 550.0   # Nửa chiều rộng đáy dưới = 550mm -> Đáy dưới rộng 1100mm (1.1m, dài hơn đáy trên 735mm)
    Z_bottom = -850.0    # Đáy dưới phẳng tại Z = -850mm tiếp xúc mặt sàn vững chãi

    arc = Part.Arc(
        App.Vector(x_tR, Y_mat, z_tR),
        App.Vector(0, Y_mat, R_mat),
        App.Vector(x_tL, Y_mat, z_tL)
    )
    edge_arc = arc.toShape()
    edge_L = Part.makeLine(App.Vector(x_tL, Y_mat, z_tL), App.Vector(-W_half_bot, Y_mat, Z_bottom))
    edge_bot = Part.makeLine(App.Vector(-W_half_bot, Y_mat, Z_bottom), App.Vector(W_half_bot, Y_mat, Z_bottom))
    edge_R = Part.makeLine(App.Vector(W_half_bot, Y_mat, Z_bottom), App.Vector(x_tR, Y_mat, z_tR))

    wire_mat = Part.Wire([edge_arc, edge_L, edge_bot, edge_R])
    face_mat = Part.Face(wire_mat)
    solid_mat = face_mat.extrude(App.Vector(0, T_mat, 0))

    # Khoét lỗ phi 65mm xuyên tâm
    hole_mat = Part.makeCylinder(32.5, T_mat + 10.0, App.Vector(0, Y_mat - 5.0, 0), App.Vector(0, 1, 0))
    hinh_mat_truoc = solid_mat.cut(hole_mat)

    # Khoét miệng ra hàng: 2 bên thành cao đúng 10cm (100mm) từ mép dưới lên trên, phía trên đường thẳng dài 50cm (500mm), phía dưới cong theo trống R392mm
    R_drum_in = 392.0
    W_mieng = 500.0
    half_W_m = W_mieng / 2.0   # 250.0mm (từ X = -250mm đến X = +250mm)
    z_edge_m = -math.sqrt(R_drum_in**2 - half_W_m**2)   # -301.93mm (mép dưới cung tròn)
    z_top_m = z_edge_m + 100.0   # -201.93mm (2 bên thành cao đúng 10cm, điểm cao nhất ở giữa ~19cm)

    arc_mieng = Part.Arc(
        App.Vector(-half_W_m, Y_mat - 5.0, z_edge_m),
        App.Vector(0.0, Y_mat - 5.0, -R_drum_in),
        App.Vector(half_W_m, Y_mat - 5.0, z_edge_m)
    )
    edge_arc_m = arc_mieng.toShape()
    edge_R_m = Part.makeLine(App.Vector(half_W_m, Y_mat - 5.0, z_edge_m), App.Vector(half_W_m, Y_mat - 5.0, z_top_m))
    edge_top_m = Part.makeLine(App.Vector(half_W_m, Y_mat - 5.0, z_top_m), App.Vector(-half_W_m, Y_mat - 5.0, z_top_m))
    edge_L_m = Part.makeLine(App.Vector(-half_W_m, Y_mat - 5.0, z_top_m), App.Vector(-half_W_m, Y_mat - 5.0, z_edge_m))

    wire_mieng = Part.Wire([edge_arc_m, edge_R_m, edge_top_m, edge_L_m])
    face_mieng = Part.Face(wire_mieng)
    solid_cutter_mieng = face_mieng.extrude(App.Vector(0, T_mat + 10.0, 0))
    hinh_mat_truoc = hinh_mat_truoc.cut(solid_cutter_mieng)

    # Khoét lỗ tròn phi 30mm nằm ngang cây láp bên trái (X = -200, Z = 0) để cắm cây thăm hàng
    P_hole_mid = App.Vector(-200.0, Y_mat + T_mat / 2.0, 0.0)
    v_dir = App.Vector(30.0, 100.0, 0.0)  # Nằm ngang cây láp (Z=0), để xéo xiên vào tâm 16.7°
    v_unit = v_dir.normalize()
    p_cut_start = P_hole_mid - v_unit * 30.0
    hole_tham = Part.makeCylinder(15.0, 60.0, p_cut_start, v_unit)
    hinh_mat_truoc = hinh_mat_truoc.cut(hole_tham)

    obj_mat_truoc = doc.addObject("Part::Feature", "Mat_May_Truoc_Ga_Trong_18mm")
    obj_mat_truoc.Shape = hinh_mat_truoc
    obj_mat_truoc.Label = "6. Mặt Máy Trước Gá Trống (Sắt Dày 1.8cm, Tròn D96cm, Chân 1.1m, Lỗ D65mm, Miệng Xả 50cm, Lỗ Thăm D30mm Ngang Cốt)"
    # Màu xám xanh thép công nghiệp dày dặn
    gan_mau(obj_mat_truoc, (0.28, 0.35, 0.45), line_color=(0.10, 0.15, 0.25), line_width=2.0)


    # -------------------------------------------------------------
    # 7. MẶT MÁY SAU ĐỂ GÁ TRỐNG: SẮT DÀY 1.8CM (COPY GIỐNG HỆT MẶT TRƯỚC, BỐ TRÍ PHÍA SAU)
    #    - Vị trí trục Y: Từ Y = +500.0mm đến Y = +518.0mm (ngay miệng sau của trống)
    #    - Kích thước giống hệt mặt trước: Cung tròn D96cm (R480mm) thắt eo -40° phía trên,
    #      chân hình thang cân đáy dưới rộng 1.1m (Z = -850mm) tiếp xúc sàn xưởng.
    #    - Lỗ khoét phi 65mm (R = 32.5mm) tại tâm (0, 0) để lọt đầu cốt láp phi 60mm phía sau.
    #    - Đoạn đầu cốt láp sau (dài 100mm, từ Y=+500 đến Y=+600) nhô ra ngoài 82mm để lắp gối bi & puly kéo.
    #    - Chi tiết tĩnh: Gá cố định vào khung bệ máy, cùng với mặt trước nâng đỡ toàn bộ trống rang.
    # -------------------------------------------------------------
    Y_mat_sau = 500.0
    arc_sau = Part.Arc(
        App.Vector(x_tR, Y_mat_sau, z_tR),
        App.Vector(0, Y_mat_sau, R_mat),
        App.Vector(x_tL, Y_mat_sau, z_tL)
    )
    edge_arc_sau = arc_sau.toShape()
    edge_L_sau = Part.makeLine(App.Vector(x_tL, Y_mat_sau, z_tL), App.Vector(-W_half_bot, Y_mat_sau, Z_bottom))
    edge_bot_sau = Part.makeLine(App.Vector(-W_half_bot, Y_mat_sau, Z_bottom), App.Vector(W_half_bot, Y_mat_sau, Z_bottom))
    edge_R_sau = Part.makeLine(App.Vector(W_half_bot, Y_mat_sau, Z_bottom), App.Vector(x_tR, Y_mat_sau, z_tR))

    wire_mat_sau = Part.Wire([edge_arc_sau, edge_L_sau, edge_bot_sau, edge_R_sau])
    face_mat_sau = Part.Face(wire_mat_sau)
    solid_mat_sau = face_mat_sau.extrude(App.Vector(0, T_mat, 0))

    # Khoét lỗ phi 65mm xuyên tâm
    hole_mat_sau = Part.makeCylinder(32.5, T_mat + 10.0, App.Vector(0, Y_mat_sau - 5.0, 0), App.Vector(0, 1, 0))
    hinh_mat_sau = solid_mat_sau.cut(hole_mat_sau)

    # Khoét 1 lỗ chữ nhật ở mặt sau: Dài 50cm (500mm), Cao 30cm (300mm), Cách chân máy 5cm (50mm)
    W_lo_sau = 500.0
    H_lo_sau = 300.0    # Giảm chiều cao còn 30cm (300mm) theo yêu cầu
    half_W_lo_sau = W_lo_sau / 2.0
    Z_bot_lo_sau = Z_bottom + 50.0   # -800.0mm (cách chân máy 5cm = 50mm)
    cutter_lo_sau = Part.makeBox(
        W_lo_sau,
        T_mat + 10.0,
        H_lo_sau,
        App.Vector(-half_W_lo_sau, Y_mat_sau - 5.0, Z_bot_lo_sau)
    )
    hinh_mat_sau = hinh_mat_sau.cut(cutter_lo_sau)

    obj_mat_sau = doc.addObject("Part::Feature", "Mat_May_Sau_Ga_Trong_18mm")
    obj_mat_sau.Shape = hinh_mat_sau
    obj_mat_sau.Label = "7. Mặt Máy Sau Gá Trống (Sắt Dày 1.8cm, Tròn D96cm Cong Vào Trên, Hình Thang Dưới Rộng 1.1m, Lỗ D65mm, Lỗ Chữ Nhật 50x30cm Cách Chân 5cm)"
    gan_mau(obj_mat_sau, (0.28, 0.35, 0.45), line_color=(0.10, 0.15, 0.25), line_width=2.0)

    # -------------------------------------------------------------
    # 8. CHÂN ĐẾ MÁY HÌNH CHỮ NHẬT: SẮT TẤM DÀY 0.5CM (5MM)
    #    - Yêu cầu: "thiết kế chân máy hình chữ nhật, dầy 0.5cm, kích thước vừa đủ, dư mỗi bên trước sau, trái phải 0.5cm"
    #    - Kích thước vừa khít theo đúng footprint của 2 chân mặt máy:
    #      + Chiều rộng (Trái - Phải theo trục X):
    #        Chân 2 mặt máy rộng 1100mm (từ X = -550mm đến X = +550mm).
    #        Dư mỗi bên trái phải 0.5cm (5mm): từ X = -555.0mm đến X = +555.0mm.
    #        -> Tổng chiều rộng: W = 1110.0mm = 111.0cm = 1.11m.
    #      + Chiều dài (Trước - Sau theo trục Y):
    #        Chân mặt trước tại Y = -518mm, chân mặt sau tại Y = +518mm (khoảng cách 1036mm).
    #        Dư mỗi bên trước sau 0.5cm (5mm): từ Y = -523.0mm đến Y = +523.0mm.
    #        -> Tổng chiều dài: L = 1046.0mm = 104.6cm = 1.046m.
    #      + Độ dày & Cao độ (theo trục Z):
    #        Độ dày tấm: đúng 0.5cm (5.0mm).
    #        Mặt trên của chân đế tại Z = -850.0mm (đỡ trọn vẹn đáy 2 mặt máy).
    #        Mặt dưới của chân đế tại Z = -855.0mm (tiếp xúc trực tiếp sàn xưởng).
    #    - Chi tiết tĩnh: Hàn/bắt bu lông chắc chắn với chân của 2 mặt máy, tạo khối khung gầm đầm chắc 100%.
    # -------------------------------------------------------------
    W_chan = 1110.0
    L_chan = 1046.0
    T_chan = 5.0
    pnt_chan = App.Vector(-555.0, -523.0, -855.0)

    hinh_chan_de = Part.makeBox(W_chan, L_chan, T_chan, pnt_chan)
    obj_chan_de = doc.addObject("Part::Feature", "Chan_De_May_Hinh_Chu_Nhat_5mm")
    obj_chan_de.Shape = hinh_chan_de
    obj_chan_de.Label = "8. Chân Đế Máy Hình Chữ Nhật (Sắt Dày 0.5cm, 111cm x 104.6cm, Dư Trước Sau Trái Phải 0.5cm)"
    # Màu xám đen thép tấm bệ sàn
    gan_mau(obj_chan_de, (0.22, 0.26, 0.32), line_color=(0.08, 0.10, 0.15), line_width=2.0)

    # -------------------------------------------------------------
    # 9. CÂY THĂM HÀNG (SAMPLER / TRIER): ỐNG KIM LOẠI INOX & MÁNG XÚC MẪU
    #    - Cắm qua lỗ tròn phi 30mm NẰM NGANG CÂY LÁP BÊN TRÁI (X = -200, Z = 0)
    #    - ĐẶT XÉO: Nằm ngang cao độ cây láp (Z = 0), xiên 16.7° vào trong tâm buồng rang
    #    - Máng xúc mẫu khoét hở hướng thẳng lên trên (+Z) đón luồng hạt rơi cuộn
    #    - CANH VỊ TRÍ TUYỆT ĐỐI KHÔNG CẤN CÁNH ĐẢO:
    #      + Đầu tip trong trống kết thúc tại Y = -427.6mm, cách 5 cây chống (Y = -410mm) tới 17.6mm
    #      + Cách tầng cánh trong (Y = -400mm) tới 27.6mm
    #      + Bán kính làm việc R = 175.6mm, cách xa cánh ngoài (R = 322mm) tới 146.4mm (~14.6cm)
    #      + Cách trục láp phi 65mm (R = 32.5mm) tới 143.1mm (~14.3cm)
    #      -> Hoàn toàn an toàn, tự do xoay lấy mẫu mà không chạm bất kỳ chi tiết quay nào!
    # -------------------------------------------------------------
    p_tube_start = P_hole_mid - v_unit * 35.0
    L_tube = 120.0
    tube_tham = Part.makeCylinder(12.0, L_tube, p_tube_start, v_unit)

    # Gờ bích chặn định vị phía ngoài mặt máy
    p_flange = P_hole_mid - v_unit * 12.0
    flange_tham = Part.makeCylinder(19.0, 6.0, p_flange, v_unit)
    tube_metal = tube_tham.fuse(flange_tham)

    # Khoét rãnh lòng máng xúc mẫu hạt ở đoạn nằm trong lòng trống
    p_cut_scoop = p_tube_start + v_unit * 50.0
    cutter_inner = Part.makeCylinder(9.5, 68.0, p_cut_scoop, v_unit)
    v_up_perp = App.Vector(0, 0, 1)  # Mở rãnh hướng thẳng lên trên đón hạt rơi
    box_open = Part.makeCylinder(13.0, 65.0, p_cut_scoop + v_up_perp * 4.0, v_unit)
    hinh_cay_tham = tube_metal.cut(cutter_inner)
    hinh_cay_tham = hinh_cay_tham.cut(box_open)

    obj_cay_tham = doc.addObject("Part::Feature", "Cay_Tham_Hang_Inox_Phi24mm")
    obj_cay_tham.Shape = hinh_cay_tham
    obj_cay_tham.Label = "9. Cây Thăm Hàng (Inox Phi 24mm, Nằm Ngang Cây Láp Z=0, Cắm Xéo Lỗ Phi 30mm)"
    # Màu inox bạc sáng bóng sang trọng
    gan_mau(obj_cay_tham, (0.85, 0.88, 0.92), line_color=(0.30, 0.35, 0.40), line_width=1.5)

    # -------------------------------------------------------------
    # 10. TAY CẦM CÂY THĂM HÀNG: GỖ TIỆN CÁCH NHIỆT CÔNG THÁI HỌC
    #     - Nằm ngang cây láp phía trước mặt máy (Z = 0), chếch ra ngoài bên trái rất thuận tay
    #     - Đường kính phi 32mm, dài 110mm, chống nóng an toàn tuyệt đối khi thao tác
    # -------------------------------------------------------------
    p_handle_start = p_tube_start - v_unit * 110.0
    hinh_tay_cam = Part.makeCylinder(16.0, 110.0, p_handle_start, v_unit)

    obj_tay_cam = doc.addObject("Part::Feature", "Tay_Cam_Cay_Tham_Hang_Go")
    obj_tay_cam.Shape = hinh_tay_cam
    obj_tay_cam.Label = "10. Tay Cầm Cây Thăm Hàng (Gỗ Tiện Cách Nhiệt Phi 32mm, Nằm Ngang Cây Láp)"
    gan_mau(obj_tay_cam, (0.55, 0.30, 0.12), line_color=(0.25, 0.12, 0.05), line_width=1.5)

    # -------------------------------------------------------------
    # 11. CỬA BUỒNG ĐỐT MẶT SAU: DÙNG LẠI TẤM SẮT ĐÃ CẮT DÀY 1.8CM, KHE CẮT 1MM
    #     - Tận dụng phôi sắt đã cắt từ lỗ 50x30cm của mặt sau
    #     - Khe cắt (kerf) 1mm đều 4 cạnh:
    #       + Chiều rộng cửa: 500 - 2 = 498mm (từ X = -249.0 đến +249.0mm)
    #       + Chiều cao cửa: 300 - 2 = 298mm (từ Z = -799.0 đến -501.0mm)
    #       + Độ dày tấm sắt: đúng 1.8cm = 18mm (từ Y = 500.0 đến 518.0mm)
    #     - Có tay khóa then gài L-handle bên phải (X = +210, Z = -650)
    # -------------------------------------------------------------
    shapes_cua = []
    # Cánh cửa sắt tấm 18mm
    plate_cua = Part.makeBox(498.0, 18.0, 298.0, App.Vector(-249.0, 500.0, -799.0))
    shapes_cua.append(plate_cua)

    # 2 Bản lề cối bên trái (nhìn trực diện từ phía sau: X = +249.5, Y = 518mm)
    for z_h in [-560.0, -740.0]:
        k_up = Part.makeCylinder(10.0, 24.0, App.Vector(249.5, 526.0, z_h + 1.0), App.Vector(0, 0, 1))
        tab_door = Part.makeBox(15.0, 8.0, 24.0, App.Vector(234.5, 518.0, z_h + 1.0))
        pin = Part.makeCylinder(6.0, 48.0, App.Vector(249.5, 526.0, z_h - 23.0), App.Vector(0, 0, 1))
        shapes_cua.extend([k_up, tab_door, pin])

    # Tay khóa then gài L-handle bên phải (nhìn trực diện từ phía sau: X = -210, Z = -650)
    h_boss = Part.makeCylinder(13.0, 16.0, App.Vector(-210.0, 518.0, -650.0), App.Vector(0, 1, 0))
    h_bar = Part.makeCylinder(7.0, 85.0, App.Vector(-210.0, 534.0, -650.0), App.Vector(0, 0, -1))
    h_knob = Part.makeSphere(10.0, App.Vector(-210.0, 534.0, -735.0))
    h_tongue = Part.makeBox(35.0, 8.0, 16.0, App.Vector(-250.0, 492.0, -658.0))
    shapes_cua.extend([h_boss, h_bar, h_knob, h_tongue])

    hinh_cua_sau = Part.makeCompound(shapes_cua)
    obj_cua_sau = doc.addObject("Part::Feature", "Cua_Buong_Dot_Mat_Sau_18mm")
    obj_cua_sau.Shape = hinh_cua_sau
    obj_cua_sau.Label = "11. Cửa Buồng Đốt Mặt Sau (Sắt Dày 1.8cm, Dài 49.8cm, Cao 29.8cm, Khe Cắt 1mm, Mở Về Bên Trái)"
    gan_mau(obj_cua_sau, (0.35, 0.42, 0.52), line_color=(0.15, 0.20, 0.30), line_width=1.8)

    # -------------------------------------------------------------
    # 12. 2 BẢN LỀ CỐI CỬA SAU: HÀN CỐ ĐỊNH VÀO MẶT MÁY SAU BÊN TRÁI
    #     - Vị trí: Mép bên trái lỗ cắt (nhìn từ phía sau: X = +249.5mm, Y = 518mm)
    #     - Cối dưới phi 20mm hàn cố định vào mặt máy sau, đệm long đền đồng
    #     - Cho phép cửa mở xoay về bên trái góc 0 - 120 độ
    # -------------------------------------------------------------
    shapes_ban_le_khung = []
    for z_h in [-560.0, -740.0]:
        k_low = Part.makeCylinder(10.0, 24.0, App.Vector(249.5, 526.0, z_h - 25.0), App.Vector(0, 0, 1))
        wash = Part.makeCylinder(11.0, 2.0, App.Vector(249.5, 526.0, z_h - 1.0), App.Vector(0, 0, 1))
        tab_frame = Part.makeBox(15.0, 8.0, 24.0, App.Vector(249.5, 518.0, z_h - 25.0))
        shapes_ban_le_khung.extend([k_low, wash, tab_frame])

    hinh_ban_le_sau = Part.makeCompound(shapes_ban_le_khung)
    obj_ban_le_sau = doc.addObject("Part::Feature", "2_Ban_Le_Coi_Cua_Sau")
    obj_ban_le_sau.Shape = hinh_ban_le_sau
    obj_ban_le_sau.Label = "12. 2 Bản Lề Cối Cửa Sau (Hàn Mặt Máy Bên Trái X=+250, Cối Phi 20mm)"
    gan_mau(obj_ban_le_sau, (0.42, 0.48, 0.58), line_color=(0.15, 0.20, 0.30), line_width=1.8)

    # -------------------------------------------------------------
    # -------------------------------------------------------------
    # 13. BUỒNG ĐỐT CỦI LÓT GẠCH SA MỐT NẰM GỌN DƯỚI TRỐNG (CHỪA NGANG 50CM, CAO ĐẾN TRỐNG, BAO 1 LỚP GẠCH):
    #     - Yêu cầu người dùng: "tôi muốn buồng đốt củi nằm gọn ở dưới trống, chỉ cần chừa ngang 50, cao đến trống là đủ đốt rồi, bên ngoài bao quanh 1 lớp gạch"
    #     - Kích thước từng viên gạch sa mốt tiêu chuẩn: Dài 300mm (30cm), Rộng 100mm (10cm), Dày 50mm (5cm).
    #     - Mạch vữa xây chịu nhiệt: khe hở 1.5mm sắc nét mô phỏng chân thực.
    #     - Kết cấu lò gạch cách nhiệt chuẩn xác:
    #       1. SÀN ĐÁY BUỒNG ĐỐT (Hearth Floor):
    #          + Đặt trực tiếp trên mặt chân máy (Z = -850mm đến -800mm, dày đúng 50mm = 1 viên gạch nằm).
    #          + Rộng đúng 700mm (7 hàng gạch x 100mm, từ X = -350mm đến +350mm, nằm gọn hoàn toàn dưới gầm máy).
    #          + Dài 1000mm (từ Y = -500mm đến +500mm), xếp so le mạch vữa.
    #          + Bảo vệ cách nhiệt 100% tấm thép chân máy 5mm khỏi than củi nhiệt độ 800 - 1000°C.
    #          + Mặt sàn gạch ở cao độ Z = -800mm, BẰNG PHẲNG KHÍT KHAO VỚI MÉP DƯỚI CỬA SAU (Z = -800mm).
    #       2. HAI VÁCH HÔNG BAO 1 LỚP GẠCH (DÀY 10CM), CHỪA LÒNG TRONG NGANG ĐÚNG 50CM:
    #          + Bề dày vách đúng 1 lớp gạch = 100mm (10cm):
    #            Vách trái: X = -350mm đến -250mm; Vách phải: X = +250mm đến +350mm.
    #          + Lòng trong thông thủy buồng đốt: Rộng đúng 500mm (50cm) khớp hoàn toàn với chiều dài cửa cắt sau 50cm.
    #          + Tổng bề ngang lò gạch chỉ 700mm (70cm), trong khi eo thắt nhỏ nhất của mặt máy là 735.4mm (X = ±367.7mm)
    #            -> Lò gạch nằm lọt thỏm hoàn toàn dưới trống và bên trong mặt máy, KHÔNG HỀ BỊ LÒI RA NGOÀI!
    #       3. CHIỀU CAO XÂY ĐẾN ĐÁY TRỐNG (9 HÀNG GẠCH = CAO 45CM TỪ SÀN, CAO 50CM TỪ BỆ CHÂN MÁY):
    #          + Đỉnh gạch xây lên đến cao độ Z = -350mm.
    #          + Bán kính cưa gọt R_cut = 425mm (cách vỏ áo ngoài trống R415mm đúng 1cm = 10mm).
    #          + Cưa gọt phần gạch vách hông và vách trước ôm khít đáy trống với khe hở giữ nhiệt chuẩn xác 1cm.
    #          + Gom toàn bộ nhiệt lượng và ngọn lửa vào đáy trống, cách nhiệt hoàn hảo, chống thất thoát.
    #       4. VÁCH CHẮN NHIỆT PHÍA TRƯỚC (Front Wall):
    #          + Xây ở đầu trước: Y = -500mm đến -400mm (dày 100mm), rộng 500mm (X = -250 đến +250mm).
    #          + Cao 8 lớp (đến Z = -400mm) và được cưa vát cong theo bán kính R=425mm, nằm gọn dưới miệng xả hạt.
    # -------------------------------------------------------------
    shapes_buong_dot = []
    gap_gach = 1.5

    # 1. Sàn đáy buồng đốt: Z = -850 đến -800mm (dày 50mm, 7 hàng x 100mm = rộng 700mm)
    z_floor = -850.0
    h_floor = 50.0 - gap_gach
    for col in range(7):
        x_min = -350.0 + col * 100.0 + gap_gach / 2.0
        w_brick = 100.0 - gap_gach
        if col % 2 == 0:
            segments = [(-500.0, 300.0), (-200.0, 300.0), (100.0, 300.0), (400.0, 100.0)]
        else:
            segments = [(-500.0, 100.0), (-400.0, 300.0), (-100.0, 300.0), (200.0, 300.0)]
        for y_start, l_seg in segments:
            y_min = y_start + gap_gach / 2.0
            l_brick = l_seg - gap_gach
            brick = Part.makeBox(w_brick, l_brick, h_floor, App.Vector(x_min, y_min, z_floor + gap_gach / 2.0))
            shapes_buong_dot.append(brick)

    # 2. Hai vách hông lò bao 1 lớp gạch dày 10cm, chừa ngang 50cm, cao 9 hàng đến Z = -350mm
    wall_cols = [(-350.0, -250.0), (250.0, 350.0)]
    for x_start, x_end in wall_cols:
        x_min = x_start + gap_gach / 2.0
        w_brick = (x_end - x_start) - gap_gach
        for course in range(9):
            z_c = -800.0 + course * 50.0 + gap_gach / 2.0
            h_c = 50.0 - gap_gach
            if course % 2 == 0:
                segments = [(-500.0, 300.0), (-200.0, 300.0), (100.0, 300.0), (400.0, 100.0)]
            else:
                segments = [(-500.0, 100.0), (-400.0, 300.0), (-100.0, 300.0), (200.0, 300.0)]
            for y_start, l_seg in segments:
                y_min = y_start + gap_gach / 2.0
                l_brick = l_seg - gap_gach
                brick = Part.makeBox(w_brick, l_brick, h_c, App.Vector(x_min, y_min, z_c))
                shapes_buong_dot.append(brick)

    # 3. Vách chắn nhiệt phía trước: Y = -500 đến -400mm (dày 100mm, cao 8 lớp)
    y_front = -500.0 + gap_gach / 2.0
    l_front = 100.0 - gap_gach
    for course in range(8):
        z_c = -800.0 + course * 50.0 + gap_gach / 2.0
        h_c = 50.0 - gap_gach
        if course % 2 == 0:
            x_segs = [(-250.0, 300.0), (50.0, 200.0)]
        else:
            x_segs = [(-250.0, 200.0), (-50.0, 300.0)]
        for xs, ws in x_segs:
            x_min = xs + gap_gach / 2.0
            w_brick = ws - gap_gach
            brick = Part.makeBox(w_brick, l_front, h_c, App.Vector(x_min, y_front, z_c))
            shapes_buong_dot.append(brick)

    # 4. CƯA GỌT GẠCH TẠO HÌNH CÁCH TRỐNG 1CM (BÁN KÍNH CƯA R = 425mm)
    raw_buong_dot = Part.makeCompound(shapes_buong_dot)
    r_cut = 425.0  # R_ao(415mm) + 10mm khoảng hở cách nhiệt = 425mm
    saw_cutter = Part.makeCylinder(r_cut, 1040.0, App.Vector(0, -520.0, 0), App.Vector(0, 1, 0))
    hinh_buong_dot = raw_buong_dot.cut(saw_cutter)

    obj_buong_dot_gach = doc.addObject("Part::Feature", "Buong_Dot_Cui_Gach_Sa_Mot_30x5x10")
    obj_buong_dot_gach.Shape = hinh_buong_dot
    obj_buong_dot_gach.Label = "13. Buồng Đốt Củi Lót Gạch Chịu Lửa (KT 30x5x10cm, Lòng Rộng 50cm, Bao 1 Lớp Gạch 10cm, Cao Đến Trống, Cưa Gọt Cách 1cm Nằm Gọn Dưới Trống)"
    gan_mau(obj_buong_dot_gach, (0.84, 0.48, 0.26), line_color=(0.35, 0.18, 0.08), line_width=1.5)

    return obj_trong, obj_ao_ngoai, obj_lap, obj_chong, obj_canh_ngoai, obj_canh_trong, obj_mat_truoc, obj_mat_sau, obj_chan_de, obj_cay_tham, obj_tay_cam, obj_cua_sau, obj_ban_le_sau, obj_buong_dot_gach


class BangDieuKhienHanCayTru(QtWidgets.QDialog):
    """Giao diện điều khiển mô phỏng: Trống Rang 2 Lớp Cách Khí 1cm & Hệ Thống Cánh Đảo."""

    def __init__(self, doc, obj_trong, obj_ao_ngoai, obj_lap, obj_chong, obj_canh_ngoai, obj_canh_trong, obj_mat_truoc=None, obj_mat_sau=None, obj_chan_de=None, obj_cay_tham=None, obj_tay_cam=None, obj_cua_sau=None, obj_ban_le_sau=None, obj_buong_dot_gach=None, parent=None):
        super(BangDieuKhienHanCayTru, self).__init__(parent)
        self.doc = doc
        self.obj_trong = obj_trong
        self.obj_ao_ngoai = obj_ao_ngoai
        self.obj_lap = obj_lap
        self.obj_chong = obj_chong
        self.obj_canh_ngoai = obj_canh_ngoai
        self.obj_canh_trong = obj_canh_trong
        self.obj_mat_truoc = obj_mat_truoc
        self.obj_mat_sau = obj_mat_sau
        self.obj_chan_de = obj_chan_de
        self.obj_cay_tham = obj_cay_tham
        self.obj_tay_cam = obj_tay_cam
        self.obj_cua_sau = obj_cua_sau
        self.obj_ban_le_sau = obj_ban_le_sau
        self.obj_buong_dot_gach = obj_buong_dot_gach

        self.current_angle = 0.0
        self.rpm = 40.0
        self.direction = 1
        self.is_running = True
        self.is_transparent = True
        self.is_drum_visible = True
        self.is_mat_visible = True
        self.is_horizontal = True
        self.is_door_open = False
        self.is_gach_visible = True

        self.init_ui()
        self.init_timer()

    def init_ui(self):
        self.setWindowTitle("Điều Khiển: Trống Rang 2 Lớp & Bệ Chân Máy Hoàn Chỉnh")
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumWidth(540)
        self.setStyleSheet("""
            QDialog { background-color: #f8fafc; font-family: 'Segoe UI', Arial, sans-serif; }
            QGroupBox { font-weight: bold; border: 1px solid #cbd5e1; border-radius: 6px; margin-top: 10px; padding-top: 14px; background-color: #ffffff; color: #1e293b; }
            QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 5px; color: #0f172a; }
            QPushButton { border-radius: 5px; font-weight: bold; padding: 6px 10px; font-size: 11px; }
        """)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 10, 12, 10)

        # 1. Thanh tiêu đề & Nút tài liệu MD
        header = QtWidgets.QFrame()
        header.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1e293b, stop:1 #334155); border-radius: 6px; padding: 6px;")
        h_layout = QtWidgets.QHBoxLayout(header)
        h_layout.setContentsMargins(10, 4, 10, 4)
        title = QtWidgets.QLabel("🎮 BẢNG ĐIỀU KHIỂN: MÁY RANG CỦI 2 LỚP")
        title.setStyleSheet("color: #38bdf8; font-weight: bold; font-size: 13px;")
        btn_md = QtWidgets.QPushButton("📖 Thông Số (MD)")
        btn_md.setStyleSheet("background-color: #0284c7; color: white; padding: 4px 10px; font-size: 10.5px; border-radius: 4px;")
        btn_md.clicked.connect(self.mo_thong_so_md)
        h_layout.addWidget(title)
        h_layout.addStretch()
        h_layout.addWidget(btn_md)
        layout.addWidget(header)

        # 2. Thanh trạng thái trực quan
        status_frame = QtWidgets.QFrame()
        status_frame.setStyleSheet("background-color: #f1f5f9; border: 1px solid #e2e8f0; border-radius: 6px; padding: 4px;")
        s_layout = QtWidgets.QHBoxLayout(status_frame)
        s_layout.setContentsMargins(10, 2, 10, 2)
        self.lbl_status = QtWidgets.QLabel("Trạng thái: 🟢 Đang quay mượt mà (40 RPM)")
        self.lbl_status.setStyleSheet("font-weight: bold; color: #0284c7; font-size: 11.5px;")
        self.lbl_angle = QtWidgets.QLabel("Góc: 0.0° | Thuận | Cửa: Đóng")
        self.lbl_angle.setStyleSheet("font-weight: bold; color: #16a34a; font-size: 11.5px;")
        s_layout.addWidget(self.lbl_status)
        s_layout.addStretch()
        s_layout.addWidget(self.lbl_angle)
        layout.addWidget(status_frame)

        # 3. Nhóm 1: Vận hành động cơ & tốc độ
        grp_motor = QtWidgets.QGroupBox("⚡ Vận Hành Động Cơ & Tốc Độ")
        l_motor = QtWidgets.QVBoxLayout(grp_motor)
        l_motor.setSpacing(6)

        r_slider = QtWidgets.QHBoxLayout()
        lbl_rpm = QtWidgets.QLabel("Tốc độ:")
        lbl_rpm.setStyleSheet("font-weight: bold; color: #475569;")
        self.slider_rpm = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_rpm.setRange(5, 120)
        self.slider_rpm.setValue(int(self.rpm))
        self.slider_rpm.valueChanged.connect(self.thay_doi_toc_do)
        self.lbl_rpm_val = QtWidgets.QLabel(f"{int(self.rpm)} RPM")
        self.lbl_rpm_val.setStyleSheet("font-weight: bold; color: #0f172a; min-width: 50px;")

        btn_20 = QtWidgets.QPushButton("20 RPM (Chậm)")
        btn_20.setStyleSheet("background-color: #e2e8f0; color: #334155; font-size: 10px; padding: 4px 6px;")
        btn_20.clicked.connect(lambda: self.slider_rpm.setValue(20))
        btn_40 = QtWidgets.QPushButton("40 RPM (Chuẩn)")
        btn_40.setStyleSheet("background-color: #e2e8f0; color: #334155; font-size: 10px; padding: 4px 6px;")
        btn_40.clicked.connect(lambda: self.slider_rpm.setValue(40))
        btn_60 = QtWidgets.QPushButton("60 RPM (Nhanh)")
        btn_60.setStyleSheet("background-color: #e2e8f0; color: #334155; font-size: 10px; padding: 4px 6px;")
        btn_60.clicked.connect(lambda: self.slider_rpm.setValue(60))

        r_slider.addWidget(lbl_rpm)
        r_slider.addWidget(self.slider_rpm)
        r_slider.addWidget(self.lbl_rpm_val)
        r_slider.addWidget(btn_20)
        r_slider.addWidget(btn_40)
        r_slider.addWidget(btn_60)
        l_motor.addLayout(r_slider)

        r_btn_motor = QtWidgets.QHBoxLayout()
        self.btn_play = QtWidgets.QPushButton("⏸ Tạm Dừng")
        self.btn_play.setStyleSheet("background-color: #f59e0b; color: white;")
        self.btn_play.clicked.connect(self.toggle_play)
        self.btn_reverse = QtWidgets.QPushButton("🔁 Đảo Chiều Xoay")
        self.btn_reverse.setStyleSheet("background-color: #2563eb; color: white;")
        self.btn_reverse.clicked.connect(self.dao_chieu)
        r_btn_motor.addWidget(self.btn_play)
        r_btn_motor.addWidget(self.btn_reverse)
        l_motor.addLayout(r_btn_motor)
        layout.addWidget(grp_motor)

        # 4. Nhóm 2: Chế độ quan sát & ẩn hiện
        grp_vis = QtWidgets.QGroupBox("👁 Chế Độ Quan Sát & Ẩn Hiện Chi Tiết")
        g_vis = QtWidgets.QGridLayout(grp_vis)
        g_vis.setSpacing(6)
        self.btn_transparency = QtWidgets.QPushButton("👁 Xuyên Thấu Vỏ Trống")
        self.btn_transparency.setStyleSheet("background-color: #0d9488; color: white;")
        self.btn_transparency.clicked.connect(self.toggle_transparency)

        self.btn_hide_drum = QtWidgets.QPushButton("📦 Ẩn/Hiện Vỏ Trống")
        self.btn_hide_drum.setStyleSheet("background-color: #6366f1; color: white;")
        self.btn_hide_drum.clicked.connect(self.toggle_drum_visibility)

        self.btn_hide_mat = QtWidgets.QPushButton("🛡 Ẩn/Hiện Khung Bệ Máy")
        self.btn_hide_mat.setStyleSheet("background-color: #475569; color: white;")
        self.btn_hide_mat.clicked.connect(self.toggle_mat_visibility)

        self.btn_gach = QtWidgets.QPushButton("🧱 Ẩn/Hiện Lò Gạch Sa Mốt")
        self.btn_gach.setStyleSheet("background-color: #ea580c; color: white;")
        self.btn_gach.clicked.connect(self.toggle_gach_visibility)

        g_vis.addWidget(self.btn_transparency, 0, 0)
        g_vis.addWidget(self.btn_hide_drum, 0, 1)
        g_vis.addWidget(self.btn_hide_mat, 1, 0)
        g_vis.addWidget(self.btn_gach, 1, 1)
        layout.addWidget(grp_vis)

        # 5. Nhóm 3: Cơ cấu mở cửa 120 độ & Góc nhìn camera thông minh
        grp_mech = QtWidgets.QGroupBox("🚪 Cơ Cấu Mở Cửa & Góc Nhìn Nhanh (1-Click View)")
        l_mech = QtWidgets.QVBoxLayout(grp_mech)
        l_mech.setSpacing(6)

        r_door = QtWidgets.QHBoxLayout()
        self.btn_cua_sau = QtWidgets.QPushButton("🚪 Mở Cửa Sau (120°)")
        self.btn_cua_sau.setStyleSheet("background-color: #7c3aed; color: white;")
        self.btn_cua_sau.clicked.connect(self.toggle_cua_sau)

        self.btn_orientation = QtWidgets.QPushButton("🔄 Đổi Tư Thế Đứng / Ngang")
        self.btn_orientation.setStyleSheet("background-color: #0891b2; color: white;")
        self.btn_orientation.clicked.connect(self.toggle_orientation)

        r_door.addWidget(self.btn_cua_sau)
        r_door.addWidget(self.btn_orientation)
        l_mech.addLayout(r_door)

        r_cams = QtWidgets.QHBoxLayout()
        self.btn_iso = QtWidgets.QPushButton("📐 Isometric")
        self.btn_iso.setStyleSheet("background-color: #64748b; color: white;")
        self.btn_iso.clicked.connect(self.view_isometric)

        self.btn_rear = QtWidgets.QPushButton("🔙 Mặt Sau (Lò Gạch)")
        self.btn_rear.setStyleSheet("background-color: #334155; color: white;")
        self.btn_rear.clicked.connect(self.view_rear)

        self.btn_front = QtWidgets.QPushButton("🔜 Mặt Trước (Miệng Xả)")
        self.btn_front.setStyleSheet("background-color: #334155; color: white;")
        self.btn_front.clicked.connect(self.view_front)

        r_cams.addWidget(self.btn_iso)
        r_cams.addWidget(self.btn_rear)
        r_cams.addWidget(self.btn_front)
        l_mech.addLayout(r_cams)
        layout.addWidget(grp_mech)

        self.adjustSize()

    def init_timer(self):
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(30)  # ~33 FPS
        self.timer.timeout.connect(self.cap_nhat_quay)
        self.timer.start()

    def cap_nhat_quay(self):
        if not self.is_running:
            return

        deg_per_tick = (self.rpm * 360.0 / 60.0) * (30.0 / 1000.0)
        self.current_angle = (self.current_angle + self.direction * deg_per_tick) % 360.0

        if self.is_horizontal:
            rot = App.Rotation(App.Vector(0, 1, 0), self.current_angle)
        else:
            rot_spin = App.Rotation(App.Vector(0, 1, 0), self.current_angle)
            rot_tilt = App.Rotation(App.Vector(0, 0, 1), 90.0)
            rot = rot_tilt.multiply(rot_spin)

        placement = App.Placement(App.Vector(0, 0, 0), rot)

        # Quay đồng bộ cả 6 đối tượng: Vỏ Trong, Áo Ngoài, Cây Láp, Cây Chống, Cánh Ngoài, Cánh Trong
        for obj in [self.obj_trong, self.obj_ao_ngoai, self.obj_lap, self.obj_chong, self.obj_canh_ngoai, self.obj_canh_trong]:
            if obj:
                try:
                    obj.Placement = placement
                except Exception:
                    pass

        chieu = "Thuận" if self.direction == 1 else "Nghịch"
        cua = "Mở 120°" if self.is_door_open else "Đóng"
        self.lbl_angle.setText(f"Góc: {self.current_angle:.1f}° | {chieu} | Cửa: {cua}")

    def thay_doi_toc_do(self, val):
        self.rpm = float(val)
        self.lbl_rpm_val.setText(f"{int(self.rpm)} RPM")
        if self.is_running:
            self.lbl_status.setText(f"Trạng thái: 🟢 Đang quay mượt mà ({int(self.rpm)} RPM)")

    def toggle_play(self):
        self.is_running = not self.is_running
        if self.is_running:
            self.btn_play.setText("⏸ Tạm Dừng")
            self.btn_play.setStyleSheet("background-color: #f59e0b; color: white;")
            self.lbl_status.setText(f"Trạng thái: 🟢 Đang quay mượt mà ({int(self.rpm)} RPM)")
            self.lbl_status.setStyleSheet("font-weight: bold; color: #0284c7; font-size: 11.5px;")
        else:
            self.btn_play.setText("▶ Tiếp Tục Quay")
            self.btn_play.setStyleSheet("background-color: #16a34a; color: white;")
            self.lbl_status.setText("Trạng thái: 🔴 Đã tạm dừng")
            self.lbl_status.setStyleSheet("font-weight: bold; color: #dc2626; font-size: 11.5px;")

    def dao_chieu(self):
        self.direction *= -1
        chieu = "Thuận" if self.direction == 1 else "Nghịch"
        cua = "Mở 120°" if self.is_door_open else "Đóng"
        self.lbl_angle.setText(f"Góc: {self.current_angle:.1f}° | {chieu} | Cửa: {cua}")

    def toggle_transparency(self):
        self.is_transparent = not self.is_transparent
        if kiem_tra_co_gui():
            for obj, val in [(self.obj_trong, 45), (self.obj_ao_ngoai, 55)]:
                if obj and hasattr(obj, "ViewObject") and obj.ViewObject:
                    obj.ViewObject.Transparency = val if self.is_transparent else 0

    def toggle_drum_visibility(self):
        self.is_drum_visible = not self.is_drum_visible
        if kiem_tra_co_gui():
            for obj in [self.obj_trong, self.obj_ao_ngoai]:
                if hasattr(obj, "ViewObject") and obj.ViewObject:
                    obj.ViewObject.Visibility = self.is_drum_visible

    def toggle_mat_visibility(self):
        self.is_mat_visible = not self.is_mat_visible
        if kiem_tra_co_gui():
            for obj in [self.obj_mat_truoc, self.obj_mat_sau, self.obj_chan_de, self.obj_cay_tham, self.obj_tay_cam, self.obj_cua_sau, self.obj_ban_le_sau, self.obj_buong_dot_gach]:
                if obj and hasattr(obj, "ViewObject") and obj.ViewObject:
                    obj.ViewObject.Visibility = self.is_mat_visible

    def toggle_gach_visibility(self):
        self.is_gach_visible = not self.is_gach_visible
        if kiem_tra_co_gui() and self.obj_buong_dot_gach and hasattr(self.obj_buong_dot_gach, "ViewObject") and self.obj_buong_dot_gach.ViewObject:
            self.obj_buong_dot_gach.ViewObject.Visibility = self.is_gach_visible

    def toggle_cua_sau(self):
        if self.obj_cua_sau is None:
            return
        self.is_door_open = not self.is_door_open
        p_hinge = App.Vector(249.5, 526.0, 0.0)
        angle = -120.0 if self.is_door_open else 0.0
        if self.is_door_open:
            self.btn_cua_sau.setText("🚪 Đóng Cửa Sau")
            self.btn_cua_sau.setStyleSheet("background-color: #dc2626; color: white;")
        else:
            self.btn_cua_sau.setText("🚪 Mở Cửa Sau (120°)")
            self.btn_cua_sau.setStyleSheet("background-color: #7c3aed; color: white;")

        rot = App.Rotation(App.Vector(0, 0, 1), angle)
        plc = App.Placement(p_hinge, rot).multiply(App.Placement(-p_hinge, App.Rotation()))
        if not self.is_horizontal:
            rot_tilt = App.Rotation(App.Vector(0, 0, 1), 90.0)
            self.obj_cua_sau.Placement = rot_tilt.multiply(plc)
        else:
            self.obj_cua_sau.Placement = plc
        if self.doc:
            self.doc.recompute()

        chieu = "Thuận" if self.direction == 1 else "Nghịch"
        cua = "Mở 120°" if self.is_door_open else "Đóng"
        self.lbl_angle.setText(f"Góc: {self.current_angle:.1f}° | {chieu} | Cửa: {cua}")

    def toggle_orientation(self):
        self.is_horizontal = not self.is_horizontal
        for obj in [self.obj_mat_truoc, self.obj_mat_sau, self.obj_chan_de, self.obj_cay_tham, self.obj_tay_cam, self.obj_ban_le_sau, self.obj_buong_dot_gach]:
            if obj:
                if self.is_horizontal:
                    obj.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0, 1, 0), 0))
                else:
                    rot_tilt = App.Rotation(App.Vector(0, 0, 1), 90.0)
                    obj.Placement = App.Placement(App.Vector(0, 0, 0), rot_tilt)
        if self.obj_cua_sau:
            p_hinge = App.Vector(249.5, 526.0, 0.0)
            angle = -120.0 if self.is_door_open else 0.0
            rot = App.Rotation(App.Vector(0, 0, 1), angle)
            plc = App.Placement(p_hinge, rot).multiply(App.Placement(-p_hinge, App.Rotation()))
            if not self.is_horizontal:
                rot_tilt = App.Rotation(App.Vector(0, 0, 1), 90.0)
                self.obj_cua_sau.Placement = rot_tilt.multiply(plc)
            else:
                self.obj_cua_sau.Placement = plc

        self.cap_nhat_quay()
        self.view_isometric()

    def view_isometric(self):
        if kiem_tra_co_gui():
            try:
                view = Gui.ActiveDocument.ActiveView
                view.viewAxometric()
                view.fitAll()
            except Exception:
                try:
                    Gui.SendMsgToActiveView("ViewAxo")
                    Gui.SendMsgToActiveView("ViewFit")
                except Exception:
                    pass

    def view_rear(self):
        if kiem_tra_co_gui():
            try:
                view = Gui.ActiveDocument.ActiveView
                view.viewRear()
                view.fitAll()
            except Exception:
                try:
                    Gui.SendMsgToActiveView("ViewRear")
                    Gui.SendMsgToActiveView("ViewFit")
                except Exception:
                    pass

    def view_front(self):
        if kiem_tra_co_gui():
            try:
                view = Gui.ActiveDocument.ActiveView
                view.viewFront()
                view.fitAll()
            except Exception:
                try:
                    Gui.SendMsgToActiveView("ViewFront")
                    Gui.SendMsgToActiveView("ViewFit")
                except Exception:
                    pass

    def mo_thong_so_md(self):
        md_path = r"c:\VAN\CAD\THONG_SO_KY_THUAT.md"
        try:
            os.startfile(md_path)
        except Exception:
            try:
                os.system(f'notepad.exe "{md_path}"')
            except Exception:
                pass

    def closeEvent(self, event):
        if hasattr(self, "timer") and self.timer.isActive():
            self.timer.stop()
        event.accept()

    def reject(self):
        if hasattr(self, "timer") and self.timer.isActive():
            self.timer.stop()
        super(BangDieuKhienHanCayTru, self).reject()


def chay_mo_phong():
    global _TRONG_DIEU_KHIEN_WINDOW

    # 1. Đóng sạch sẽ tất cả tài liệu cũ đang mở
    dong_sach_tat_ca_tai_lieu_cu()
    _TRONG_DIEU_KHIEN_WINDOW = None

    # 2. Tạo mới tài liệu trắng tinh
    doc = App.newDocument("Trong_Lap_10Chong_CanhDao_Han_Vao_Cay_Tru")

    # 3. Tạo hình Trống 2 Lớp Cách Khí, Cây Láp, 10 Cây Chống, Cánh Đảo, 2 Mặt Máy, Chân Đế 0.5cm, Cây Thăm Hàng, Cửa Buồng Đốt & Buồng Đốt Gạch Sa Mốt
    obj_trong, obj_ao_ngoai, obj_lap, obj_chong, obj_canh_ngoai, obj_canh_trong, obj_mat_truoc, obj_mat_sau, obj_chan_de, obj_cay_tham, obj_tay_cam, obj_cua_sau, obj_ban_le_sau, obj_buong_dot_gach = tao_mo_hinh_chi_tiet(doc)
    doc.recompute()

    # 4. Căn góc nhìn Isometric & hiển thị bảng điều khiển
    if kiem_tra_co_gui():
        try:
            Gui.SendMsgToActiveView("ViewAxo")
            Gui.SendMsgToActiveView("ViewFit")
        except Exception:
            pass

        main_win = None
        try:
            main_win = Gui.getMainWindow()
        except Exception:
            pass

        _TRONG_DIEU_KHIEN_WINDOW = BangDieuKhienHanCayTru(
            doc, obj_trong, obj_ao_ngoai, obj_lap, obj_chong, obj_canh_ngoai, obj_canh_trong, obj_mat_truoc, obj_mat_sau, obj_chan_de, obj_cay_tham, obj_tay_cam, obj_cua_sau, obj_ban_le_sau, obj_buong_dot_gach, parent=main_win
        )
        _TRONG_DIEU_KHIEN_WINDOW.show()

        App.Console.PrintMessage("\n" + "=" * 80 + "\n")
        App.Console.PrintMessage(">> ĐÃ CẬP NHẬT: TRỐNG RANG 2 LỚP, 2 MẶT MÁY, CHÂN ĐẾ 0.5CM, MIỆNG RA HÀNG, CÂY THĂM HÀNG, CỬA BUỒNG ĐỐT & BUỒNG ĐỐT GẠCH SA MỐT NẰM GỌN DƯỚI TRỐNG!\n")
        App.Console.PrintMessage(">> Vỏ trong: Dài 1m, Phi 80cm, Dày 0.8cm (8mm)\n")
        App.Console.PrintMessage(">> Vỏ ngoài: Dài 1m, Phi 83cm, Dày 0.5cm (5mm), hở 1cm đệm khí cách nhiệt\n")
        App.Console.PrintMessage(">> 2 Mặt máy trước & sau: Sắt tấm dày 1.8cm (18mm), tròn trên D96cm (R480mm) thắt cong vào, dưới hình thang cân đáy phẳng 1.1m, lỗ cốt phi 65mm.\n")
        App.Console.PrintMessage(">> Mặt máy sau: Lỗ chữ nhật 50x30cm (dài 50cm, cao 30cm) cách chân máy 5cm. Dùng lại phôi sắt 18mm làm cửa, khe cắt 1mm, 2 bản lề cối mở về bên trái!\n")
        App.Console.PrintMessage(">> Buồng đốt củi gạch sa mốt nằm gọn dưới trống (KT 30x5x10cm): Chừa ngang 50cm, bao 1 lớp gạch dày 10cm (rộng lò 70cm không lòi ra ngoài), sàn dày 5cm, xây 9 hàng cao đến đáy trống (Z=-350mm), cưa gọt lòng máng R=425mm ôm trống cách chuẩn 1cm giữ nhiệt tuyệt đối, vách trước dày 10cm!\n")
        App.Console.PrintMessage(">> Miệng ra hàng mặt trước: 2 bên thành cao 10cm, dài 50cm, đỉnh thẳng, đáy cong ôm lòng trống R392mm, hạt trút sạch 100%!\n")
        App.Console.PrintMessage(">> Lỗ & Cây thăm hàng: Lỗ phi 30mm nằm ngang cây láp bên trái (X=-200, Z=0), cây thăm inox để xéo xiên vào tâm 16.7°, không cấn cánh đảo!\n")
        App.Console.PrintMessage(">> Chân đế máy hình chữ nhật: Sắt dày 0.5cm (5mm), kích thước 111cm x 104.6cm, dư mỗi bên trước sau 0.5cm, trái phải 0.5cm\n")
        App.Console.PrintMessage(">> 5 Cánh đảo trong: Bản rộng 10cm, dày 0.8cm, dài 65cm, ở giữa thân cây chống\n")
        App.Console.PrintMessage(">> 5 Cánh đảo ngoài: Bản rộng 7cm, dày 0.5cm, vừa chạm cả 10 cây chống để hàn\n")
        App.Console.PrintMessage("=" * 80 + "\n")
    else:
        print(">> [CLI Mode] Đã tạo thành công: Trống Rang 2 Lớp, 2 Mặt Máy, Chân Đế 0.5cm, Miệng Ra Hàng, Cây Thăm Hàng, Cửa Sau 50x30cm & Buồng Đốt Gạch Sa Mốt Nằm Gọn Dưới Trống (Ngang 50cm, Bao 1 Lớp Gạch, Cách Trống 1cm)!")
        print(">> Vỏ trong: D80cm x Dày 0.8cm | Vỏ ngoài: D83cm x Dày 0.5cm | Hở 1cm đệm khí")
        print(">> 2 Mặt máy trước & sau: Sắt tấm dày 1.8cm, tròn trên D96cm (R480mm) thắt cong vào, dưới hình thang cân đáy phẳng 1.1m, lỗ cốt D65mm")
        print(">> Mặt máy sau: Lỗ chữ nhật dài 50cm, cao 30cm, cách chân máy 5cm, cửa 18mm khe 1mm mở về bên trái")
        print(">> Buồng đốt củi gạch chịu lửa: Lòng rộng 50cm, bao 1 lớp gạch dày 10cm (rộng phủ bì 70cm lọt thỏm dưới eo máy), sàn 5cm, xây cao 9 hàng đến đáy trống Z=-350mm, cưa gọt R425mm ôm cách trống 1cm giữ nhiệt tuyệt đối, vách trước 10cm")
        print(">> Miệng ra hàng mặt trước: 2 bên thành cao 10cm, dài 50cm, đỉnh thẳng ngang, đáy cong ôm vách trong trống R392mm")
        print(">> Lỗ & Cây thăm hàng: Lỗ phi 30mm nằm ngang cây láp bên trái (X=-200, Z=0), cây thăm inox xiên 16.7°, không cấn cánh đảo!")
        print(">> Chân đế máy chữ nhật: Sắt dày 0.5cm, KT 111cm x 104.6cm (dư trước sau trái phải 0.5cm)")
        print(">> 5 Cánh trong: Bản 10cm x Dày 0.8cm x Dài 65cm, ở giữa cây chống, không chạm láp")
        print(">> 5 Cánh ngoài: Bản 7cm x Dày 0.5cm, vừa chạm cả 10 cây chống để thợ hàn liên kết!")



if __name__ == "__main__" or __name__ == "FreeCAD":
    chay_mo_phong()
