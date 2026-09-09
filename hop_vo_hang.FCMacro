# -*- coding: utf-8 -*-
"""
========================================================================================
 Tên file : hop_vo_hang.py / hop_vo_hang.FCMacro
 Mô tả    : Macro FreeCAD thiết kế HỘP VÔ HÀNG (Phễu nạp hạt cà phê / nông sản):
            - Vật liệu: Tấm to Inox 304 dày 3mm (3 ly) cắt CNC/Laser.
            - Biên dạng hông: Ghép từ 1 hình chữ nhật (250 x 400mm) + 1 hình tam giác (200 x 400mm)
              tạo thành hình thang vuông chuẩn xác:
              + Chiều cao đứng: 400mm (40cm)
              + Đáy lớn ở trên: 450mm (45cm = 250 + 200)
              + Đáy nhỏ ở dưới: 250mm (25cm)
              + Cạnh nghiêng dốc: 447.2mm (góc dốc 63.4° trôi hạt cực mượt)
            - Nhân đôi 2 tấm hông cách nhau đúng 30cm (300mm lọt lòng).
            - Bọc toàn bộ các mặt xung quanh bằng tôn Inox 3mm:
              1. Tấm hông trái (Hình thang vuông 3mm)
              2. Tấm hông phải (Hình thang vuông 3mm)
              3. Tấm vách sau thẳng đứng (300 x 400 x 3mm)
              4. Tấm vách nghiêng dốc trước (300 x 447.2 x 3mm)
              5. Tấm đáy dưới (300 x 250 x 3mm)
              6. Tấm nắp trên (300 x 450 x 3mm - có thể ẩn/hiện hoặc mở nắp nạp hạt)
            - Tách từng chi tiết độc lập để dễ dàng chỉnh sửa, khoét lỗ, làm van gạt ở các bước tiếp theo.
 Tác giả  : Kỹ Sư Thiết Kế Cơ Khí & CAD Tự Động Hóa
 Phiên bản: 1.0 - Infeed Box 3mm Stainless Steel (Rectangle + Triangle Right Trapezoid)
========================================================================================
"""

import sys
import math
import os
import FreeCAD as App
import Part

# Cấu hình UTF-8 an toàn cho console Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Nhập thư viện Qt hỗ trợ PySide6 / PySide2 / PySide
try:
    from PySide6 import QtCore, QtWidgets, QtGui
except ImportError:
    try:
        from PySide2 import QtCore, QtWidgets, QtGui
    except ImportError:
        try:
            from PySide import QtCore, QtWidgets, QtGui
        except ImportError:
            QtWidgets = None
            QtCore = None
            QtGui = None

try:
    import FreeCADGui as Gui
except ImportError:
    Gui = None

# Biến toàn cục giữ tham chiếu cửa sổ điều khiển
_HOP_VO_HANG_WINDOW = None


# ======================================================================================
# THÔNG SỐ KỸ THUẬT THAM SỐ (PARAMETRIC DIMENSIONS)
# Dễ dàng tinh chỉnh kích thước theo yêu cầu tiếp theo của bạn
# ======================================================================================
DO_DAY_INOX = 3.0          # Độ dày tấm inox: 3mm (3 ly)
KHOANG_CACH_2_TAM = 300.0  # Khoảng cách lọt lòng giữa 2 tấm hông: 300mm (30cm)
CHIEU_DAI_DAY = 300.0      # Chiều dài đáy dưới: 300mm (30cm) - Mặt vuông 30x30cm khoét lỗ Ø200mm
CHIEU_CAO_TONG_TRUOC = 650.0  # Chiều cao tổng thể hông trước: 650mm (65cm) - Giữ nguyên vẹn 65cm!
CHIEU_CAO_VACH_TRUOC = 450.0  # Chiều cao tấm inox ốp vách trước: 450mm (45cm) - Cắt tấm 30x45cm
KHOANG_TRONG_NAP_CAO = CHIEU_CAO_TONG_TRUOC - CHIEU_CAO_VACH_TRUOC  # 200mm (20cm) - Chừa khoảng trống 20x30cm ở trên
CHIEU_CAO_SAU = 300.0      # Chiều cao vách đứng sau: 300mm (30cm) - Vuông 30x30cm nguyên tấm (Quay ngược lại)
CHIEU_CAO_TAM_GIAC = CHIEU_CAO_TONG_TRUOC - CHIEU_CAO_SAU  # 350mm (35cm)

# Tính toán các đại lượng phụ thuộc
CANH_NGHIENG_TRUOC = math.sqrt(CHIEU_DAI_DAY**2 + CHIEU_CAO_TAM_GIAC**2)  # ~460.98mm
GOC_DOC_DO = math.degrees(math.atan2(CHIEU_CAO_TAM_GIAC, CHIEU_DAI_DAY)) # ~49.40 độ
THE_TICH_LIT = ((CHIEU_CAO_TONG_TRUOC + CHIEU_CAO_SAU) * CHIEU_DAI_DAY / 2.0 * KHOANG_CACH_2_TAM) / 1e6  # ~42.8 Lít


def kiem_tra_co_gui():
    """Kiểm tra môi trường FreeCAD có giao diện đồ họa GUI hay không."""
    if Gui is None:
        return False
    try:
        if callable(getattr(Gui, "getMainWindow", None)):
            return Gui.getMainWindow() is not None
    except Exception:
        return False
    return False


def dong_tai_lieu_cu(doc_name="Hop_Vo_Hang_Inox_3mm"):
    """Đóng sạch tài liệu cũ nếu đang mở để tạo mới tinh tươm."""
    global _HOP_VO_HANG_WINDOW
    if _HOP_VO_HANG_WINDOW is not None:
        try:
            _HOP_VO_HANG_WINDOW.close()
        except Exception:
            pass
        _HOP_VO_HANG_WINDOW = None

    if doc_name in App.listDocuments():
        try:
            App.closeDocument(doc_name)
        except Exception:
            pass


def gan_mau_inox(obj, line_color=(0.15, 0.20, 0.25), line_width=1.8, do_trong_suot=0):
    """Gán màu sắc Inox 304 sáng bóng kim loại sắc nét."""
    if kiem_tra_co_gui() and hasattr(obj, "ViewObject") and obj.ViewObject:
        vo = obj.ViewObject
        vo.ShapeColor = (0.83, 0.86, 0.90)  # Ánh bạc Inox 304
        vo.LineColor = line_color
        vo.Transparency = do_trong_suot
        if hasattr(vo, "LineWidth"):
            vo.LineWidth = line_width


