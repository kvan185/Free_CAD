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

def tao_bo_chinh_phuong_an_chi_tiet(doc, plc_base=None, is_exploded=False, prefix=""):
    """
    CỤM BỘ CHỈNH GỐI BI TRỤC PHI 60MM - KIỂU PHƯƠNG ÂN (CHUẨN THỰC TẾ 100%)
    - is_exploded=True: Tách rời 7 chi tiết theo thứ tự dọc trục Y để soi cấu tạo (Phần 1 Tab 3)
    - is_exploded=False: Lắp ráp 100% ăn khớp hoàn chỉnh (Phần 2 Tab 3 & Gắn trên 2 Mặt Máy Tab 1)

    7 Chi Tiết Cấu Tạo:
    1. Thân bệ bích vuông gang đúc 165x165mm dày 16mm, cổ tròn D125mm, tai kẹp xẻ rãnh góc -150°, vú mỡ +35°.
    2. 4 Bu-lông M14 bắt mặt máy (kèm long đền D14 mạ kẽm).
    3. Bạc đạn đỡ trục UC212 (Phi 60/110mm, 8 bi cầu, 2 phớt chặn mỡ).
    4. Đoạn cốt láp Phi 60mm kèm rãnh then cavet 18x11mm.
    5. Cổ siết lục giác ren ngoài S=105mm (ống ren M100 tịnh tiến khe hở trống).
    6. Cần gạt khóa nhanh chống rung góc -150° (tay gạt công thái học kèm núm tròn).
    7. Nắp tròn bịt đầu Phi 86mm có 3 vít M4 (ngăn 100% bụi vỏ lụa cà phê).
    """
    objs = []

    W_b = 165.0
    T_b = 16.0
    j_half = 65.0

    dY_base = -130.0 if is_exploded else 0.0
    dY_bearing = -40.0 if is_exploded else 0.0
    dY_shaft = 40.0 if is_exploded else 0.0
    dY_hex = 120.0 if is_exploded else 0.0
    dY_cap = 200.0 if is_exploded else 0.0
    d_lever = 35.0 if is_exploded else 0.0

    # 1. Thân bệ bích vuông gang đúc
    p_box = Part.makeBox(W_b, T_b, W_b, App.Vector(-W_b / 2.0, dY_base, -W_b / 2.0))
    edges_Y = [e for e in p_box.Edges if abs(e.tangentAt(0).y) > 0.9]
    p_box = p_box.makeFillet(15.0, edges_Y)

    for xb in [-j_half, j_half]:
        for zb in [-j_half, j_half]:
            h = Part.makeCylinder(7.5, T_b + 10.0, App.Vector(xb, dY_base - 5.0, zb), App.Vector(0, 1, 0))
            p_box = p_box.cut(h)

    p_box = p_box.cut(Part.makeCylinder(31.0, T_b + 10.0, App.Vector(0, dY_base - 5.0, 0), App.Vector(0, 1, 0)))

    cyl_body = Part.makeCylinder(62.5, 60.0, App.Vector(0, dY_base + T_b, 0), App.Vector(0, 1, 0))
    cone_trans = Part.makeCone(70.0, 62.5, 15.0, App.Vector(0, dY_base + T_b, 0), App.Vector(0, 1, 0))
    bore_body = Part.makeCylinder(52.0, 62.0, App.Vector(0, dY_base + T_b, 0), App.Vector(0, 1, 0))
    cyl_body = cyl_body.fuse(cone_trans).cut(bore_body)

    # Tai kẹp xẻ rãnh góc -150 độ (hướng sang trái hơi chúc xuống)
    ang_lever = math.radians(-150.0)
    x_boss = 62.5 * math.cos(ang_lever)
    z_boss = 62.5 * math.sin(ang_lever)
    boss_cyl = Part.makeCylinder(15.0, 32.0, App.Vector(x_boss, dY_base + 35.0, z_boss), App.Vector(0, 1, 0))

    # Rãnh xẻ kẹp
    slot_box = Part.makeBox(40.0, 40.0, 3.5, App.Vector(-65.0, dY_base + 30.0, -1.75))
    rot_slot = App.Rotation(App.Vector(0, 1, 0), 30.0)
    slot_box.Placement = App.Placement(App.Vector(0, 0, 0), rot_slot)

    # Vú mỡ đối diện góc +35 độ
    ang_opp = math.radians(35.0)
    x_opp = 62.5 * math.cos(ang_opp)
    z_opp = 62.5 * math.sin(ang_opp)
    opp_boss = Part.makeCylinder(9.0, 20.0, App.Vector(x_opp, dY_base + 40.0, z_opp), App.Vector(0, 1, 0))
    grease_nipple = Part.makeCylinder(5.0, 12.0, App.Vector(x_opp, dY_base + 60.0, z_opp), App.Vector(0, 1, 0))

    body_solid = p_box.fuse(cyl_body).fuse(boss_cyl).fuse(opp_boss).fuse(grease_nipple).cut(slot_box)
    obj_body = doc.addObject("Part::Feature", f"{prefix}1_Than_Goi_Gang")
    obj_body.Shape = body_solid
    obj_body.Label = f"{prefix}1. Thân Bệ Bích Gang 16.5cm (Cổ Tròn D125mm, Tai Kẹp Xẻ Rãnh)"
    gan_mau(obj_body, (0.28, 0.35, 0.45), line_color=(0.12, 0.18, 0.25), line_width=1.8)
    objs.append(obj_body)

    # 2. 4 Bu-lông M14 kèm long đền
    bolts = []
    for xb in [-j_half, j_half]:
        for zb in [-j_half, j_half]:
            dY_b = dY_base - 25.0 if is_exploded else dY_base + T_b
            b_head = Part.makeCylinder(11.0, 10.0, App.Vector(xb, dY_b, zb), App.Vector(0, 1, 0))
            w_wash = Part.makeCylinder(14.0, 2.5, App.Vector(xb, dY_b - 2.5 if is_exploded else dY_base + T_b - 2.5, zb), App.Vector(0, 1, 0))
            b_shank = Part.makeCylinder(7.0, 25.0, App.Vector(xb, dY_b - 25.0, zb), App.Vector(0, 1, 0))
            bolts.append(b_head.fuse(w_wash).fuse(b_shank))
    obj_bolts = doc.addObject("Part::Feature", f"{prefix}2_4_BuLong_M14")
    obj_bolts.Shape = Part.makeCompound(bolts)
    obj_bolts.Label = f"{prefix}2. 4 Bu-lông M14 Bắt Mặt Máy (Kèm Long Đền D14)"
    gan_mau(obj_bolts, (0.92, 0.78, 0.25), line_color=(0.45, 0.35, 0.08), line_width=1.3)
    objs.append(obj_bolts)

    # 3. Vòng bi bạc đạn lòng cầu UC212 (Phi 60/110mm)
    Y_bear = dY_bearing + 45.0
    r_out = 55.0  # Phi 110
    r_in = 30.0   # Phi 60
    b_wid = 24.0
    out_ring = Part.makeCylinder(r_out, b_wid, App.Vector(0, Y_bear - b_wid / 2.0, 0), App.Vector(0, 1, 0)).cut(
        Part.makeCylinder(r_out - 8.0, b_wid + 4.0, App.Vector(0, Y_bear - b_wid / 2.0 - 2.0, 0), App.Vector(0, 1, 0))
    )
    in_ring = Part.makeCylinder(r_in + 8.0, b_wid, App.Vector(0, Y_bear - b_wid / 2.0, 0), App.Vector(0, 1, 0)).cut(
        Part.makeCylinder(r_in, b_wid + 4.0, App.Vector(0, Y_bear - b_wid / 2.0 - 2.0, 0), App.Vector(0, 1, 0))
    )
    balls = []
    for i in range(8):
        ang = i * (2.0 * math.pi / 8.0)
        bx = 42.5 * math.cos(ang)
        bz = 42.5 * math.sin(ang)
        ball = Part.makeSphere(6.5, App.Vector(bx, Y_bear, bz))
        balls.append(ball)
    seal_front = Part.makeCylinder(46.5, 2.0, App.Vector(0, Y_bear + b_wid / 2.0 - 2.0, 0), App.Vector(0, 1, 0)).cut(
        Part.makeCylinder(38.5, 4.0, App.Vector(0, Y_bear + b_wid / 2.0 - 3.0, 0), App.Vector(0, 1, 0))
    )
    seal_back = Part.makeCylinder(46.5, 2.0, App.Vector(0, Y_bear - b_wid / 2.0, 0), App.Vector(0, 1, 0)).cut(
        Part.makeCylinder(38.5, 4.0, App.Vector(0, Y_bear - b_wid / 2.0 - 1.0, 0), App.Vector(0, 1, 0))
    )
    solid_bearing = Part.makeCompound([out_ring, in_ring, seal_front, seal_back] + balls)
    obj_bearing = doc.addObject("Part::Feature", f"{prefix}3_Bac_Dan_UC212")
    obj_bearing.Shape = solid_bearing
    obj_bearing.Label = f"{prefix}3. Bạc Đạn Đỡ Trục Phi 60/110mm (8 Bi Cầu, Phớt Chắn Mỡ)"
    gan_mau(obj_bearing, (0.15, 0.68, 0.48), line_color=(0.06, 0.35, 0.22), line_width=1.8)
    objs.append(obj_bearing)

    # 4. Đoạn cốt láp bậc Phi 60mm có rãnh then
    Y_sh = dY_shaft + 45.0
    sh_cyl = Part.makeCylinder(30.0, 110.0, App.Vector(0, Y_sh - 45.0, 0), App.Vector(0, 1, 0))
    sh_key = Part.makeBox(18.0, 50.0, 9.0, App.Vector(-9.0, Y_sh, 23.0))
    sh_solid = sh_cyl.cut(sh_key)
    obj_sh = doc.addObject("Part::Feature", f"{prefix}4_Cot_Lap_Phi60")
    obj_sh.Shape = sh_solid
    obj_sh.Label = f"{prefix}4. Đoạn Cốt Láp Phi 60mm (Rãnh Then Cavet 18x11mm)"
    gan_mau(obj_sh, (0.90, 0.72, 0.22), line_color=(0.35, 0.25, 0.05), line_width=2.0)
    objs.append(obj_sh)

    # 5. Cổ siết lục giác ren ngoài S=105mm
    Y_h = dY_hex + 76.0
    pts_hex = []
    R_hex = 56.0
    for i in range(6):
        a = math.radians(i * 60.0 + 30.0)
        pts_hex.append(App.Vector(R_hex * math.cos(a), Y_h, R_hex * math.sin(a)))
    pts_hex.append(pts_hex[0])
    face_hex = Part.Face(Part.makePolygon(pts_hex))
    solid_hex = face_hex.extrude(App.Vector(0, 40.0, 0))
    bore_hex = Part.makeCylinder(43.5, 50.0, App.Vector(0, Y_h - 5.0, 0), App.Vector(0, 1, 0))
    solid_hex = solid_hex.cut(bore_hex)

    ring_thread = Part.makeCylinder(51.0, 20.0, App.Vector(0, Y_h - 18.0, 0), App.Vector(0, 1, 0)).cut(
        Part.makeCylinder(43.5, 25.0, App.Vector(0, Y_h - 20.0, 0), App.Vector(0, 1, 0))
    )
    solid_hex_ring = solid_hex.fuse(ring_thread)
    obj_hex = doc.addObject("Part::Feature", f"{prefix}5_Co_Luc_Giac_Ren")
    obj_hex.Shape = solid_hex_ring
    obj_hex.Label = f"{prefix}5. Cổ Siết Lục Giác Ren Ngoài S=105mm (Tịnh Tiến Khe Hở Trống)"
    gan_mau(obj_hex, (0.68, 0.72, 0.76), line_color=(0.35, 0.38, 0.42), line_width=1.6)
    objs.append(obj_hex)

    # 6. Cần gạt khóa nhanh bên hông
    v_arm = App.Vector(math.cos(ang_lever), 0, math.sin(ang_lever))
    p_arm_start = App.Vector(x_boss, dY_base + 50.0, z_boss) + v_arm * d_lever
    p_arm_end = p_arm_start + v_arm * 65.0
    arm_bar = Part.makeCylinder(6.0, 65.0, p_arm_start, v_arm)
    arm_knob = Part.makeSphere(12.0, p_arm_end)
    arm_paddle = Part.makeCylinder(10.0, 8.0, p_arm_end - App.Vector(0, 4.0, 0), App.Vector(0, 1, 0))
    solid_lever = arm_bar.fuse(arm_knob).fuse(arm_paddle)
    obj_lever = doc.addObject("Part::Feature", f"{prefix}6_Can_Khoa_Nhanh")
    obj_lever.Shape = solid_lever
    obj_lever.Label = f"{prefix}6. Cần Gạt Khóa Nhanh Chống Rung (Góc -150 Độ)"
    gan_mau(obj_lever, (0.10, 0.65, 0.45), line_color=(0.04, 0.35, 0.22), line_width=1.6)
    objs.append(obj_lever)

    # 7. Nắp tròn bịt đầu & 3 vít M4
    Y_c = dY_cap + 116.0
    cap_round = Part.makeCylinder(43.0, 8.0, App.Vector(0, Y_c, 0), App.Vector(0, 1, 0))
    cap_rim = Part.makeCylinder(40.0, 3.0, App.Vector(0, Y_c + 8.0, 0), App.Vector(0, 1, 0))
    cap_spigot = Part.makeCylinder(38.0, 6.0, App.Vector(0, Y_c - 6.0, 0), App.Vector(0, 1, 0))
    cap_screws = []
    for i in range(3):
        a_scr = math.radians(i * 120.0 + 30.0)
        xs = 32.5 * math.cos(a_scr)
        zs = 32.5 * math.sin(a_scr)
        scr = Part.makeCylinder(3.5, 4.0, App.Vector(xs, Y_c + 7.0, zs), App.Vector(0, 1, 0))
        cap_screws.append(scr)
    solid_cap_bolts = Part.makeCompound([cap_round, cap_rim, cap_spigot] + cap_screws)
    obj_cap = doc.addObject("Part::Feature", f"{prefix}7_Nap_Tron_Va_3_Vit_M4")
    obj_cap.Shape = solid_cap_bolts
    obj_cap.Label = f"{prefix}7. Nắp Tròn Bịt Đầu Chống Bụi (3 Vít M4, Chắn Vỏ Lụa Cà Phê)"
    gan_mau(obj_cap, (0.88, 0.75, 0.25), line_color=(0.45, 0.35, 0.08), line_width=1.4)
    objs.append(obj_cap)

    if plc_base is not None and plc_base != App.Placement():
        for ob in objs:
            if ob and hasattr(ob, "Placement"):
                ob.Placement = plc_base.multiply(ob.Placement)
    return objs


def tao_bo_chinh_6_chi_tiet(doc, plc_base=None, is_exploded=False, prefix=""):
    """
    MÔ HÌNH BỘ CHỈNH GỐI BI TRỤC PHI 60MM GỒM 6 CHI TIẾT THEO YÊU CẦU:
    1. Chân bệ cao 15cm (150mm), có 4 lỗ bắt bu-lông (đã bỏ 4 ốc màu), thân hình trụ, lòng có ren trong M110.
    2. Phần cố định có ren ngoài M110 gắn vào 1.
    3. Long đền / tán hãm lục giác để giữ chặt, vặn bằng lục giác 20cm (cờ lê 200mm).
    4. Phần trụ tròn nhẵn dày đúng 3mm nằm trong dùng để cố định bạc đạn.
    5. Bạc đạn đỡ trục phi 60mm nằm trong 4.
    6. Mặt bít (nắp bịt đầu ngoài).
    """
    objs = []

    H_chan = 150.0
    W_bich = 165.0
    T_bich = 16.0
    R_tru_out = 65.0
    R_ren_dinh = 55.0
    R_ren_day = 52.0

    L_ren2 = 115.0
    T_hex2 = 18.0
    R2_out_crest = R_ren_dinh - 0.5
    R2_out_root = R_ren_day + 0.5
    R2_in = 43.0

    T_nut = 5.0
    R_hex3 = 66.5  # S = 115mm

    R4_out = 43.0
    thick4 = 3.0
    R4_in = R4_out - thick4
    L4 = 65.0

    R5_out = 40.0
    R5_in = 30.0
    B5 = 22.0

    R6 = 52.0
    T_flange6 = 8.0
    T_spigot6 = 6.0

    # Tọa độ Y riêng biệt cho từng chi tiết (TÁCH XA NHAU RẤT RỘNG 15-20CM)
    if is_exploded:
        Y_base_1 = -600.0  # Chi tiết 1: -600 đến -450mm
        Y_nut    = -300.0  # Chi tiết 3: -300 đến -295mm (trên trục ren M110, cách 1: 150mm)
        Y_base_2 = -150.0  # Chi tiết 2: -150 đến -17mm (đầu lục giác to tại -35..-17mm, cách 3: 145mm)
        Y_4      = 150.0   # Chi tiết 4: 150 đến 215mm (cách 2: 167mm)
        Y_5      = 400.0   # Chi tiết 5: 400 đến 422mm (cách 4: 185mm)
        Y_6      = 620.0   # Chi tiết 6: 620 đến 628mm (cách 5: 198mm)
    else:
        Y_base_1 = 0.0     # Chi tiết 1: 0 đến 150mm (miệng ống tại Y = 150mm)
        Y_nut    = 150.0   # Chi tiết 3: 150 đến 155mm (Áp sát mặt miệng chân bệ, LỘ 100% RA NGOÀI!)
        Y_base_2 = 40.0    # Chi tiết 2: thân ren 40..155mm, đầu lục giác to S125 tại 155..173mm (kẹp sát long đền 3)
        Y_4      = 100.0   # Chi tiết 4: 100 đến 165mm (nằm trong lòng ống 2)
        Y_5      = 125.0   # Chi tiết 5: 125 đến 147mm (nằm trong ống 4)
        Y_6      = 173.0   # Chi tiết 6: 173 đến 181mm (Mặt bít nguyên khối đặc kín, gờ định vị 167..173mm)

    # 1. Chân bệ bích 4 lỗ + Thân trụ cao 15cm ren trong (BỎ 4 ỐC MÀU)
    p_bich = Part.makeBox(W_bich, T_bich, W_bich, App.Vector(-W_bich / 2.0, Y_base_1, -W_bich / 2.0))
    edges_Y = [e for e in p_bich.Edges if abs(e.tangentAt(0).y) > 0.9]
    p_bich = p_bich.makeFillet(15.0, edges_Y)

    for xb in [-65.0, 65.0]:
        for zb in [-65.0, 65.0]:
            h_bolt = Part.makeCylinder(7.25, T_bich + 10.0, App.Vector(xb, Y_base_1 - 5.0, zb), App.Vector(0, 1, 0))
            p_bich = p_bich.cut(h_bolt)

    cyl_tru = Part.makeCylinder(R_tru_out, H_chan - T_bich, App.Vector(0, Y_base_1 + T_bich, 0), App.Vector(0, 1, 0))
    cone_gan = Part.makeCone(R_tru_out + 10.0, R_tru_out, 20.0, App.Vector(0, Y_base_1 + T_bich, 0), App.Vector(0, 1, 0))
    bore_in = Part.makeCylinder(R_ren_day, H_chan + 20.0, App.Vector(0, Y_base_1 - 10.0, 0), App.Vector(0, 1, 0))

    chan_solid = p_bich.fuse(cyl_tru).fuse(cone_gan).cut(bore_in)

    for i in range(8):
        y_th = Y_base_1 + 40.0 + i * 12.0
        ring_groove = Part.makeCylinder(R_ren_dinh, 3.0, App.Vector(0, y_th, 0), App.Vector(0, 1, 0)).cut(
            Part.makeCylinder(R_ren_day - 1.0, 5.0, App.Vector(0, y_th - 1.0, 0), App.Vector(0, 1, 0))
        )
        chan_solid = chan_solid.cut(ring_groove)

    obj_1 = doc.addObject("Part::Feature", f"{prefix}1_Chan_Be_Tru_Ren_Trong")
    obj_1.Shape = chan_solid
    obj_1.Label = f"{prefix}1. Chân Bệ Trụ Ren Trong Cao 15cm (4 Lỗ Bắt Ốc, Bỏ Ốc Màu)"
    gan_mau(obj_1, (0.35, 0.40, 0.48), line_color=(0.15, 0.20, 0.28), line_width=1.8)
    objs.append(obj_1)

    # 2. Phần cố định ren ngoài M110: ĐẦU BÊN PHẢI LÀ LỤC GIÁC TO HƠN
    body2 = Part.makeCylinder(R2_out_root, L_ren2, App.Vector(0, Y_base_2, 0), App.Vector(0, 1, 0)).cut(
        Part.makeCylinder(R2_in, L_ren2 + 20.0, App.Vector(0, Y_base_2 - 10.0, 0), App.Vector(0, 1, 0))
    )
    threads2 = []
    for i in range(10):
        y_t2 = Y_base_2 + 8.0 + i * 9.0
        th_ring = Part.makeCylinder(R2_out_crest, 4.5, App.Vector(0, y_t2, 0), App.Vector(0, 1, 0)).cut(
            Part.makeCylinder(R2_out_root - 1.0, 6.0, App.Vector(0, y_t2 - 1.0, 0), App.Vector(0, 1, 0))
        )
        threads2.append(th_ring)

    # ĐẦU BÊN PHẢI: LỤC GIÁC TO HƠN (S = 125mm, R_hex = 72.2mm)
    Y_hex2 = Y_base_2 + L_ren2
    R_hex2 = 72.2  # S = 125mm
    pts_hex2 = []
    for i in range(6):
        a = math.radians(i * 60.0 + 30.0)
        pts_hex2.append(App.Vector(R_hex2 * math.cos(a), Y_hex2, R_hex2 * math.sin(a)))
    pts_hex2.append(pts_hex2[0])
    head_hex2 = Part.Face(Part.makePolygon(pts_hex2)).extrude(App.Vector(0, T_hex2, 0))
    head_hex2 = head_hex2.cut(Part.makeCylinder(R2_in, T_hex2 + 4.0, App.Vector(0, Y_hex2 - 2.0, 0), App.Vector(0, 1, 0)))

    for i in range(4):
        a_sc = math.radians(i * 90.0 + 45.0)
        xs = 47.0 * math.cos(a_sc)
        zs = 47.0 * math.sin(a_sc)
        head_hex2 = head_hex2.cut(Part.makeCylinder(2.5, 12.0, App.Vector(xs, Y_hex2 + T_hex2 - 10.0, zs), App.Vector(0, 1, 0)))

    solid_2 = Part.makeCompound([body2, head_hex2] + threads2)
    obj_2 = doc.addObject("Part::Feature", f"{prefix}2_Ong_Co_Dinh_Ren_Ngoai")
    obj_2.Shape = solid_2
    obj_2.Label = f"{prefix}2. Phần Cố Định Ren Ngoài M110 (Đầu Phải Lục Giác To S125)"
    gan_mau(obj_2, (0.12, 0.55, 0.82), line_color=(0.05, 0.30, 0.50), line_width=1.6)
    objs.append(obj_2)

    # 3. Long đền mỏng chỉ cần 5mm (ĐÃ XÓA CÂY CÙI TRÒN, LỘ 100% RA NGOÀI)
    pts_hex3 = []
    for i in range(6):
        a = math.radians(i * 60.0 + 30.0)
        pts_hex3.append(App.Vector(R_hex3 * math.cos(a), Y_nut, R_hex3 * math.sin(a)))
    pts_hex3.append(pts_hex3[0])
    solid_hex3 = Part.Face(Part.makePolygon(pts_hex3)).extrude(App.Vector(0, T_nut, 0))
    solid_hex3 = solid_hex3.cut(Part.makeCylinder(R_ren_dinh + 0.5, T_nut + 4.0, App.Vector(0, Y_nut - 2.0, 0), App.Vector(0, 1, 0)))

    obj_3 = doc.addObject("Part::Feature", f"{prefix}3_Long_Den_Tan_Khoa_Luc_Giac_20cm")
    obj_3.Shape = solid_hex3
    obj_3.Label = f"{prefix}3. Long Đền Hãm Mỏng 5mm (Đã Xóa Cây Cùi Tròn)"
    gan_mau(obj_3, (0.90, 0.42, 0.15), line_color=(0.50, 0.20, 0.05), line_width=1.8)
    objs.append(obj_3)

    # 4. Phần trụ tròn nhẵn dày đúng 3mm nằm trong
    cyl4_out = Part.makeCylinder(R4_out, L4, App.Vector(0, Y_4, 0), App.Vector(0, 1, 0))
    cyl4_in = Part.makeCylinder(R4_in, L4 + 10.0, App.Vector(0, Y_4 - 5.0, 0), App.Vector(0, 1, 0))
    go_chan = Part.makeCylinder(R4_in, 5.0, App.Vector(0, Y_4, 0), App.Vector(0, 1, 0)).cut(
        Part.makeCylinder(31.0, 7.0, App.Vector(0, Y_4 - 1.0, 0), App.Vector(0, 1, 0))
    )
    solid_4 = cyl4_out.cut(cyl4_in).fuse(go_chan)

    obj_4 = doc.addObject("Part::Feature", f"{prefix}4_Ong_Tru_Tron_Nhan_3mm")
    obj_4.Shape = solid_4
    obj_4.Label = f"{prefix}4. Ống Trụ Tròn Nhẵn Dày 3mm (Cố Định Bạc Đạn Bên Trong)"
    gan_mau(obj_4, (0.15, 0.72, 0.52), line_color=(0.06, 0.40, 0.25), line_width=1.6)
    objs.append(obj_4)

    # 5. Bạc đạn đỡ trục phi 60mm ở trong 4
    out_ring5 = Part.makeCylinder(R5_out, B5, App.Vector(0, Y_5, 0), App.Vector(0, 1, 0)).cut(
        Part.makeCylinder(R5_out - 4.0, B5 + 4.0, App.Vector(0, Y_5 - 2.0, 0), App.Vector(0, 1, 0))
    )
    in_ring5 = Part.makeCylinder(R5_in + 4.0, B5, App.Vector(0, Y_5, 0), App.Vector(0, 1, 0)).cut(
        Part.makeCylinder(R5_in, B5 + 4.0, App.Vector(0, Y_5 - 2.0, 0), App.Vector(0, 1, 0))
    )
    balls5 = []
    for i in range(10):
        ang = i * (2.0 * math.pi / 10.0)
        bx = 35.0 * math.cos(ang)
        bz = 35.0 * math.sin(ang)
        balls5.append(Part.makeSphere(4.0, App.Vector(bx, Y_5 + B5 / 2.0, bz)))

    seal5_front = Part.makeCylinder(R5_out - 1.0, 1.5, App.Vector(0, Y_5 + B5 - 1.5, 0), App.Vector(0, 1, 0)).cut(
        Part.makeCylinder(R5_in + 3.0, 3.0, App.Vector(0, Y_5 + B5 - 2.0, 0), App.Vector(0, 1, 0))
    )
    seal5_back = Part.makeCylinder(R5_out - 1.0, 1.5, App.Vector(0, Y_5, 0), App.Vector(0, 1, 0)).cut(
        Part.makeCylinder(R5_in + 3.0, 3.0, App.Vector(0, Y_5 - 0.5, 0), App.Vector(0, 1, 0))
    )
    solid_5 = Part.makeCompound([out_ring5, in_ring5, seal5_front, seal5_back] + balls5)

    obj_5 = doc.addObject("Part::Feature", f"{prefix}5_Bac_Dan_Trong_4")
    obj_5.Shape = solid_5
    obj_5.Label = f"{prefix}5. Bạc Đạn Đỡ Trục Phi 60mm (Lắp Trong Ống Tròn 4)"
    gan_mau(obj_5, (0.92, 0.75, 0.22), line_color=(0.45, 0.35, 0.08), line_width=1.8)
    objs.append(obj_5)

    # 6. Mặt bít NGUYÊN KHỐI (Solid End Cap - Đặc kín 100%, không thủng lỗ giữa)
    flange_bit = Part.makeCylinder(R6, T_flange6, App.Vector(0, Y_6, 0), App.Vector(0, 1, 0))
    spigot_bit = Part.makeCylinder(R2_in - 0.5, T_spigot6, App.Vector(0, Y_6 - T_spigot6, 0), App.Vector(0, 1, 0))
    solid_6 = flange_bit.fuse(spigot_bit)

    for i in range(4):
        a_sc = math.radians(i * 90.0 + 45.0)
        xs = 47.0 * math.cos(a_sc)
        zs = 47.0 * math.sin(a_sc)
        hole_sc = Part.makeCylinder(3.25, T_flange6 + 4.0, App.Vector(xs, Y_6 - 2.0, zs), App.Vector(0, 1, 0))
        cbore_sc = Part.makeCylinder(5.5, 4.0, App.Vector(xs, Y_6 + T_flange6 - 3.5, zs), App.Vector(0, 1, 0))
        solid_6 = solid_6.cut(hole_sc).cut(cbore_sc)

    obj_6 = doc.addObject("Part::Feature", f"{prefix}6_Mat_Bit")
    obj_6.Shape = solid_6
    obj_6.Label = f"{prefix}6. Mặt Bít Nguyên Khối (Đặc Kín Chắn Bụi & Chặn Bạc Đạn)"
    gan_mau(obj_6, (0.65, 0.70, 0.76), line_color=(0.30, 0.35, 0.40), line_width=1.6)
    objs.append(obj_6)

    if plc_base is not None and plc_base != App.Placement():
        for ob in objs:
            if ob and hasattr(ob, "Placement"):
                ob.Placement = plc_base.multiply(ob.Placement)

    return objs