def tao_hop_vo_hang(doc, plc=None, prefix=""):
    """
    Tạo mô hình Hộp Vô Hàng DỰNG ĐỨNG từ các tấm Inox 3mm (QUAY NGƯỢC LẠI & CHỪA KHOẢNG TRỐNG 20x30CM Ở TRÊN):
    - Vật liệu: Tấm to Inox 304 dày 3mm (3 ly)
    - Chiều cao hộp: GIỮ NGUYÊN VẸN 65cm (650mm) ở vách trước, 30cm (300mm) ở vách sau.
    - Biên dạng hông (2 tấm): Hình thang vuông dựng đứng:
      + Đáy dưới: 300mm (30cm)
      + Vách trước đứng: 650mm (65cm)
      + Vách sau đứng: 300mm (30cm) - Mặt vuông 30x30cm nguyên tấm
      + Cạnh dốc trên: 461.0mm (dốc 49.4° nối từ đỉnh trước 65cm xuống đỉnh sau 30cm)
      + Khoan lỗ Ø20mm tại góc tù sau (X=10.5, Z=296.12), mép cách cạnh đúng 0.5mm
    - Tấm đáy dưới: Vuông 30x30cm, khoét lỗ tròn Ø20cm (200mm) xả hạt chính giữa
    - Tấm vách đứng trước: Kích thước phôi 30cm x 45cm (cao từ Z=0 đến 450mm).
      PHÍA TRÊN CHỪA KHOẢNG TRỐNG 20cm x 30cm (từ Z=450 đến 650mm) LÀM CỬA ĐỔ HẠT VÀO!
    - Tấm vách đứng sau: Vuông 30x30cm nguyên tấm
    - Tấm vách dốc nghiêng trên: Rộng 30cm x Dài 46.1cm (mái che dốc 49.4° che chắn hạt)
    - Khối tham chiếu: Chữ nhật đáy (30x30x30cm) + Tam giác đỉnh (30x35x30cm)
    """
    T = DO_DAY_INOX
    B = KHOANG_CACH_2_TAM
    W_rec = CHIEU_DAI_DAY                  # 300mm
    H_front_total = CHIEU_CAO_TONG_TRUOC   # 650mm (Hộp cao 65cm nguyên vẹn)
    H_front_plate = CHIEU_CAO_VACH_TRUOC   # 450mm (Tấm ốp trước cao 45cm)
    H_back = CHIEU_CAO_SAU                 # 300mm
    H_tri = CHIEU_CAO_TAM_GIAC             # 350mm
    half_B = B / 2.0                       # 150mm
    L_slope = CANH_NGHIENG_TRUOC            # ~460.98mm

    # ==========================================================================
    # 1 & 2. HAI TẤM HÔNG (HÌNH THANG VUÔNG DỰNG ĐỨNG) DÀY 3MM, CAO 65CM / 30CM
    # XOAY NGƯỢC ĐẦU LẠI CHO ĐẦU NHỌN XUỐNG ĐÁY (GÓC NHỌN 40.6° TẠI ĐÁY TRƯỚC X=300, Z=0)
    # KHOAN LỖ Ø20MM Ở GÓC TÙ (X=10.5, Z=353.88), CÁCH VÁCH SAU VÀ CẠNH DỐC ĐÚNG 0.5MM
    # ==========================================================================
    # 4 đỉnh hình thang vuông trên mặt phẳng X-Z (Đầu nhọn hướng xuống):
    # P1 (0, 650): Đỉnh sau trên (vuông 90°)
    # P2 (W_rec, 650): Đỉnh trước trên (vuông 90°)
    # P3 (W_rec, 0): Đáy trước (góc nhọn 40.6° - ĐẦU NHỌN HƯỚNG XUỐNG ĐÁY)
    # P4 (0, 350): Đáy vách sau (góc tù 139.4° - chân vách dốc đáy nghiêng)

    Z_bot_back = H_front_total - H_back  # 350.0mm

    # Thông số lỗ khoan phi 20mm tại góc tù P4(0, 350):
    R_LO = 10.0           # Bán kính lỗ phi 20mm
    GAP_MEP = 0.5         # Cách mép vách đứng sau đúng 0.5mm
    X_LO = R_LO + GAP_MEP # 10.5mm (cách vách sau X=0 đúng 0.5mm)
    # Đường thẳng dốc đáy nghiêng nối (0, 350) -> (300, 0): 7X + 6Z - 2100 = 0
    # Tâm Z tính để mép lỗ cách đường dốc đúng 0.5mm:
    Z_LO = (2100.0 - 7.0 * X_LO + (R_LO + GAP_MEP) * math.sqrt(85.0)) / 6.0  # ~353.88mm

    # --- TẤM HÔNG TRÁI (Tại Y = -half_B = -150mm, đùn dày 3mm về phía -Y) ---
    pts_left = [
        App.Vector(0.0, -half_B, H_front_total),
        App.Vector(W_rec, -half_B, H_front_total),
        App.Vector(W_rec, -half_B, 0.0),
        App.Vector(0.0, -half_B, Z_bot_back),
        App.Vector(0.0, -half_B, H_front_total)
    ]
    poly_L = Part.makePolygon(pts_left)
    face_L = Part.Face(poly_L)
    solid_hong_trai = face_L.extrude(App.Vector(0.0, -T, 0.0))
    cutter_lo_L = Part.makeCylinder(R_LO, T + 10.0, App.Vector(X_LO, -half_B - T - 5.0, Z_LO), App.Vector(0.0, 1.0, 0.0))
    solid_hong_trai = solid_hong_trai.cut(cutter_lo_L)

    obj_hong_trai = doc.addObject("Part::Feature", f"{prefix}Tam_Hong_Trai_HinhThangVuong_3mm")
    obj_hong_trai.Shape = solid_hong_trai
    obj_hong_trai.Label = "1. Tấm Hông Trái (Hình Thang Inox 3mm, Đầu Nhọn Đáy 40.6°, Lỗ Ø20mm Góc Tù)"
    gan_mau_inox(obj_hong_trai)

    # --- TẤM HÔNG PHẢI (Tại Y = +half_B = +150mm, đùn dày 3mm về phía +Y) ---
    pts_right = [
        App.Vector(0.0, half_B, H_front_total),
        App.Vector(W_rec, half_B, H_front_total),
        App.Vector(W_rec, half_B, 0.0),
        App.Vector(0.0, half_B, Z_bot_back),
        App.Vector(0.0, half_B, H_front_total)
    ]
    poly_R = Part.makePolygon(pts_right)
    face_R = Part.Face(poly_R)
    solid_hong_phai = face_R.extrude(App.Vector(0.0, T, 0.0))
    cutter_lo_R = Part.makeCylinder(R_LO, T + 10.0, App.Vector(X_LO, half_B - 5.0, Z_LO), App.Vector(0.0, 1.0, 0.0))
    solid_hong_phai = solid_hong_phai.cut(cutter_lo_R)

    obj_hong_phai = doc.addObject("Part::Feature", f"{prefix}Tam_Hong_Phai_HinhThangVuong_3mm")
    obj_hong_phai.Shape = solid_hong_phai
    obj_hong_phai.Label = "2. Tấm Hông Phải (Hình Thang Inox 3mm, Cách 30cm, Đầu Nhọn Đáy, Lỗ Ø20mm)"
    gan_mau_inox(obj_hong_phai)

    # ==========================================================================
    # ==========================================================================
    # 3. TẤM NẮP ĐỈNH TRÊN: VUÔNG 30CM x 30CM x DÀY 3MM (Z=650MM)
    # KHOÉT LỖ TRÒN Ø20CM (200MM) CHÍNH GIỮA MẶT VUÔNG 30x30CM
    # ==========================================================================
    solid_day = Part.makeBox(W_rec, B, T, App.Vector(0.0, -half_B, H_front_total))
    R_LO_NAP = 100.0  # Bán kính lỗ tròn phi 20cm = 100mm (đường kính Ø200mm)
    cutter_nap = Part.makeCylinder(
        R_LO_NAP,
        T + 10.0,
        App.Vector(W_rec / 2.0, 0.0, H_front_total - 5.0),
        App.Vector(0.0, 0.0, 1.0)
    )
    solid_day = solid_day.cut(cutter_nap)

    obj_day = doc.addObject("Part::Feature", f"{prefix}Tam_Nap_Dinh_Tren_3mm")
    obj_day.Shape = solid_day
    obj_day.Label = "3. Tấm Nắp Đỉnh Trên (Inox 3mm, Vuông 30x30cm, Khoét Lỗ Tròn Ø20cm Ở Giữa, Z=650)"
    gan_mau_inox(obj_day)

    # ==========================================================================
    # 4. TẤM VÁCH ĐỨNG TRƯỚC: RỘNG 30CM x CAO 45CM (LẮP TỪ Z=200 ĐẾN 650MM)
    # - Phía dưới chân vách từ Z = 0 đến 200mm chừa khoảng trống 20x30cm xả hạt
    # - Ở phía bên kia (đỉnh trên của tấm), khoét lỗ tròn Ø20cm (200mm), mép trên chừa lại 1cm
    # ==========================================================================
    solid_vach_truoc = Part.makeBox(T, B, H_front_plate, App.Vector(W_rec, -half_B, KHOANG_TRONG_NAP_CAO))
    R_LO_TRUOC = 100.0       # Bán kính lỗ tròn phi 20cm = 100mm
    MEP_TREN_CHUA = 10.0     # Chừa lại 1cm = 10mm tính từ mép trên đỉnh tấm (Z = 650mm)
    Z_LO_TRUOC = H_front_total - MEP_TREN_CHUA - R_LO_TRUOC  # 650 - 10 - 100 = 540.0mm
    cutter_vach_truoc = Part.makeCylinder(
        R_LO_TRUOC,
        T + 10.0,
        App.Vector(W_rec - 5.0, 0.0, Z_LO_TRUOC),
        App.Vector(1.0, 0.0, 0.0)
    )
    solid_vach_truoc = solid_vach_truoc.cut(cutter_vach_truoc)

    obj_vach_truoc = doc.addObject("Part::Feature", f"{prefix}Tam_Vach_Dung_Truoc_3mm")
    obj_vach_truoc.Shape = solid_vach_truoc
    obj_vach_truoc.Label = "4. Tấm Vách Đứng Trước (Inox 3mm, 30x45cm, Khoét Lỗ Tròn Ø20cm Chừa 1cm, Đáy Trống 20cm)"
    gan_mau_inox(obj_vach_truoc)

    # ==========================================================================
    # 5. TẤM VÁCH ĐỨNG SAU: RỘNG 30CM x CAO 30CM x DÀY 3MM (VUÔNG 30X30 NGUYÊN TẤM, Z=350->650)
    # ==========================================================================
    solid_vach_sau = Part.makeBox(T, B, H_back, App.Vector(-T, -half_B, Z_bot_back))
    obj_vach_sau = doc.addObject("Part::Feature", f"{prefix}Tam_Vach_Dung_Sau_3mm")
    obj_vach_sau.Shape = solid_vach_sau
    obj_vach_sau.Label = "5. Tấm Vách Đứng Sau (Inox 3mm, Vuông 30x30cm Nguyên Tấm, Z=350->650)"
    gan_mau_inox(obj_vach_sau)

    # ==========================================================================
    # 6. TẤM VÁCH DỐC NGHIÊNG ĐÁY / MÁNG TRƯỢT: RỘNG 30CM x DÀI 46.1CM x DÀY 3MM
    # NỐI TỪ CHÂN VÁCH SAU (0, 350) DỐC XUỐNG ĐẦU NHỌN ĐÁY TRƯỚC (300, 0)
    # NGUYÊN TẤM LIỀN (MÁNG DỐC 49.4° TRÔI HẠT)
    # ==========================================================================
    dx = -T * (H_tri / L_slope)
    dz = -T * (W_rec / L_slope)
    pts_slope = [
        App.Vector(0.0, -half_B, Z_bot_back),
        App.Vector(W_rec, -half_B, 0.0),
        App.Vector(W_rec + dx, -half_B, dz),
        App.Vector(dx, -half_B, Z_bot_back + dz),
        App.Vector(0.0, -half_B, Z_bot_back)
    ]
    poly_slope = Part.makePolygon(pts_slope)
    face_slope = Part.Face(poly_slope)
    solid_nap = face_slope.extrude(App.Vector(0.0, B, 0.0))

    obj_nap = doc.addObject("Part::Feature", f"{prefix}Tam_Vach_Nghieng_Day_3mm")
    obj_nap.Shape = solid_nap
    obj_nap.Label = "6. Tấm Vách Dốc Nghiêng Đáy (Inox 3mm, 30x46.1cm, Dốc Trôi Hạt 49.4°)"
    gan_mau_inox(obj_nap, do_trong_suot=20)

    # ==========================================================================
    # 7. ỐNG NẠP LIỆU TRÒN TỪ TRÊN XUỐNG: PHI 19.9CM (199MM) x DÀI 30CM (300MM)
    # Lắp lọt qua lỗ Ø20cm trên nắp đỉnh Z=650mm, ăn sâu 30cm xuống Z=350mm
    # ==========================================================================
    PHI_NGOAI_ONG = 199.0     # Đường kính ngoài: 19.9cm = 199mm (khe hở 0.5mm với lỗ Ø200mm)
    R_OUT_ONG = PHI_NGOAI_ONG / 2.0  # 99.5mm
    DO_DAY_ONG = 2.0          # Độ dày thành ống inox: 2mm (2 ly)
    R_IN_ONG = R_OUT_ONG - DO_DAY_ONG  # 97.5mm
    CHIEU_DAI_ONG = 300.0     # Chiều dài ống: 30cm = 300mm
    X_ONG = W_rec / 2.0       # 150.0mm (đồng tâm với lỗ nắp đỉnh)
    Y_ONG = 0.0               # 0.0mm
    Z_ONG_TOP = H_front_total # 650.0mm (mặt nắp đỉnh trên)
    Z_ONG_BOT = Z_ONG_TOP - CHIEU_DAI_ONG  # 350.0mm

    cyl_out = Part.makeCylinder(
        R_OUT_ONG,
        CHIEU_DAI_ONG,
        App.Vector(X_ONG, Y_ONG, Z_ONG_BOT),
        App.Vector(0.0, 0.0, 1.0)
    )
    cyl_in = Part.makeCylinder(
        R_IN_ONG,
        CHIEU_DAI_ONG + 10.0,
        App.Vector(X_ONG, Y_ONG, Z_ONG_BOT - 5.0),
        App.Vector(0.0, 0.0, 1.0)
    )
    solid_ong = cyl_out.cut(cyl_in)

    obj_ong = doc.addObject("Part::Feature", f"{prefix}Ong_Nap_Lieu_Phi199_Dai300")
    obj_ong.Shape = solid_ong
    obj_ong.Label = "7. Ống Nạp Liệu Tròn (Inox 304, Ø19.9cm x Dài 30cm, Rỗng Dày 2mm, Từ Trên Xuống)"
    gan_mau_inox(obj_ong, line_color=(0.10, 0.15, 0.20), line_width=1.8)

    # ==========================================================================
    # 8. CƠ CẤU VAN GẠT ĐÁY ỐNG: CÂY LÁP Ø20MM + LÁ VAN INOX 3MM (HÌNH GÓC TỌA ĐỘ)
    # - Cây láp Inox phi 20mm xuyên qua 2 lỗ bên hông tại góc tù (X=10.5, Z=353.9)
    # - Lá van gạt cắt từ tấm Inox 3mm (250x220x3mm) nằm ngay dưới đáy ống Z=350mm
    # - 2 vách gân chắn hông hình góc tọa độ vuông (Inox 3mm, cao 45mm) chống tràn hạt
    # - Tay gạt điều khiển bên ngoài & Cung chia góc tọa độ để kiểm soát hàng qua ống
    # ==========================================================================
    # 8. Cơ cấu van gạt đáy ống: Cây láp Ø20mm nhô 10cm bên phải + 4 Vòng tròn (ID Ø20mm) + Lá van Inox 3mm bo tròn
    R_SHAFT_VAN = 10.0        # Bán kính cây láp: phi 20mm -> R = 10mm
    R_RING_IN = 10.0          # Đường kính trong vòng tròn = 20mm (bằng cây láp)
    R_RING_OUT = 16.0         # Đường kính ngoài vòng tròn = 32mm (thành dày 6mm)
    T_RING_BOX = 10.0         # Vòng dày 10mm hàn vào thành hộp
    T_RING_SHAFT = 8.0        # Vòng ngoài 8mm hàn vào cây láp
    GAP_RING = 0.5            # Khe hở vận hành giữa 2 vòng

    def tao_vong_tron(y_start, chieu_day):
        cyl_o = Part.makeCylinder(
            R_RING_OUT,
            chieu_day,
            App.Vector(X_LO, y_start, Z_LO),
            App.Vector(0.0, 1.0, 0.0)
        )
        cyl_i = Part.makeCylinder(
            R_RING_IN,
            chieu_day + 2.0,
            App.Vector(X_LO, y_start - 1.0, Z_LO),
            App.Vector(0.0, 1.0, 0.0)
        )
        return cyl_o.cut(cyl_i)

    # 8a. Hai vòng dày hàn vào hộp (1 vòng mỗi bên hông, hàn chặt vào mặt ngoài tấm hông):
    solid_vong_hop_P = tao_vong_tron(half_B + DO_DAY_INOX, T_RING_BOX)
    solid_vong_hop_T = tao_vong_tron(-half_B - DO_DAY_INOX - T_RING_BOX, T_RING_BOX)

    solid_hong_trai = Part.makeCompound([solid_hong_trai, solid_vong_hop_T])
    obj_hong_trai.Shape = solid_hong_trai
    obj_hong_trai.Label = "1. Tấm Hông Trái (Kèm Vòng Bạc Đỡ Ø20 Dày 10mm Hàn Ngoài)"

    solid_hong_phai = Part.makeCompound([solid_hong_phai, solid_vong_hop_P])
    obj_hong_phai.Shape = solid_hong_phai
    obj_hong_phai.Label = "2. Tấm Hông Phải (Kèm Vòng Bạc Đỡ Ø20 Dày 10mm Hàn Ngoài)"

    # 8b. Cây láp Ø20mm: Dư ra đúng 10cm (100mm) về bên phải (+253mm), bên trái Y = -175mm:
    Y_SHAFT_MIN = -half_B - DO_DAY_INOX - T_RING_BOX - GAP_RING - T_RING_SHAFT - 3.5  # -175.0mm
    Y_SHAFT_MAX = half_B + DO_DAY_INOX + 100.0  # +253.0mm (dư ra đúng 10cm tính từ mặt ngoài tấm hông phải)
    L_SHAFT_VAN = Y_SHAFT_MAX - Y_SHAFT_MIN  # 428.0mm

    solid_truc_lap = Part.makeCylinder(
        R_SHAFT_VAN,
        L_SHAFT_VAN,
        App.Vector(X_LO, Y_SHAFT_MIN, Z_LO),
        App.Vector(0.0, 1.0, 0.0)
    )

    # 8c. Hai vòng ngoài hàn vào cây láp (xoay cùng cây láp):
    solid_vong_lap_P = tao_vong_tron(half_B + DO_DAY_INOX + T_RING_BOX + GAP_RING, T_RING_SHAFT)
    solid_vong_lap_T = tao_vong_tron(-half_B - DO_DAY_INOX - T_RING_BOX - GAP_RING - T_RING_SHAFT, T_RING_SHAFT)

    # 8d. Tấm lá van Inox 3mm bo tròn đẹp mắt, ôm trọn và đồng tâm với ống nạp Ø19.9cm:
    W_VAN = 220.0             # Rộng 220mm (che phủ ống phi 19.9cm, mép dư 10.5mm đều 2 bên)
    R_ROUND = W_VAN / 2.0     # 110.0mm (bán kính bo tròn đầu lá van)
    T_VAN = DO_DAY_INOX       # Dày 3mm inox
    Z_VAN = Z_bot_back - T_VAN  # 347.0mm

    edge1 = Part.makeLine(App.Vector(X_LO, -R_ROUND, Z_VAN), App.Vector(X_ONG, -R_ROUND, Z_VAN))
    arc_edge = Part.Arc(
        App.Vector(X_ONG, -R_ROUND, Z_VAN),
        App.Vector(X_ONG + R_ROUND, 0.0, Z_VAN),
        App.Vector(X_ONG, R_ROUND, Z_VAN)
    ).toShape()
    edge2 = Part.makeLine(App.Vector(X_ONG, R_ROUND, Z_VAN), App.Vector(X_LO, R_ROUND, Z_VAN))
    edge3 = Part.makeLine(App.Vector(X_LO, R_ROUND, Z_VAN), App.Vector(X_LO, -R_ROUND, Z_VAN))

    wire_la = Part.Wire([edge1, arc_edge, edge2, edge3])
    face_la = Part.Face(wire_la)
    solid_la_van = face_la.extrude(App.Vector(0.0, 0.0, T_VAN))

    # 8e. Cơ cấu góc tọa độ 3 góc vuông ở đầu cây láp nhô ra 10cm bên phải (Y = +240mm):
    # Nằm ngay chỗ vuông góc ở trên, tạo đúng 3 góc vuông trực giao hoàn hảo (Hệ tọa độ 3 trục X, Y, Z Ø20mm):
    # - Trục Y: Cây láp ngang Ø20mm (trục xoay chính)
    # - Trục X: Cây vuông góc thứ 1 dài 22cm (220mm) vươn theo phương ngang ra ngoài (-X)
    # - Trục Z: Cây vuông góc thứ 2 dài 22cm (220mm) chúc thẳng đứng xuống dưới (-Z)
    # -> Đúng yêu cầu: 1 cây quay ra ngoài, 1 cây quay xuống dưới!
    Y_HANDLE = Y_SHAFT_MAX - 13.0  # +240.0mm (cách đầu mút cây láp 13mm)
    L_LEVER = 220.0                # Cần gạt vuông góc theo trục X (dài 22cm, vươn ra ngoài)
    L_LEVER_Z = 220.0              # Cần gạt vuông góc theo trục Z (dài 22cm, chúc xuống dưới)
    R_LEVER = 10.0                 # Bán kính 10mm -> Láp Ø20mm (bằng đúng cây láp ngang Ø20mm)

    # Cây vuông góc 1 (vươn theo phương ngang -X hướng ra ngoài / phía người vận hành):
    solid_lever = Part.makeCylinder(
        R_LEVER,
        L_LEVER,
        App.Vector(X_LO, Y_HANDLE, Z_LO),
        App.Vector(-1.0, 0.0, 0.0)
    )

    # Cây vuông góc 2 (nằm ngay chỗ vuông góc, chúc thẳng đứng xuống dưới -Z -> 1 ra ngoài 1 xuống):
    solid_lever_z = Part.makeCylinder(
        R_LEVER,
        L_LEVER_Z,
        App.Vector(X_LO, Y_HANDLE, Z_LO),
        App.Vector(0.0, 0.0, -1.0)
    )

    # Cụm van gạt xoay: Cây láp 428mm + 1 Lá Inox bo tròn + 2 Vòng ngoài hàn láp + Góc tọa độ 3 góc vuông Ø20mm
    shape_van = Part.makeCompound([
        solid_truc_lap,
        solid_la_van,
        solid_vong_lap_T,
        solid_vong_lap_P,
        solid_lever,
        solid_lever_z
    ])

    obj_van = doc.addObject("Part::Feature", f"{prefix}CoCau_VanGat_Lap20_Inox3mm")
    obj_van.Shape = shape_van
    obj_van.Label = "8. Cơ Cấu Van Gạt Đáy Ống (Láp Ø20 Dài 42.8cm, 2 Vòng Chặn Láp, Góc Tọa Độ 3 Góc Vuông Ø20)"
    gan_mau_inox(obj_van, line_color=(0.10, 0.20, 0.30), line_width=1.8)

    # ==========================================================================
    # 9. KHỐI THAM CHIẾU: HÌNH CHỮ NHẬT TRÊN (30x30x30) & TAM GIÁC ĐÁY (30x35x30)
    # ==========================================================================
    box_ref = Part.makeBox(W_rec, B, H_back, App.Vector(0.0, -half_B, Z_bot_back))
    obj_ref_rect = doc.addObject("Part::Feature", f"{prefix}ThamChieu_1_HinhChuNhat_30x30x30cm")
    obj_ref_rect.Shape = box_ref
    obj_ref_rect.Label = "📐 Tham Chiếu 1: Khối Chữ Nhật Trên (30cm x 30cm x 30cm, Z=350->650)"
    gan_mau_inox(obj_ref_rect, line_color=(0.1, 0.5, 0.8), do_trong_suot=70)
    if hasattr(obj_ref_rect, "ViewObject") and obj_ref_rect.ViewObject:
        obj_ref_rect.ViewObject.Visibility = False

    pts_tri_ref = [
        App.Vector(0.0, -half_B, Z_bot_back),
        App.Vector(W_rec, -half_B, Z_bot_back),
        App.Vector(W_rec, -half_B, 0.0),
        App.Vector(0.0, -half_B, Z_bot_back)
    ]
    face_tri_ref = Part.Face(Part.makePolygon(pts_tri_ref))
    prism_tri = face_tri_ref.extrude(App.Vector(0.0, B, 0.0))
    obj_ref_tri = doc.addObject("Part::Feature", f"{prefix}ThamChieu_2_HinhTamGiac_30x35x30cm")
    obj_ref_tri.Shape = prism_tri
    obj_ref_tri.Label = "📐 Tham Chiếu 2: Khối Tam Giác Vuông Đáy (30cm x 35cm x 30cm, Đầu Nhọn Đáy)"
    gan_mau_inox(obj_ref_tri, line_color=(0.8, 0.3, 0.1), do_trong_suot=70)
    if hasattr(obj_ref_tri, "ViewObject") and obj_ref_tri.ViewObject:
        obj_ref_tri.ViewObject.Visibility = False

    # ==========================================================================
    # 10. TỔNG HỢP TOÀN BỘ HỘP VÔ HÀNG (COMPOUND)
    # ==========================================================================
    tat_ca_tam = [
        solid_hong_trai,
        solid_hong_phai,
        solid_vach_sau,
        solid_day,
        solid_nap,
        solid_vach_truoc,
        solid_ong,
        shape_van
    ]
    hinh_hop_tong_the = Part.makeCompound(tat_ca_tam)
    obj_tong_the = doc.addObject("Part::Feature", f"{prefix}Hop_Vo_Hang_Tong_The_Inox_3mm")
    obj_tong_the.Shape = hinh_hop_tong_the
    obj_tong_the.Label = "⭐ HỘP VÔ HÀNG INOX 3MM DỰNG ĐỨNG (ĐẦU NHỌN XUỐNG, CỬA NẠP 20x30CM)"
    gan_mau_inox(obj_tong_the)
    if hasattr(obj_tong_the, "ViewObject") and obj_tong_the.ViewObject:
        obj_tong_the.ViewObject.Visibility = False

    all_hop_objs = [
        obj_hong_trai,
        obj_hong_phai,
        obj_vach_sau,
        obj_day,
        obj_nap,
        obj_vach_truoc,
        obj_ong,
        obj_van,
        obj_ref_rect,
        obj_ref_tri,
        obj_tong_the
    ]
    if plc is not None:
        for ob in all_hop_objs:
            if ob:
                try:
                    ob.Placement = plc
                except Exception:
                    pass
    if prefix:
        for ob in all_hop_objs:
            if ob and hasattr(ob, "Label"):
                ob.Label = f"{prefix}{ob.Label}"

    return tuple(all_hop_objs)