def tao_tab_3_bo_chinh(doc):
    """
    Tạo tài liệu Tab 3 gồm 2 phần rõ rệt (Bộ Chỉnh Gối Bi Trục Phi 60mm Mới 6 Chi Tiết):
    - Phần 1 (Bên Trái - X = -280mm): Chi tiết tháo rời 6 linh kiện (Exploded View).
    - Phần 2 (Bên Phải - X = +280mm): Cụm lắp ráp hoàn chỉnh 100% (Assembled View).
    """
    plc_exploded = App.Placement(App.Vector(-280.0, 0, 0), App.Rotation())
    plc_assembled = App.Placement(App.Vector(280.0, 0, 0), App.Rotation())

    objs_exp = tao_bo_chinh_6_chi_tiet(doc, plc_base=plc_exploded, is_exploded=True, prefix="1_Thao_Roi_")
    objs_asm = tao_bo_chinh_6_chi_tiet(doc, plc_base=plc_assembled, is_exploded=False, prefix="2_Lap_Rap_")

    return objs_exp + objs_asm


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
    # 1. VỎ TRỐNG TRONG HÌNH TRỤ SẮT (D80cm x L1m x DÀY 0.8cm)
    #    - Yêu cầu: Giữ nguyên trống 100cm, dời 2 mặt máy ra xa nhau thêm 10cm (lọt lòng 110cm)
    #    - Đầu trước áp sát mặt máy trước, chừa lại 0.5mm: Y_drum_start = -500.0 + 0.5 = -499.5mm
    #    - Chiều dài trống: 1000mm (Y = -499.5 đến +500.5mm)
    #    - Mặt sau còn lại đúng 9.95cm (99.5mm): mặt máy sau đặt tại Y = +500.5 + 99.5 = +600.0mm!
    # -------------------------------------------------------------
    chieu_dai = 1000.0   # 1m = 100cm
    r_ngoai = 400.0      # Ngang 80cm -> R = 400mm
    do_day = 8.0         # Dày 0.8cm = 8mm
    r_trong = r_ngoai - do_day  # 392mm
    Y_drum_start = -499.5  # Đầu trước cách mặt máy trước (-500) đúng 0.5mm chống cạ

    cyl_out = Part.makeCylinder(r_ngoai, chieu_dai, App.Vector(0, Y_drum_start, 0), App.Vector(0, 1, 0))
    cyl_in = Part.makeCylinder(r_trong, chieu_dai + 20.0, App.Vector(0, Y_drum_start - 10.0, 0), App.Vector(0, 1, 0))
    hinh_trong = cyl_out.cut(cyl_in)

    obj_trong = doc.addObject("Part::Feature", "Trong_Hinh_Tru_Sat")
    obj_trong.Shape = hinh_trong
    obj_trong.Label = "1. Vỏ Trống Trong (D80cm x L1m x Dày 0.8cm, Hở Trước 0.5mm)"
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

    cyl_ao_out = Part.makeCylinder(r_ao_out, chieu_dai, App.Vector(0, Y_drum_start, 0), App.Vector(0, 1, 0))
    cyl_ao_in = Part.makeCylinder(r_ao_in, chieu_dai + 20.0, App.Vector(0, Y_drum_start - 10.0, 0), App.Vector(0, 1, 0))
    hinh_ao = cyl_ao_out.cut(cyl_ao_in)

    obj_ao_ngoai = doc.addObject("Part::Feature", "Lop_Ao_Trong_Ngoai_Cach_Khi")
    obj_ao_ngoai.Shape = hinh_ao
    obj_ao_ngoai.Label = "1b. Lớp Áo Trống Ngoài (D83cm x Dày 0.5cm, Hở Khí 1cm)"
    # Để độ trong suốt 55% để nhìn rõ lớp đệm khí 1cm và vỏ trống trong
    gan_mau(obj_ao_ngoai, (0.70, 0.75, 0.82), do_trong_suot=55, line_color=(0.15, 0.20, 0.30), line_width=1.5)

    # -------------------------------------------------------------
    # 1c. TẤM SẮT TRÒN ĐÁY SAU TRỐNG RANG: LỌT LÒNG VÒNG TRÒN NHỎ (D78.4CM, DÀY 8MM, LỖ D65MM)
    #    - Khớp chính xác với vòng tròn NHỎ bên trong (Vỏ trống trong Rin = 392mm -> D = 784mm = 78.4cm)
    #    - Thụt vào trong lòng trống 8mm (bằng đúng chiều dày đĩa) tạo gờ mép bảo vệ và khe hàn góc âm
    #    - Khoét lỗ xuyên tâm phi 65mm (R = 32.5mm) xỏ khít qua thân cây láp chính phi 65mm
    #    - Mối hàn ngấu:
    #      + Vành hàn cổ trục: Fillet collar ôm cốt láp phi 65mm (R = 32.5 -> 38mm, dày 4mm)
    #      + Vành hàn mép chu vi trong: Fillet seam ôm khít thành trong trống (R = 386 -> 392mm, dày 4mm)
    #    - Vị trí trục Y: Nằm từ Y = 484.5mm đến Y = 496.5mm (thụt vào trong lòng trống so với mép đuôi 500.5mm)
    #    - Khoảng cách từ đuôi trống đến mặt máy sau (+600.0mm) bảo toàn chuẩn xác 9.95cm (99.5mm)!
    # -------------------------------------------------------------
    Y_drum_end = Y_drum_start + chieu_dai  # +500.5mm
    T_day = 8.0
    recess = 5.0
    Y_day_out = Y_drum_end - recess       # 495.5mm
    Y_day_in = Y_day_out - T_day          # 487.5mm
    r_shaft = 32.5                        # Bán kính thân cây láp phi 65mm

    # Đĩa sắt tròn chính lọt lòng
    cyl_day_out = Part.makeCylinder(r_trong, T_day, App.Vector(0, Y_day_in, 0), App.Vector(0, 1, 0))
    cyl_day_in = Part.makeCylinder(r_shaft, T_day + 10.0, App.Vector(0, Y_day_in - 5.0, 0), App.Vector(0, 1, 0))
    dia_chinh = cyl_day_out.cut(cyl_day_in)

    # Vành hàn ngấu cổ trục (fillet weld collar quanh cốt láp)
    weld_shaft_out = Part.makeCylinder(38.0, 4.0, App.Vector(0, Y_day_out, 0), App.Vector(0, 1, 0))
    weld_shaft_in = Part.makeCylinder(r_shaft, 6.0, App.Vector(0, Y_day_out - 1.0, 0), App.Vector(0, 1, 0))
    co_han_truc = weld_shaft_out.cut(weld_shaft_in)

    # Vành hàn ngấu mép chu vi trong (fillet weld seam)
    weld_rim_out = Part.makeCylinder(r_trong, 4.0, App.Vector(0, Y_day_out, 0), App.Vector(0, 1, 0))
    weld_rim_in = Part.makeCylinder(r_trong - 6.0, 6.0, App.Vector(0, Y_day_out - 1.0, 0), App.Vector(0, 1, 0))
    vanh_han_mep = weld_rim_out.cut(weld_rim_in)

    hinh_day_sau = Part.makeCompound([dia_chinh, co_han_truc, vanh_han_mep])

    obj_day_sau = doc.addObject("Part::Feature", "Day_Trong_Sau_Sat_Tron_Lot_Long")
    obj_day_sau.Shape = hinh_day_sau
    obj_day_sau.Label = "1c. Tấm Sắt Tròn Đáy Sau Trống (D78.4cm x Dày 0.8cm Lọt Lòng, Lỗ D65mm, Hàn Góc Âm)"
    gan_mau(obj_day_sau, (0.75, 0.78, 0.82), line_color=(0.20, 0.25, 0.35), line_width=1.8, do_trong_suot=45)

    # -------------------------------------------------------------
    # 2. CÂY LÁP (TRỤC BẬC) DÀI 1M3, THÂN PHI 65MM, 2 ĐẦU PHI 60MM X 10CM
    # -------------------------------------------------------------
    shapes_lap = []
    # Đầu 1: phi 60mm (R = 30mm), dài 100mm (10cm) tại Y: -600 đến -500 (nhô ra 82mm ngoài mặt trước)
    dau_1 = Part.makeCylinder(30.0, 100.0, App.Vector(0, -600.0, 0), App.Vector(0, 1, 0))
    # Thân giữa (Cây Trụ Chính): phi 65mm (R = 32.5mm), dài 1100mm tại Y: -500 đến +600
    than_giua = Part.makeCylinder(32.5, 1100.0, App.Vector(0, -500.0, 0), App.Vector(0, 1, 0))
    # Đầu 2: phi 60mm (R = 30mm), dài 100mm (10cm) tại Y: +600 đến +700 (nhô ra 82mm ngoài mặt sau)
    dau_2 = Part.makeCylinder(30.0, 100.0, App.Vector(0, 600.0, 0), App.Vector(0, 1, 0))

    shapes_lap.extend([dau_1, than_giua, dau_2])
    hinh_lap = Part.makeCompound(shapes_lap)

    obj_lap = doc.addObject("Part::Feature", "Cay_Lap_Truc_Bac")
    obj_lap.Shape = hinh_lap
    obj_lap.Label = "2. Cây Láp Trục Bậc (L1m3, Thân D65mm, 2 Đầu D60mm x 10cm)"
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

    W_half_bot = 550.0   # Nửa chiều rộng đáy dưới = 550mm -> Đáy dưới rộng 1100mm (1.1m)
    Z_bottom = -850.0    # Đáy dưới phẳng tại Z = -850mm tiếp xúc mặt sàn vững chãi
    Z_step = Z_bottom + 55.0  # -795.0mm (Gờ chân đứng cao 5.5cm = 55mm)

    # Chân mặt máy trước theo Phương án C.2 (C chuẩn + Gờ đứng 5.5cm):
    # 1. Từ eo thắt (X = ±367.7mm) vát chéo thẳng ra mép biên X = ±550mm tại cao độ Z_step = -795mm (cách chân 5.5cm)
    # 2. Từ cao độ Z_step bẻ góc vuông thẳng đứng xuống sàn Z_bottom = -850mm tạo gờ chân cao đúng 5.5cm
    # 3. Đáy phẳng rộng 1100mm (1.1m) tiếp xúc vững chãi với bệ chân đế máy
    arc = Part.Arc(
        App.Vector(x_tR, Y_mat, z_tR),
        App.Vector(0, Y_mat, R_mat),
        App.Vector(x_tL, Y_mat, z_tL)
    )
    edge_arc = arc.toShape()
    edge_L_slant = Part.makeLine(App.Vector(x_tL, Y_mat, z_tL), App.Vector(-W_half_bot, Y_mat, Z_step))
    edge_L_foot = Part.makeLine(App.Vector(-W_half_bot, Y_mat, Z_step), App.Vector(-W_half_bot, Y_mat, Z_bottom))
    edge_bot = Part.makeLine(App.Vector(-W_half_bot, Y_mat, Z_bottom), App.Vector(W_half_bot, Y_mat, Z_bottom))
    edge_R_foot = Part.makeLine(App.Vector(W_half_bot, Y_mat, Z_bottom), App.Vector(W_half_bot, Y_mat, Z_step))
    edge_R_slant = Part.makeLine(App.Vector(W_half_bot, Y_mat, Z_step), App.Vector(x_tR, Y_mat, z_tR))

    wire_mat = Part.Wire([edge_arc, edge_L_slant, edge_L_foot, edge_bot, edge_R_foot, edge_R_slant])
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

    # Khoét lỗ nạp liệu chữ nhật 20x30cm (ngang 30cm theo trục X, cao 20cm theo trục Z) ĐẨY LÊN CAO TỐI ĐA TRÊN MẶT TRƯỚC:
    # - Bề rộng ngang: W = 300mm (X từ -150 đến +150mm đối xứng qua tâm máy)
    # - Chiều cao đứng: H = 200mm (Đẩy lên cao nhất có thể: Z từ +155 đến +355mm)
    # - Tại 2 góc trên (X = ±150mm, Z = 355mm): Bán kính góc R = 385.4mm < Rin = 392mm (cách vành trong trống đúng 6.6mm)
    # - Nằm cao cách xa miệng ra hàng phía dưới (>35cm) và lỗ thăm hàng (Z=0)
    W_lo_nap = 300.0
    H_lo_nap = 200.0
    half_W_lo_nap = W_lo_nap / 2.0
    Z_bot_lo_nap = 155.0  # Đỉnh lỗ đạt Z = 355mm (sát kịch trần vòm trống)
    cutter_lo_nap_truoc = Part.makeBox(
        W_lo_nap,
        T_mat + 20.0,
        H_lo_nap,
        App.Vector(-half_W_lo_nap, Y_mat - 10.0, Z_bot_lo_nap)
    )
    hinh_mat_truoc = hinh_mat_truoc.cut(cutter_lo_nap_truoc)

    obj_mat_truoc = doc.addObject("Part::Feature", "Mat_May_Truoc_Ga_Trong_18mm")
    obj_mat_truoc.Shape = hinh_mat_truoc
    obj_mat_truoc.Label = "6. Mặt Máy Trước Gá Trống (Sắt 1.8cm, D96cm, Chân Vát Gờ Đứng 5.5cm Đáy 1.1m, Lỗ D65mm, Lỗ Nạp 20x30cm, Miệng Xả 50cm, Lỗ Thăm D30mm)"
    # Màu xám xanh thép công nghiệp dày dặn
    gan_mau(obj_mat_truoc, (0.28, 0.35, 0.45), line_color=(0.10, 0.15, 0.25), line_width=2.0)

    # -------------------------------------------------------------
    # 6b. CỤM MIỆNG RA HÀNG LẮP RỜI 3 PHẦN (INOX 1.5MM, BẺ GÓC TÙ 120°, 2 VÁCH BO R30MM, 2 THANH LA 4 ỐC M8)
    #     - Thiết kế module cơ động tháo lắp độc lập:
    #       1. Tấm đáy Inox 1.5mm bo theo cung miệng khoét R392mm (cách vành trống đúng 0.1mm),
    #          bẻ góc tù 120° (dốc 30° chúc xuống đất) vươn dài 120mm cho cà phê trôi tuột 100% rơi xuống thau làm nguội.
    #       2. Hai vách hông Inox 1.5mm dựng tại X = ±250mm, cao 100mm, bo tròn phía trên R30mm (tiếp tuyến G1), vát dốc 30°.
    #       3. Hai thanh la bản 30x5mm (dài 140mm) khoan 2 lỗ phi 10mm bắt bằng 4 bu-lông M8 cố định vào mặt máy sắt 18mm.
    # -------------------------------------------------------------
    GAP_CHUTE = 0.1
    T_INOX_CHUTE = 1.5
    R_chute_out = R_drum_in - GAP_CHUTE       # 391.9mm
    R_chute_in = R_chute_out - T_INOX_CHUTE   # 390.4mm
    z_chute_in_edge = -math.sqrt(R_chute_in**2 - half_W_m**2)

    # Đoạn 1 đáy: Xuyên qua mặt máy từ Y = -500.1mm đến Y = -518.0mm
    arc_chute_top1 = Part.Arc(
        App.Vector(-half_W_m, -500.1, z_edge_m),
        App.Vector(0.0, -500.1, -R_chute_out),
        App.Vector(half_W_m, -500.1, z_edge_m)
    )
    arc_chute_bot1 = Part.Arc(
        App.Vector(half_W_m, -500.1, z_chute_in_edge),
        App.Vector(0.0, -500.1, -R_chute_in),
        App.Vector(-half_W_m, -500.1, z_chute_in_edge)
    )
    edge_chute_L1 = Part.makeLine(App.Vector(-half_W_m, -500.1, z_chute_in_edge), App.Vector(-half_W_m, -500.1, z_edge_m))
    edge_chute_R1 = Part.makeLine(App.Vector(half_W_m, -500.1, z_edge_m), App.Vector(half_W_m, -500.1, z_chute_in_edge))
    wire_sec_chute1 = Part.Wire([arc_chute_top1.toShape(), edge_chute_R1, arc_chute_bot1.toShape(), edge_chute_L1])
    solid_chute_seg1 = Part.Face(wire_sec_chute1).extrude(App.Vector(0.0, -17.9, 0.0))

    # Đoạn 2 đáy: Bẻ góc tù 120° (dốc 30° chúc xuống) vươn xiên 120mm
    # Vector tịnh tiến dốc 30°: v_ext = (0, -120*cos(30°), -120*sin(30°))
    L_chute_out = 120.0
    dY_chute_out = -L_chute_out * math.cos(math.radians(30.0))   # -103.923mm
    dZ_chute_out = -L_chute_out * math.sin(math.radians(30.0))   # -60.000mm
    v_ext_chute = App.Vector(0.0, dY_chute_out, dZ_chute_out)

    arc_chute_top2 = Part.Arc(
        App.Vector(-half_W_m, Y_mat, z_edge_m),
        App.Vector(0.0, Y_mat, -R_chute_out),
        App.Vector(half_W_m, Y_mat, z_edge_m)
    )
    arc_chute_bot2 = Part.Arc(
        App.Vector(half_W_m, Y_mat, z_chute_in_edge),
        App.Vector(0.0, Y_mat, -R_chute_in),
        App.Vector(-half_W_m, Y_mat, z_chute_in_edge)
    )
    edge_chute_L2 = Part.makeLine(App.Vector(-half_W_m, Y_mat, z_chute_in_edge), App.Vector(-half_W_m, Y_mat, z_edge_m))
    edge_chute_R2 = Part.makeLine(App.Vector(half_W_m, Y_mat, z_edge_m), App.Vector(half_W_m, Y_mat, z_chute_in_edge))
    wire_sec_chute2 = Part.Wire([arc_chute_top2.toShape(), edge_chute_R2, arc_chute_bot2.toShape(), edge_chute_L2])
    solid_chute_seg2 = Part.Face(wire_sec_chute2).extrude(v_ext_chute)

    solid_chute_floor = solid_chute_seg1.fuse(solid_chute_seg2)
    obj_chute_floor = doc.addObject("Part::Feature", "Mieng_Ra_Hang_Day_Inox_1p5mm")
    obj_chute_floor.Shape = solid_chute_floor
    obj_chute_floor.Label = "6b1. Tấm Đáy Miệng Ra Hàng Inox 1.5mm (Bo Cung R392 Cách Trống 0.1mm, Bẻ Góc Tù 120° Dốc 30°)"
    gan_mau(obj_chute_floor, (0.84, 0.88, 0.93), line_color=(0.10, 0.20, 0.35), line_width=1.8)

    # Phần 2: Hai vách hông Inox 1.5mm bo tròn trên R30mm & vát dốc 30°
    R_bo_vach = 30.0
    Y_c_bo = Y_mat - 32.0   # -550.0mm
    Z_c_bo = z_top_m - R_bo_vach
    P_start_bo = App.Vector(0.0, Y_c_bo, z_top_m)
    P_mid_bo = App.Vector(0.0, Y_c_bo + R_bo_vach * math.cos(math.radians(105.0)), Z_c_bo + R_bo_vach * math.sin(math.radians(105.0)))
    P_end_bo = App.Vector(0.0, Y_c_bo + R_bo_vach * math.cos(math.radians(120.0)), Z_c_bo + R_bo_vach * math.sin(math.radians(120.0)))
    arc_bo_vach = Part.Arc(P_start_bo, P_mid_bo, P_end_bo).toShape()

    edge_v1 = Part.makeLine(App.Vector(0.0, Y_mat, z_edge_m), App.Vector(0.0, Y_mat, z_top_m))
    edge_v2 = Part.makeLine(App.Vector(0.0, Y_mat, z_top_m), P_start_bo)
    edge_v3 = arc_bo_vach
    edge_v4 = Part.makeLine(P_end_bo, App.Vector(0.0, Y_mat + dY_chute_out, z_edge_m + dZ_chute_out + 30.0))
    edge_v5 = Part.makeLine(App.Vector(0.0, Y_mat + dY_chute_out, z_edge_m + dZ_chute_out + 30.0), App.Vector(0.0, Y_mat + dY_chute_out, z_edge_m + dZ_chute_out))
    edge_v6 = Part.makeLine(App.Vector(0.0, Y_mat + dY_chute_out, z_edge_m + dZ_chute_out), App.Vector(0.0, Y_mat, z_edge_m))
    wire_vach_base = Part.Wire([edge_v1, edge_v2, edge_v3, edge_v4, edge_v5, edge_v6])

    # Vách hông trái tại X = -half_W_m (-250mm) extrude ra ngoài -1.5mm
    face_vach_L = Part.Face(wire_vach_base)
    face_vach_L.translate(App.Vector(-half_W_m, 0.0, 0.0))
    solid_vach_L = face_vach_L.extrude(App.Vector(-T_INOX_CHUTE, 0.0, 0.0))

    # Vách hông phải tại X = +half_W_m (+250mm) extrude ra ngoài +1.5mm
    face_vach_R = Part.Face(wire_vach_base)
    face_vach_R.translate(App.Vector(half_W_m, 0.0, 0.0))
    solid_vach_R = face_vach_R.extrude(App.Vector(T_INOX_CHUTE, 0.0, 0.0))

    obj_chute_vach = doc.addObject("Part::Feature", "Mieng_Ra_Hang_2_Vach_Hong_Inox")
    obj_chute_vach.Shape = Part.makeCompound([solid_vach_L, solid_vach_R])
    obj_chute_vach.Label = "6b2. Hai Tấm Vách Hông Inox (Cao 100mm, Bo Tròn Phía Trên R30mm Tiếp Tuyến G1, Vát Dốc 30°)"
    gan_mau(obj_chute_vach, (0.78, 0.83, 0.89), line_color=(0.10, 0.20, 0.35), line_width=1.8)

    # Phần 3: Hai thanh la bản 30x5mm (dài 140mm) khoan 2 lỗ phi 10mm & 4 bu-lông M8
    W_la_chute = 30.0
    T_la_chute = 5.0
    L_la_chute = 140.0
    z_la_mid = (z_top_m + z_edge_m) / 2.0   # -251.93mm
    z_hole1 = z_la_mid + 35.0               # -216.93mm (khoảng cách 70mm)
    z_hole2 = z_la_mid - 35.0               # -286.93mm

    box_la_L = Part.makeBox(W_la_chute, T_la_chute, L_la_chute, App.Vector(-half_W_m - W_la_chute, Y_mat - T_la_chute, z_la_mid - L_la_chute / 2.0))
    h1_L = Part.makeCylinder(5.0, T_la_chute + 10.0, App.Vector(-half_W_m - W_la_chute / 2.0, Y_mat - T_la_chute - 5.0, z_hole1), App.Vector(0, 1, 0))
    h2_L = Part.makeCylinder(5.0, T_la_chute + 10.0, App.Vector(-half_W_m - W_la_chute / 2.0, Y_mat - T_la_chute - 5.0, z_hole2), App.Vector(0, 1, 0))
    solid_la_L = box_la_L.cut(h1_L).cut(h2_L)

    box_la_R = Part.makeBox(W_la_chute, T_la_chute, L_la_chute, App.Vector(half_W_m, Y_mat - T_la_chute, z_la_mid - L_la_chute / 2.0))
    h1_R = Part.makeCylinder(5.0, T_la_chute + 10.0, App.Vector(half_W_m + W_la_chute / 2.0, Y_mat - T_la_chute - 5.0, z_hole1), App.Vector(0, 1, 0))
    h2_R = Part.makeCylinder(5.0, T_la_chute + 10.0, App.Vector(half_W_m + W_la_chute / 2.0, Y_mat - T_la_chute - 5.0, z_hole2), App.Vector(0, 1, 0))
    solid_la_R = box_la_R.cut(h1_R).cut(h2_R)

    obj_chute_la = doc.addObject("Part::Feature", "Mieng_Ra_Hang_2_Thanh_La_Bat_Oc")
    obj_chute_la.Shape = Part.makeCompound([solid_la_L, solid_la_R])
    obj_chute_la.Label = "6b3. Hai Thanh La Gá Bản 30x5mm Khoan 2 Lỗ Phi 10mm Bắt Ốc Cố Định Vào Mặt Máy"
    gan_mau(obj_chute_la, (0.35, 0.40, 0.48), line_color=(0.10, 0.15, 0.20), line_width=1.5)

    # 4 Bu-lông M8 cố định cụm máng vào mặt máy 18mm
    chute_bolts = []
    for x_b in [-half_W_m - W_la_chute / 2.0, half_W_m + W_la_chute / 2.0]:
        for z_b in [z_hole1, z_hole2]:
            shank_b = Part.makeCylinder(4.0, T_la_chute + 16.0, App.Vector(x_b, Y_mat - T_la_chute, z_b), App.Vector(0, 1, 0))
            head_b = Part.makeCylinder(6.5, 5.5, App.Vector(x_b, Y_mat - T_la_chute - 5.5, z_b), App.Vector(0, 1, 0))
            chute_bolts.append(head_b.fuse(shank_b))

    obj_chute_bolts = doc.addObject("Part::Feature", "Mieng_Ra_Hang_4_BuLong_M8")
    obj_chute_bolts.Shape = Part.makeCompound(chute_bolts)
    obj_chute_bolts.Label = "6b4. 4 Bu-lông Lục Giác M8 Cố Định Cụm Miệng Ra Hàng Vào Mặt Máy 18mm"
    gan_mau(obj_chute_bolts, (0.85, 0.70, 0.20), line_color=(0.45, 0.35, 0.05), line_width=1.2)

    # -------------------------------------------------------------
    # 6c. CÁNH CỬA XẢ SẮT 18MM (THU NHỎ 1MM ĐỀU) & Ô KÍNH QUAN SÁT 10CM CHÍNH GIỮA CỬA
    #     - Cánh cửa xả: Tái sử dụng chính phôi sắt tấm 1.8cm cắt ra từ miệng khoét mặt máy trước.
    #     - Kích thước thu nhỏ đúng 1.0mm đều xung quanh (khe hở cắt CNC 1mm) để đóng mở êm ái:
    #       + Mép trên: Z = -202.93mm (gốc -201.93mm)
    #       + Cạnh bên: X = ±249.0mm (gốc ±250.0mm -> rộng 498mm)
    #       + Đáy uốn cong: R = 391.0mm (gốc 392.0mm)
    #     - Ô kính thạch anh chịu nhiệt 10cm: Lỗ tròn phi 100mm nằm ngay trọng tâm hình học của cửa
    #       tại X = 0.0, Z = -297.0mm, đĩa kính phi 100mm dày 8mm đặt âm giữa chiều dày cửa,
    #       kèm vành Inox 304 kẹp giữ kính ngoài phi 124mm x 3mm và 4 vít chìm M5.
    #     - 2 Bản lề cối phi 20mm bên trái (mở ngang 120°) và tay khóa chữ L bên phải.
    # -------------------------------------------------------------
    CLEARANCE_DOOR = 1.0
    half_W_door = half_W_m - CLEARANCE_DOOR   # 249.0mm
    z_top_door = z_top_m - CLEARANCE_DOOR      # -202.93mm
    R_arc_door = R_drum_in - CLEARANCE_DOOR    # 391.0mm
    z_edge_door = -math.sqrt(R_arc_door**2 - half_W_door**2) # -301.46mm

    # Biên dạng cánh cửa sắt 18mm
    arc_door = Part.Arc(
        App.Vector(-half_W_door, Y_mat, z_edge_door),
        App.Vector(0.0, Y_mat, -R_arc_door),
        App.Vector(half_W_door, Y_mat, z_edge_door)
    )
    edge_arc_d = arc_door.toShape()
    edge_R_d = Part.makeLine(App.Vector(half_W_door, Y_mat, z_edge_door), App.Vector(half_W_door, Y_mat, z_top_door))
    edge_top_d = Part.makeLine(App.Vector(half_W_door, Y_mat, z_top_door), App.Vector(-half_W_door, Y_mat, z_top_door))
    edge_L_d = Part.makeLine(App.Vector(-half_W_door, Y_mat, z_top_door), App.Vector(-half_W_door, Y_mat, z_edge_door))
    wire_door = Part.Wire([edge_arc_d, edge_R_d, edge_top_d, edge_L_d])
    solid_door_raw = Part.Face(wire_door).extrude(App.Vector(0.0, T_mat, 0.0))

    # Ô kính thạch anh 10cm nằm chính giữa cửa
    z_bot_door = -R_arc_door  # -391.0mm
    z_mid_glass = (z_top_door + z_bot_door) / 2.0  # -296.965mm
    D_glass = 100.0  # 10cm
    R_glass = D_glass / 2.0  # 50.0mm

    # Khoét lỗ phi 100mm trên cửa sắt
    hole_glass = Part.makeCylinder(R_glass, T_mat + 10.0, App.Vector(0.0, Y_mat - 5.0, z_mid_glass), App.Vector(0, 1, 0))
    solid_door = solid_door_raw.cut(hole_glass)

    obj_cua_xa = doc.addObject("Part::Feature", "Cua_Xa_Hat_Sat_18mm")
    obj_cua_xa.Shape = solid_door
    obj_cua_xa.Label = "6c1. Cánh Cửa Xả Sắt 1.8cm (Phôi Cắt Miệng Thu Nhỏ 1mm Đều, Lỗ Kính D100mm)"
    gan_mau(obj_cua_xa, (0.32, 0.38, 0.46), line_color=(0.10, 0.15, 0.20), line_width=1.8)

    # Đĩa kính thạch anh chịu nhiệt phi 100mm dày 8mm
    T_glass = 8.0
    Y_glass_pos = Y_mat + (T_mat - T_glass) / 2.0  # -513.0mm
    solid_glass = Part.makeCylinder(R_glass - 0.5, T_glass, App.Vector(0.0, Y_glass_pos, z_mid_glass), App.Vector(0, 1, 0))
    obj_kieng_xa = doc.addObject("Part::Feature", "O_Kieng_Quan_Sat_Phi_10cm")
    obj_kieng_xa.Shape = solid_glass
    obj_kieng_xa.Label = "6c2. Ô Kính Thạch Anh Chịu Nhiệt Phi 10cm (Nằm Giữa Miệng Cửa Xả)"
    gan_mau(obj_kieng_xa, (0.72, 0.92, 0.96), line_color=(0.40, 0.75, 0.85), line_width=1.0, do_trong_suot=65)

    # Vành Inox 304 giữ kính phía ngoài (OD 124mm, ID 92mm, dày 3mm) & 4 vít chìm M5
    flange_out = Part.makeCylinder(62.0, 3.0, App.Vector(0.0, Y_mat - 3.0, z_mid_glass), App.Vector(0, 1, 0))
    flange_hole = Part.makeCylinder(46.0, 5.0, App.Vector(0.0, Y_mat - 4.0, z_mid_glass), App.Vector(0, 1, 0))
    solid_flange = flange_out.cut(flange_hole)
    screws = []
    for angle_deg in [45.0, 135.0, 225.0, 315.0]:
        rad = math.radians(angle_deg)
        xs = 54.0 * math.cos(rad)
        zs = z_mid_glass + 54.0 * math.sin(rad)
        screw = Part.makeCylinder(2.5, 6.0, App.Vector(xs, Y_mat - 3.5, zs), App.Vector(0, 1, 0))
        screws.append(screw)
    solid_vanh_kieng = Part.makeCompound([solid_flange, Part.makeCompound(screws)])
    obj_vanh_kieng = doc.addObject("Part::Feature", "Vanh_Inox_Giu_Kieng_Phi_10cm")
    obj_vanh_kieng.Shape = solid_vanh_kieng
    obj_vanh_kieng.Label = "6c3. Vành Inox 304 & 4 Vít Chìm M5 Kẹp Giữ Kính Quan Sát D100mm"
    gan_mau(obj_vanh_kieng, (0.85, 0.88, 0.92), line_color=(0.20, 0.25, 0.30), line_width=1.2)

    # -------------------------------------------------------------
    # 6d. CÂY LÁP PHI 30MM DÀI 100CM BẺ CẦN GẠT 30CM & 2 GỐI ĐỠ BẠC ĐẠN RÙA UCP206 (CÁCH MIỆNG 3CM, ĐỆM 1CM)
    #     - Cây láp tròn đặc phi 30mm: Dài tổng thể 100cm (thân ngang 70cm từ X = -350..+350mm,
    #       bẻ cong cần gạt dài 30cm tại X = -350mm chúc xuống dưới nghiêng 45° chĩa ra phía trước kèm núm cầu phi 42mm và vòng chặn cốt).
    #     - Vị trí: Gắn cao hơn mép trên miệng xả đúng 3cm = 30mm (Z = -171.93mm).
    #     - Khoảng cách từ bề mặt cây láp đến mặt máy: đúng 1cm = 10mm (Y_shaft = -543.0mm).
    #     - 2 Gối đỡ bạc đạn rùa UCP206 cốt phi 30mm: Vỏ gang đúc mai rùa, bạc đạn cầu tự lựa, vú mỡ M8,
    #       đặt tại X = ±310mm (cách mép thanh la máng xả 10mm = 1cm).
    #     - 4 Bu-lông M14 cắm ren vào mặt máy sắt 18mm.
    #     - 2 Khâu nối đôi cân bằng 2 bên (X = ±130mm, Dài 8cm, Rộng 3cm, Dày 10mm):
    #       Nhẫn tròn Ø50x30mm vuông góc 90° tấm chữ nhật 3x8cm dày 10mm đầu nửa tròn.
    #       MẶT LƯNG ÁP SÁT 100% VÀO MẶT MÁY VÀ CÁNH CỬA XẢ SẮT 18MM TẠI Y = -518mm.
    #     - 2 Chốt Pin M10 liên kết chặt khâu nối vào cánh cửa xả sắt 18mm.
    #     - Cụm tay khóa chữ L bên phải (X = +229mm) giữ cánh cửa đóng kín khít.
    # -------------------------------------------------------------
    Z_shaft = z_top_m + 30.0   # -171.93mm (cao hơn mép trên miệng xả 3cm)
    R_shaft = 15.0             # Bán kính trục phi 30mm
    GAP_shaft_face = 10.0      # Khoảng hở từ bề mặt cây láp đến mặt máy đúng 1cm = 10mm
    Y_shaft = Y_mat - GAP_shaft_face - R_shaft  # -543.0mm (tâm trục cây láp)

    # Cây láp phi 30mm dài 100cm bẻ cần gạt 30cm sang bên TRÁI nghiêng 45° chĩa ra phía trước
    R_bend = 45.0
    X_R_shaft = 350.0
    X_L_bend = -350.0
    L_handle = 300.0

    ang_handle = math.radians(45.0)
    sin_h = math.sin(ang_handle)
    cos_h = math.cos(ang_handle)

    p_start_R = App.Vector(X_R_shaft, Y_shaft, Z_shaft)
    p_bend_start_L = App.Vector(X_L_bend + R_bend, Y_shaft, Z_shaft)
    edge_straight = Part.makeLine(p_start_R, p_bend_start_L)

    p_bend_end_L = App.Vector(
        X_L_bend,
        Y_shaft - R_bend * sin_h,
        Z_shaft - R_bend * cos_h
    )
    p_arc_mid_L = App.Vector(
        X_L_bend + R_bend * (1.0 - sin_h),
        Y_shaft - R_bend * sin_h * (1.0 - cos_h),
        Z_shaft - R_bend * cos_h * (1.0 - cos_h)
    )
    arc_bend_L = Part.Arc(p_bend_start_L, p_arc_mid_L, p_bend_end_L).toShape()

    p_handle_end_L = App.Vector(
        X_L_bend,
        Y_shaft - L_handle * sin_h,
        Z_shaft - L_handle * cos_h
    )
    edge_handle_L = Part.makeLine(p_bend_end_L, p_handle_end_L)

    wire_spine = Part.Wire([edge_straight, arc_bend_L, edge_handle_L])
    circle_prof = Part.Circle(p_start_R, App.Vector(-1, 0, 0), R_shaft)
    face_prof = Part.Face(Part.Wire([circle_prof.toShape()]))
    solid_shaft = wire_spine.makePipe(face_prof)

    knob_handle = Part.makeSphere(22.0, p_handle_end_L)
    collar_R = Part.makeCylinder(22.5, 12.0, App.Vector(X_R_shaft - 12.0, Y_shaft, Z_shaft), App.Vector(1, 0, 0))
    solid_shaft_full = solid_shaft.fuse(knob_handle).fuse(collar_R)

    obj_truc_lap = doc.addObject("Part::Feature", "Truc_Lap_Cua_Xa_Phi_30mm")
    obj_truc_lap.Shape = solid_shaft_full
    obj_truc_lap.Label = "6d1. Cây Láp Tròn Phi 30mm Dài 100cm Bẻ Cần Gạt 30cm Sang Bên Trái Nghiêng 45 Độ Ra Trước (Cách Miệng 3cm)"
    gan_mau(obj_truc_lap, (0.82, 0.85, 0.88), line_color=(0.20, 0.25, 0.30), line_width=1.5)

    # 2 Gối đỡ bạc đạn rùa UCP206 & Bu-lông M14
    def make_ucp206_bearing(x_pos):
        base_ucp = Part.makeBox(48.0, 16.0, 165.0, App.Vector(x_pos - 24.0, Y_mat - 16.0, Z_shaft - 82.5))
        h_b1 = Part.makeCylinder(7.0, 20.0, App.Vector(x_pos, Y_mat - 18.0, Z_shaft - 60.5), App.Vector(0, 1, 0))
        h_b2 = Part.makeCylinder(7.0, 20.0, App.Vector(x_pos, Y_mat - 18.0, Z_shaft + 60.5), App.Vector(0, 1, 0))
        base_cut = base_ucp.cut(h_b1).cut(h_b2)

        body_housing = Part.makeCylinder(36.0, 36.0, App.Vector(x_pos - 18.0, Y_shaft, Z_shaft), App.Vector(1, 0, 0))
        gusset = Part.makeBox(36.0, 20.0, 48.0, App.Vector(x_pos - 18.0, Y_shaft, Z_shaft - 24.0))
        hole_shaft = Part.makeCylinder(15.25, 50.0, App.Vector(x_pos - 25.0, Y_shaft, Z_shaft), App.Vector(1, 0, 0))
        nipple = Part.makeCylinder(4.0, 10.0, App.Vector(x_pos, Y_shaft, Z_shaft + 36.0), App.Vector(0, 0, 1))

        bolts = []
        for zb in [Z_shaft - 60.5, Z_shaft + 60.5]:
            b_shank = Part.makeCylinder(7.0, 16.0 + 16.0, App.Vector(x_pos, Y_mat - 16.0, zb), App.Vector(0, 1, 0))
            b_head = Part.makeCylinder(11.0, 9.0, App.Vector(x_pos, Y_mat - 25.0, zb), App.Vector(0, 1, 0))
            bolts.append(b_shank.fuse(b_head))

        ucp_body = base_cut.fuse(body_housing).fuse(gusset).fuse(nipple).cut(hole_shaft)
        return ucp_body, Part.makeCompound(bolts)

    ucp_L, b_L = make_ucp206_bearing(-310.0)
    ucp_R, b_R = make_ucp206_bearing(310.0)

    obj_goi_rua = doc.addObject("Part::Feature", "Hai_Goi_Bac_Dan_Rua_UCP206")
    obj_goi_rua.Shape = Part.makeCompound([ucp_L, ucp_R])
    obj_goi_rua.Label = "6d2. Hai Gối Đỡ Bạc Đạn Rùa UCP206 Cốt 30mm (Vỏ Gang Mai Rùa, Bạc Đạn Cầu, Vú Mỡ M8)"
    gan_mau(obj_goi_rua, (0.22, 0.38, 0.48), line_color=(0.10, 0.18, 0.25), line_width=1.6)

    obj_bulong_goi = doc.addObject("Part::Feature", "BuLong_M14_Ga_Goi_Rua")
    obj_bulong_goi.Shape = Part.makeCompound([b_L, b_R])
    obj_bulong_goi.Label = "6d3. 4 Bu-lông M14 Bắt Chặt Hai Gối Đỡ Bạc Đạn Rùa Vào Mặt Máy Sắt 18mm"
    gan_mau(obj_bulong_goi, (0.85, 0.70, 0.20), line_color=(0.40, 0.30, 0.05), line_width=1.2)

    # Cụm tay khóa chữ L bên phải
    x_lock = half_W_door - 20.0
    z_lock = z_mid_glass
    lock_shaft = Part.makeCylinder(8.0, 45.0, App.Vector(x_lock, Y_mat - 25.0, z_lock), App.Vector(0, 1, 0))
    lock_latch = Part.makeBox(12.0, 15.0, 60.0, App.Vector(x_lock - 6.0, Y_mat + T_mat, z_lock - 20.0))
    lock_handle = Part.makeCylinder(12.0, 25.0, App.Vector(x_lock, Y_mat - 30.0, z_lock), App.Vector(0, 1, 0))
    lock_arm = Part.makeBox(14.0, 14.0, 75.0, App.Vector(x_lock - 7.0, Y_mat - 28.0, z_lock - 65.0))
    solid_lock = lock_shaft.fuse(lock_latch).fuse(lock_handle).fuse(lock_arm)

    obj_tay_khoa = doc.addObject("Part::Feature", "Tay_Khoa_Gai_Cua_Xa")
    obj_tay_khoa.Shape = solid_lock
    obj_tay_khoa.Label = "6d4. Cụm Tay Khóa Gài Chữ L Khóa Ép Chặt Cánh Cửa Xả Vào Mặt Máy Khi Đóng"
    gan_mau(obj_tay_khoa, (0.75, 0.60, 0.20), line_color=(0.40, 0.30, 0.05), line_width=1.5)

    # -------------------------------------------------------------
    # 6d5. HAI KHÂU NỐI ĐÔI CÂN BẰNG 2 BÊN (DÀI 8CM, VUÔNG GÓC 90°, ÁP SÁT MẶT MÁY)
    #      - 2 Nhẫn tròn ôm cây láp Ø30mm: Dài 3cm, dày 10mm (OD 50mm, ID 30mm) kèm vít chí M8.
    #      - 2 Tấm hình chữ nhật rộng 3cm, dài 8cm, dày 10mm, đầu ngoài bo nửa tròn R15mm, lỗ pin Ø10mm.
    #      - Vị trí đối xứng tại X = ±130mm (cân bằng 2 bên, không che khuất ô kính Ø10cm ở giữa).
    #      - Mặt lưng phẳng của tấm ÁP SÁT 100% vào mặt máy và cánh cửa xả sắt 18mm khi đóng kín (Y = -518mm).
    #      - 2 Chốt xoay Pin M10 liên kết chặt khâu nối vào cánh cửa xả sắt 18mm.
    # -------------------------------------------------------------
    L_nhan = 30.0   # 3cm dọc trục X
    ID_nhan = 30.0  # Ø30mm ôm vừa khít cây láp
    T_nhan = 10.0   # Dày 10mm -> OD 50mm
    OD_nhan = ID_nhan + 2 * T_nhan  # 50mm
    R_out_nhan = OD_nhan / 2.0      # 25mm

    L_plate = 80.0  # Dài 8cm theo yêu cầu (chỉnh từ 6 thành 8)
    W_plate = 30.0  # Rộng 3cm
    T_plate = 10.0  # Dày 10mm (bằng khoảng hở từ cây láp đến mặt máy)
    R_tip = W_plate / 2.0  # 15mm
    D_pin = 10.0    # Lỗ Pin Phi 10mm
    R_pin = D_pin / 2.0
    L_eff = L_plate - R_tip  # 65mm
    z_pin = Z_shaft - L_eff  # -236.93mm (cách mép trên cánh cửa xả 34mm)

    def tao_mot_khau_noi(x_pos):
        # Nhẫn tròn dọc trục X ôm cây láp
        cyl_out = Part.makeCylinder(R_out_nhan, L_nhan, App.Vector(x_pos - L_nhan / 2.0, Y_shaft, Z_shaft), App.Vector(1, 0, 0))
        cyl_in = Part.makeCylinder(R_shaft, L_nhan + 4.0, App.Vector(x_pos - L_nhan / 2.0 - 2.0, Y_shaft, Z_shaft), App.Vector(1, 0, 0))
        vit_chi = Part.makeCylinder(4.0, T_nhan + 4.0, App.Vector(x_pos, Y_shaft, Z_shaft + R_shaft - 2.0), App.Vector(0, 0, 1))
        nhan = cyl_out.cut(cyl_in).cut(vit_chi)

        # Tấm hình chữ nhật rộng 3cm, dài 8cm, dày 10mm:
        # Mặt lưng phẳng ÁP SÁT 100% vào mặt máy và cánh cửa xả sắt 18mm tại Y = -518.0mm!
        # Mặt trước tại Y = -528.0mm (tiếp xúc phẳng khít với bề mặt cây láp).
        box = Part.makeBox(W_plate, T_plate, L_eff, App.Vector(x_pos - W_plate / 2.0, Y_mat - T_plate, z_pin))
        tip = Part.makeCylinder(R_tip, T_plate, App.Vector(x_pos, Y_mat - T_plate, z_pin), App.Vector(0, 1, 0))
        hole = Part.makeCylinder(R_pin, T_plate + 4.0, App.Vector(x_pos, Y_mat - T_plate - 2.0, z_pin), App.Vector(0, 1, 0))
        plate = box.fuse(tip).cut(hole)
        return nhan.fuse(plate)

    kn_L = tao_mot_khau_noi(-130.0)
    kn_R = tao_mot_khau_noi(130.0)
    dual_connectors = kn_L.fuse(kn_R)

    obj_khau_noi = doc.addObject("Part::Feature", "Hai_Khau_Noi_Cua_Xa_8cm")
    obj_khau_noi.Shape = dual_connectors
    obj_khau_noi.Label = "6d5. Hai Khâu Nối Đôi Cân Bằng 2 Bên (Dài 8cm, Rộng 3cm, Vuông Góc 90° ÁP SÁT MẶT MÁY)"
    gan_mau(obj_khau_noi, (0.85, 0.88, 0.92), line_color=(0.10, 0.15, 0.22), line_width=1.6)

    # 2 Bu-lông chốt xoay Pin M10 & Ê-cu tự hãm liên kết vào cánh cửa xả sắt 18mm
    def tao_chot_pin(x_pos):
        pin_bolt = Part.makeCylinder(R_pin - 0.2, T_plate + T_mat + 4.0, App.Vector(x_pos, Y_mat - T_plate - 4.0, z_pin), App.Vector(0, 1, 0))
        pin_head = Part.makeCylinder(8.5, 5.0, App.Vector(x_pos, Y_mat - T_plate - 5.0, z_pin), App.Vector(0, 1, 0))
        pin_nut = Part.makeCylinder(8.5, 6.0, App.Vector(x_pos, Y_mat + T_mat - 2.0, z_pin), App.Vector(0, 1, 0))
        return pin_bolt.fuse(pin_head).fuse(pin_nut)

    pin_L = tao_chot_pin(-130.0)
    pin_R = tao_chot_pin(130.0)

    obj_chot_pin = doc.addObject("Part::Feature", "Hai_Chot_Pin_M10_Cua_Xa")
    obj_chot_pin.Shape = pin_L.fuse(pin_R)
    obj_chot_pin.Label = "6d6. Hai Bu-lông Chốt Xoay Pin M10 & Ê-cu Tự Hãm Khớp Cửa Xả Sắt 18mm"
    gan_mau(obj_chot_pin, (0.90, 0.75, 0.25), line_color=(0.40, 0.30, 0.05), line_width=1.2)


    # -------------------------------------------------------------
    # 7. MẶT MÁY SAU ĐỂ GÁ TRỐNG: SẮT DÀY 1.8CM (CHÂN VÁT GỜ ĐỨNG 5.5CM GIỐNG MẶT TRƯỚC)
    #    - Yêu cầu mới: Khoảng cách lọt lòng 2 mặt máy tăng từ 100cm -> 110cm
    #    - Đầu trước trống cách mặt máy trước 0.5mm (Y_drum_front = -499.5mm)
    #    - Đuôi sau trống tại Y_drum_rear = +500.5mm
    #    - Mặt sau còn lại đúng 9.95cm (99.5mm): Y_mat_sau = 500.5 + 99.5 = 600.0mm!
    #    - Vị trí trục Y: Từ Y = +600.0mm đến Y = +618.0mm (dày 18mm)
    #    - Lỗ khoét phi 65mm (R = 32.5mm) tại tâm (0, 0) để lọt đầu cốt láp phi 60mm phía sau.
    #    - Đoạn đầu cốt láp sau (dài 100mm, từ Y=+600 đến Y=+700) nhô ra ngoài 82mm để lắp gối bi & puly kéo.
    # -------------------------------------------------------------
    Y_mat_sau = 600.0
    arc_sau = Part.Arc(
        App.Vector(x_tR, Y_mat_sau, z_tR),
        App.Vector(0, Y_mat_sau, R_mat),
        App.Vector(x_tL, Y_mat_sau, z_tL)
    )
    edge_arc_sau = arc_sau.toShape()
    edge_L_sau_slant = Part.makeLine(App.Vector(x_tL, Y_mat_sau, z_tL), App.Vector(-W_half_bot, Y_mat_sau, Z_step))
    edge_L_sau_foot = Part.makeLine(App.Vector(-W_half_bot, Y_mat_sau, Z_step), App.Vector(-W_half_bot, Y_mat_sau, Z_bottom))
    edge_bot_sau = Part.makeLine(App.Vector(-W_half_bot, Y_mat_sau, Z_bottom), App.Vector(W_half_bot, Y_mat_sau, Z_bottom))
    edge_R_sau_foot = Part.makeLine(App.Vector(W_half_bot, Y_mat_sau, Z_bottom), App.Vector(W_half_bot, Y_mat_sau, Z_step))
    edge_R_sau_slant = Part.makeLine(App.Vector(W_half_bot, Y_mat_sau, Z_step), App.Vector(x_tR, Y_mat_sau, z_tR))

    wire_mat_sau = Part.Wire([edge_arc_sau, edge_L_sau_slant, edge_L_sau_foot, edge_bot_sau, edge_R_sau_foot, edge_R_sau_slant])
    face_mat_sau = Part.Face(wire_mat_sau)
    solid_mat_sau = face_mat_sau.extrude(App.Vector(0, T_mat, 0))

    # Khoét lỗ phi 65mm xuyên tâm
    hole_mat_sau = Part.makeCylinder(32.5, T_mat + 10.0, App.Vector(0, Y_mat_sau - 5.0, 0), App.Vector(0, 1, 0))
    hinh_mat_sau = solid_mat_sau.cut(hole_mat_sau)

    # Khoét 1 lỗ chữ nhật ở mặt sau: Dài 50cm (500mm), Cao 30cm (300mm), Cách chân máy 5cm (50mm) - Cửa lò đốt
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
    obj_mat_sau.Label = "7. Mặt Máy Sau (Sắt 1.8cm, Chân Vát Gờ Đứng 5.5cm, Lỗ Cốt D65mm, Cửa Lò 50x30cm Dưới)"
    gan_mau(obj_mat_sau, (0.28, 0.35, 0.45), line_color=(0.10, 0.15, 0.25), line_width=2.0)

    # 7b. MÁNG NẠP LIỆU DẪN HƯỚNG INOX 304 CHỐNG RỚT HẠT (MẶT TRƯỚC VÀO SÂU TRỐNG 6CM, ĐỘ DỐC CỰC ĐẠI 50.6°):
    # - Vượt qua khe hở quay 2mm giữa mép trống và mặt máy trước tĩnh (Y = -500mm)
    # - Nhô sâu 60mm vào trong lòng trống (đến Y = -440mm), đảm bảo 100% hạt rơi vào trống không rớt ra ngoài
    # - Sàn máng nghiêng dốc từ Z = 155mm (Y = -518) xuống Z = 60mm (Y = -440), tạo góc dốc cực đại 50.6° hạt trôi siêu nhanh
    # - 2 thành be chắn hai bên cao 60mm (từ Z = 155 đến 215mm) ngăn hạt văng sang hai bên
    T_CHUTE = 2.0  # Inox tấm 2mm
    pts_side_L = [
        App.Vector(-half_W_lo_nap, Y_mat, Z_bot_lo_nap),
        App.Vector(-half_W_lo_nap, -440.0, 60.0),
        App.Vector(-half_W_lo_nap, -440.0, 120.0),
        App.Vector(-half_W_lo_nap, Y_mat, Z_bot_lo_nap + 60.0),
        App.Vector(-half_W_lo_nap, Y_mat, Z_bot_lo_nap)
    ]
    face_side_L = Part.Face(Part.makePolygon(pts_side_L))
    solid_side_L = face_side_L.extrude(App.Vector(T_CHUTE, 0.0, 0.0))

    pts_side_R = [
        App.Vector(half_W_lo_nap - T_CHUTE, Y_mat, Z_bot_lo_nap),
        App.Vector(half_W_lo_nap - T_CHUTE, -440.0, 60.0),
        App.Vector(half_W_lo_nap - T_CHUTE, -440.0, 120.0),
        App.Vector(half_W_lo_nap - T_CHUTE, Y_mat, Z_bot_lo_nap + 60.0),
        App.Vector(half_W_lo_nap - T_CHUTE, Y_mat, Z_bot_lo_nap)
    ]
    face_side_R = Part.Face(Part.makePolygon(pts_side_R))
    solid_side_R = face_side_R.extrude(App.Vector(T_CHUTE, 0.0, 0.0))

    pts_floor = [
        App.Vector(-half_W_lo_nap, Y_mat, Z_bot_lo_nap),
        App.Vector(half_W_lo_nap, Y_mat, Z_bot_lo_nap),
        App.Vector(half_W_lo_nap, -440.0, 60.0),
        App.Vector(-half_W_lo_nap, -440.0, 60.0),
        App.Vector(-half_W_lo_nap, Y_mat, Z_bot_lo_nap)
    ]
    face_floor = Part.Face(Part.makePolygon(pts_floor))
    solid_floor = face_floor.extrude(App.Vector(0.0, 0.0, -T_CHUTE))

    solid_mang = Part.makeCompound([solid_floor, solid_side_L, solid_side_R])
    obj_mang_nap = doc.addObject("Part::Feature", "Mang_Nap_Lieu_Inox_Vao_Trong")
    obj_mang_nap.Shape = solid_mang
    obj_mang_nap.Label = "7b. Máng Nạp Liệu Dẫn Hướng Inox (Mặt Trước Vào Sâu Trống 6cm, Rộng 30cm, Dốc 50.6° Cực Đại Chống Rớt Hạt)"
    gan_mau(obj_mang_nap, (0.83, 0.86, 0.90), line_color=(0.15, 0.20, 0.25), line_width=1.8)

    # 7c. HỘP VÔ HÀNG INOX 3MM GẮN LIỀN VÀO MẶT MÁY TRƯỚC:
    # Cửa xả 20x30cm của hộp khớp khít 100% với lỗ nạp 20x30cm nâng cao trên mặt máy trước (Y = -518mm, Z = 155->355mm)
    rot_hop = App.Rotation(App.Vector(0, 0, 1), 90.0)
    pos_hop = App.Vector(0.0, -818.0, 155.0)
    plc_hop = App.Placement(pos_hop, rot_hop)
    items_hop_may = tao_hop_vo_hang(doc, plc=plc_hop, prefix="May_")

    # -------------------------------------------------------------
    # 8. CHÂN ĐẾ MÁY HÌNH CHỮ NHẬT: SẮT TẤM DÀY 0.5CM (5MM)
    #    - Yêu cầu: "thiết kế chân máy hình chữ nhật, dầy 0.5cm, kích thước vừa đủ, dư mỗi bên trước sau, trái phải 0.5cm"
    #    - Kích thước vừa khít theo đúng footprint của 2 chân mặt máy:
    #      + Chiều rộng (Trái - Phải theo trục X):
    #        Chân 2 mặt máy rộng 1100mm (từ X = -550mm đến X = +550mm).
    #        Dư mỗi bên trái phải 0.5cm (5mm): từ X = -555.0mm đến X = +555.0mm.
    #        -> Tổng chiều rộng: W = 1110.0mm = 111.0cm = 1.11m.
    #      + Chiều dài (Trước - Sau theo trục Y):
    #        Chân mặt trước tại Y = -518mm, chân mặt sau mới tại Y = +618mm (khoảng cách 1136mm).
    #        Dư mỗi bên trước sau 0.5cm (5mm): từ Y = -523.0mm đến Y = +623.0mm.
    #        -> Tổng chiều dài: L = 1146.0mm = 114.6cm = 1.146m.
    #      + Độ dày & Cao độ (theo trục Z):
    #        Độ dày tấm: đúng 0.5cm (5.0mm).
    #        Mặt trên của chân đế tại Z = -850.0mm (đỡ trọn vẹn đáy 2 mặt máy).
    #        Mặt dưới của chân đế tại Z = -855.0mm (tiếp xúc trực tiếp sàn xưởng).
    #    - Chi tiết tĩnh: Hàn/bắt bu lông chắc chắn với chân của 2 mặt máy, tạo khối khung gầm đầm chắc 100%.
    # -------------------------------------------------------------
    W_chan = 1110.0
    L_chan = 1146.0  # Dư mỗi bên trước sau 0.5cm (từ Y = -523.0 đến +623.0mm)
    T_chan = 5.0
    pnt_chan = App.Vector(-555.0, -523.0, -855.0)

    hinh_chan_de = Part.makeBox(W_chan, L_chan, T_chan, pnt_chan)
    obj_chan_de = doc.addObject("Part::Feature", "Chan_De_May_Hinh_Chu_Nhat_5mm")
    obj_chan_de.Shape = hinh_chan_de
    obj_chan_de.Label = "8. Chân Đế Máy Hình Chữ Nhật (Sắt Dày 0.5cm, 111cm x 114.6cm, Dư Trước Sau Trái Phải 0.5cm)"
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
    # Cánh cửa sắt tấm 18mm (tại Y_mat_sau = 600mm đến 618mm)
    plate_cua = Part.makeBox(498.0, 18.0, 298.0, App.Vector(-249.0, Y_mat_sau, -799.0))
    shapes_cua.append(plate_cua)

    # 2 Bản lề cối bên trái (nhìn trực diện từ phía sau: X = +249.5, Y = Y_mat_sau + 18mm = 618mm)
    for z_h in [-560.0, -740.0]:
        k_up = Part.makeCylinder(10.0, 24.0, App.Vector(249.5, Y_mat_sau + 26.0, z_h + 1.0), App.Vector(0, 0, 1))
        tab_door = Part.makeBox(15.0, 8.0, 24.0, App.Vector(234.5, Y_mat_sau + 18.0, z_h + 1.0))
        pin = Part.makeCylinder(6.0, 48.0, App.Vector(249.5, Y_mat_sau + 26.0, z_h - 23.0), App.Vector(0, 0, 1))
        shapes_cua.extend([k_up, tab_door, pin])

    # Tay khóa then gài L-handle bên phải (nhìn trực diện từ phía sau: X = -210, Z = -650)
    h_boss = Part.makeCylinder(13.0, 16.0, App.Vector(-210.0, Y_mat_sau + 18.0, -650.0), App.Vector(0, 1, 0))
    h_bar = Part.makeCylinder(7.0, 85.0, App.Vector(-210.0, Y_mat_sau + 34.0, -650.0), App.Vector(0, 0, -1))
    h_knob = Part.makeSphere(10.0, App.Vector(-210.0, Y_mat_sau + 34.0, -735.0))
    h_tongue = Part.makeBox(35.0, 8.0, 16.0, App.Vector(-250.0, Y_mat_sau - 8.0, -658.0))
    shapes_cua.extend([h_boss, h_bar, h_knob, h_tongue])

    hinh_cua_sau = Part.makeCompound(shapes_cua)
    obj_cua_sau = doc.addObject("Part::Feature", "Cua_Buong_Dot_Mat_Sau_18mm")
    obj_cua_sau.Shape = hinh_cua_sau
    obj_cua_sau.Label = "11. Cửa Buồng Đốt Mặt Sau (Sắt Dày 1.8cm, Dài 49.8cm, Cao 29.8cm, Khe Cắt 1mm, Mở Về Bên Trái)"
    gan_mau(obj_cua_sau, (0.35, 0.42, 0.52), line_color=(0.15, 0.20, 0.30), line_width=1.8)

    # -------------------------------------------------------------
    # 12. 2 BẢN LỀ CỐI CỬA SAU: HÀN CỐ ĐỊNH VÀO MẶT MÁY SAU BÊN TRÁI
    #     - Vị trí: Mép bên trái lỗ cắt (nhìn từ phía sau: X = +249.5mm, Y = Y_mat_sau + 18mm)
    #     - Cối dưới phi 20mm hàn cố định vào mặt máy sau, đệm long đền đồng
    #     - Cho phép cửa mở xoay về bên trái góc 0 - 120 độ
    # -------------------------------------------------------------
    shapes_ban_le_khung = []
    for z_h in [-560.0, -740.0]:
        k_low = Part.makeCylinder(10.0, 24.0, App.Vector(249.5, Y_mat_sau + 26.0, z_h - 25.0), App.Vector(0, 0, 1))
        wash = Part.makeCylinder(11.0, 2.0, App.Vector(249.5, Y_mat_sau + 26.0, z_h - 1.0), App.Vector(0, 0, 1))
        tab_frame = Part.makeBox(15.0, 8.0, 24.0, App.Vector(249.5, Y_mat_sau + 18.0, z_h - 25.0))
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

    # 1. SÀN ĐÁY BUỒNG ĐỐT: Z = -850 đến -800mm (dày 50mm, 7 hàng x 100mm = rộng 700mm, dài 1100mm từ Y = -500 đến +600mm)
    z_floor = -850.0
    h_floor = 50.0 - gap_gach
    for col in range(7):
        x_min = -350.0 + col * 100.0 + gap_gach / 2.0
        w_brick = 100.0 - gap_gach
        if col % 2 == 0:
            segments = [(-500.0, 300.0), (-200.0, 300.0), (100.0, 300.0), (400.0, 200.0)]
        else:
            segments = [(-500.0, 200.0), (-300.0, 300.0), (0.0, 300.0), (300.0, 300.0)]
        for y_start, l_seg in segments:
            y_min = y_start + gap_gach / 2.0
            l_brick = l_seg - gap_gach
            brick = Part.makeBox(w_brick, l_brick, h_floor, App.Vector(x_min, y_min, z_floor + gap_gach / 2.0))
            shapes_buong_dot.append(brick)

    # 2. Hai vách hông lò bao 1 lớp gạch dày 10cm, chừa ngang 50cm, cao 9 hàng đến Z = -350mm (dài 1100mm)
    wall_cols = [(-350.0, -250.0), (250.0, 350.0)]
    for x_start, x_end in wall_cols:
        x_min = x_start + gap_gach / 2.0
        w_brick = (x_end - x_start) - gap_gach
        for course in range(9):
            z_c = -800.0 + course * 50.0 + gap_gach / 2.0
            h_c = 50.0 - gap_gach
            if course % 2 == 0:
                segments = [(-500.0, 300.0), (-200.0, 300.0), (100.0, 300.0), (400.0, 200.0)]
            else:
                segments = [(-500.0, 200.0), (-300.0, 300.0), (0.0, 300.0), (300.0, 300.0)]
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
    saw_cutter = Part.makeCylinder(r_cut, 1150.0, App.Vector(0, -525.0, 0), App.Vector(0, 1, 0))
    hinh_buong_dot = raw_buong_dot.cut(saw_cutter)

    obj_buong_dot_gach = doc.addObject("Part::Feature", "Buong_Dot_Cui_Gach_Sa_Mot_30x5x10")
    obj_buong_dot_gach.Shape = hinh_buong_dot
    obj_buong_dot_gach.Label = "13. Buồng Đốt Củi Lót Gạch Chịu Lửa (KT 30x5x10cm, Dài 110cm, Lòng Rộng 50cm, Bao 1 Lớp Gạch 10cm, Cưa Gọt Cách 1cm Nằm Gọn Dưới Trống)"
    gan_mau(obj_buong_dot_gach, (0.84, 0.48, 0.26), line_color=(0.35, 0.18, 0.08), line_width=1.5)

    # 14. HAI CỤM BỘ CHỈNH GỐI BI TRỤC PHI 60MM (KIỂU PHƯƠNG ÂN CHI TIẾT) LẮP TRÊN 2 MẶT MÁY
    # - Cụm trước: Bắt trên Mặt Máy Trước tại Y = -518mm, ôm trọn cốt láp trước Phi 60mm
    # - Cụm sau: Bắt trên Mặt Máy Sau tại Y = +618mm, ôm trọn cốt láp sau Phi 60mm
    plc_chinh_truoc = App.Placement(App.Vector(0, -518.0, 0), App.Rotation(App.Vector(0, 0, 1), 180.0))
    plc_chinh_sau = App.Placement(App.Vector(0, 618.0, 0), App.Rotation())

    cum_chinh_truoc = tao_bo_chinh_phuong_an_chi_tiet(doc, plc_base=plc_chinh_truoc, is_exploded=False, prefix="May_Chinh_Truoc_")
    cum_chinh_sau = tao_bo_chinh_phuong_an_chi_tiet(doc, plc_base=plc_chinh_sau, is_exploded=False, prefix="May_Chinh_Sau_")
    items_chinh_may = cum_chinh_truoc + cum_chinh_sau

    return obj_trong, obj_ao_ngoai, obj_lap, obj_chong, obj_canh_ngoai, obj_canh_trong, obj_day_sau, obj_mat_truoc, obj_mat_sau, obj_chan_de, obj_cay_tham, obj_tay_cam, obj_cua_sau, obj_ban_le_sau, obj_buong_dot_gach, obj_mang_nap, items_hop_may, items_chinh_may