# ======================================================================================
# GIAO DIỆN ĐIỀU KHIỂN & BẢNG THÔNG TIN PHÔI CẮT INOX 3MM
# ======================================================================================
class BangDieuKhienHopVoHang(QtWidgets.QDialog if QtWidgets else object):
    """Bảng điều khiển trực quan cho Hộp Vô Hàng Inox 3mm."""

    def __init__(self, doc, items, parent=None):
        if not QtWidgets:
            return
        super(BangDieuKhienHopVoHang, self).__init__(parent)
        self.doc = doc
        (
            self.obj_hong_trai,
            self.obj_hong_phai,
            self.obj_vach_sau,
            self.obj_day,
            self.obj_nap,
            self.obj_vach_nghieng,
            self.obj_ong,
            self.obj_van,
            self.obj_ref_rect,
            self.obj_ref_tri,
            self.obj_tong_the
        ) = items

        self.is_transparent = False
        self.is_thung_visible = True
        self.is_top_open = False
        self.is_ref_visible = False
        self.goc_van = 0.0  # 0° = Đóng kín, 45° = Mở thông

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Hộp Vô Hàng Inox 3mm (30cm) - Điều Khiển & Phôi Cắt")
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumWidth(480)
        self.setStyleSheet("""
            QDialog { background-color: #f8fafc; font-family: 'Segoe UI', Arial, sans-serif; }
            QGroupBox { font-weight: bold; border: 1px solid #cbd5e1; border-radius: 6px; margin-top: 10px; padding-top: 14px; background-color: #ffffff; color: #1e293b; }
            QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 5px; color: #0f172a; }
            QPushButton { border-radius: 5px; font-weight: bold; padding: 7px 12px; font-size: 11.5px; }
        """)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 10, 12, 10)

        # Header
        header = QtWidgets.QFrame()
        header.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0f172a, stop:1 #334155); border-radius: 6px; padding: 8px;")
        h_layout = QtWidgets.QVBoxLayout(header)
        h_layout.setContentsMargins(10, 4, 10, 4)
        t1 = QtWidgets.QLabel("📥 HỘP VÔ HÀNG INOX 3MM (30CM)")
        t1.setStyleSheet("color: #38bdf8; font-weight: bold; font-size: 13.5px;")
        t2 = QtWidgets.QLabel(f"Hộp dựng đứng: Đáy 30cm, Cao 65cm/30cm | Vách trước 45cm chừa khoảng trống 20x30cm ở trên")
        t2.setStyleSheet("color: #cbd5e1; font-size: 11px;")
        h_layout.addWidget(t1)
        h_layout.addWidget(t2)
        layout.addWidget(header)

        # Nhóm Quan sát & Điều khiển
        grp_ctrl = QtWidgets.QGroupBox("👁 Chế Độ Quan Sát")
        g_ctrl = QtWidgets.QGridLayout(grp_ctrl)
        g_ctrl.setSpacing(6)

        self.btn_trans = QtWidgets.QPushButton("👁 Xuyên Thấu Hộp")
        self.btn_trans.setStyleSheet("background-color: #0d9488; color: white;")
        self.btn_trans.clicked.connect(self.toggle_transparency)

        self.btn_thung = QtWidgets.QPushButton("📦 Ẩn/Hiện Thùng Bên Ngoài")
        self.btn_thung.setStyleSheet("background-color: #6366f1; color: white;")
        self.btn_thung.clicked.connect(self.toggle_thung_visibility)

        self.btn_nap = QtWidgets.QPushButton("📦 Mở / Đậy Nắp Trên")
        self.btn_nap.setStyleSheet("background-color: #7c3aed; color: white;")
        self.btn_nap.clicked.connect(self.toggle_nap)

        self.btn_ref = QtWidgets.QPushButton("📐 Ẩn/Hiện Khối Tham Chiếu")
        self.btn_ref.setStyleSheet("background-color: #ea580c; color: white;")
        self.btn_ref.clicked.connect(self.toggle_ref)

        g_ctrl.addWidget(self.btn_trans, 0, 0)
        g_ctrl.addWidget(self.btn_thung, 0, 1)
        g_ctrl.addWidget(self.btn_nap, 1, 0)
        g_ctrl.addWidget(self.btn_ref, 1, 1)
        layout.addWidget(grp_ctrl)

        # Nhóm Điều khiển Van Gạt Đáy Ống (Láp Ø20mm & Lá Inox 3mm)
        grp_van = QtWidgets.QGroupBox("🎛️ Kiểm Soát Hàng Qua Ống (Van Gạt Láp Ø20mm & Inox 3mm)")
        l_van = QtWidgets.QVBoxLayout(grp_van)
        l_van.setSpacing(6)

        r_van_btn = QtWidgets.QHBoxLayout()
        self.btn_toggle_van = QtWidgets.QPushButton("🔓 Mở Van Gạt (45°)")
        self.btn_toggle_van.setStyleSheet("background-color: #16a34a; color: white; font-weight: bold;")
        self.btn_toggle_van.clicked.connect(self.toggle_van_gat)

        self.lbl_goc_van = QtWidgets.QLabel("Góc tọa độ: 🔴 0.0° (ĐÓNG KÍN)")
        self.lbl_goc_van.setStyleSheet("font-weight: bold; color: #dc2626; font-size: 11.5px;")

        r_van_btn.addWidget(self.btn_toggle_van)
        r_van_btn.addWidget(self.lbl_goc_van)
        l_van.addLayout(r_van_btn)

        # Slider góc mở van (0 đến 45 độ)
        self.sld_van = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sld_van.setRange(0, 45)
        self.sld_van.setValue(0)
        self.sld_van.valueChanged.connect(self.cap_nhat_goc_van)
        l_van.addWidget(self.sld_van)
        layout.addWidget(grp_van)

        # Nhóm Góc nhìn
        grp_cams = QtWidgets.QGroupBox("📐 Góc Nhìn 1-Click")
        r_cams = QtWidgets.QHBoxLayout(grp_cams)
        r_cams.setSpacing(6)

        btn_iso = QtWidgets.QPushButton("📐 Isometric")
        btn_iso.setStyleSheet("background-color: #475569; color: white;")
        btn_iso.clicked.connect(self.view_isometric)

        btn_side = QtWidgets.QPushButton("🔙 Nhìn Cạnh (Hình Thang)")
        btn_side.setStyleSheet("background-color: #334155; color: white;")
        btn_side.clicked.connect(self.view_side)

        btn_front = QtWidgets.QPushButton("🔜 Nhìn Mặt Trước (Cửa Nạp 20x30)")
        btn_front.setStyleSheet("background-color: #334155; color: white;")
        btn_front.clicked.connect(self.view_front)

        r_cams.addWidget(btn_iso)
        r_cams.addWidget(btn_side)
        r_cams.addWidget(btn_front)
        layout.addWidget(grp_cams)

        # Bảng kê phôi cắt inox 3mm
        grp_bom = QtWidgets.QGroupBox("📋 Kích Thước Cắt Phôi Inox 3mm (BOM)")
        v_bom = QtWidgets.QVBoxLayout(grp_bom)
        txt_bom = QtWidgets.QTextEdit()
        txt_bom.setReadOnly(True)
        txt_bom.setStyleSheet("background-color: #f1f5f9; border: 1px solid #cbd5e1; font-size: 11px; color: #0f172a;")
        txt_bom.setHtml(f"""
        <table style="width: 100%; border-collapse: collapse; font-size: 11px;">
            <tr style="background-color: #e2e8f0; font-weight: bold;">
                <td style="padding: 4px;">Tên chi tiết</td>
                <td style="padding: 4px;">Kích thước phôi (mm)</td>
                <td style="padding: 4px;">SL</td>
            </tr>
            <tr>
                <td style="padding: 4px;">1. Tấm hông (Hình thang đầu nhọn đáy)</td>
                <td style="padding: 4px;">Đỉnh 300, trước 650, sau 300, dốc 461 (Khoan lỗ Ø20mm góc tù X=10.5, Z=353.9)</td>
                <td style="padding: 4px;"><b>2 tấm</b></td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 4px;">2. Tấm nắp đỉnh trên (vuông 30)</td>
                <td style="padding: 4px;">300 x 300 mm (Khoét lỗ tròn Ø20cm / 200mm chính giữa, Z=650)</td>
                <td style="padding: 4px;"><b>1 tấm</b></td>
            </tr>
            <tr>
                <td style="padding: 4px;">3. Tấm vách đứng trước (45x30)</td>
                <td style="padding: 4px;">300 x 450 mm (Khoét lỗ tròn Ø20cm cách đỉnh 1cm, đáy trống 20x30cm)</td>
                <td style="padding: 4px;"><b>1 tấm</b></td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 4px;">4. Tấm vách đứng sau (vuông 30)</td>
                <td style="padding: 4px;">300 x 300 mm (Nguyên tấm vuông 30x30cm, Z=350->650)</td>
                <td style="padding: 4px;"><b>1 tấm</b></td>
            </tr>
            <tr>
                <td style="padding: 4px;">5. Tấm vách dốc nghiêng đáy / Máng trượt</td>
                <td style="padding: 4px;">300 x 461 mm (Nguyên tấm liền, máng dốc 49.4° trôi hạt)</td>
                <td style="padding: 4px;"><b>1 tấm</b></td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 4px;">6. Ống nạp liệu tròn (từ trên xuống)</td>
                <td style="padding: 4px;">Ø19.9cm (Ø199mm) x Dài 30cm (Dày 2mm Inox 304, đút lọt qua lỗ nắp Ø20cm)</td>
                <td style="padding: 4px;"><b>1 ống</b></td>
            </tr>
            <tr>
                <td style="padding: 4px;">7. Cây láp xoay van gạt (phi 20)</td>
                <td style="padding: 4px;">Ø20mm x Dài 428mm (Láp đặc, dư 10cm sang phải, xuyên qua 2 lỗ hông X=10.5, Z=353.9)</td>
                <td style="padding: 4px;"><b>1 cây</b></td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 4px;">8. Bạc chặn & Cữ định vị (Ø32xØ20)</td>
                <td style="padding: 4px;">2 vòng dày 10mm hàn vào 2 hông hộp; 2 vòng ngoài 8mm hàn vào cây láp</td>
                <td style="padding: 4px;"><b>4 vòng</b></td>
            </tr>
            <tr>
                <td style="padding: 4px;">9. Lá van gạt đáy ống (Inox 3mm)</td>
                <td style="padding: 4px;">1 lá Inox 3mm bo tròn bán nguyệt R110mm ôm trọn ống Ø19.9cm (hàn vào láp Ø20)</td>
                <td style="padding: 4px;"><b>1 tấm</b></td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 4px;">10. Cơ cấu góc tọa độ 3 góc vuông (Ø20mm)</td>
                <td style="padding: 4px;">2 cây láp Ø20 dài 220mm hàn vuông góc ở trên (1 cây ngang +X, 1 cây đứng +Z tạo 3 góc vuông với láp Y)</td>
                <td style="padding: 4px;"><b>2 cây</b></td>
            </tr>
        </table>
        <p style="margin-top: 6px; font-size: 10.5px; color: #475569;">
            * <b>Hộp dựng đứng (Đầu nhọn hướng xuống):</b> Góc nhọn 40.6° ở đáy trước (Z=0). Vách trước cao 65cm, vách sau cao 30cm (từ Z=35 đến 65cm).<br>
            * <b>Lỗ nạp tròn Ø20cm trên vách trước:</b> Ở phía trên của tấm vách trước (phía bên kia của mép cắt 20cm), khoét lỗ tròn Ø20cm, mép trên chừa lại đúng 1cm (10mm).<br>
            * <b>Cửa xả hạt đáy (Khoảng trống 20x30cm):</b> Ở phía dưới chân vách trước (từ Z=0 đến 200mm), chừa trống đúng 20x30cm làm cửa xả hạt.<br>
            * <b>Lỗ tròn Ø20cm ở mặt vuông 30x30cm:</b> Khoét chính giữa mặt nắp vuông 30x30cm (Z=650), đường kính Ø20cm (200mm), chừa mép đều 5cm (50mm) mỗi bên.<br>
            * <b>Ống nạp liệu Ø19.9cm dài 30cm:</b> Nằm từ nắp đỉnh Z=650mm đâm thẳng xuống Z=350mm, rỗng ruột dày 2mm, khe hở 0.5mm so với lỗ nắp Ø20cm.<br>
            * <b>Cơ cấu van gạt láp Ø20mm & Inox 3mm:</b> Lắp ở góc tọa độ (X=10.5, Z=353.9mm), gạt xoay từ 0° (đóng kín chặn hạt) đến 45° (mở thông cho hạt qua ống rơi xuống buồng rang).<br>
            * Khoảng cách lọt lòng 2 tấm hông: đúng <b>300mm (30cm)</b> | Thể tích buồng chứa: <b>~{THE_TICH_LIT:.1f} Lít</b> (~25 - 35 kg hạt).
        </p>
        """)
        txt_bom.setFixedHeight(210)
        v_bom.addWidget(txt_bom)
        layout.addWidget(grp_bom)

        self.adjustSize()

    def cap_nhat_goc_van(self, val):
        self.goc_van = float(val)
        pivot = App.Vector(10.5, 0.0, 353.88)
        rot = App.Rotation(App.Vector(0, 1, 0), self.goc_van)
        pos = pivot - rot.multVec(pivot)
        if self.obj_van:
            try:
                self.obj_van.Placement = App.Placement(pos, rot)
            except Exception:
                pass
        if self.goc_van == 0:
            self.lbl_goc_van.setText("Góc tọa độ: 🔴 0.0° (ĐÓNG KÍN)")
            self.lbl_goc_van.setStyleSheet("font-weight: bold; color: #dc2626; font-size: 11.5px;")
            self.btn_toggle_van.setText("🔓 Mở Van Gạt (45°)")
            self.btn_toggle_van.setStyleSheet("background-color: #16a34a; color: white; font-weight: bold;")
        else:
            pct = int(self.goc_van / 45.0 * 100.0)
            self.lbl_goc_van.setText(f"Góc tọa độ: 🟢 {self.goc_van:.1f}° (Mở {pct}%)")
            self.lbl_goc_van.setStyleSheet("font-weight: bold; color: #16a34a; font-size: 11.5px;")
            if self.goc_van >= 40:
                self.btn_toggle_van.setText("🔒 Đóng Van Gạt (0°)")
                self.btn_toggle_van.setStyleSheet("background-color: #dc2626; color: white; font-weight: bold;")

    def toggle_van_gat(self):
        target = 45 if self.goc_van < 20 else 0
        self.sld_van.setValue(target)

    def toggle_thung_visibility(self):
        """Ẩn/hiện các tấm vỏ thùng bên ngoài như ẩn vỏ trống."""
        self.is_thung_visible = not self.is_thung_visible
        if kiem_tra_co_gui():
            for obj in [
                self.obj_hong_trai,
                self.obj_hong_phai,
                self.obj_vach_sau,
                self.obj_day,
                self.obj_nap,
                self.obj_vach_nghieng,
            ]:
                if obj and hasattr(obj, "ViewObject") and obj.ViewObject:
                    obj.ViewObject.Visibility = self.is_thung_visible
        if self.is_thung_visible:
            self.btn_thung.setText("📦 Ẩn Thùng Bên Ngoài")
            self.btn_thung.setStyleSheet("background-color: #6366f1; color: white;")
        else:
            self.btn_thung.setText("📦 Hiện Thùng Bên Ngoài")
            self.btn_thung.setStyleSheet("background-color: #475569; color: white;")

    def toggle_transparency(self):
        self.is_transparent = not self.is_transparent
        val = 50 if self.is_transparent else 0
        if kiem_tra_co_gui():
            for obj in [self.obj_hong_trai, self.obj_hong_phai, self.obj_vach_sau, self.obj_day, self.obj_vach_nghieng, self.obj_ong, self.obj_van]:
                if hasattr(obj, "ViewObject") and obj.ViewObject:
                    obj.ViewObject.Transparency = val

    def toggle_nap(self):
        self.is_top_open = not self.is_top_open
        if kiem_tra_co_gui() and hasattr(self.obj_nap, "ViewObject") and self.obj_nap.ViewObject:
            self.obj_nap.ViewObject.Visibility = not self.is_top_open

    def toggle_ref(self):
        self.is_ref_visible = not self.is_ref_visible
        if kiem_tra_co_gui():
            for obj in [self.obj_ref_rect, self.obj_ref_tri]:
                if hasattr(obj, "ViewObject") and obj.ViewObject:
                    obj.ViewObject.Visibility = self.is_ref_visible

    def view_isometric(self):
        if kiem_tra_co_gui():
            try:
                Gui.SendMsgToActiveView("ViewAxo")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def view_side(self):
        if kiem_tra_co_gui():
            try:
                Gui.SendMsgToActiveView("ViewRight")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def view_front(self):
        if kiem_tra_co_gui():
            try:
                Gui.SendMsgToActiveView("ViewFront")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass


def chay_mo_hinh():
    """Hàm chính thực thi tạo mô hình và hiển thị trong FreeCAD."""
    global _HOP_VO_HANG_WINDOW

    # 1. Đóng sạch tài liệu cũ
    dong_tai_lieu_cu("Hop_Vo_Hang_Inox_3mm")

    # 2. Khởi tạo tài liệu mới
    doc = App.newDocument("Hop_Vo_Hang_Inox_3mm")

    # 3. Tạo mô hình các chi tiết
    items = tao_hop_vo_hang(doc)
    doc.recompute()

    # In thông số ra console
    print("\n" + "=" * 80)
    print(">> ĐÃ TẠO THÀNH CÔNG: HỘP VÔ HÀNG INOX 3MM DỰNG ĐỨNG (ĐẦU NHỌN HƯỚNG XUỐNG)")
    print(">> 1. Kích thước hình thang vuông (Chữ nhật trên 30x30cm + Tam giác đáy 30x35cm):")
    print(f"      - Chiều cao tổng thể hông trước: {CHIEU_CAO_TONG_TRUOC:.1f} mm (65 cm)")
    print(f"      - Chiều cao tấm ốp vách trước  : {CHIEU_CAO_VACH_TRUOC:.1f} mm (45 cm - Cắt phôi 45x30cm, Z=200->650)")
    print(f"      - Lỗ nạp tròn Ø20cm vách trước : Khoét tròn Ø200mm tại Z=540mm, mép trên chừa lại đúng 1.0cm (10mm)")
    print(f"      - Cửa xả hạt đáy (khoảng trống): {KHOANG_TRONG_NAP_CAO:.1f} mm x 300 mm (20x30cm ở phía dưới đáy Z=0->200)")
    print(f"      - Chiều cao vách đứng sau      : {CHIEU_CAO_SAU:.1f} mm (30 cm - Vuông 30x30cm nguyên tấm, Z=350->650)")
    print(f"      - Chiều dài đỉnh trên          : {CHIEU_DAI_DAY:.1f} mm (30 cm)")
    print(f"      - Cạnh dốc nghiêng đáy         : {CANH_NGHIENG_TRUOC:.1f} mm (~46.1 cm, dốc {GOC_DOC_DO:.1f}°)")
    print(f">> 2. Đầu nhọn đáy (góc nhọn 40.6°) hướng xuống dưới tại chân vách trước (X=300, Z=0).")
    print(f">> 3. Hai tấm hông nhân đôi cách nhau: {KHOANG_CACH_2_TAM:.1f} mm ({KHOANG_CACH_2_TAM/10:.0f} cm lọt lòng)")
    print(f">> 4. Lỗ trục gạt Ø20mm ở góc tù sau (X=10.5, Z=353.9mm), mép cách 2 cạnh đúng 0.5mm.")
    print(f">> 5. Lỗ tròn Ø25cm (250mm) khoét chính giữa mặt dốc đáy theo đúng ảnh chỉ định.")
    print(f">> 6. Thể tích chứa hữu dụng: ~{THE_TICH_LIT:.1f} Lít (~25 - 35 kg cà phê nhân).")
    print("=" * 80 + "\n")

    # 4. Hiển thị GUI & Căn góc nhìn
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

        if QtWidgets:
            _HOP_VO_HANG_WINDOW = BangDieuKhienHopVoHang(doc, items, parent=main_win)
            _HOP_VO_HANG_WINDOW.show()


if __name__ == "__main__" or __name__ == "FreeCAD":
    chay_mo_hinh()