def tao_hop_vo_hang(doc, plc=None, prefix=""):
    """
    Tạo mô hình HỘP VÔ HÀNG (Phễu nạp liệu) Inox 3mm tấm to (QUAY NGƯỢC LẠI & CHỪA KHOẢNG TRỐNG 20x30CM Ở TRÊN):
    - Kích thước chuẩn: Chiều cao hộp GIỮ NGUYÊN VẸN 65cm (650mm), Vách sau 30cm (300mm), Đáy vuông 30x30cm
    - Biên dạng hông: Ghép từ 1 hình chữ nhật (300 x 300mm) + 1 tam giác (300 x 350mm)
      tạo thành hình thang vuông quay ngược (Vách trước 650mm, vách sau 300mm, đáy 300mm, dốc 49.4°).
    - Vách trước: Cắt phôi 45x30cm (cao từ Z=0 đến 450mm).
      Phía trên chừa khoảng trống 20x30cm (từ Z=450 đến 650mm) làm cửa đổ hạt vào!
    - Khoan lỗ trục gạt Ø20mm ở góc tù vách sau (X=10.5, Z=296.1mm), mép cách cạnh đúng 0.5mm.
    - Nhân đôi 2 tấm hông cách nhau 300mm (30cm lọt lòng).
    - Bọc các mặt bằng inox 3mm (Vách trước 45x30, Vách sau vuông 30x30, Đáy vuông 30 khoét lỗ Ø20cm, Mái chụp nghiêng dốc).
    """
    T = 3.0           # Độ dày inox 3mm
    B = 300.0         # Khoảng cách lọt lòng giữa 2 tấm hông: 30cm (300mm)
    W_rec = 300.0     # Chiều dài đáy dưới: 300mm (30cm) - Mặt vuông 30x30cm khoét lỗ Ø200mm
    H_front_total = 650.0  # Chiều cao tổng thể hông trước: 650mm (65cm - giữ nguyên 65cm)
    H_front_plate = 450.0  # Chiều cao tấm ốp vách trước: 450mm (45cm - cắt phôi 45x30cm)
    H_back = 300.0    # Chiều cao vách đứng sau: 300mm (30cm) - Vuông 30x30cm nguyên tấm
    H_tri = H_front_total - H_back  # 350mm (35cm)
    half_B = B / 2.0  # 150mm
    L_slope = math.sqrt(W_rec**2 + H_tri**2)  # ~460.98mm

    Z_bot_back = H_front_total - H_back  # 350.0mm

    # Thông số lỗ khoan phi 20mm tại góc tù P4(0, 350):
    R_LO = 10.0           # Bán kính lỗ phi 20mm
    GAP_MEP = 0.5         # Cách mép vách đứng sau đúng 0.5mm
    X_LO = R_LO + GAP_MEP # 10.5mm (cách vách sau X=0 đúng 0.5mm)
    # Đường thẳng dốc đáy nghiêng nối (0, 350) -> (300, 0): 7X + 6Z - 2100 = 0
    # Tâm Z tính để mép lỗ cách đường dốc đúng 0.5mm:
    Z_LO = (2100.0 - 7.0 * X_LO + (R_LO + GAP_MEP) * math.sqrt(85.0)) / 6.0  # ~353.88mm

    # 1. Tấm hông trái (Hình thang đứng đầu nhọn đáy tại Y = -150mm, đùn -Y dày 3mm, khoan lỗ Ø20mm)
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
    gan_mau(obj_hong_trai, (0.83, 0.86, 0.90), line_color=(0.15, 0.20, 0.25), line_width=1.8)

    # 2. Tấm hông phải (Hình thang đứng đầu nhọn đáy tại Y = +150mm, đùn +Y dày 3mm, cách 30cm, khoan lỗ Ø20mm)
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
    gan_mau(obj_hong_phai, (0.83, 0.86, 0.90), line_color=(0.15, 0.20, 0.25), line_width=1.8)

    # 3. Tấm nắp đỉnh trên: Vuông 30cm x 30cm x Dày 3mm (Z=650mm)
    # Khoét lỗ tròn Ø20cm (200mm) chính giữa mặt vuông 30x30cm
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
    gan_mau(obj_day, (0.83, 0.86, 0.90), line_color=(0.15, 0.20, 0.25), line_width=1.8)

    # 4. Tấm vách đứng trước: Rộng 30cm x Cao 45cm (Lắp từ Z=200 đến 650mm)
    # - Phía dưới chân vách từ Z = 0 đến 200mm chừa khoảng trống 20x30cm xả hạt
    # - Ở phía bên kia (đỉnh trên của tấm), khoét lỗ tròn Ø20cm (200mm), mép trên chừa lại 1cm
    solid_vach_truoc = Part.makeBox(T, B, H_front_plate, App.Vector(W_rec, -half_B, H_front_total - H_front_plate))
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
    gan_mau(obj_vach_truoc, (0.83, 0.86, 0.90), line_color=(0.15, 0.20, 0.25), line_width=1.8)

    # 5. Tấm vách đứng sau: Rộng 30cm x Cao 30cm x Dày 3mm (Vuông 30x30cm nguyên tấm, Z=350->650)
    solid_vach_sau = Part.makeBox(T, B, H_back, App.Vector(-T, -half_B, Z_bot_back))
    obj_vach_sau = doc.addObject("Part::Feature", f"{prefix}Tam_Vach_Dung_Sau_3mm")
    obj_vach_sau.Shape = solid_vach_sau
    obj_vach_sau.Label = "5. Tấm Vách Đứng Sau (Inox 3mm, Vuông 30x30cm Nguyên Tấm, Z=350->650)"
    gan_mau(obj_vach_sau, (0.83, 0.86, 0.90), line_color=(0.15, 0.20, 0.25), line_width=1.8)

    # 6. Tấm vách dốc nghiêng đáy / Máng trượt: Rộng 30cm x Dài 46.1cm x Dày 3mm
    # Nối từ chân vách sau (0, 350) dốc xuống đầu nhọn đáy trước (300, 0)
    # NGUYÊN TẤM LIỀN (MÁNG DỐC 49.4° TRÔI HẠT)
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
    gan_mau(obj_nap, (0.83, 0.86, 0.90), line_color=(0.15, 0.20, 0.25), line_width=1.8, do_trong_suot=20)

    # 7. Ống nạp liệu tròn từ trên xuống: phi 19.9cm (199mm) x dài 30cm (300mm)
    # Lắp lọt qua lỗ Ø20cm trên nắp đỉnh Z=650mm, ăn sâu 30cm xuống Z=350mm
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
    gan_mau(obj_ong, (0.83, 0.86, 0.90), line_color=(0.10, 0.15, 0.20), line_width=1.8)

    # 8. Cơ cấu van gạt đáy ống: Cây láp Ø20mm nhô 10cm bên phải + 4 Vòng tròn (ID Ø20mm) + Lá van Inox 3mm bo tròn
    # - Cây láp Inox phi 20mm: Chiều dài tổng 428mm, dư ra 10cm (100mm) về bên phải (Y = +153 -> +253mm)
    # - Mỗi bên có 2 vòng tròn (ID Ø20mm bằng cây láp, OD Ø32mm dày thành 6mm):
    #   * Vòng dày (10mm) hàn vào mặt ngoài thành hộp: gối bạc trượt đỡ trục láp
    #   * Vòng ngoài (8mm) hàn vào cây láp: cữ chặn định vị chống trượt dọc trục, xoay cùng cây láp
    # - Tấm lá van Inox 3mm bo tròn bán nguyệt R=110mm đồng tâm với ống Ø19.9cm
    # - Tay gạt điều khiển & núm xoay ở đầu cây láp nhô ra 10cm bên phải
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
    # Vòng dày hông phải: từ Y = 153.0 đến 163.0mm
    solid_vong_hop_P = tao_vong_tron(half_B + T, T_RING_BOX)
    # Vòng dày hông trái: từ Y = -163.0 đến -153.0mm
    solid_vong_hop_T = tao_vong_tron(-half_B - T - T_RING_BOX, T_RING_BOX)

    # Gắn 2 vòng dày vào 2 tấm hông hộp (hàn cố định vào hộp):
    solid_hong_trai = Part.makeCompound([solid_hong_trai, solid_vong_hop_T])
    obj_hong_trai.Shape = solid_hong_trai
    obj_hong_trai.Label = "1. Tấm Hông Trái (Kèm Vòng Bạc Đỡ Ø20 Dày 10mm Hàn Ngoài)"

    solid_hong_phai = Part.makeCompound([solid_hong_phai, solid_vong_hop_P])
    obj_hong_phai.Shape = solid_hong_phai
    obj_hong_phai.Label = "2. Tấm Hông Phải (Kèm Vòng Bạc Đỡ Ø20 Dày 10mm Hàn Ngoài)"

    # 8b. Cây láp Ø20mm: Dư ra đúng 10cm (100mm) về bên phải (+253mm), bên trái Y = -175mm:
    Y_SHAFT_MIN = -half_B - T - T_RING_BOX - GAP_RING - T_RING_SHAFT - 3.5  # -175.0mm
    Y_SHAFT_MAX = half_B + T + 100.0  # +253.0mm (dư ra đúng 10cm tính từ mặt ngoài tấm hông phải)
    L_SHAFT_VAN = Y_SHAFT_MAX - Y_SHAFT_MIN  # 428.0mm

    solid_truc_lap = Part.makeCylinder(
        R_SHAFT_VAN,
        L_SHAFT_VAN,
        App.Vector(X_LO, Y_SHAFT_MIN, Z_LO),
        App.Vector(0.0, 1.0, 0.0)
    )

    # 8c. Hai vòng ngoài hàn vào cây láp (xoay cùng cây láp):
    # Vòng ngoài bên phải: từ Y = 163.5 đến 171.5mm
    solid_vong_lap_P = tao_vong_tron(half_B + T + T_RING_BOX + GAP_RING, T_RING_SHAFT)
    # Vòng ngoài bên trái: từ Y = -171.5 đến -163.5mm
    solid_vong_lap_T = tao_vong_tron(-half_B - T - T_RING_BOX - GAP_RING - T_RING_SHAFT, T_RING_SHAFT)

    # 8d. Tấm lá van Inox 3mm bo tròn đẹp mắt, ôm trọn và đồng tâm với ống nạp Ø19.9cm:
    W_VAN = 220.0             # Rộng 220mm (che phủ ống phi 19.9cm, mép dư 10.5mm đều 2 bên)
    R_ROUND = W_VAN / 2.0     # 110.0mm (bán kính bo tròn đầu lá van)
    T_VAN = T                 # Dày 3mm inox
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
    gan_mau(obj_van, (0.83, 0.86, 0.90), line_color=(0.10, 0.20, 0.30), line_width=1.8)

    # 9. Tham chiếu: Khối chữ nhật trên & Tam giác đáy (Ẩn mặc định)
    box_ref = Part.makeBox(W_rec, B, H_back, App.Vector(0.0, -half_B, Z_bot_back))
    obj_ref_rect = doc.addObject("Part::Feature", f"{prefix}ThamChieu_1_HinhChuNhat_30x30x30cm")
    obj_ref_rect.Shape = box_ref
    obj_ref_rect.Label = "📐 Tham Chiếu 1: Khối Chữ Nhật Trên (30cm x 30cm x 30cm, Z=350->650)"
    gan_mau(obj_ref_rect, (0.83, 0.86, 0.90), line_color=(0.1, 0.5, 0.8), do_trong_suot=70)
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
    gan_mau(obj_ref_tri, (0.83, 0.86, 0.90), line_color=(0.8, 0.3, 0.1), do_trong_suot=70)
    if hasattr(obj_ref_tri, "ViewObject") and obj_ref_tri.ViewObject:
        obj_ref_tri.ViewObject.Visibility = False

    # 10. Compound tổng thể
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
    gan_mau(obj_tong_the, (0.83, 0.86, 0.90), line_color=(0.15, 0.20, 0.25), line_width=1.8)
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


class BangDieuKhienHanCayTru(QtWidgets.QDialog):
    """Bảng điều khiển GUI tích hợp: Máy Rang Củi 2 Lớp & Hộp Vô Hàng Inox 3mm."""

    def __init__(
        self,
        doc=None,
        obj_trong=None,
        obj_ao_ngoai=None,
        obj_lap=None,
        obj_chong=None,
        obj_canh_ngoai=None,
        obj_canh_trong=None,
        obj_day_sau=None,
        obj_mat_truoc=None,
        obj_mat_sau=None,
        obj_chan_de=None,
        obj_cay_tham=None,
        obj_tay_cam=None,
        obj_cua_sau=None,
        obj_ban_le_sau=None,
        obj_buong_dot_gach=None,
        obj_mang_nap=None,
        items_hop_may=None,
        items_chinh_may=None,
        doc_hop=None,
        items_hop=None,
        doc_chinh=None,
        items_chinh=None,
        parent=None,
    ):
        if not QtWidgets:
            return
        super(BangDieuKhienHanCayTru, self).__init__(parent)
        self.doc = doc
        self.doc_hop = doc_hop
        self.items_hop = items_hop
        self.doc_chinh = doc_chinh
        self.items_chinh = items_chinh

        # Đối tượng Tab 1: Máy rang củi
        self.obj_trong = obj_trong
        self.obj_ao_ngoai = obj_ao_ngoai
        self.obj_lap = obj_lap
        self.obj_chong = obj_chong
        self.obj_canh_ngoai = obj_canh_ngoai
        self.obj_canh_trong = obj_canh_trong
        self.obj_day_sau = obj_day_sau
        self.obj_mat_truoc = obj_mat_truoc
        self.obj_mat_sau = obj_mat_sau
        self.obj_chan_de = obj_chan_de
        self.obj_cay_tham = obj_cay_tham
        self.obj_tay_cam = obj_tay_cam
        self.obj_cua_sau = obj_cua_sau
        self.obj_ban_le_sau = obj_ban_le_sau
        self.obj_buong_dot_gach = obj_buong_dot_gach
        self.obj_mang_nap = obj_mang_nap
        self.items_chinh_may = items_chinh_may or []
        self.hop_van_may = items_hop_may[7] if items_hop_may and len(items_hop_may) > 7 else None
        self.plc_hop = App.Placement(App.Vector(0.0, -818.0, 155.0), App.Rotation(App.Vector(0, 0, 1), 90.0))
        self.is_hop_may_visible = True
        self.is_chinh_may_visible = True
        self.is_chinh_transparency = False

        # Đối tượng Tab 2: Hộp vô hàng
        if self.items_hop and len(self.items_hop) >= 11:
            (
                self.hop_hong_trai,
                self.hop_hong_phai,
                self.hop_vach_sau,
                self.hop_day,
                self.hop_nap,
                self.hop_vach_truoc,
                self.hop_ong,
                self.hop_van,
                self.hop_ref_rect,
                self.hop_ref_tri,
                self.hop_tong_the,
            ) = self.items_hop[:11]
        else:
            self.hop_hong_trai = None
            self.hop_hong_phai = None
            self.hop_vach_sau = None
            self.hop_day = None
            self.hop_nap = None
            self.hop_vach_truoc = None
            self.hop_ong = None
            self.hop_van = None
            self.hop_ref_rect = None
            self.hop_ref_tri = None
            self.hop_tong_the = None

        # Trạng thái Tab 1: Máy rang
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

        # Trạng thái Tab 2: Hộp vô hàng & van gạt
        self.is_hop_transparent = False
        self.is_hop_thung_visible = True
        self.is_hop_top_open = False
        self.is_hop_ref_visible = False
        self.goc_van_hop = 0.0  # 0° = Đóng kín, 45° = Mở thông

        self.init_ui()
        self.init_timer()

    def init_ui(self):
        self.setWindowTitle("Điều Khiển Đồng Bộ: Máy Rang Củi 2 Lớp & Hộp Vô Hàng Inox 3mm")
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumWidth(560)
        self.setStyleSheet("""
            QDialog { background-color: #f8fafc; font-family: 'Segoe UI', Arial, sans-serif; }
            QTabWidget::pane { border: 1px solid #cbd5e1; border-radius: 6px; background-color: #ffffff; padding: 6px; }
            QTabBar::tab { background: #e2e8f0; color: #334155; padding: 8px 16px; font-weight: bold; border-top-left-radius: 6px; border-top-right-radius: 6px; margin-right: 2px; }
            QTabBar::tab:selected { background: #ffffff; color: #0284c7; border-bottom: 2px solid #0284c7; }
            QGroupBox { font-weight: bold; border: 1px solid #cbd5e1; border-radius: 6px; margin-top: 10px; padding-top: 14px; background-color: #ffffff; color: #1e293b; }
            QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 5px; color: #0f172a; }
            QPushButton { border-radius: 5px; font-weight: bold; padding: 6px 10px; font-size: 11px; }
        """)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 10, 12, 10)

        # 1. Thanh tiêu đề & Nút chuyển Tab / Tài liệu MD
        header = QtWidgets.QFrame()
        header.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1e293b, stop:1 #334155); border-radius: 6px; padding: 6px;")
        h_layout = QtWidgets.QHBoxLayout(header)
        h_layout.setContentsMargins(10, 4, 10, 4)
        title = QtWidgets.QLabel("🎮 ĐIỀU KHIỂN: MÁY RANG CỦI & BỘ CHỈNH")
        title.setStyleSheet("color: #38bdf8; font-weight: bold; font-size: 13px;")

        self.btn_header_may = QtWidgets.QPushButton("🏭 Tab 1: Máy Rang")
        self.btn_header_may.setStyleSheet("background-color: #0284c7; color: white; padding: 4px 10px; font-size: 10.5px; border-radius: 4px; font-weight: bold;")
        self.btn_header_may.clicked.connect(self.chuyen_tab_may)

        self.btn_header_hop = QtWidgets.QPushButton("📥 Tab 2: Hộp Vô Hàng")
        self.btn_header_hop.setStyleSheet("background-color: #0d9488; color: white; padding: 4px 10px; font-size: 10.5px; border-radius: 4px; font-weight: bold;")
        self.btn_header_hop.clicked.connect(self.chuyen_tab_hop)

        self.btn_header_chinh = QtWidgets.QPushButton("⚙️ Tab 3: Bộ Chỉnh Chi Tiết")
        self.btn_header_chinh.setStyleSheet("background-color: #f59e0b; color: white; padding: 4px 10px; font-size: 10.5px; border-radius: 4px; font-weight: bold;")
        self.btn_header_chinh.clicked.connect(self.chuyen_tab_chinh)

        btn_md = QtWidgets.QPushButton("📖 Thông Số (MD)")
        btn_md.setStyleSheet("background-color: #475569; color: white; padding: 4px 10px; font-size: 10.5px; border-radius: 4px;")
        btn_md.clicked.connect(self.mo_thong_so_md)

        h_layout.addWidget(title)
        h_layout.addStretch()
        h_layout.addWidget(self.btn_header_may)
        h_layout.addWidget(self.btn_header_hop)
        h_layout.addWidget(self.btn_header_chinh)
        h_layout.addWidget(btn_md)
        layout.addWidget(header)

        # 2. Main QTabWidget
        self.main_tabs = QtWidgets.QTabWidget()
        self.main_tabs.currentChanged.connect(self.on_tab_changed)

        # ---------------- TAB 1: MÁY RANG CỦI (TRỐNG 2 LỚP) ----------------
        tab_may = QtWidgets.QWidget()
        l_tab_may = QtWidgets.QVBoxLayout(tab_may)
        l_tab_may.setSpacing(8)
        l_tab_may.setContentsMargins(6, 6, 6, 6)

        # Trạng thái quay trống
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
        l_tab_may.addWidget(status_frame)

        # Vận hành động cơ & tốc độ
        grp_motor = QtWidgets.QGroupBox("⚡ Vận Hành Động Cơ & Tốc Độ Trống")
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

        btn_20 = QtWidgets.QPushButton("20 RPM")
        btn_20.setStyleSheet("background-color: #e2e8f0; color: #334155; font-size: 10px; padding: 4px 6px;")
        btn_20.clicked.connect(lambda: self.slider_rpm.setValue(20))
        btn_40 = QtWidgets.QPushButton("40 RPM")
        btn_40.setStyleSheet("background-color: #e2e8f0; color: #334155; font-size: 10px; padding: 4px 6px;")
        btn_40.clicked.connect(lambda: self.slider_rpm.setValue(40))
        btn_60 = QtWidgets.QPushButton("60 RPM")
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
        l_tab_may.addWidget(grp_motor)

        # Chế độ quan sát & ẩn hiện
        grp_vis = QtWidgets.QGroupBox("👁 Quan Sát & Ẩn Hiện Chi Tiết Máy Rang")
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

        self.btn_hop_may = QtWidgets.QPushButton("📥 Ẩn/Hiện Hộp Vô Hàng (Mặt Trước)")
        self.btn_hop_may.setStyleSheet("background-color: #059669; color: white; font-weight: bold;")
        self.btn_hop_may.clicked.connect(self.toggle_hop_may_visibility)
        g_vis.addWidget(self.btn_hop_may, 2, 0, 1, 2)

        l_tab_may.addWidget(grp_vis)

        # Nhóm Bộ Chỉnh Gối Bi Gắn Trên 2 Mặt Máy
        grp_tk_bc = QtWidgets.QGroupBox("⚙️ Bộ Chỉnh Gối Bi Trục Phi 60mm (Kiểu Phương Ân)")
        l_tk_bc = QtWidgets.QVBoxLayout(grp_tk_bc)
        l_tk_bc.setSpacing(5)

        r_btn_bc = QtWidgets.QHBoxLayout()
        self.btn_chinh_may = QtWidgets.QPushButton("⚙️ Ẩn/Hiện Bộ Chỉnh Trên Máy")
        self.btn_chinh_may.setStyleSheet("background-color: #d97706; color: white; font-weight: bold;")
        self.btn_chinh_may.clicked.connect(self.toggle_chinh_may_visibility)

        self.btn_chinh_transparency = QtWidgets.QPushButton("🔍 Xuyên Thấu Vỏ Gang (Soi Bi)")
        self.btn_chinh_transparency.setStyleSheet("background-color: #0284c7; color: white; font-weight: bold;")
        self.btn_chinh_transparency.clicked.connect(self.toggle_chinh_transparency)

        self.btn_goto_tab3 = QtWidgets.QPushButton("🔬 Soi Chi Tiết (Tab 3)")
        self.btn_goto_tab3.setStyleSheet("background-color: #7c3aed; color: white; font-weight: bold;")
        self.btn_goto_tab3.clicked.connect(self.chuyen_tab_chinh)

        r_btn_bc.addWidget(self.btn_chinh_may)
        r_btn_bc.addWidget(self.btn_chinh_transparency)
        r_btn_bc.addWidget(self.btn_goto_tab3)
        l_tk_bc.addLayout(r_btn_bc)
        l_tab_may.addWidget(grp_tk_bc)

        # Cơ cấu mở cửa & Góc nhìn máy rang
        grp_mech = QtWidgets.QGroupBox("🚪 Cơ Cấu Mở Cửa & Góc Nhìn Máy Rang")
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
        l_tab_may.addWidget(grp_mech)

        self.main_tabs.addTab(tab_may, "🏭 Máy Rang Củi (Trống 2 Lớp)")

        # ---------------- TAB 2: HỘP VÔ HÀNG INOX 3MM ----------------
        tab_hop = QtWidgets.QWidget()
        l_tab_hop = QtWidgets.QVBoxLayout(tab_hop)
        l_tab_hop.setSpacing(8)
        l_tab_hop.setContentsMargins(6, 6, 6, 6)

        # Header info
        hop_info = QtWidgets.QFrame()
        hop_info.setStyleSheet("background-color: #f1f5f9; border: 1px solid #e2e8f0; border-radius: 6px; padding: 4px;")
        hi_layout = QtWidgets.QHBoxLayout(hop_info)
        hi_layout.setContentsMargins(10, 3, 10, 3)
        t_hop = QtWidgets.QLabel("📥 Hộp Vô Hàng Inox 3mm: Đáy 30cm, Cao 65/30cm | Cửa nạp 20x30cm đáy trước")
        t_hop.setStyleSheet("font-weight: bold; color: #0f172a; font-size: 11px;")
        v_hop = QtWidgets.QLabel("Thể tích: ~62.6 Lít (~30kg)")
        v_hop.setStyleSheet("font-weight: bold; color: #0284c7; font-size: 11px;")
        hi_layout.addWidget(t_hop)
        hi_layout.addStretch()
        hi_layout.addWidget(v_hop)
        l_tab_hop.addWidget(hop_info)

        # Điều khiển Van Gạt Láp Ø20mm & Inox 3mm
        grp_van = QtWidgets.QGroupBox("🎛️ Kiểm Soát Hàng Qua Ống (Van Gạt Láp Ø20mm & Inox 3mm)")
        l_van = QtWidgets.QVBoxLayout(grp_van)
        l_van.setSpacing(6)

        r_van_top = QtWidgets.QHBoxLayout()
        self.btn_toggle_van_hop = QtWidgets.QPushButton("🔓 Mở Van Gạt (45°)")
        self.btn_toggle_van_hop.setStyleSheet("background-color: #16a34a; color: white; font-weight: bold;")
        self.btn_toggle_van_hop.clicked.connect(self.toggle_van_gat_hop)

        self.lbl_goc_van_hop = QtWidgets.QLabel("Góc van gạt: 🔴 0.0° (ĐÓNG KÍN)")
        self.lbl_goc_van_hop.setStyleSheet("font-weight: bold; color: #dc2626; font-size: 11.5px;")

        r_van_top.addWidget(self.btn_toggle_van_hop)
        r_van_top.addWidget(self.lbl_goc_van_hop)
        l_van.addLayout(r_van_top)

        # Slider góc mở van (0° đến 45°)
        r_van_sld = QtWidgets.QHBoxLayout()
        lbl_sld_van = QtWidgets.QLabel("Góc gạt:")
        lbl_sld_van.setStyleSheet("font-weight: bold; color: #475569;")
        self.sld_van_hop = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sld_van_hop.setRange(0, 45)
        self.sld_van_hop.setValue(0)
        self.sld_van_hop.valueChanged.connect(self.cap_nhat_goc_van_hop)

        btn_van_0 = QtWidgets.QPushButton("0° (Đóng)")
        btn_van_0.setStyleSheet("background-color: #fee2e2; color: #dc2626; font-size: 10px; padding: 4px 6px; font-weight: bold;")
        btn_van_0.clicked.connect(lambda: self.sld_van_hop.setValue(0))

        btn_van_25 = QtWidgets.QPushButton("25° (Vừa)")
        btn_van_25.setStyleSheet("background-color: #fef3c7; color: #d97706; font-size: 10px; padding: 4px 6px; font-weight: bold;")
        btn_van_25.clicked.connect(lambda: self.sld_van_hop.setValue(25))

        btn_van_45 = QtWidgets.QPushButton("45° (Hết)")
        btn_van_45.setStyleSheet("background-color: #dcfce7; color: #16a34a; font-size: 10px; padding: 4px 6px; font-weight: bold;")
        btn_van_45.clicked.connect(lambda: self.sld_van_hop.setValue(45))

        r_van_sld.addWidget(lbl_sld_van)
        r_van_sld.addWidget(self.sld_van_hop)
        r_van_sld.addWidget(btn_van_0)
        r_van_sld.addWidget(btn_van_25)
        r_van_sld.addWidget(btn_van_45)
        l_van.addLayout(r_van_sld)
        l_tab_hop.addWidget(grp_van)

        # Quan sát & Chi tiết hộp (có nút Ẩn/Hiện Thùng Bên Ngoài như Ẩn Vỏ Trống)
        grp_hop_vis = QtWidgets.QGroupBox("👁 Quan Sát & Ẩn Hiện Chi Tiết Hộp Vô Hàng")
        g_hop_vis = QtWidgets.QGridLayout(grp_hop_vis)
        g_hop_vis.setSpacing(6)

        self.btn_hop_trans = QtWidgets.QPushButton("👁 Xuyên Thấu Hộp")
        self.btn_hop_trans.setStyleSheet("background-color: #0d9488; color: white;")
        self.btn_hop_trans.clicked.connect(self.toggle_hop_transparency)

        self.btn_hide_hop_thung = QtWidgets.QPushButton("📦 Ẩn/Hiện Thùng Bên Ngoài")
        self.btn_hide_hop_thung.setStyleSheet("background-color: #6366f1; color: white;")
        self.btn_hide_hop_thung.clicked.connect(self.toggle_hop_thung_visibility)

        self.btn_hop_nap = QtWidgets.QPushButton("📦 Mở / Đậy Nắp Trên")
        self.btn_hop_nap.setStyleSheet("background-color: #7c3aed; color: white;")
        self.btn_hop_nap.clicked.connect(self.toggle_hop_nap)

        self.btn_hop_ref = QtWidgets.QPushButton("📐 Hiện Khối Tham Chiếu")
        self.btn_hop_ref.setStyleSheet("background-color: #ea580c; color: white;")
        self.btn_hop_ref.clicked.connect(self.toggle_hop_ref)

        g_hop_vis.addWidget(self.btn_hop_trans, 0, 0)
        g_hop_vis.addWidget(self.btn_hide_hop_thung, 0, 1)
        g_hop_vis.addWidget(self.btn_hop_nap, 1, 0)
        g_hop_vis.addWidget(self.btn_hop_ref, 1, 1)
        l_tab_hop.addWidget(grp_hop_vis)

        # Góc nhìn 1-Click Hộp Vô Hàng
        grp_hop_cams = QtWidgets.QGroupBox("📐 Góc Nhìn Hộp Vô Hàng (1-Click View)")
        r_hop_cams = QtWidgets.QHBoxLayout(grp_hop_cams)
        r_hop_cams.setSpacing(6)

        btn_hop_iso = QtWidgets.QPushButton("📐 Isometric Hộp")
        btn_hop_iso.setStyleSheet("background-color: #475569; color: white;")
        btn_hop_iso.clicked.connect(self.view_hop_isometric)

        btn_hop_side = QtWidgets.QPushButton("🔙 Nhìn Cạnh (Hình Thang)")
        btn_hop_side.setStyleSheet("background-color: #334155; color: white;")
        btn_hop_side.clicked.connect(self.view_hop_side)

        btn_hop_front = QtWidgets.QPushButton("🔜 Nhìn Mặt Trước (Cửa Nạp)")
        btn_hop_front.setStyleSheet("background-color: #334155; color: white;")
        btn_hop_front.clicked.connect(self.view_hop_front)

        r_hop_cams.addWidget(btn_hop_iso)
        r_hop_cams.addWidget(btn_hop_side)
        r_hop_cams.addWidget(btn_hop_front)
        l_tab_hop.addWidget(grp_hop_cams)

        # Bảng kê phôi cắt Inox 3mm (BOM)
        grp_bom = QtWidgets.QGroupBox("📋 Kích Thước Cắt Phôi Inox 3mm (BOM)")
        v_bom = QtWidgets.QVBoxLayout(grp_bom)
        txt_bom = QtWidgets.QTextEdit()
        txt_bom.setReadOnly(True)
        txt_bom.setStyleSheet("background-color: #f1f5f9; border: 1px solid #cbd5e1; font-size: 10.5px; color: #0f172a;")
        txt_bom.setHtml("""
        <table style="width: 100%; border-collapse: collapse; font-size: 10.5px;">
            <tr style="background-color: #e2e8f0; font-weight: bold;">
                <td style="padding: 3px;">Tên chi tiết</td>
                <td style="padding: 3px;">Kích thước phôi (mm)</td>
                <td style="padding: 3px;">SL</td>
            </tr>
            <tr>
                <td style="padding: 3px;">1. Tấm hông (Hình thang nhọn đáy)</td>
                <td style="padding: 3px;">Đỉnh 300, trước 650, sau 300, dốc 461 (Lỗ Ø20mm X=10.5, Z=353.9)</td>
                <td style="padding: 3px;"><b>2 tấm</b></td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 3px;">2. Tấm nắp đỉnh trên (vuông 30)</td>
                <td style="padding: 3px;">300 x 300 mm (Khoét lỗ tròn Ø200mm chính giữa nắp)</td>
                <td style="padding: 3px;"><b>1 tấm</b></td>
            </tr>
            <tr>
                <td style="padding: 3px;">3. Tấm vách đứng trước (45x30)</td>
                <td style="padding: 3px;">300 x 450 mm (Lỗ tròn Ø200mm cách đỉnh 1cm, đáy chừa cửa nạp 20x30cm)</td>
                <td style="padding: 3px;"><b>1 tấm</b></td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 3px;">4. Tấm vách đứng sau (vuông 30)</td>
                <td style="padding: 3px;">300 x 300 mm (Nguyên tấm vuông 30x30cm, Z=350->650)</td>
                <td style="padding: 3px;"><b>1 tấm</b></td>
            </tr>
            <tr>
                <td style="padding: 3px;">5. Tấm vách dốc nghiêng đáy</td>
                <td style="padding: 3px;">300 x 461 mm (Máng dốc nghiêng 49.4° hạt tự trượt xuống)</td>
                <td style="padding: 3px;"><b>1 tấm</b></td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 3px;">6. Ống nạp liệu tròn (trên xuống)</td>
                <td style="padding: 3px;">Ø199mm x Dài 300mm (Dày 2mm Inox 304, đút qua lỗ nắp Ø20cm)</td>
                <td style="padding: 3px;"><b>1 ống</b></td>
            </tr>
            <tr>
                <td style="padding: 3px;">7. Cây láp xoay van gạt (phi 20)</td>
                <td style="padding: 3px;">Ø20mm x Dài 428mm (Láp đặc, dư 10cm về bên phải làm tay gạt)</td>
                <td style="padding: 3px;"><b>1 cây</b></td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 3px;">8. Bộ 4 vòng bạc chặn trục (Ø32xØ20)</td>
                <td style="padding: 3px;">2 vòng dày 10mm hàn vào 2 hông hộp; 2 vòng ngoài 8mm hàn vào cây láp</td>
                <td style="padding: 3px;"><b>4 vòng</b></td>
            </tr>
            <tr>
                <td style="padding: 3px;">9. Lá van gạt đáy ống (Inox 3mm)</td>
                <td style="padding: 3px;">1 lá Inox 3mm bo tròn bán nguyệt R110mm ôm trọn đáy ống Ø19.9cm</td>
                <td style="padding: 3px;"><b>1 tấm</b></td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 3px;">10. Cơ cấu góc tọa độ 3 góc vuông (Ø20mm)</td>
                <td style="padding: 3px;">2 cây láp Ø20 dài 220mm hàn vuông góc ở trên (1 cây ngang +X, 1 cây đứng +Z tạo 3 góc vuông với láp Y)</td>
                <td style="padding: 3px;"><b>2 cây</b></td>
            </tr>
        </table>
        """)
        txt_bom.setFixedHeight(170)
        v_bom.addWidget(txt_bom)
        l_tab_hop.addWidget(grp_bom)

        self.main_tabs.addTab(tab_hop, "📥 Hộp Vô Hàng & Van Gạt (Ống Ø20)")

        # ---------------- TAB 3: BỘ CHỈNH GỐI BI TRỤC PHI 60MM (TRƯỜNG HỢP 1A) ----------------
        tab_chinh = QtWidgets.QWidget()
        l_tab_chinh = QtWidgets.QVBoxLayout(tab_chinh)
        l_tab_chinh.setSpacing(8)
        l_tab_chinh.setContentsMargins(6, 6, 6, 6)

        # Header info Tab 3
        chinh_info = QtWidgets.QFrame()
        chinh_info.setStyleSheet("background-color: #fef3c7; border: 1px solid #fde68a; border-radius: 6px; padding: 4px;")
        ci_layout = QtWidgets.QHBoxLayout(chinh_info)
        ci_layout.setContentsMargins(10, 3, 10, 3)
        t_chinh = QtWidgets.QLabel("⚙️ BỘ CHỈNH GỐI BI TRỤC PHI 60MM (6 CHI TIẾT MỚI)")
        t_chinh.setStyleSheet("font-weight: bold; color: #92400e; font-size: 11px;")
        v_chinh = QtWidgets.QLabel("Phần 1: Tháo Rời 6 Chi Tiết (Trái) | Phần 2: Cụm Lắp Ráp Hoàn Chỉnh (Phải)")
        v_chinh.setStyleSheet("font-weight: bold; color: #b45309; font-size: 11px;")
        ci_layout.addWidget(t_chinh)
        ci_layout.addStretch()
        ci_layout.addWidget(v_chinh)
        l_tab_chinh.addWidget(chinh_info)

        # Camera views Tab 3
        grp_cams_chinh = QtWidgets.QGroupBox("📐 Các Góc Nhìn & Quan Sát Bộ Chỉnh 6 Chi Tiết (Tab 3)")
        l_cams_chinh = QtWidgets.QVBoxLayout(grp_cams_chinh)
        l_cams_chinh.setSpacing(6)

        r_cams_c1 = QtWidgets.QHBoxLayout()
        self.btn_chinh_iso = QtWidgets.QPushButton("📐 Phối Cảnh Toàn Bộ")
        self.btn_chinh_iso.setStyleSheet("background-color: #0284c7; color: white; font-weight: bold;")
        self.btn_chinh_iso.clicked.connect(self.view_chinh_iso)

        self.btn_chinh_exploded = QtWidgets.QPushButton("💥 Phần 1: Tháo Rời 6 Chi Tiết")
        self.btn_chinh_exploded.setStyleSheet("background-color: #0891b2; color: white; font-weight: bold;")
        self.btn_chinh_exploded.clicked.connect(self.view_chinh_exploded)

        self.btn_chinh_assembled = QtWidgets.QPushButton("⭐ Phần 2: Cụm Lắp Ráp Hoàn Chỉnh")
        self.btn_chinh_assembled.setStyleSheet("background-color: #059669; color: white; font-weight: bold;")
        self.btn_chinh_assembled.clicked.connect(self.view_chinh_assembled)

        r_cams_c1.addWidget(self.btn_chinh_iso)
        r_cams_c1.addWidget(self.btn_chinh_exploded)
        r_cams_c1.addWidget(self.btn_chinh_assembled)
        l_cams_chinh.addLayout(r_cams_c1)

        r_cams_c2 = QtWidgets.QHBoxLayout()
        self.btn_chinh_front = QtWidgets.QPushButton("👁️ Chiếu Đứng (Front)")
        self.btn_chinh_front.setStyleSheet("background-color: #334155; color: white;")
        self.btn_chinh_front.clicked.connect(self.view_chinh_front)

        self.btn_chinh_top = QtWidgets.QPushButton("🔝 Chiếu Bằng (Top)")
        self.btn_chinh_top.setStyleSheet("background-color: #334155; color: white;")
        self.btn_chinh_top.clicked.connect(self.view_chinh_top)

        self.btn_chinh_right = QtWidgets.QPushButton("👉 Chiếu Cạnh (Right)")
        self.btn_chinh_right.setStyleSheet("background-color: #334155; color: white;")
        self.btn_chinh_right.clicked.connect(self.view_chinh_right)

        r_cams_c2.addWidget(self.btn_chinh_front)
        r_cams_c2.addWidget(self.btn_chinh_top)
        r_cams_c2.addWidget(self.btn_chinh_right)
        l_cams_chinh.addLayout(r_cams_c2)
        l_tab_chinh.addWidget(grp_cams_chinh)

        # Bảng danh mục 6 chi tiết cấu tạo
        grp_bom_chinh = QtWidgets.QGroupBox("📋 Danh Mục 6 Chi Tiết Bộ Chỉnh Gối Bi Trục Phi 60mm")
        v_bom_c = QtWidgets.QVBoxLayout(grp_bom_chinh)
        v_bom_c.setContentsMargins(6, 6, 6, 6)

        txt_bom_c = QtWidgets.QTextEdit()
        txt_bom_c.setReadOnly(True)
        txt_bom_c.setStyleSheet("background-color: #ffffff; border: 1px solid #e2e8f0; font-size: 10.5px; color: #1e293b;")
        txt_bom_c.setHtml("""
        <table style="width: 100%; border-collapse: collapse; font-family: 'Segoe UI', Arial;">
            <tr style="background-color: #fef3c7; color: #92400e; font-weight: bold;">
                <th style="padding: 5px; text-align: center; border-bottom: 1px solid #cbd5e1; width: 35px;">STT</th>
                <th style="padding: 5px; text-align: left; border-bottom: 1px solid #cbd5e1; width: 170px;">Tên Chi Tiết</th>
                <th style="padding: 5px; text-align: left; border-bottom: 1px solid #cbd5e1;">Quy Cách Kỹ Thuật & Chức Năng</th>
                <th style="padding: 5px; text-align: left; border-bottom: 1px solid #cbd5e1; width: 110px;">Vật Liệu</th>
            </tr>
            <tr>
                <td style="padding: 4px; text-align: center; font-weight: bold;">1</td>
                <td style="padding: 4px; font-weight: bold; color: #1e293b;">Chân bệ trụ ren trong</td>
                <td style="padding: 4px;">Bích vuông 165x165mm có 4 lỗ Ø14.5mm (đã bỏ 4 ốc màu) + Thân trụ cao đúng 15cm (150mm), ren trong M110x3</td>
                <td style="padding: 4px;">Gang xám đúc FC250</td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 4px; text-align: center; font-weight: bold;">2</td>
                <td style="padding: 4px; font-weight: bold; color: #1e293b;">Phần cố định ren ngoài</td>
                <td style="padding: 4px;">Ống ren M110 vặn vào chân 1, ĐẦU PHẢI LỤC GIÁC TO S=125mm dùng cờ-lê vặn tăng chỉnh khe hở</td>
                <td style="padding: 4px;">Thép chế tạo máy C45</td>
            </tr>
            <tr>
                <td style="padding: 4px; text-align: center; font-weight: bold;">3</td>
                <td style="padding: 4px; font-weight: bold; color: #1e293b;">Long đền mỏng 5mm</td>
                <td style="padding: 4px;">Long đền / tán hãm lục giác ren trong M110, DÀY ĐÚNG 5MM (ĐÃ XÓA CÂY CÙI TRÒN) khóa cứng vị trí</td>
                <td style="padding: 4px;">Thép C45 / Mạ kẽm</td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 4px; text-align: center; font-weight: bold;">4</td>
                <td style="padding: 4px; font-weight: bold; color: #1e293b;">Ống trụ tròn nhẵn 3mm</td>
                <td style="padding: 4px;">Ống trụ tròn nhẵn dày đúng 3mm (Øngoài 86 / Øtrong 80mm) nằm trong ống 2, có gờ chặn định vị bạc đạn</td>
                <td style="padding: 4px;">Thép hợp kim mài bóng</td>
            </tr>
            <tr>
                <td style="padding: 4px; text-align: center; font-weight: bold;">5</td>
                <td style="padding: 4px; font-weight: bold; color: #1e293b;">Bạc đạn đỡ trục Ø60mm</td>
                <td style="padding: 4px;">Bạc đạn lỗ trong Ø60mm ôm cốt láp, Øngoài 80mm lọt khít trong ống 4, có bi cầu thép và phớt chắn bụi</td>
                <td style="padding: 4px;">Thép ổ lăn GCr15</td>
            </tr>
            <tr style="background-color: #f8fafc;">
                <td style="padding: 4px; text-align: center; font-weight: bold;">6</td>
                <td style="padding: 4px; font-weight: bold; color: #1e293b;">Mặt bít</td>
                <td style="padding: 4px;">Nắp bít tròn Ø94mm bắt 4 vít M6 vào mặt đầu ống 2, chặn giữ bạc đạn và ngăn 100% bụi vỏ lụa</td>
                <td style="padding: 4px;">Thép dập / Mạ kẽm</td>
            </tr>
        </table>
        """)
        txt_bom_c.setFixedHeight(200)
        v_bom_c.addWidget(txt_bom_c)
        l_tab_chinh.addWidget(grp_bom_chinh)

        self.main_tabs.addTab(tab_chinh, "⚙️ Tab 3: Bộ Chỉnh 6 Chi Tiết (Chân 15cm)")

        layout.addWidget(self.main_tabs)
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

        # Quay đồng bộ cả 7 đối tượng: Vỏ Trong, Áo Ngoài, Cây Láp, Cây Chống, Cánh Ngoài, Cánh Trong, Đáy Sau
        for obj in [self.obj_trong, self.obj_ao_ngoai, self.obj_lap, self.obj_chong, self.obj_canh_ngoai, self.obj_canh_trong, self.obj_day_sau]:
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
            for obj, val in [(self.obj_trong, 45), (self.obj_ao_ngoai, 55), (self.obj_day_sau, 45)]:
                if obj and hasattr(obj, "ViewObject") and obj.ViewObject:
                    obj.ViewObject.Transparency = val if self.is_transparent else 0

    def toggle_drum_visibility(self):
        self.is_drum_visible = not self.is_drum_visible
        if kiem_tra_co_gui():
            for obj in [self.obj_trong, self.obj_ao_ngoai, self.obj_day_sau]:
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
        p_hinge = App.Vector(249.5, 626.0, 0.0)
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
            p_hinge = App.Vector(249.5, 626.0, 0.0)
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
        if kiem_tra_co_gui() and self.doc:
            try:
                Gui.setActiveDocument(self.doc)
                Gui.SendMsgToActiveView("ViewAxo")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def view_rear(self):
        if kiem_tra_co_gui() and self.doc:
            try:
                Gui.setActiveDocument(self.doc)
                Gui.SendMsgToActiveView("ViewRear")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def view_front(self):
        if kiem_tra_co_gui() and self.doc:
            try:
                Gui.setActiveDocument(self.doc)
                Gui.SendMsgToActiveView("ViewFront")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def toggle_hop_may_visibility(self):
        """Ẩn/Hiện cụm Hộp Vô Hàng gắn trên mặt máy sau của máy rang củi."""
        self.is_hop_may_visible = not getattr(self, "is_hop_may_visible", True)
        if hasattr(self, "items_hop_may") and self.items_hop_may:
            for ob in self.items_hop_may:
                if ob and hasattr(ob, "ViewObject") and ob.ViewObject:
                    ob.ViewObject.Visibility = self.is_hop_may_visible
        if hasattr(self, "obj_mang_nap") and self.obj_mang_nap:
            if hasattr(self.obj_mang_nap, "ViewObject") and self.obj_mang_nap.ViewObject:
                self.obj_mang_nap.ViewObject.Visibility = self.is_hop_may_visible
        if hasattr(self, "btn_hop_may"):
            if self.is_hop_may_visible:
                self.btn_hop_may.setText("📥 Ẩn Hộp Vô Hàng (Mặt Trước)")
                self.btn_hop_may.setStyleSheet("background-color: #059669; color: white; font-weight: bold;")
            else:
                self.btn_hop_may.setText("📥 Hiện Hộp Vô Hàng (Mặt Trước)")
                self.btn_hop_may.setStyleSheet("background-color: #f59e0b; color: white; font-weight: bold;")

    # ---------------- PHƯƠNG THỨC TAB 2: HỘP VÔ HÀNG ----------------
    def cap_nhat_goc_van_hop(self, val):
        self.goc_van_hop = float(val)
        pivot = App.Vector(10.5, 0.0, 353.88)
        rot = App.Rotation(App.Vector(0, 1, 0), self.goc_van_hop)
        pos = pivot - rot.multVec(pivot)
        local_plc = App.Placement(pos, rot)

        # 1. Cập nhật Tab 2: Hộp vô hàng standalone
        if hasattr(self, "hop_van") and self.hop_van:
            try:
                self.hop_van.Placement = local_plc
            except Exception:
                pass
        if hasattr(self, "doc_hop") and self.doc_hop:
            try:
                self.doc_hop.recompute()
            except Exception:
                pass

        # 2. Cập nhật Tab 1: Hộp vô hàng gắn trên mặt sau máy rang
        if hasattr(self, "hop_van_may") and self.hop_van_may and hasattr(self, "plc_hop"):
            try:
                self.hop_van_may.Placement = self.plc_hop.multiply(local_plc)
            except Exception:
                pass
        if hasattr(self, "doc") and self.doc:
            try:
                self.doc.recompute()
            except Exception:
                pass

        if hasattr(self, "lbl_goc_van_hop"):
            if self.goc_van_hop == 0:
                self.lbl_goc_van_hop.setText("Góc van gạt: 🔴 0.0° (ĐÓNG KÍN)")
                self.lbl_goc_van_hop.setStyleSheet("font-weight: bold; color: #dc2626; font-size: 11.5px;")
                if hasattr(self, "btn_toggle_van_hop"):
                    self.btn_toggle_van_hop.setText("🔓 Mở Van Gạt (45°)")
                    self.btn_toggle_van_hop.setStyleSheet("background-color: #16a34a; color: white; font-weight: bold;")
            else:
                pct = int(self.goc_van_hop / 45.0 * 100.0)
                self.lbl_goc_van_hop.setText(f"Góc van gạt: 🟢 {self.goc_van_hop:.1f}° (Mở {pct}%)")
                self.lbl_goc_van_hop.setStyleSheet("font-weight: bold; color: #16a34a; font-size: 11.5px;")
                if hasattr(self, "btn_toggle_van_hop") and self.goc_van_hop >= 40:
                    self.btn_toggle_van_hop.setText("🔒 Đóng Van Gạt (0°)")
                    self.btn_toggle_van_hop.setStyleSheet("background-color: #dc2626; color: white; font-weight: bold;")

    def toggle_van_gat_hop(self):
        target = 45 if self.goc_van_hop < 20 else 0
        if hasattr(self, "sld_van_hop"):
            self.sld_van_hop.setValue(target)

    def toggle_hop_thung_visibility(self):
        """Ẩn / hiện toàn bộ các tấm vỏ thùng bên ngoài của hộp vô hàng (như ẩn vỏ trống)."""
        self.is_hop_thung_visible = not self.is_hop_thung_visible
        if kiem_tra_co_gui():
            # 1. Ẩn/hiện Tab 2: Hộp standalone
            for obj in [
                self.hop_hong_trai,
                self.hop_hong_phai,
                self.hop_vach_sau,
                self.hop_day,
                self.hop_nap,
                self.hop_vach_truoc,
            ]:
                if obj and hasattr(obj, "ViewObject") and obj.ViewObject:
                    obj.ViewObject.Visibility = self.is_hop_thung_visible

            # 2. Ẩn/hiện Tab 1: Vỏ hộp gắn trên mặt máy sau
            if hasattr(self, "items_hop_may") and self.items_hop_may:
                for idx in [0, 1, 2, 3, 4, 5]: # hông trái, hông phải, vách sau, đáy, nắp, vách trước
                    if idx < len(self.items_hop_may):
                        ob = self.items_hop_may[idx]
                        if ob and hasattr(ob, "ViewObject") and ob.ViewObject:
                            ob.ViewObject.Visibility = self.is_hop_thung_visible
        if self.is_hop_thung_visible:
            self.btn_hide_hop_thung.setText("📦 Ẩn Thùng Bên Ngoài")
            self.btn_hide_hop_thung.setStyleSheet("background-color: #6366f1; color: white;")
        else:
            self.btn_hide_hop_thung.setText("📦 Hiện Thùng Bên Ngoài")
            self.btn_hide_hop_thung.setStyleSheet("background-color: #475569; color: white;")

    def toggle_hop_transparency(self):
        self.is_hop_transparent = not self.is_hop_transparent
        val = 50 if self.is_hop_transparent else 0
        if kiem_tra_co_gui():
            for obj in [
                self.hop_hong_trai,
                self.hop_hong_phai,
                self.hop_vach_sau,
                self.hop_day,
                self.hop_vach_truoc,
                self.hop_ong,
                self.hop_van,
            ]:
                if obj and hasattr(obj, "ViewObject") and obj.ViewObject:
                    obj.ViewObject.Transparency = val
        if self.is_hop_transparent:
            self.btn_hop_trans.setText("👁 Đục Vỏ Hộp (Bình Thường)")
            self.btn_hop_trans.setStyleSheet("background-color: #475569; color: white;")
        else:
            self.btn_hop_trans.setText("👁 Xuyên Thấu Hộp")
            self.btn_hop_trans.setStyleSheet("background-color: #0284c7; color: white;")

    def toggle_hop_nap(self):
        self.is_hop_top_open = not self.is_hop_top_open
        if kiem_tra_co_gui() and self.hop_nap and hasattr(self.hop_nap, "ViewObject") and self.hop_nap.ViewObject:
            self.hop_nap.ViewObject.Visibility = not self.is_hop_top_open
        if self.is_hop_top_open:
            self.btn_hop_nap.setText("📦 Đậy Nắp Trên")
            self.btn_hop_nap.setStyleSheet("background-color: #475569; color: white;")
        else:
            self.btn_hop_nap.setText("📦 Mở / Đậy Nắp Trên")
            self.btn_hop_nap.setStyleSheet("background-color: #7c3aed; color: white;")

    def toggle_hop_ref(self):
        self.is_hop_ref_visible = not self.is_hop_ref_visible
        if kiem_tra_co_gui():
            for obj in [self.hop_ref_rect, self.hop_ref_tri]:
                if obj and hasattr(obj, "ViewObject") and obj.ViewObject:
                    obj.ViewObject.Visibility = self.is_hop_ref_visible
        if self.is_hop_ref_visible:
            self.btn_hop_ref.setText("📐 Ẩn Khối Tham Chiếu")
            self.btn_hop_ref.setStyleSheet("background-color: #475569; color: white;")
        else:
            self.btn_hop_ref.setText("📐 Hiện Khối Tham Chiếu")
            self.btn_hop_ref.setStyleSheet("background-color: #ea580c; color: white;")

    def view_hop_isometric(self):
        if kiem_tra_co_gui() and self.doc_hop:
            try:
                Gui.setActiveDocument(self.doc_hop)
                Gui.SendMsgToActiveView("ViewAxo")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def view_hop_side(self):
        if kiem_tra_co_gui() and self.doc_hop:
            try:
                Gui.setActiveDocument(self.doc_hop)
                Gui.SendMsgToActiveView("ViewRight")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def view_hop_front(self):
        if kiem_tra_co_gui() and self.doc_hop:
            try:
                Gui.setActiveDocument(self.doc_hop)
                Gui.SendMsgToActiveView("ViewFront")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def toggle_chinh_may_visibility(self):
        """Ẩn/Hiện bộ chỉnh trên 2 mặt máy."""
        self.is_chinh_may_visible = not getattr(self, "is_chinh_may_visible", True)
        if kiem_tra_co_gui() and hasattr(self, "items_chinh_may"):
            for ob in self.items_chinh_may:
                if ob and hasattr(ob, "ViewObject") and ob.ViewObject:
                    ob.ViewObject.Visibility = self.is_chinh_may_visible
            if self.doc:
                self.doc.recompute()
        if hasattr(self, "btn_chinh_may"):
            if self.is_chinh_may_visible:
                self.btn_chinh_may.setText("⚙️ Ẩn Bộ Chỉnh Trên Máy")
                self.btn_chinh_may.setStyleSheet("background-color: #d97706; color: white; font-weight: bold;")
            else:
                self.btn_chinh_may.setText("⚙️ Hiện Bộ Chỉnh Trên Máy")
                self.btn_chinh_may.setStyleSheet("background-color: #475569; color: white; font-weight: bold;")

    def toggle_chinh_transparency(self):
        """Bật/tắt xuyên thấu thân gang để soi bạc đạn UC212 và cốt láp bên trong."""
        self.is_chinh_transparency = not getattr(self, "is_chinh_transparency", False)
        val = 65 if self.is_chinh_transparency else 0
        if kiem_tra_co_gui() and hasattr(self, "items_chinh_may"):
            for ob in self.items_chinh_may:
                if ob and hasattr(ob, "ViewObject") and ob.ViewObject:
                    if "Than_Goi_Gang" in ob.Name or "Nap_Tron" in ob.Name or "Co_Luc_Giac" in ob.Name:
                        ob.ViewObject.Transparency = val
            if self.doc:
                self.doc.recompute()
        if hasattr(self, "btn_chinh_transparency"):
            if self.is_chinh_transparency:
                self.btn_chinh_transparency.setText("👁️ Tắt Xuyên Thấu Gang")
                self.btn_chinh_transparency.setStyleSheet("background-color: #0891b2; color: white; font-weight: bold;")
            else:
                self.btn_chinh_transparency.setText("🔍 Xuyên Thấu Vỏ Gang (Soi Bi)")
                self.btn_chinh_transparency.setStyleSheet("background-color: #0284c7; color: white; font-weight: bold;")

    # ---------------- PHƯƠNG THỨC TAB 3: BỘ CHỈNH CHI TIẾT ----------------
    def view_chinh_iso(self):
        """Phối cảnh toàn bộ cả 2 phần (tháo rời & lắp ráp)."""
        if kiem_tra_co_gui() and self.doc_chinh:
            try:
                Gui.setActiveDocument(self.doc_chinh)
                Gui.SendMsgToActiveView("ViewAxo")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def view_chinh_exploded(self):
        """Soi cận cảnh Phần 1: Tháo rời 6 chi tiết (X = -280mm)."""
        if kiem_tra_co_gui() and self.doc_chinh:
            try:
                Gui.setActiveDocument(self.doc_chinh)
                Gui.Selection.clearSelection()
                if hasattr(self, "items_chinh") and self.items_chinh:
                    for obj in self.items_chinh[:6]:
                        Gui.Selection.addSelection(obj)
                    Gui.SendMsgToActiveView("ViewFit")
                    Gui.Selection.clearSelection()
            except Exception:
                pass

    def view_chinh_assembled(self):
        """Soi cận cảnh Phần 2: Cụm lắp ráp hoàn chỉnh 100% (X = +280mm)."""
        if kiem_tra_co_gui() and self.doc_chinh:
            try:
                Gui.setActiveDocument(self.doc_chinh)
                Gui.Selection.clearSelection()
                if hasattr(self, "items_chinh") and self.items_chinh and len(self.items_chinh) >= 12:
                    for obj in self.items_chinh[6:12]:
                        Gui.Selection.addSelection(obj)
                    Gui.SendMsgToActiveView("ViewFit")
                    Gui.Selection.clearSelection()
            except Exception:
                pass

    def view_chinh_front(self):
        if kiem_tra_co_gui() and self.doc_chinh:
            try:
                Gui.setActiveDocument(self.doc_chinh)
                Gui.SendMsgToActiveView("ViewFront")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def view_chinh_top(self):
        if kiem_tra_co_gui() and self.doc_chinh:
            try:
                Gui.setActiveDocument(self.doc_chinh)
                Gui.SendMsgToActiveView("ViewTop")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def view_chinh_right(self):
        if kiem_tra_co_gui() and self.doc_chinh:
            try:
                Gui.setActiveDocument(self.doc_chinh)
                Gui.SendMsgToActiveView("ViewRight")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    # ---------------- ĐIỀU HƯỚNG TAB & TÀI LIỆU ----------------
    def on_tab_changed(self, idx):
        if idx == 0:
            if kiem_tra_co_gui() and self.doc:
                try:
                    Gui.setActiveDocument(self.doc)
                    Gui.SendMsgToActiveView("ViewAxo")
                    Gui.SendMsgToActiveView("ViewFit")
                except Exception:
                    pass
        elif idx == 1:
            if kiem_tra_co_gui() and self.doc_hop:
                try:
                    Gui.setActiveDocument(self.doc_hop)
                    Gui.SendMsgToActiveView("ViewAxo")
                    Gui.SendMsgToActiveView("ViewFit")
                except Exception:
                    pass
        elif idx == 2:
            if kiem_tra_co_gui() and self.doc_chinh:
                try:
                    Gui.setActiveDocument(self.doc_chinh)
                    Gui.SendMsgToActiveView("ViewAxo")
                    Gui.SendMsgToActiveView("ViewFit")
                except Exception:
                    pass

    def chuyen_tab_may(self):
        """Chuyển sang Tab 1: Máy Rang Củi 2 Lớp."""
        if hasattr(self, "main_tabs"):
            self.main_tabs.setCurrentIndex(0)
        if kiem_tra_co_gui() and self.doc:
            try:
                Gui.setActiveDocument(self.doc)
                Gui.SendMsgToActiveView("ViewAxo")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def chuyen_tab_hop(self):
        """Chuyển sang Tab 2: Hộp Vô Hàng Inox 3mm."""
        if hasattr(self, "main_tabs"):
            self.main_tabs.setCurrentIndex(1)
        if kiem_tra_co_gui() and self.doc_hop:
            try:
                Gui.setActiveDocument(self.doc_hop)
                Gui.SendMsgToActiveView("ViewAxo")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def chuyen_tab_chinh(self):
        """Chuyển sang Tab 3: Bộ Chỉnh Gối Bi Trục Phi 60mm."""
        if hasattr(self, "main_tabs"):
            self.main_tabs.setCurrentIndex(2)
        if kiem_tra_co_gui() and self.doc_chinh:
            try:
                Gui.setActiveDocument(self.doc_chinh)
                Gui.SendMsgToActiveView("ViewAxo")
                Gui.SendMsgToActiveView("ViewFit")
            except Exception:
                pass

    def mo_thong_so_md(self):
        import os
        base_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else r"d:\CAD\Free_CAD"
        md_path = os.path.join(base_dir, "THONG_SO_KY_THUAT.md")
        if not os.path.exists(md_path):
            md_path = r"d:\CAD\Free_CAD\THONG_SO_KY_THUAT.md"
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

    # 1. Đóng sạch sẽ tất cả tài liệu cũ và tiến trình cũ đang mở
    dong_sach_tat_ca_tai_lieu_cu()
    _TRONG_DIEU_KHIEN_WINDOW = None

    # 2. Tạo TAB 1: Máy Rang Củi Hoàn Chỉnh
    doc_may = App.newDocument("1_May_Rang_Cui_Hoan_Chinh")
    items_may = tao_mo_hinh_chi_tiet(doc_may)
    doc_may.recompute()

    # 3. Tạo TAB 2: Hộp Vô Hàng Inox 3mm (Hình thang vuông, cách 30cm, bọc toàn bộ)
    doc_hop = App.newDocument("2_Hop_Vo_Hang_Inox_3mm")
    items_hop = tao_hop_vo_hang(doc_hop)
    doc_hop.recompute()

    # 4. Tạo TAB 3: Bộ Chỉnh Gối Bi Trục Phi 60mm (Trường hợp 1A: Tháo rời & Lắp ráp)
    doc_chinh = App.newDocument("3_Bo_Chinh_Goi_Bi_Truc_Phi60")
    items_chinh = tao_tab_3_bo_chinh(doc_chinh)
    doc_chinh.recompute()

    # 5. Căn góc nhìn Isometric, FitAll cho cả 3 tab và hiển thị bảng điều khiển
    if kiem_tra_co_gui():
        # Căn góc nhìn cho Tab 1
        try:
            Gui.setActiveDocument(doc_may)
            Gui.SendMsgToActiveView("ViewAxo")
            Gui.SendMsgToActiveView("ViewFit")
        except Exception:
            pass

        # Căn góc nhìn cho Tab 2
        try:
            Gui.setActiveDocument(doc_hop)
            Gui.SendMsgToActiveView("ViewAxo")
            Gui.SendMsgToActiveView("ViewFit")
        except Exception:
            pass

        # Căn góc nhìn cho Tab 3
        try:
            Gui.setActiveDocument(doc_chinh)
            Gui.SendMsgToActiveView("ViewAxo")
            Gui.SendMsgToActiveView("ViewFit")
        except Exception:
            pass

        # Đặt lại active tab ban đầu là Tab 1 (Máy rang)
        try:
            Gui.setActiveDocument(doc_may)
        except Exception:
            pass

        main_win = None
        try:
            main_win = Gui.getMainWindow()
        except Exception:
            pass

        _TRONG_DIEU_KHIEN_WINDOW = BangDieuKhienHanCayTru(
            doc_may,
            *items_may,
            doc_hop=doc_hop,
            items_hop=items_hop,
            doc_chinh=doc_chinh,
            items_chinh=items_chinh,
            parent=main_win,
        )
        _TRONG_DIEU_KHIEN_WINDOW.show()

        App.Console.PrintMessage("\n" + "=" * 80 + "\n")
        App.Console.PrintMessage(">> ĐÃ MỞ TỰ ĐỘNG CẢ 3 TAB: MÁY RANG CỦI, HỘP VÔ HÀNG VÀ BỘ CHỈNH 6 CHI TIẾT MỚI!\n")
        App.Console.PrintMessage(">> TAB 1: [1_May_Rang_Cui_Hoan_Chinh] - Trống 2 lớp, 10 cánh, bệ đế, lò gạch sa mốt, bộ chỉnh gắn 2 mặt máy.\n")
        App.Console.PrintMessage(">> TAB 2: [2_Hop_Vo_Hang_Inox_3mm] - Hình thang vuông (chữ nhật + tam giác), cách 30cm, bọc toàn bộ.\n")
        App.Console.PrintMessage(">> TAB 3: [3_Bo_Chinh_Goi_Bi_Truc_Phi60] - Bộ Chỉnh 6 Chi Tiết: Phần 1 Tháo Rời (Trái) & Phần 2 Lắp Ráp Hoàn Chỉnh (Phải).\n")
        App.Console.PrintMessage(">> Chân trụ cao 15cm ren trong M110, bỏ 4 ốc màu, tán khóa lục giác 20cm, ống lót nhẵn 3mm, bạc đạn Ø60mm, mặt bít!\n")
        App.Console.PrintMessage("=" * 80 + "\n")
    else:
        print(">> [CLI Mode] Đã tạo thành công 3 Tab tài liệu:")
        print(">> TAB 1: 1_May_Rang_Cui_Hoan_Chinh (Máy rang củi 2 lớp & Bộ chỉnh gối bi gắn 2 mặt máy)")
        print(">> TAB 2: 2_Hop_Vo_Hang_Inox_3mm (Hộp vô hàng inox 3mm hình thang vuông)")
        print(">> TAB 3: 3_Bo_Chinh_Goi_Bi_Truc_Phi60 (Bộ chỉnh 6 chi tiết: Chân trụ 15cm ren trong, ống ren ngoài, tán khóa 20cm, ống lót 3mm, bạc đạn, mặt bít)")


if __name__ == "__main__" or __name__ == "FreeCAD":
    chay_mo_phong()
