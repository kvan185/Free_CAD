# -*- coding: utf-8 -*-
"""
HỆ THỐNG XUẤT HỒ SƠ THIẾT KẾ CƠ KHÍ CHÍNH XÁC:
- 6 Bản vẽ kỹ thuật 2D chi tiết (Hình chiếu Đứng, Bằng, Cạnh + Mặt cắt + Kích thước + Dung sai + Khung tên)
- 1 Bản vẽ tổng hợp cụm lắp ráp & tháo rời (BOM vật tư)
- Nhúng ảnh mô hình 3D Solid trực tiếp vào từng bản vẽ
- Xuất 8 file 3D STEP tiêu chuẩn quốc tế (.step)
- Xuất 6 file 2D DXF vector cho máy CNC (.dxf)
Tác giả: Khánh Văn <kvan18052004@gmail.com>
"""
import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass
if hasattr(sys.stderr, 'reconfigure'):
    try: sys.stderr.reconfigure(encoding='utf-8')
    except Exception: pass

sys.path.extend([r'C:\Program Files\FreeCAD 1.1\bin', r'C:\Program Files\FreeCAD 1.1\lib'])

import math
import FreeCAD as App
import Part
import importDXF

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Rectangle, Circle, Wedge, Arc
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Thư mục lưu trữ
OUT_DIR = r"c:\VAN\CAD\ban_ve_2d"
DXF_DIR = r"c:\VAN\CAD\dxf"
STEP_DIR = r"c:\VAN\CAD\step"
ARTIFACT_DIR = r"C:\Users\admin\.gemini\antigravity\brain\0b789148-0c1a-433f-9f39-ee380f84bb46"
THUMB_DIR = os.path.join(ARTIFACT_DIR, "scratch", "thumbs")

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(DXF_DIR, exist_ok=True)
os.makedirs(STEP_DIR, exist_ok=True)
os.makedirs(THUMB_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Segoe UI', 'Tahoma', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 1. TẠO CÁC MÔ HÌNH 3D SOLID BẰNG FREECAD
# ==========================================

def tao_solid_chi_tiet_1():
    # 1. Chân bệ trụ ren trong M110 cao 15cm (150mm)
    W_bich = 165.0
    T_bich = 16.0
    H_chan = 150.0
    R_tru = 65.0
    R_ren_dinh = 55.0
    R_ren_day = 52.0

    p_bich = Part.makeBox(W_bich, W_bich, T_bich, App.Vector(-W_bich/2, -W_bich/2, 0))
    edges_Z = [e for e in p_bich.Edges if abs(e.tangentAt(0).z) > 0.9]
    p_bich = p_bich.makeFillet(15.0, edges_Z)

    # 4 lỗ bu lông Ø14.5
    for xb in [-65.0, 65.0]:
        for yb in [-65.0, 65.0]:
            hole = Part.makeCylinder(7.25, T_bich + 10.0, App.Vector(xb, yb, -5.0), App.Vector(0, 0, 1))
            p_bich = p_bich.cut(hole)

    # Trụ tròn cao 150mm và gờ loe chân
    cyl_tru = Part.makeCylinder(R_tru, H_chan - T_bich, App.Vector(0, 0, T_bich), App.Vector(0, 0, 1))
    cone_loe = Part.makeCone(R_tru + 10.0, R_tru, 25.0, App.Vector(0, 0, T_bich), App.Vector(0, 0, 1))

    # Lỗ ren trong M110 sâu 110mm (đáy có lỗ thông phoi Ø104)
    bore_ren = Part.makeCylinder(R_ren_day, 115.0, App.Vector(0, 0, H_chan - 110.0), App.Vector(0, 0, 1))
    bore_day = Part.makeCylinder(52.0, H_chan - 110.0 + 5.0, App.Vector(0, 0, -2.0), App.Vector(0, 0, 1))

    solid = p_bich.fuse(cyl_tru).fuse(cone_loe).cut(bore_ren).cut(bore_day)
    return solid

def tao_solid_chi_tiet_2():
    # 2. Ống cố định ren ngoài M110 dài 115mm, đầu lục giác to S125 dày 18mm
    L_ren = 115.0
    T_hex = 18.0
    R_ren = 54.5
    R_in = 43.0  # Lòng trong Ø86mm
    R_hex = 72.2 # S=125mm -> R = 125 / sqrt(3) = 72.17mm

    cyl_ren = Part.makeCylinder(R_ren, L_ren, App.Vector(0, 0, 0), App.Vector(0, 0, 1))
    
    # Đầu lục giác S125
    pts = []
    for i in range(6):
        ang = math.radians(i * 60.0 + 30.0)
        pts.append(App.Vector(R_hex * math.cos(ang), R_hex * math.sin(ang), L_ren))
    pts.append(pts[0])
    hex_head = Part.Face(Part.makePolygon(pts)).extrude(App.Vector(0, 0, T_hex))

    solid = cyl_ren.fuse(hex_head)
    bore = Part.makeCylinder(R_in, L_ren + T_hex + 10.0, App.Vector(0, 0, -5.0), App.Vector(0, 0, 1))
    solid = solid.cut(bore)

    # 4 lỗ ren M6 sâu 12mm trên PCD Ø94
    for i in range(4):
        ang = math.radians(i * 90.0 + 45.0)
        xs = 47.0 * math.cos(ang)
        ys = 47.0 * math.sin(ang)
        m6 = Part.makeCylinder(2.5, 14.0, App.Vector(xs, ys, L_ren + T_hex - 12.0), App.Vector(0, 0, 1))
        solid = solid.cut(m6)

    return solid

def tao_solid_chi_tiet_3():
    # 3. Long đền / tán khóa lục giác mỏng đúng 5.0mm, S115mm, ren trong M110x3
    T_nut = 5.0
    R_hex = 66.4 # S=115mm -> R = 115 / sqrt(3) = 66.4mm
    R_ren = 55.0

    pts = []
    for i in range(6):
        ang = math.radians(i * 60.0 + 30.0)
        pts.append(App.Vector(R_hex * math.cos(ang), R_hex * math.sin(ang), 0))
    pts.append(pts[0])
    solid = Part.Face(Part.makePolygon(pts)).extrude(App.Vector(0, 0, T_nut))
    hole = Part.makeCylinder(R_ren, T_nut + 4.0, App.Vector(0, 0, -2.0), App.Vector(0, 0, 1))
    solid = solid.cut(hole)
    return solid

def tao_solid_chi_tiet_4():
    # 4. Ống trụ tròn nhẵn dày đúng 3mm (Ø86 x Ø80 x dài 65mm), gờ chặn dày 5mm lỗ Ø62
    L = 65.0
    R_out = 43.0
    R_in = 40.0
    R_lip = 31.0

    cyl_out = Part.makeCylinder(R_out, L, App.Vector(0, 0, 0), App.Vector(0, 0, 1))
    bore_in = Part.makeCylinder(R_in, L + 10.0, App.Vector(0, 0, -5.0), App.Vector(0, 0, 1))
    tube = cyl_out.cut(bore_in)

    # Gờ chặn dày 5mm ở đáy
    lip = Part.makeCylinder(R_in, 5.0, App.Vector(0, 0, 0), App.Vector(0, 0, 1)).cut(
        Part.makeCylinder(R_lip, 10.0, App.Vector(0, 0, -2.0), App.Vector(0, 0, 1))
    )
    solid = tube.fuse(lip)
    return solid

def tao_solid_chi_tiet_5():
    # 5. Bạc đạn đỡ trục phi 60mm (6012-2RS: Ø60 x Ø80 x 22mm)
    B = 22.0
    R_out = 40.0
    R_in = 30.0

    out_ring = Part.makeCylinder(R_out, B, App.Vector(0, 0, 0), App.Vector(0, 0, 1)).cut(
        Part.makeCylinder(R_out - 4.0, B + 4.0, App.Vector(0, 0, -2.0), App.Vector(0, 0, 1))
    )
    in_ring = Part.makeCylinder(R_in + 4.0, B, App.Vector(0, 0, 0), App.Vector(0, 0, 1)).cut(
        Part.makeCylinder(R_in, B + 4.0, App.Vector(0, 0, -2.0), App.Vector(0, 0, 1))
    )
    balls = []
    for i in range(10):
        ang = i * (2.0 * math.pi / 10.0)
        bx = 35.0 * math.cos(ang)
        by = 35.0 * math.sin(ang)
        balls.append(Part.makeSphere(4.0, App.Vector(bx, by, B/2.0)))

    # Nắp cao su 2RS
    seal_f = Part.makeCylinder(R_out - 1.0, 1.2, App.Vector(0, 0, B - 1.2), App.Vector(0, 0, 1)).cut(
        Part.makeCylinder(R_in + 2.5, 3.0, App.Vector(0, 0, B - 2.0), App.Vector(0, 0, 1))
    )
    seal_b = Part.makeCylinder(R_out - 1.0, 1.2, App.Vector(0, 0, 0), App.Vector(0, 0, 1)).cut(
        Part.makeCylinder(R_in + 2.5, 3.0, App.Vector(0, 0, -1.0), App.Vector(0, 0, 1))
    )
    solid = Part.makeCompound([out_ring, in_ring, seal_f, seal_b] + balls)
    return solid

def tao_solid_chi_tiet_6():
    # 6. Mặt bít NGUYÊN KHỐI đặc kín 100% (Vành Ø104x8mm, gờ định vị Ø85.5x6mm, 4 lỗ vít chìm M6 PCD Ø94)
    R_flange = 52.0
    T_flange = 8.0
    R_spigot = 42.75
    T_spigot = 6.0

    cyl_spigot = Part.makeCylinder(R_spigot, T_spigot, App.Vector(0, 0, 0), App.Vector(0, 0, 1))
    cyl_flange = Part.makeCylinder(R_flange, T_flange, App.Vector(0, 0, T_spigot), App.Vector(0, 0, 1))
    solid = cyl_spigot.fuse(cyl_flange)

    # 4 lỗ bu-lông chìm M6 (lỗ suốt Ø6.5, lỗ khoét bậc Ø11 sâu 3.5mm)
    for i in range(4):
        ang = math.radians(i * 90.0 + 45.0)
        xs = 47.0 * math.cos(ang)
        ys = 47.0 * math.sin(ang)
        h_through = Part.makeCylinder(3.25, T_flange + T_spigot + 4.0, App.Vector(xs, ys, -2.0), App.Vector(0, 0, 1))
        h_cbore = Part.makeCylinder(5.5, 4.0, App.Vector(xs, ys, T_spigot + T_flange - 3.5), App.Vector(0, 0, 1))
        solid = solid.cut(h_through).cut(h_cbore)

    return solid

# ==========================================
# 2. XUẤT ẢNH 3D ISOMETRIC THUMBNAIL
# ==========================================

def render_3d_thumbnail(shape, filepath, color='#0284c7', edge_color='#0369a1', elev=25, azim=-45, deflection=1.5):
    fig = plt.figure(figsize=(4.5, 4.2), facecolor='#ffffff')
    ax = fig.add_axes([0.02, 0.02, 0.96, 0.96], projection='3d', facecolor='#ffffff')
    
    tess = shape.tessellate(deflection)
    pts = tess[0]
    facets = tess[1]
    triangles = [[[pts[f[0]].x, pts[f[0]].y, pts[f[0]].z],
                  [pts[f[1]].x, pts[f[1]].y, pts[f[1]].z],
                  [pts[f[2]].x, pts[f[2]].y, pts[f[2]].z]] for f in facets]

    poly = Poly3DCollection(triangles, facecolor=color, edgecolor=edge_color, lw=0.25, alpha=0.92)
    ax.add_collection3d(poly)

    xs = [p.x for p in pts]
    ys = [p.y for p in pts]
    zs = [p.z for p in pts]
    max_range = max(max(xs)-min(xs), max(ys)-min(ys), max(zs)-min(zs)) * 0.6
    mid_x = (max(xs)+min(xs))/2.0
    mid_y = (max(ys)+min(ys))/2.0
    mid_z = (max(zs)+min(zs))/2.0

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    ax.view_init(elev=elev, azim=azim)
    ax.axis('off')

    fig.savefig(filepath, dpi=160, facecolor='#ffffff')
    plt.close(fig)

# ==========================================
# 3. CÁC HÀM TIỆN ÍCH VẼ 2D KỸ THUẬT
# ==========================================

def setup_canvas():
    fig = plt.figure(figsize=(16.54, 11.69), dpi=200, facecolor='#ffffff')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 420)
    ax.set_ylim(0, 297)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Khung bản vẽ tiêu chuẩn TCVN
    border = patches.Rectangle((20, 10), 390, 277, fill=False, edgecolor='#000000', linewidth=1.8)
    ax.add_patch(border)
    outer = patches.Rectangle((5, 5), 410, 287, fill=False, edgecolor='#94a3b8', linewidth=0.5)
    ax.add_patch(outer)
    return fig, ax

def draw_title_block(ax, part_name, part_no, material, qty="02 Cái", scale="1:1"):
    x0, y0 = 265, 10
    w, h = 145, 38
    ax.add_patch(patches.Rectangle((x0, y0), w, h, fill=False, edgecolor='#000000', linewidth=1.5))
    ax.plot([x0, x0 + w], [y0 + 14, y0 + 14], 'k-', lw=1.0)
    ax.plot([x0, x0 + w], [y0 + 24, y0 + 24], 'k-', lw=1.0)
    ax.plot([x0, x0 + w], [y0 + 31, y0 + 31], 'k-', lw=0.8)
    
    ax.plot([x0 + 42, x0 + 42], [y0, y0 + 24], 'k-', lw=1.0)
    ax.plot([x0 + 88, x0 + 88], [y0, y0 + 24], 'k-', lw=1.0)
    ax.plot([x0 + 115, x0 + 115], [y0, y0 + 24], 'k-', lw=1.0)

    ax.text(x0 + w/2, y0 + 34.5, "BẢN VẼ CHẾ TẠO CƠ KHÍ CHÍNH XÁC", fontsize=9.5, fontweight='bold', ha='center', va='center', color='#0f172a')
    ax.text(x0 + w/2, y0 + 27.5, part_name.upper(), fontsize=10.5, fontweight='bold', ha='center', va='center', color='#0284c7')
    
    ax.text(x0 + 21, y0 + 19, "VẬT LIỆU", fontsize=7.5, ha='center', va='center', color='#64748b')
    ax.text(x0 + 21, y0 + 7, material, fontsize=9.0, fontweight='bold', ha='center', va='center', color='#0f172a')
    
    ax.text(x0 + 65, y0 + 19, "KÝ HIỆU", fontsize=7.5, ha='center', va='center', color='#64748b')
    ax.text(x0 + 65, y0 + 7, part_no, fontsize=9.5, fontweight='bold', ha='center', va='center', color='#0f172a')
    
    ax.text(x0 + 101.5, y0 + 19, "SỐ LƯỢNG", fontsize=7.5, ha='center', va='center', color='#64748b')
    ax.text(x0 + 101.5, y0 + 7, qty, fontsize=9.5, ha='center', va='center', color='#0f172a')
    
    ax.text(x0 + 130, y0 + 19, "TỶ LỆ", fontsize=7.5, ha='center', va='center', color='#64748b')
    ax.text(x0 + 130, y0 + 7, scale, fontsize=9.5, fontweight='bold', ha='center', va='center', color='#0f172a')

def draw_tech_notes(ax, notes, x=140, y=14):
    ax.text(x, y + len(notes)*4.8 + 2, "YÊU CẦU KỸ THUẬT:", fontsize=9.5, fontweight='bold', color='#0f172a')
    for i, note in enumerate(notes):
        ax.text(x, y + (len(notes) - 1 - i)*4.8, f"{i+1}. {note}", fontsize=8.0, color='#334155')

def draw_3d_box(ax, thumb_path, x=275, y=145, w=130, h=132, title="HÌNH CHIẾU TRỤC ĐO 3D (PHỐI CẢNH)"):
    # Hộp viền phối cảnh 3D
    ax.add_patch(patches.Rectangle((x, y), w, h, fill=True, facecolor='#f8fafc', edgecolor='#cbd5e1', lw=1.0))
    ax.plot([x, x + w], [y + h - 16, y + h - 16], color='#cbd5e1', lw=0.8)
    ax.text(x + w/2, y + h - 8, title, fontsize=9, fontweight='bold', ha='center', va='center', color='#0284c7')

    if os.path.exists(thumb_path):
        img = mpimg.imread(thumb_path)
        # Chèn ảnh vào giữa hộp
        pad = 6
        ax.imshow(img, extent=[x + pad, x + w - pad, y + pad, y + h - 18], aspect='auto', zorder=5)

def dim_h(ax, x1, x2, y, text, offset=4, text_offset=1.5, fontsize=8.5, color='#000000'):
    ax.plot([x1, x1], [y, y + (offset if offset>0 else -offset)], 'k-', lw=0.5, alpha=0.7)
    ax.plot([x2, x2], [y, y + (offset if offset>0 else -offset)], 'k-', lw=0.5, alpha=0.7)
    y_line = y + offset
    ax.annotate('', xy=(x1, y_line), xytext=(x2, y_line),
                arrowprops=dict(arrowstyle='<->', lw=0.8, color='black'))
    ax.text((x1 + x2)/2, y_line + (text_offset if offset>0 else -text_offset*2.2), text, 
            ha='center', va='center', fontsize=fontsize, fontweight='bold', color=color,
            bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='none'))

def dim_v(ax, y1, y2, x, text, offset=4, text_offset=1.5, fontsize=8.5, color='#000000'):
    ax.plot([x, x + (offset if offset>0 else -offset)], [y1, y1], 'k-', lw=0.5, alpha=0.7)
    ax.plot([x, x + (offset if offset>0 else -offset)], [y2, y2], 'k-', lw=0.5, alpha=0.7)
    x_line = x + offset
    ax.annotate('', xy=(x_line, y1), xytext=(x_line, y2),
                arrowprops=dict(arrowstyle='<->', lw=0.8, color='black'))
    ax.text(x_line + (text_offset if offset>0 else -text_offset*2.2), (y1 + y2)/2, text, 
            ha='center', va='center', rotation=90, fontsize=fontsize, fontweight='bold', color=color,
            bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='none'))

def draw_centerline(ax, x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], color='#ef4444', linestyle='-.', lw=0.7, alpha=0.85)

# ==========================================
# 4. VẼ TỪNG CHI TIẾT 2D KỸ THUẬT CƠ KHÍ
# ==========================================

# -------------------------------------------------------------
# CHI TIẾT 1: CHÂN BỆ TRỤ REN TRONG CAO 15CM (TỶ LỆ 1:2)
# -------------------------------------------------------------
def ve_chi_tiet_1():
    fig, ax = setup_canvas()
    S = 0.5 # Tỷ lệ 1:2

    thumb_path = os.path.join(THUMB_DIR, "thumb_ct1.png")
    draw_3d_box(ax, thumb_path, title="PHỐI CẢNH 3D SOLID: CHÂN BỆ CAO 15CM")

    # 1. HÌNH CHIẾU ĐỨNG (Mặt cắt bổ dọc A-A)
    # Tâm x=80, đáy y=170
    xc1, y0 = 80, 170
    H_tot = 150.0 * S # 75mm
    W_flange = 165.0 * S # 82.5mm
    T_flange = 16.0 * S  # 8mm
    D_cyl = 130.0 * S    # 65mm
    D_ren = 110.0 * S    # 55mm
    H_ren = 110.0 * S    # 55mm

    ax.text(xc1, 280, "HÌNH CHIẾU ĐỨNG (MẶT CẮT BỔ DỌC A-A)", fontsize=10, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, xc1, y0 - 8, xc1, y0 + H_tot + 10)

    # Nửa trái: Hình chiếu ngoài
    # Bích đáy
    ax.plot([xc1 - W_flange/2, xc1], [y0, y0], 'k-', lw=1.2)
    ax.plot([xc1 - W_flange/2, xc1 - W_flange/2], [y0, y0 + T_flange], 'k-', lw=1.2)
    ax.plot([xc1 - W_flange/2, xc1 - D_cyl/2 - 6], [y0 + T_flange, y0 + T_flange], 'k-', lw=1.2)
    # Loe chân
    ax.plot([xc1 - D_cyl/2 - 6, xc1 - D_cyl/2], [y0 + T_flange, y0 + T_flange + 12*S], 'k-', lw=1.2)
    # Thân trụ
    ax.plot([xc1 - D_cyl/2, xc1 - D_cyl/2], [y0 + T_flange + 12*S, y0 + H_tot], 'k-', lw=1.2)
    ax.plot([xc1 - D_cyl/2, xc1], [y0 + H_tot, y0 + H_tot], 'k-', lw=1.2)
    # Lỗ bắt ốc bên trái
    xb_hole = xc1 - 65.0*S
    ax.plot([xb_hole - 7.25*S, xb_hole - 7.25*S], [y0, y0 + T_flange], 'k--', lw=0.6)
    ax.plot([xb_hole + 7.25*S, xb_hole + 7.25*S], [y0, y0 + T_flange], 'k--', lw=0.6)
    draw_centerline(ax, xb_hole, y0 - 3, xb_hole, y0 + T_flange + 3)

    # Nửa phải: Mặt cắt kim loại A-A
    # Vỏ ngoài
    ax.plot([xc1, xc1 + W_flange/2], [y0, y0], 'k-', lw=1.2)
    ax.plot([xc1 + W_flange/2, xc1 + W_flange/2], [y0, y0 + T_flange], 'k-', lw=1.2)
    ax.plot([xc1 + W_flange/2, xc1 + D_cyl/2 + 6], [y0 + T_flange, y0 + T_flange], 'k-', lw=1.2)
    ax.plot([xc1 + D_cyl/2 + 6, xc1 + D_cyl/2], [y0 + T_flange, y0 + T_flange + 12*S], 'k-', lw=1.2)
    ax.plot([xc1 + D_cyl/2, xc1 + D_cyl/2], [y0 + T_flange + 12*S, y0 + H_tot], 'k-', lw=1.2)
    ax.plot([xc1 + D_cyl/2, xc1 + D_ren/2], [y0 + H_tot, y0 + H_tot], 'k-', lw=1.2)
    # Ren trong
    ax.plot([xc1 + D_ren/2, xc1 + D_ren/2], [y0 + H_tot, y0 + H_tot - H_ren], 'k-', lw=1.2)
    # Đáy ren thoát phoi
    ax.plot([xc1 + D_ren/2, xc1 + 52.0*S], [y0 + H_tot - H_ren, y0 + H_tot - H_ren], 'k-', lw=1.2)
    ax.plot([xc1 + 52.0*S, xc1 + 52.0*S], [y0 + H_tot - H_ren, y0], 'k-', lw=1.2)
    ax.plot([xc1, xc1 + 52.0*S], [y0, y0], 'k-', lw=1.2)

    # Lỗ bắt bu-lông bên phải
    xb_r = xc1 + 65.0*S
    ax.plot([xb_r - 7.25*S, xb_r - 7.25*S], [y0, y0 + T_flange], 'k-', lw=1.0)
    ax.plot([xb_r + 7.25*S, xb_r + 7.25*S], [y0, y0 + T_flange], 'k-', lw=1.0)
    draw_centerline(ax, xb_r, y0 - 3, xb_r, y0 + T_flange + 3)

    # Gạch mặt cắt hatching
    hatch_poly1 = patches.Polygon([
        (xc1 + D_ren/2, y0 + H_tot), (xc1 + D_cyl/2, y0 + H_tot),
        (xc1 + D_cyl/2, y0 + T_flange + 12*S), (xc1 + D_cyl/2 + 6, y0 + T_flange),
        (xc1 + W_flange/2, y0 + T_flange), (xc1 + W_flange/2, y0),
        (xb_r + 7.25*S, y0), (xb_r + 7.25*S, y0 + T_flange),
        (xb_r - 7.25*S, y0 + T_flange), (xb_r - 7.25*S, y0),
        (xc1 + 52.0*S, y0), (xc1 + 52.0*S, y0 + H_tot - H_ren),
        (xc1 + D_ren/2, y0 + H_tot - H_ren)
    ], closed=True, fill=True, facecolor='#cbd5e1', edgecolor='black', lw=1.0, hatch='//', alpha=0.6)
    ax.add_patch(hatch_poly1)

    # Kích thước hình chiếu đứng
    dim_v(ax, y0, y0 + H_tot, xc1 - W_flange/2, "150 mm (15cm)", offset=-10, fontsize=8.5)
    dim_v(ax, y0, y0 + T_flange, xc1 - W_flange/2, "16", offset=-4, fontsize=8.0)
    dim_v(ax, y0 + H_tot - H_ren, y0 + H_tot, xc1 + D_ren/2, "Sâu ren 110", offset=4, fontsize=8.0)
    dim_h(ax, xc1 - W_flange/2, xc1 + W_flange/2, y0, "165", offset=-8, fontsize=8.5)
    dim_h(ax, xc1 - D_cyl/2, xc1 + D_cyl/2, y0 + H_tot, "Ø 130", offset=6, fontsize=8.5)
    dim_h(ax, xc1, xc1 + D_ren/2, y0 + H_tot, "M110 x 3", offset=12, fontsize=8.5, color='#0284c7')

    # 2. HÌNH CHIẾU BẰNG (Nhìn từ trên xuống)
    # Tâm x=80, y=75
    yc2 = 75
    ax.text(xc1, 130, "HÌNH CHIẾU BẰNG (TOP VIEW)", fontsize=10, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, xc1 - 50, yc2, xc1 + 50, yc2)
    draw_centerline(ax, xc1, yc2 - 50, xc1, yc2 + 50)

    # Bích vuông 165x165 bo góc R15
    bich_sq = patches.FancyBboxPatch((xc1 - W_flange/2, yc2 - W_flange/2), W_flange, W_flange,
                                    boxstyle="round,pad=0,rounding_size=7.5",
                                    fill=False, edgecolor='black', lw=1.2)
    ax.add_patch(bich_sq)

    # Trụ ngoài Ø130
    ax.add_patch(patches.Circle((xc1, yc2), D_cyl/2, fill=False, edgecolor='black', lw=1.2))
    # Gờ loe đáy Ø150 (nét đứt)
    ax.add_patch(patches.Circle((xc1, yc2), 150.0*S/2, fill=False, edgecolor='#64748b', linestyle=':', lw=0.8))
    # Vòng ren M110
    ax.add_patch(patches.Circle((xc1, yc2), 52.0*S, fill=False, edgecolor='black', lw=1.0))
    ax.add_patch(patches.Arc((xc1, yc2), D_ren, D_ren, angle=0, theta1=15, theta2=300, edgecolor='#0284c7', lw=1.0))

    # 4 lỗ bắt bu-lông Ø14.5
    for xb in [-65.0*S, 65.0*S]:
        for yb in [-65.0*S, 65.0*S]:
            ax.add_patch(patches.Circle((xc1 + xb, yc2 + yb), 7.25*S, fill=False, edgecolor='black', lw=1.0))
            draw_centerline(ax, xc1 + xb - 5, yc2 + yb, xc1 + xb + 5, yc2 + yb)
            draw_centerline(ax, xc1 + xb, yc2 + yb - 5, xc1 + xb, yc2 + yb + 5)

    dim_h(ax, xc1 - 65.0*S, xc1 + 65.0*S, yc2 - W_flange/2, "130 ±0.15", offset=-6, fontsize=8.0)
    dim_v(ax, yc2 - 65.0*S, yc2 + 65.0*S, xc1 - W_flange/2, "130 ±0.15", offset=-6, fontsize=8.0)
    ax.annotate("4 Lỗ Ø 14.5\n(Đã bỏ ốc màu)",
                xy=(xc1 + 65.0*S, yc2 + 65.0*S),
                xytext=(xc1 + 65.0*S + 14, yc2 + 65.0*S + 14),
                arrowprops=dict(arrowstyle="->", color="black", lw=0.8),
                fontsize=8.0, fontweight='bold', color='#0f172a', ha='left', va='bottom')

    # 3. HÌNH CHIẾU CẠNH (Tâm x=195, y=170)
    xc3 = 195
    ax.text(xc3, 280, "HÌNH CHIẾU CẠNH (SIDE VIEW)", fontsize=10, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, xc3, y0 - 8, xc3, y0 + H_tot + 10)
    # Bích đáy bên cạnh
    ax.plot([xc3 - W_flange/2, xc3 + W_flange/2], [y0, y0], 'k-', lw=1.2)
    ax.plot([xc3 - W_flange/2, xc3 - W_flange/2], [y0, y0 + T_flange], 'k-', lw=1.2)
    ax.plot([xc3 + W_flange/2, xc3 + W_flange/2], [y0, y0 + T_flange], 'k-', lw=1.2)
    ax.plot([xc3 - W_flange/2, xc3 + W_flange/2], [y0 + T_flange, y0 + T_flange], 'k-', lw=1.2)
    # Thân trụ
    ax.plot([xc3 - D_cyl/2, xc3 - D_cyl/2], [y0 + T_flange + 12*S, y0 + H_tot], 'k-', lw=1.2)
    ax.plot([xc3 + D_cyl/2, xc3 + D_cyl/2], [y0 + T_flange + 12*S, y0 + H_tot], 'k-', lw=1.2)
    ax.plot([xc3 - D_cyl/2, xc3 + D_cyl/2], [y0 + H_tot, y0 + H_tot], 'k-', lw=1.2)
    # Đường loe chân
    ax.plot([xc3 - D_cyl/2 - 6, xc3 - D_cyl/2], [y0 + T_flange, y0 + T_flange + 12*S], 'k-', lw=1.2)
    ax.plot([xc3 + D_cyl/2 + 6, xc3 + D_cyl/2], [y0 + T_flange, y0 + T_flange + 12*S], 'k-', lw=1.2)

    # 4 lỗ ren nét đứt
    for xb in [xc3 - 65.0*S, xc3 + 65.0*S]:
        ax.plot([xb - 7.25*S, xb - 7.25*S], [y0, y0 + T_flange], 'k--', lw=0.6)
        ax.plot([xb + 7.25*S, xb + 7.25*S], [y0, y0 + T_flange], 'k--', lw=0.6)

    # Ghi chú kỹ thuật & Khung tên
    notes = [
        "Vật liệu: Gang xám FC250 hoặc Thép C45 đúc/tiện CNC nguyên khối.",
        "Tiện ren trong M110 bước ren P = 3.0mm, chiều sâu hữu dụng ren 110mm.",
        "Độ vuông góc giữa mặt bích đáy và đường tâm ren ≤ 0.04mm.",
        "Mặt bích đáy mài phẳng Ra ≤ 1.6µm, 4 lỗ bu-lông Ø14.5 thông suốt.",
        "Làm sạch ba-via sắc cạnh, vát mép đầu ren 2 x 45°."
    ]
    draw_tech_notes(ax, notes, x=135, y=14)
    draw_title_block(ax, "CHÂN BỆ TRỤ REN TRONG CAO 15CM", "KT-CT01", "Gang FC250 / C45", qty="02 Cái", scale="1:2")

    path = os.path.join(OUT_DIR, "ban_ve_chi_tiet_1_chan_be.png")
    fig.savefig(path, dpi=200)
    fig.savefig(os.path.join(ARTIFACT_DIR, "ban_ve_chi_tiet_1_chan_be.png"), dpi=200)
    plt.close(fig)
    print(">> Đã xuất bản vẽ Chi tiết 1 (Tỷ lệ 1:2 chuẩn TCVN)")

# -------------------------------------------------------------
# CHI TIẾT 2: ỐNG CỐ ĐỊNH REN NGOÀI LỤC GIÁC S125 (TỶ LỆ 1:2)
# -------------------------------------------------------------
def ve_chi_tiet_2():
    fig, ax = setup_canvas()
    S = 0.5

    thumb_path = os.path.join(THUMB_DIR, "thumb_ct2.png")
    draw_3d_box(ax, thumb_path, title="PHỐI CẢNH 3D SOLID: ĐẦU LỤC GIÁC TO S125")

    # 1. HÌNH CHIẾU ĐỨNG (Mặt cắt toàn phần A-A)
    # Tâm x=80, y=210
    x0, y0 = 40, 210
    L_tot = 133.0 * S # 66.5mm
    L_ren = 115.0 * S # 57.5mm
    T_hex = 18.0 * S  # 9.0mm
    D_ren = 110.0 * S # 55.0mm
    S_hex = 125.0 * S # 62.5mm
    D_in  = 86.0 * S  # 43.0mm

    ax.text(x0 + L_tot/2, 280, "HÌNH CHIẾU ĐỨNG (MẶT CẮT TOÀN PHẦN A-A)", fontsize=10, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, x0 - 8, y0, x0 + L_tot + 8, y0)

    # Vỏ ngoài thân ren
    ax.plot([x0, x0 + L_ren], [y0 + D_ren/2, y0 + D_ren/2], 'k-', lw=1.2)
    ax.plot([x0, x0 + L_ren], [y0 - D_ren/2, y0 - D_ren/2], 'k-', lw=1.2)
    ax.plot([x0, x0], [y0 + D_ren/2, y0 + D_in/2], 'k-', lw=1.2)
    ax.plot([x0, x0], [y0 - D_ren/2, y0 - D_in/2], 'k-', lw=1.2)

    # Đầu lục giác S125
    ax.plot([x0 + L_ren, x0 + L_ren], [y0 + D_ren/2, y0 + S_hex/2], 'k-', lw=1.2)
    ax.plot([x0 + L_ren, x0 + L_ren], [y0 - D_ren/2, y0 - S_hex/2], 'k-', lw=1.2)
    ax.plot([x0 + L_ren, x0 + L_tot], [y0 + S_hex/2, y0 + S_hex/2], 'k-', lw=1.2)
    ax.plot([x0 + L_ren, x0 + L_tot], [y0 - S_hex/2, y0 - S_hex/2], 'k-', lw=1.2)
    ax.plot([x0 + L_tot, x0 + L_tot], [y0 + S_hex/2, y0 + D_in/2], 'k-', lw=1.2)
    ax.plot([x0 + L_tot, x0 + L_tot], [y0 - S_hex/2, y0 - D_in/2], 'k-', lw=1.2)

    # Lòng trong Ø86mm
    ax.plot([x0, x0 + L_tot], [y0 + D_in/2, y0 + D_in/2], 'k-', lw=1.2)
    ax.plot([x0, x0 + L_tot], [y0 - D_in/2, y0 - D_in/2], 'k-', lw=1.2)

    # 2 lỗ ren M6 sâu 12mm trên mặt đầu lục giác
    xs_m6 = x0 + L_tot - 12.0*S
    ax.plot([xs_m6, x0 + L_tot], [y0 + 47.0*S, y0 + 47.0*S], 'k-', lw=0.8)
    ax.plot([xs_m6, x0 + L_tot], [y0 + 47.0*S - 5.0*S, y0 + 47.0*S - 5.0*S], 'k-', lw=0.8)
    ax.plot([xs_m6, xs_m6], [y0 + 47.0*S - 5.0*S, y0 + 47.0*S], 'k-', lw=0.8)

    ax.plot([xs_m6, x0 + L_tot], [y0 - 47.0*S, y0 - 47.0*S], 'k-', lw=0.8)
    ax.plot([xs_m6, x0 + L_tot], [y0 - 47.0*S + 5.0*S, y0 - 47.0*S + 5.0*S], 'k-', lw=0.8)
    ax.plot([xs_m6, xs_m6], [y0 - 47.0*S, y0 - 47.0*S + 5.0*S], 'k-', lw=0.8)

    # Gạch mặt cắt hatching trên và dưới
    poly_top = patches.Polygon([
        (x0, y0 + D_in/2), (x0, y0 + D_ren/2), (x0 + L_ren, y0 + D_ren/2),
        (x0 + L_ren, y0 + S_hex/2), (x0 + L_tot, y0 + S_hex/2),
        (x0 + L_tot, y0 + 47.0*S), (xs_m6, y0 + 47.0*S),
        (xs_m6, y0 + 47.0*S - 5.0*S), (x0 + L_tot, y0 + 47.0*S - 5.0*S),
        (x0 + L_tot, y0 + D_in/2)
    ], closed=True, fill=True, facecolor='#cbd5e1', edgecolor='black', lw=1.0, hatch='//', alpha=0.6)
    ax.add_patch(poly_top)

    poly_bot = patches.Polygon([
        (x0, y0 - D_in/2), (x0, y0 - D_ren/2), (x0 + L_ren, y0 - D_ren/2),
        (x0 + L_ren, y0 - S_hex/2), (x0 + L_tot, y0 - S_hex/2),
        (x0 + L_tot, y0 - 47.0*S), (xs_m6, y0 - 47.0*S),
        (xs_m6, y0 - 47.0*S + 5.0*S), (x0 + L_tot, y0 - 47.0*S + 5.0*S),
        (x0 + L_tot, y0 - D_in/2)
    ], closed=True, fill=True, facecolor='#cbd5e1', edgecolor='black', lw=1.0, hatch='//', alpha=0.6)
    ax.add_patch(poly_bot)

    # Kích thước hình chiếu đứng
    dim_h(ax, x0, x0 + L_tot, y0 + S_hex/2, "133 mm (Tổng dài)", offset=8, fontsize=8.5)
    dim_h(ax, x0, x0 + L_ren, y0 - S_hex/2, "115 (Dài ren M110)", offset=-8, fontsize=8.0)
    dim_h(ax, x0 + L_ren, x0 + L_tot, y0 - S_hex/2, "18", offset=-8, fontsize=8.0)
    dim_v(ax, y0 - D_ren/2, y0 + D_ren/2, x0, "M110 x 3", offset=-8, fontsize=8.5, color='#0284c7')
    dim_v(ax, y0 - D_in/2, y0 + D_in/2, x0 + L_tot, "Ø 86 ±0.03", offset=8, fontsize=8.5, color='#059669')

    # 2. HÌNH CHIẾU CẠNH (Nhìn từ đầu lục giác)
    # Tâm x=195, y=210
    xc2 = 195
    ax.text(xc2, 280, "HÌNH CHIẾU CẠNH (ĐẦU LỤC GIÁC S125)", fontsize=10, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, xc2 - 45, y0, xc2 + 45, y0)
    draw_centerline(ax, xc2, y0 - 45, xc2, y0 + 45)

    # Lục giác S=125mm (R = 72.2mm -> scaled = 36.1mm)
    R_h = 72.2 * S
    pts_hex = []
    for i in range(6):
        ang = math.radians(i * 60.0 + 30.0)
        pts_hex.append((xc2 + R_h * math.cos(ang), y0 + R_h * math.sin(ang)))
    ax.add_patch(Polygon(pts_hex, closed=True, fill=False, edgecolor='black', lw=1.2))

    # Vòng tròn lòng trong Ø86mm
    ax.add_patch(patches.Circle((xc2, y0), D_in/2, fill=False, edgecolor='black', lw=1.2))
    # PCD Ø94mm (đường chấm gạch)
    ax.add_patch(patches.Circle((xc2, y0), 94.0*S/2, fill=False, edgecolor='#ef4444', linestyle='-.', lw=0.7))

    # 4 lỗ ren M6
    for i in range(4):
        ang = math.radians(i * 90.0 + 45.0)
        xh = xc2 + 47.0*S * math.cos(ang)
        yh = y0 + 47.0*S * math.sin(ang)
        ax.add_patch(patches.Circle((xh, yh), 2.5*S, fill=False, edgecolor='black', lw=1.0))
        draw_centerline(ax, xh - 3, yh, xh + 3, yh)
        draw_centerline(ax, xh, yh - 3, xh, yh + 3)

    dim_v(ax, y0 - S_hex/2, y0 + S_hex/2, xc2 + R_h*math.cos(math.radians(30)), "S = 125 mm", offset=8, fontsize=8.5, color='#0284c7')
    ax.text(xc2, y0 - 46, "4 Lỗ ren M6 sâu 12mm\n(PCD Ø 94mm)", fontsize=8.0, ha='center', color='#0f172a', fontweight='bold')

    # 3. HÌNH CHIẾU BẰNG (Top view)
    # Tâm x=75, y=85
    yc3 = 85
    ax.text(x0 + L_tot/2, 125, "HÌNH CHIẾU BẰNG (TOP VIEW)", fontsize=9.5, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, x0 - 8, yc3, x0 + L_tot + 8, yc3)
    # Bao ngoài thân ren
    ax.plot([x0, x0 + L_ren], [yc3 + D_ren/2, yc3 + D_ren/2], 'k-', lw=1.2)
    ax.plot([x0, x0 + L_ren], [yc3 - D_ren/2, yc3 - D_ren/2], 'k-', lw=1.2)
    ax.plot([x0, x0], [yc3 - D_ren/2, yc3 + D_ren/2], 'k-', lw=1.2)
    # Đầu lục giác hình chiếu bằng
    ax.plot([x0 + L_ren, x0 + L_tot], [yc3 + S_hex/2, yc3 + S_hex/2], 'k-', lw=1.2)
    ax.plot([x0 + L_ren, x0 + L_tot], [yc3 - S_hex/2, yc3 - S_hex/2], 'k-', lw=1.2)
    ax.plot([x0 + L_ren, x0 + L_ren], [yc3 - S_hex/2, yc3 + S_hex/2], 'k-', lw=1.2)
    ax.plot([x0 + L_tot, x0 + L_tot], [yc3 - S_hex/2, yc3 + S_hex/2], 'k-', lw=1.2)
    # Đường lọt lòng nét đứt
    ax.plot([x0, x0 + L_tot], [yc3 + D_in/2, yc3 + D_in/2], 'k--', lw=0.6)
    ax.plot([x0, x0 + L_tot], [yc3 - D_in/2, yc3 - D_in/2], 'k--', lw=0.6)

    # Ghi chú kỹ thuật & Khung tên
    notes = [
        "Vật liệu: Thép kết cấu C45 tiện và phay CNC chính xác.",
        "Ren ngoài M110 bước ren P = 3.0mm, chiều dài tiện ren 115mm.",
        "Đầu lục giác S=125mm phay chính xác để vừa cờ-lê hoặc khẩu vặn 125mm.",
        "Lòng trong Ø86mm mài bóng đạt độ nhám Ra ≤ 0.8µm để lắp trượt ống lót [4].",
        "4 Lỗ ren M6 trên mặt đầu ta-rô sâu 12mm đều trên PCD Ø94mm."
    ]
    draw_tech_notes(ax, notes, x=135, y=14)
    draw_title_block(ax, "ỐNG CỐ ĐỊNH REN NGOÀI ĐẦU LỤC GIÁC S125", "KT-CT02", "Thép C45", qty="02 Cái", scale="1:2")

    path = os.path.join(OUT_DIR, "ban_ve_chi_tiet_2_ong_ren_ngoai_s125.png")
    fig.savefig(path, dpi=200)
    fig.savefig(os.path.join(ARTIFACT_DIR, "ban_ve_chi_tiet_2_ong_ren_ngoai_s125.png"), dpi=200)
    plt.close(fig)
    print(">> Đã xuất bản vẽ Chi tiết 2 (Tỷ lệ 1:2 chuẩn TCVN)")

# -------------------------------------------------------------
# CHI TIẾT 3: LONG ĐỀN TÁN KHÓA LỤC GIÁC MỎNG 5MM (TỶ LỆ 1:1)
# -------------------------------------------------------------
def ve_chi_tiet_3():
    fig, ax = setup_canvas()

    thumb_path = os.path.join(THUMB_DIR, "thumb_ct3.png")
    draw_3d_box(ax, thumb_path, title="PHỐI CẢNH 3D: LONG ĐỀN MỎNG 5MM")

    # 1. HÌNH CHIẾU BẰNG (Biên dạng lục giác S115) - Đặt rộng rãi ở bên trái
    xc1, yc1 = 90, 150
    R_hex = 66.4 # S = 115mm (R = 115 / sqrt(3) = 66.4mm)
    D_ren = 110.0
    T_nut = 5.0 # Chiều dày đúng 5mm

    ax.text(xc1, 235, "HÌNH CHIẾU BẰNG (TOP VIEW - LỤC GIÁC S115)", fontsize=10, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, xc1 - 70, yc1, xc1 + 70, yc1)
    draw_centerline(ax, xc1, yc1 - 70, xc1, yc1 + 70)

    # Lục giác S115mm (2 cạnh phẳng thẳng đứng x = +/- 57.5)
    pts_hex = []
    for i in range(6):
        ang = math.radians(i * 60.0 + 30.0)
        pts_hex.append((xc1 + R_hex * math.cos(ang), yc1 + R_hex * math.sin(ang)))
    ax.add_patch(Polygon(pts_hex, closed=True, fill=False, edgecolor='black', lw=1.3))

    # Vòng ren trong M110
    ax.add_patch(patches.Circle((xc1, yc1), 52.5, fill=False, edgecolor='black', lw=1.2))
    ax.add_patch(patches.Arc((xc1, yc1), D_ren, D_ren, angle=0, theta1=20, theta2=310, edgecolor='#ea580c', lw=1.2))

    # Kích thước hình chiếu bằng
    dim_h(ax, xc1 - 57.5, xc1 + 57.5, yc1 - 66.4, "S = 115 mm", offset=-10, fontsize=9.0, color='#0284c7')
    ax.annotate("Ren trong M110 x 3",
                xy=(xc1 - 55.0*math.cos(math.radians(45)), yc1 + 55.0*math.sin(math.radians(45))),
                xytext=(xc1 - 15, yc1 + 72),
                arrowprops=dict(arrowstyle="->", color="#ea580c", lw=0.9),
                fontsize=8.5, fontweight='bold', color='#ea580c', ha='center')

    # 2. HÌNH CHIẾU ĐỨNG (Mặt cắt bổ dọc thể hiện độ dày 5.0mm) - Đặt ở cột giữa phía trên
    xc2, yc2 = 205, 205
    ax.text(xc2, 235, "HÌNH CHIẾU ĐỨNG (MẶT CẮT BỔ DỌC)", fontsize=9.5, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, xc2, yc2 - 18, xc2, yc2 + 18)

    # Nửa trái kim loại (từ xc2 - 57.5 đến xc2 - 55.0)
    ax.add_patch(patches.Rectangle((xc2 - 57.5, yc2 - T_nut/2), 2.5, T_nut,
                                   fill=True, facecolor='#fed7aa', edgecolor='black', lw=1.1, hatch='//'))
    # Nửa phải kim loại (từ xc2 + 55.0 đến xc2 + 57.5)
    ax.add_patch(patches.Rectangle((xc2 + 55.0, yc2 - T_nut/2), 2.5, T_nut,
                                   fill=True, facecolor='#fed7aa', edgecolor='black', lw=1.1, hatch='//'))

    # Đường gióng và kích thước hình chiếu đứng
    dim_v(ax, yc2 - T_nut/2, yc2 + T_nut/2, xc2 + 57.5, "5.0 mm", offset=8, fontsize=9.0, color='#ea580c')
    dim_h(ax, xc2 - 57.5, xc2 + 57.5, yc2 + T_nut/2, "S = 115 mm", offset=10, fontsize=8.5, color='#0284c7')
    dim_h(ax, xc2 - 55.0, xc2 + 55.0, yc2 - T_nut/2, "Ren trong M110 x 3", offset=-10, fontsize=8.5, color='#ea580c')

    # 3. TRÍCH ĐOẠN PHÓNG TO CHI TIẾT REN & VÁT MÉP (TỶ LỆ 4:1) - Đặt ở cột giữa phía dưới
    xc_zoom = 205
    yc_zoom = 130
    ax.text(xc_zoom, 155, "TRÍCH ĐOẠN PHÓNG TO A (TỶ LỆ 4:1)", fontsize=10, fontweight='bold', ha='center', color='#ea580c')
    
    # Vẽ phóng to 4x độ dày 5mm -> 20mm, bề rộng 50mm
    zoom_t = 20.0
    zoom_w = 50.0
    ax.add_patch(patches.Rectangle((xc_zoom - zoom_w/2, yc_zoom - zoom_t/2), zoom_w, zoom_t,
                                   fill=True, facecolor='#fed7aa', edgecolor='black', lw=1.3, hatch='///', alpha=0.7))
    # Vát mép 1 x 45 độ ở mép lỗ ren
    ax.plot([xc_zoom - zoom_w/2, xc_zoom - zoom_w/2 + 5], [yc_zoom + zoom_t/2 - 5, yc_zoom + zoom_t/2], 'r-', lw=1.2)
    ax.plot([xc_zoom - zoom_w/2, xc_zoom - zoom_w/2 + 5], [yc_zoom - zoom_t/2 + 5, yc_zoom - zoom_t/2], 'r-', lw=1.2)

    dim_v(ax, yc_zoom - zoom_t/2, yc_zoom + zoom_t/2, xc_zoom + zoom_w/2, "5.0 mm (-0.1/0)", offset=12, fontsize=8.5, color='#ea580c')
    
    # Hộp thông báo quan trọng về xóa cây cùi tròn
    ax.text(xc_zoom, 80, 
            "★ ĐÃ XÓA HOÀN TOÀN CÂY CÙI TRÒN ★\n(Theo đúng yêu cầu chỉ đạo)\n\n- Độ dày mỏng đúng 5.0mm\n- Vặn hãm bằng cờ-lê hoặc mỏ-lết 115mm\n- Không cản trở hành trình chỉnh trống", 
            fontsize=8.5, fontweight='bold', ha='center', color='#b45309',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fef3c7', edgecolor='#f59e0b', lw=1.2))

    # Ghi chú kỹ thuật & Khung tên
    notes = [
        "Vật liệu: Thép tấm C45 hoặc phôi thanh lục giác S115 tiện phay mỏng.",
        "ĐỘ DÀY: Đúng 5.0mm (-0.1 / 0mm) theo yêu cầu chỉ đạo nghiêm ngặt.",
        "ĐÃ XÓA CÂY CÙI TRÒN: Không hàn thêm cần vặn hay bi cầu tròn.",
        "Ren trong M110 bước ren 3.0mm, vát mép nhẹ 1.0 x 45° mép ren.",
        "Xử lý bề mặt: Mạ kẽm điện phân hoặc nhuộm đen chống oxy hóa."
    ]
    draw_tech_notes(ax, notes, x=25, y=14)
    draw_title_block(ax, "LONG ĐỀN TÁN KHÓA LỤC GIÁC MỎNG 5MM", "KT-CT03", "Thép C45", qty="02 Cái", scale="1:1 (Trích 4:1)")

    path = os.path.join(OUT_DIR, "ban_ve_chi_tiet_3_long_den_mong_5mm.png")
    fig.savefig(path, dpi=200)
    fig.savefig(os.path.join(ARTIFACT_DIR, "ban_ve_chi_tiet_3_long_den_mong_5mm.png"), dpi=200)
    plt.close(fig)
    print(">> Đã xuất bản vẽ Chi tiết 3 (Tỷ lệ 1:1 chuẩn TCVN)")

# -------------------------------------------------------------
# CHI TIẾT 4: ỐNG TRỤ TRÒN NHẴN DÀY ĐÚNG 3MM (TỶ LỆ 1:1)
# -------------------------------------------------------------
def ve_chi_tiet_4():
    fig, ax = setup_canvas()

    thumb_path = os.path.join(THUMB_DIR, "thumb_ct4.png")
    draw_3d_box(ax, thumb_path, title="PHỐI CẢNH 3D: ỐNG TRỤ TRÒN NHẴN 3MM")

    # 1. HÌNH CHIẾU ĐỨNG (Mặt cắt bổ dọc A-A)
    # Chiều dài 65mm, Ø ngoài 86, Ø trong 80 -> Thành dày đúng 3mm! Gờ chặn 5mm lỗ Ø62
    x0, y0 = 45, 195
    L = 65.0
    R_out = 43.0
    R_in = 40.0
    R_lip = 31.0
    T_lip = 5.0

    ax.text(x0 + L/2, 280, "HÌNH CHIẾU ĐỨNG (MẶT CẮT BỔ DỌC TOÀN PHẦN A-A)", fontsize=10, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, x0 - 8, y0, x0 + L + 8, y0)

    # Nửa trên
    poly_top = patches.Polygon([
        (x0, y0 + R_lip), (x0, y0 + R_out), (x0 + L, y0 + R_out),
        (x0 + L, y0 + R_in), (x0 + T_lip, y0 + R_in), (x0 + T_lip, y0 + R_lip)
    ], closed=True, fill=True, facecolor='#a7f3d0', edgecolor='black', lw=1.2, hatch='//')
    ax.add_patch(poly_top)

    # Nửa dưới
    poly_bot = patches.Polygon([
        (x0, y0 - R_lip), (x0, y0 - R_out), (x0 + L, y0 - R_out),
        (x0 + L, y0 - R_in), (x0 + T_lip, y0 - R_in), (x0 + T_lip, y0 - R_lip)
    ], closed=True, fill=True, facecolor='#a7f3d0', edgecolor='black', lw=1.2, hatch='//')
    ax.add_patch(poly_bot)

    # Kích thước hình chiếu đứng
    dim_h(ax, x0, x0 + L, y0 - R_out, "65 mm", offset=-8, fontsize=8.5)
    dim_h(ax, x0, x0 + T_lip, y0 + R_out, "5", offset=6, fontsize=8.0)
    dim_v(ax, y0 - R_out, y0 + R_out, x0 + L, "Ø 86 -0.03 (g6)", offset=8, fontsize=8.5, color='#059669')
    dim_v(ax, y0 - R_in, y0 + R_in, x0, "Ø 80 +0.03 (H7)", offset=-6, fontsize=8.5, color='#0284c7')
    dim_v(ax, y0 - R_lip, y0 + R_lip, x0, "Ø 62", offset=-12, fontsize=8.0)

    # Chú dẫn thành dày 3mm
    ax.annotate("DÀY THÀNH ĐÚNG 3.0 mm\n((86 - 80) / 2 = 3.0mm)", xy=(x0 + 35, y0 + R_out - 1.5),
                xytext=(x0 + 20, y0 + R_out + 18),
                arrowprops=dict(arrowstyle='->', lw=1.0, color='#047857'),
                fontsize=8.5, fontweight='bold', color='#047857', ha='center',
                bbox=dict(boxstyle='square,pad=0.2', facecolor='#ffffff', edgecolor='#047857'))

    # 2. HÌNH CHIẾU CẠNH (Nhìn từ đầu ống)
    # Tâm xc2=195, y0=195
    xc2 = 195
    ax.text(xc2, 280, "HÌNH CHIẾU CẠNH (NHÌN TỪ ĐẦU ỐNG)", fontsize=10, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, xc2 - 50, y0, xc2 + 50, y0)
    draw_centerline(ax, xc2, y0 - 50, xc2, y0 + 50)

    # Vòng ngoài Ø86
    ax.add_patch(patches.Circle((xc2, y0), R_out, fill=False, edgecolor='black', lw=1.2))
    # Vòng trong Ø80
    ax.add_patch(patches.Circle((xc2, y0), R_in, fill=False, edgecolor='black', lw=1.0))
    # Gờ chặn Ø62
    ax.add_patch(patches.Circle((xc2, y0), R_lip, fill=False, edgecolor='black', lw=1.0))

    dim_v(ax, y0 - R_out, y0 + R_out, xc2 + R_out, "Ø 86 mm", offset=6, fontsize=8.5)
    dim_h(ax, xc2 - R_lip, xc2 + R_lip, y0 - R_out, "Lỗ thông Ø 62 mm", offset=-6, fontsize=8.0)

    # Ghi chú kỹ thuật & Khung tên
    notes = [
        "Vật liệu: Thép kết cấu C45 gia công tiện CNC chính xác cao.",
        "ĐỘ DÀY THÀNH ỐNG: Đúng 3.0mm ((86 - 80) / 2 = 3.0mm).",
        "Bề mặt ngoài Ø86g6 mài bóng trơn nhẵn Ra ≤ 0.8µm để trượt khít êm vào lòng [2].",
        "Mặt trong Ø80H7 tiện tinh để ôm khít chặt ca ngoài bạc đạn [5].",
        "Gờ chặn dày 5mm làm vai tỳ giữ cứng ca ngoài bạc đạn không bị chạy dọc trục."
    ]
    draw_tech_notes(ax, notes, x=135, y=14)
    draw_title_block(ax, "ỐNG TRỤ TRÒN NHẴN DÀY ĐÚNG 3MM (ÁO BẠC ĐẠN)", "KT-CT04", "Thép C45 Mài Bóng", qty="02 Cái", scale="1:1")

    path = os.path.join(OUT_DIR, "ban_ve_chi_tiet_4_ong_truot_3mm.png")
    fig.savefig(path, dpi=200)
    fig.savefig(os.path.join(ARTIFACT_DIR, "ban_ve_chi_tiet_4_ong_truot_3mm.png"), dpi=200)
    plt.close(fig)
    print(">> Đã xuất bản vẽ Chi tiết 4 (Tỷ lệ 1:1 chuẩn TCVN)")

# -------------------------------------------------------------
# CHI TIẾT 5: BẠC ĐẠN ĐỠ TRỤC PHI 60MM (TỶ LỆ 1:1)
# -------------------------------------------------------------
def ve_chi_tiet_5():
    fig, ax = setup_canvas()

    thumb_path = os.path.join(THUMB_DIR, "thumb_ct5.png")
    draw_3d_box(ax, thumb_path, title="PHỐI CẢNH 3D: VÒNG BI 6012-2RS")

    # 1. HÌNH CHIẾU ĐỨNG (Mặt cắt 1/2 vòng bi)
    # Bề rộng 22mm, Ø ngoài 80, Ø trong 60, bi Ø8
    x0, y0 = 65, 195
    B = 22.0
    R_out = 40.0
    R_in = 30.0
    R_pcd = 35.0

    ax.text(x0 + B/2, 280, "HÌNH CHIẾU ĐỨNG (MẶT CẮT 1/2 DỌC TRỤC)", fontsize=10, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, x0 - 8, y0, x0 + B + 8, y0)

    # Nửa trên
    # Ca ngoài
    ax.add_patch(patches.Rectangle((x0, y0 + R_out - 4.5), B, 4.5, fill=True, facecolor='#fde047', edgecolor='black', lw=1.0, hatch='//'))
    # Ca trong
    ax.add_patch(patches.Rectangle((x0, y0 + R_in), B, 4.5, fill=True, facecolor='#fde047', edgecolor='black', lw=1.0, hatch='//'))
    # Viên bi cầu Ø8
    ax.add_patch(patches.Circle((x0 + B/2, y0 + R_pcd), 4.0, fill=True, facecolor='#eab308', edgecolor='black', lw=1.2))

    # Nửa dưới
    ax.add_patch(patches.Rectangle((x0, y0 - R_out), B, 4.5, fill=True, facecolor='#fde047', edgecolor='black', lw=1.0, hatch='//'))
    ax.add_patch(patches.Rectangle((x0, y0 - R_in - 4.5), B, 4.5, fill=True, facecolor='#fde047', edgecolor='black', lw=1.0, hatch='//'))
    ax.add_patch(patches.Circle((x0 + B/2, y0 - R_pcd), 4.0, fill=True, facecolor='#eab308', edgecolor='black', lw=1.2))

    # Nắp cao su chắn bụi 2RS
    ax.plot([x0 + 1.2, x0 + 1.2], [y0 + R_in + 4.5, y0 + R_out - 4.5], '-', lw=1.5, color='#475569')
    ax.plot([x0 + B - 1.2, x0 + B - 1.2], [y0 + R_in + 4.5, y0 + R_out - 4.5], '-', lw=1.5, color='#475569')
    ax.plot([x0 + 1.2, x0 + 1.2], [y0 - R_out + 4.5, y0 - R_in - 4.5], '-', lw=1.5, color='#475569')
    ax.plot([x0 + B - 1.2, x0 + B - 1.2], [y0 - R_out + 4.5, y0 - R_in - 4.5], '-', lw=1.5, color='#475569')

    # Kích thước
    dim_h(ax, x0, x0 + B, y0 - R_out, "B = 22 mm", offset=-8, fontsize=8.5)
    dim_v(ax, y0 - R_out, y0 + R_out, x0 + B, "Ø 80 mm (Ca ngoài)", offset=8, fontsize=8.5)
    dim_v(ax, y0 - R_in, y0 + R_in, x0, "Ø 60 mm (Lỗ trục)", offset=-8, fontsize=8.5, color='#0284c7')

    # 2. HÌNH CHIẾU CẠNH (Tâm vòng bi và 10 viên bi cầu)
    xc2 = 195
    ax.text(xc2, 280, "HÌNH CHIẾU CẠNH (TÂM VÒNG BI & 10 VIÊN BI CẦU)", fontsize=10, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, xc2 - 45, y0, xc2 + 45, y0)
    draw_centerline(ax, xc2, y0 - 45, xc2, y0 + 45)

    # Các đường tròn
    ax.add_patch(patches.Circle((xc2, y0), R_out, fill=False, edgecolor='black', lw=1.2))
    ax.add_patch(patches.Circle((xc2, y0), R_in, fill=False, edgecolor='black', lw=1.2))
    # PCD Ø70mm
    ax.add_patch(patches.Circle((xc2, y0), R_pcd, fill=False, edgecolor='#ef4444', linestyle='-.', lw=0.7))

    # 10 viên bi cầu Ø8
    for i in range(10):
        ang = i * (2.0 * math.pi / 10.0)
        bx = xc2 + R_pcd * math.cos(ang)
        by = y0 + R_pcd * math.sin(ang)
        ax.add_patch(patches.Circle((bx, by), 4.0, fill=True, facecolor='#fef08a', edgecolor='black', lw=0.8))

    dim_h(ax, xc2 - R_pcd, xc2 + R_pcd, y0 - R_out, "PCD Ø 70 mm (10 Viên Bi Ø8)", offset=-8, fontsize=8.0, color='#b45309')

    # Ghi chú kỹ thuật & Khung tên
    notes = [
        "Quy cách tiêu chuẩn: Ổ bi đỡ rãnh sâu một dãy (Deep Groove Ball Bearing).",
        "Kích thước danh định: Đường kính trong Ø60 x Đường kính ngoài Ø80 x Bề rộng 22mm.",
        "Trang bị phốt cao su 2 mặt (2RS) ngăn ngừa tuyệt đối mạt củi và bụi tro máy rang.",
        "Mỡ bôi trơn gốc Lithium chịu nhiệt độ cao (>150°C) chuyên dụng máy rang cà phê.",
        "Khả năng chịu tải trọng: Tải động C = 29.5 kN, tải tĩnh C0 = 24.0 kN."
    ]
    draw_tech_notes(ax, notes, x=135, y=14)
    draw_title_block(ax, "BẠC ĐẠN ĐỠ TRỤC PHI 60MM (6012-2RS)", "KT-CT05", "Thép Vòng Bi GCr15", qty="02 Cái", scale="1:1")

    path = os.path.join(OUT_DIR, "ban_ve_chi_tiet_5_bac_dan_phi60.png")
    fig.savefig(path, dpi=200)
    fig.savefig(os.path.join(ARTIFACT_DIR, "ban_ve_chi_tiet_5_bac_dan_phi60.png"), dpi=200)
    plt.close(fig)
    print(">> Đã xuất bản vẽ Chi tiết 5 (Tỷ lệ 1:1 chuẩn TCVN)")

# -------------------------------------------------------------
# CHI TIẾT 6: MẶT BÍT NGUYÊN KHỐI ĐẶC KÍN (TỶ LỆ 1:1)
# -------------------------------------------------------------
def ve_chi_tiet_6():
    fig, ax = setup_canvas()

    thumb_path = os.path.join(THUMB_DIR, "thumb_ct6.png")
    draw_3d_box(ax, thumb_path, title="PHỐI CẢNH 3D: MẶT BÍT NGUYÊN KHỐI")

    # 1. HÌNH CHIẾU ĐỨNG (Mặt cắt A-A - ĐẶC KÍN NGUYÊN KHỐI 100%)
    # Gờ định vị Ø85.5x6mm, vành Ø104x8mm, tổng dày 14mm
    x0, y0 = 65, 195
    T_spigot = 6.0
    T_flange = 8.0
    R_spigot = 42.75
    R_flange = 52.0

    ax.text(x0 + 7, 280, "HÌNH CHIẾU ĐỨNG (MẶT CẮT BỔ DỌC A-A)", fontsize=10, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, x0 - 8, y0, x0 + 14 + 8, y0)

    # ĐẶC KÍN TOÀN BỘ KIM LOẠI TỪ TRÊN XUỐNG DƯỚI (KHÔNG CÓ LỖ TRỤC Ở TÂM)
    poly_mat_bit = patches.Polygon([
        (x0, y0 - R_spigot), (x0, y0 + R_spigot),
        (x0 + T_spigot, y0 + R_spigot), (x0 + T_spigot, y0 + R_flange),
        (x0 + T_spigot + T_flange, y0 + R_flange),
        (x0 + T_spigot + T_flange, y0 - R_flange),
        (x0 + T_spigot, y0 - R_flange),
        (x0 + T_spigot, y0 - R_spigot)
    ], closed=True, fill=True, facecolor='#e2e8f0', edgecolor='black', lw=1.3, hatch='//')
    ax.add_patch(poly_mat_bit)

    # Lỗ vít chìm M6 ở trên và dưới
    ax.plot([x0, x0 + 14], [y0 + 47.0 - 3.25, y0 + 47.0 - 3.25], 'k-', lw=0.8)
    ax.plot([x0, x0 + 14], [y0 + 47.0 + 3.25, y0 + 47.0 + 3.25], 'k-', lw=0.8)
    ax.add_patch(patches.Rectangle((x0 + 14 - 3.5, y0 + 47.0 - 5.5), 3.5, 11.0, fill=True, facecolor='#ffffff', edgecolor='black', lw=0.8))

    ax.plot([x0, x0 + 14], [y0 - 47.0 - 3.25, y0 - 47.0 - 3.25], 'k-', lw=0.8)
    ax.plot([x0, x0 + 14], [y0 - 47.0 + 3.25, y0 - 47.0 + 3.25], 'k-', lw=0.8)
    ax.add_patch(patches.Rectangle((x0 + 14 - 3.5, y0 - 47.0 - 5.5), 3.5, 11.0, fill=True, facecolor='#ffffff', edgecolor='black', lw=0.8))

    # Chữ nổi bật ĐẶC KÍN NGUYÊN KHỐI
    ax.text(x0 + 7, y0, "ĐẶC KÍN\nNGUYÊN KHỐI\n(KHÔNG THỦNG TÂM)", fontsize=7.5, fontweight='bold',
            ha='center', va='center', color='#0369a1',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f9ff', edgecolor='#0284c7', lw=1.0))

    # Kích thước
    dim_h(ax, x0, x0 + 14, y0 + R_flange, "14 mm", offset=8, fontsize=8.5)
    dim_h(ax, x0, x0 + T_spigot, y0 - R_flange, "6", offset=-8, fontsize=8.0)
    dim_h(ax, x0 + T_spigot, x0 + 14, y0 - R_flange, "8", offset=-8, fontsize=8.0)
    dim_v(ax, y0 - R_spigot, y0 + R_spigot, x0, "Ø 85.5 -0.05", offset=-8, fontsize=8.5, color='#0284c7')
    dim_v(ax, y0 - R_flange, y0 + R_flange, x0 + 14, "Ø 104 (Vành bích)", offset=8, fontsize=8.5)

    # 2. HÌNH CHIẾU BẰNG (Mặt ngoài & 4 lỗ bắt vít M6)
    xc2 = 195
    ax.text(xc2, 280, "HÌNH CHIẾU BẰNG (MẶT NGOÀI & 4 LỖ BẮT VÍT M6)", fontsize=10, fontweight='bold', ha='center', color='#0284c7')
    draw_centerline(ax, xc2 - 55, y0, xc2 + 55, y0)
    draw_centerline(ax, xc2, y0 - 55, xc2, y0 + 55)

    # Vành ngoài Ø104
    ax.add_patch(patches.Circle((xc2, y0), R_flange, fill=False, edgecolor='black', lw=1.3))
    # Gờ định vị Ø85.5 nét đứt
    ax.add_patch(patches.Circle((xc2, y0), R_spigot, fill=False, edgecolor='#64748b', linestyle='--', lw=0.8))
    # PCD Ø94
    ax.add_patch(patches.Circle((xc2, y0), 47.0, fill=False, edgecolor='#ef4444', linestyle='-.', lw=0.7))

    # 4 lỗ bắt bu-lông chìm M6
    for i in range(4):
        ang = math.radians(i * 90.0 + 45.0)
        xh = xc2 + 47.0 * math.cos(ang)
        yh = y0 + 47.0 * math.sin(ang)
        ax.add_patch(patches.Circle((xh, yh), 5.5, fill=False, edgecolor='black', lw=1.0))
        ax.add_patch(patches.Circle((xh, yh), 3.25, fill=False, edgecolor='black', lw=0.8))
        draw_centerline(ax, xh - 3, yh, xh + 3, yh)
        draw_centerline(ax, xh, yh - 3, xh, yh + 3)

    dim_h(ax, xc2 - 47.0, xc2 + 47.0, y0 - R_flange, "4 Lỗ Vít Chìm M6 trên PCD Ø 94 mm", offset=-8, fontsize=8.5, color='#0f172a')

    # Ghi chú kỹ thuật & Khung tên
    notes = [
        "Vật liệu: Thép C45 hoặc Hợp kim nhôm tiện nguyên khối (Solid CNC).",
        "MẶT BÍT NGUYÊN KHỐI: Tâm đĩa đặc kín 100%, tuyệt đối không khoét lỗ thông tâm.",
        "Gờ định vị Ø85.5 (-0.05mm) lắp vừa khít vào lòng ống [2], chặn cứng ca ngoài bạc đạn [5].",
        "4 Lỗ bậc khoét âm Ø11 x 3.5mm chứa chìm hoàn toàn đầu bu-lông lục giác chìm M6.",
        "Vát mép ngoài 1.5 x 45° chống bén tay, bề mặt ngoài mạ kẽm sáng bóng."
    ]
    draw_tech_notes(ax, notes, x=135, y=14)
    draw_title_block(ax, "MẶT BÍT NGUYÊN KHỐI (ĐẶC KÍN CHẶN BẠC ĐẠN)", "KT-CT06", "Thép C45 / Nhôm", qty="02 Cái", scale="1:1")

    path = os.path.join(OUT_DIR, "ban_ve_chi_tiet_6_mat_bit_nguyen_khoi.png")
    fig.savefig(path, dpi=200)
    fig.savefig(os.path.join(ARTIFACT_DIR, "ban_ve_chi_tiet_6_mat_bit_nguyen_khoi.png"), dpi=200)
    plt.close(fig)
    print(">> Đã xuất bản vẽ Chi tiết 6 (Tỷ lệ 1:1 chuẩn TCVN)")

# -------------------------------------------------------------
# 7. BẢN VẼ TỔNG HỢP CƠ KHÍ & BẢNG KÊ BOM
# -------------------------------------------------------------
def ve_ban_ve_tong_hop():
    fig, ax = setup_canvas()

    # Tiêu đề lớn bản vẽ tổng hợp
    ax.text(210, 280, "BẢN VẼ TỔNG HỢP BỘ CHỈNH GỐI BI TRỤC PHI 60MM", fontsize=13, fontweight='bold', ha='center', color='#0f172a')
    ax.text(210, 272, "HỆ THỐNG ĐỠ TRỐNG RANG CÀ PHÊ 100CM - TRỌN BỘ 6 CHI TIẾT CƠ KHÍ", fontsize=9.5, ha='center', color='#475569')

    # BẢNG KÊ VẬT TƯ & CHI TIẾT GIA CÔNG (BOM)
    # Bảng ở góc dưới bên trái x=25, y=55, w=380, h=70
    table_data = [
        ["STT", "TÊN CHI TIẾT GIA CÔNG", "QUY CÁCH KÍCH THƯỚC CHÍNH", "VẬT LIỆU", "S.LƯỢNG", "GHI CHÚ KỸ THUẬT"],
        ["01", "Chân bệ trụ ren trong M110", "Cao 15cm (150mm), Bích 165x165x16, 4 lỗ Ø14.5", "Gang FC250 / C45", "02 Cái", "Ren trong M110x3 sâu 110mm, bỏ ốc màu"],
        ["02", "Ống cố định ren ngoài S125", "Ren ngoài M110x3 dài 115 (tổng 133), Hex S125", "Thép C45", "02 Cái", "Đầu lục giác to S125 phay phẳng, 4 lỗ M6"],
        ["03", "Long đền tán khóa mỏng 5mm", "Lục giác S115mm, DÀY ĐÚNG 5.0mm, Ren M110x3", "Thép C45", "02 Cái", "ĐÃ XÓA CÂY CÙI TRÒN, vặn cờ-lê 115mm"],
        ["04", "Ống trụ tròn nhẵn mài bóng", "Dài 65mm, Ø ngoài 86, Ø trong 80 -> DÀY 3.0MM", "Thép C45 Mài Bóng", "02 Cái", "Mặt ngoài Ra≤0.8 trượt êm, gờ chặn trong Ø62"],
        ["05", "Bạc đạn đỡ trục phi 60mm", "Tiêu chuẩn 6012-2RS: Ø60 x Ø80 x Bề rộng 22mm", "Thép GCr15", "02 Cái", "10 Viên bi Ø8 PCD Ø70, phốt cao su 2RS"],
        ["06", "Mặt bít nguyên khối đặc kín", "Vành Ø104x8mm, Gờ Ø85.5x6mm, 4 vít chìm M6", "Thép C45 / Nhôm", "02 Cái", "ĐẶC KÍN NGUYÊN KHỐI 100% (KHÔNG THỦNG TÂM)"],
        ["07", "Bu-lông lục giác chìm DIN 7991", "Ren M6 x Bước 1.0 x Chiều dài 20mm (Chìm đầu)", "Inox 304", "08 Con", "Siết chặt cố định mặt bít [6] vào đầu [2]"]
    ]

    col_widths = [16, 75, 115, 45, 24, 105]
    row_height = 8.2
    x_t, y_t = 25, 55

    for row_idx, row in enumerate(table_data):
        curr_y = y_t + (len(table_data) - 1 - row_idx) * row_height
        curr_x = x_t
        is_header = (row_idx == 0)
        bg_color = '#0284c7' if is_header else ('#f1f5f9' if row_idx % 2 == 1 else '#ffffff')
        txt_color = '#ffffff' if is_header else '#0f172a'
        f_weight = 'bold' if is_header else ('bold' if row_idx in [1,2,3,4,5,6] else 'normal')

        for col_idx, text in enumerate(row):
            w_c = col_widths[col_idx]
            ax.add_patch(patches.Rectangle((curr_x, curr_y), w_c, row_height, fill=True, facecolor=bg_color, edgecolor='#94a3b8', lw=0.6))
            ax.text(curr_x + w_c/2, curr_y + row_height/2, text, fontsize=7.5 if not is_header else 8.0,
                    fontweight=f_weight, ha='center', va='center', color=txt_color)
            curr_x += w_c

    # 6 CARD THÔNG SỐ VÀNG CỦA 6 CHI TIẾT Ở NỬA TRÊN BẢN VẼ
    col_w = 122
    row_h = 60
    xs = [25, 153, 281]
    ys = [198, 132]

    cards = [
        ("[CT-01] CHÂN BỆ TRỤ REN TRONG CAO 15CM", xs[0], ys[0],
         ["- Bích vuông 165 x 165 x 16mm (4 lỗ bu-lông Ø14.5)", "- Thân trụ tròn Ø130mm, chiều cao tổng 15cm (150mm)", "- Ren trong M110x3 sâu 110mm, gờ loe chân Ø150mm", "- Đã bỏ hoàn toàn 4 ốc màu dưới chân bệ"]),
        ("[CT-02] ỐNG CỐ ĐỊNH REN NGOÀI LỤC GIÁC S125", xs[1], ys[0],
         ["- Thân tiện ren ngoài M110x3 dài 115mm (Tổng dài 133mm)", "- Đầu vặn lục giác to S = 125mm, bề dày 18mm phẳng đẹp", "- Lòng trong Ø86mm mài bóng trơn nhẵn Ra ≤ 0.8µm", "- 4 Lỗ ren M6 sâu 12mm phân bố đều trên PCD Ø94mm"]),
        ("[CT-03] LONG ĐỀN TÁN KHÓA LỤC GIÁC MỎNG 5MM", xs[2], ys[0],
         ["- Lục giác đều S = 115mm vừa vặn cờ-lê hoặc mỏ-lết tiêu chuẩn", "- ĐỘ DÀY: Đúng 5.0mm (-0.1 / 0mm) theo yêu cầu chỉ đạo", "- Ren trong M110x3 vặn siết chặt vào mặt bệ chân [1]", "- ĐÃ XÓA HOÀN TOÀN CÂY CÙI TRÒN / TAY CẦM"]),
        ("[CT-04] ỐNG TRỤ TRÒN NHẴN DÀY ĐÚNG 3MM", xs[0], ys[1],
         ["- Chiều dài 65mm, mặt ngoài mài bóng trơn nhẵn 100% Ra≤0.8", "- Ø ngoài 86mm, Ø trong 80mm -> DÀY THÀNH ĐÚNG 3.0MM", "- Gờ chặn trong dày 5mm, lỗ xuyên tâm láp Ø62mm", "- Trượt êm khít bên trong lòng ống ren ngoài [2]"]),
        ("[CT-05] BẠC ĐẠN ĐỠ TRỤC PHI 60MM (6012-2RS)", xs[1], ys[1],
         ["- Vòng bi tiêu chuẩn: Ø trong 60 x Ø ngoài 80 x Bề rộng 22mm", "- 10 Viên bi cầu Ø8mm phân bố đều trên vòng lăn PCD Ø70mm", "- Trang bị 2 phốt cao su 2RS chắn tuyệt đối bụi tro & mạt củi", "- Lắp ôm khít trục láp phi 60mm của trống rang 100cm"]),
        ("[CT-06] MẶT BÍT NGUYÊN KHỐI (ĐẶC KÍN)", xs[2], ys[1],
         ["- ĐẶC KÍN NGUYÊN KHỐI 100% (Hoàn toàn KHÔNG thủng lỗ tâm)", "- Vành bích Ø104 x 8mm, gờ định vị nguyên khối Ø85.5 x 6mm", "- 4 Lỗ bu-lông chìm M6 (khoét bậc Ø11 x 3.5) trên PCD Ø94", "- Bịt kín chống bụi bẩn và chặn cứng ca ngoài bạc đạn [5]"])
    ]

    for title, px, py, bullets in cards:
        ax.add_patch(patches.Rectangle((px, py), col_w, row_h, fill=True, facecolor='#f8fafc', edgecolor='#0284c7', lw=1.2))
        ax.add_patch(patches.Rectangle((px, py + row_h - 18), col_w, 18, fill=True, facecolor='#0284c7', edgecolor='#0284c7'))
        ax.text(px + col_w/2, py + row_h - 9, title, fontsize=8.2, fontweight='bold', ha='center', va='center', color='#ffffff')
        for idx, b in enumerate(bullets):
            ax.text(px + 6, py + row_h - 28 - idx*10.5, b, fontsize=7.5, color='#1e293b')

    # Khung tên tổng hợp ở góc phải
    draw_title_block(ax, "BỘ CHỈNH GỐI BI TRỤC PHI 60MM (6 CHI TIẾT)", "KT-BO-CHINH-01", "C45 / Gang FC250", qty="02 Cụm", scale="1:1 & 1:2")

    path = os.path.join(OUT_DIR, "ban_ve_tong_hop_6_chi_tiet_co_khi.png")
    fig.savefig(path, dpi=200)
    fig.savefig(os.path.join(ARTIFACT_DIR, "ban_ve_tong_hop_6_chi_tiet_co_khi.png"), dpi=200)
    plt.close(fig)
    print(">> Đã xuất bản vẽ tổng hợp 6 chi tiết cơ khí")

# ==========================================
# 5. HÀM MAIN THỰC HIỆN TOÀN BỘ QUY TRÌNH
# ==========================================
def main():
    print("=== BẮT ĐẦU TẠO TOÀN BỘ HỒ SƠ THIẾT KẾ CƠ KHÍ 2D & 3D ===")

    # 1. Tạo các solid trong FreeCAD và xuất 3D STEP
    print("1. Đang dựng 3D Solid và xuất file STEP tiêu chuẩn quốc tế...")
    doc = App.newDocument('BoChinhCoKhi')
    s1 = tao_solid_chi_tiet_1()
    s2 = tao_solid_chi_tiet_2()
    s3 = tao_solid_chi_tiet_3()
    s4 = tao_solid_chi_tiet_4()
    s5 = tao_solid_chi_tiet_5()
    s6 = tao_solid_chi_tiet_6()

    s1.exportStep(os.path.join(STEP_DIR, "CT01_Chan_Be_Ren_Trong_M110_H150.step"))
    s2.exportStep(os.path.join(STEP_DIR, "CT02_Ong_Ren_Ngoai_Luc_Giac_S125.step"))
    s3.exportStep(os.path.join(STEP_DIR, "CT03_Long_Den_Mong_5mm_S115.step"))
    s4.exportStep(os.path.join(STEP_DIR, "CT04_Ong_Truot_Tron_Nhan_Day_3mm.step"))
    s5.exportStep(os.path.join(STEP_DIR, "CT05_Bac_Dan_Do_Truc_Phi60_6012_2RS.step"))
    s6.exportStep(os.path.join(STEP_DIR, "CT06_Mat_Bit_Nguyen_Khoi_Dac_Kin.step"))

    # Xuất cụm lắp ráp hoàn chỉnh và cụm tháo rời 3D
    s2_asm = s2.copy(); s2_asm.translate(App.Vector(0, 0, 80))
    s3_asm = s3.copy(); s3_asm.translate(App.Vector(0, 0, 150))
    s4_asm = s4.copy(); s4_asm.translate(App.Vector(0, 0, 130))
    s5_asm = s5.copy(); s5_asm.translate(App.Vector(0, 0, 135))
    s6_asm = s6.copy(); s6_asm.translate(App.Vector(0, 0, 195))
    cum_lap_rap = Part.makeCompound([s1, s2_asm, s3_asm, s4_asm, s5_asm, s6_asm])
    cum_lap_rap.exportStep(os.path.join(STEP_DIR, "CUM_BO_CHINH_LAP_RAP_HOAN_CHINH.step"))

    s1_exp = s1.copy()
    s3_exp = s3.copy(); s3_exp.translate(App.Vector(0, 0, 180))
    s2_exp = s2.copy(); s2_exp.translate(App.Vector(0, 0, 250))
    s4_exp = s4.copy(); s4_exp.translate(App.Vector(0, 0, 430))
    s5_exp = s5.copy(); s5_exp.translate(App.Vector(0, 0, 540))
    s6_exp = s6.copy(); s6_exp.translate(App.Vector(0, 0, 640))
    cum_thao_roi = Part.makeCompound([s1_exp, s3_exp, s2_exp, s4_exp, s5_exp, s6_exp])
    cum_thao_roi.exportStep(os.path.join(STEP_DIR, "CUM_BO_CHINH_THAO_ROI_EXPLODED.step"))

    print("   -> Đã xuất xong 6 file STEP chi tiết + 2 file STEP cụm lắp ráp & tháo rời")

    # 2. Render 3D thumbnails
    print("2. Đang render phối cảnh 3D isometric cho từng chi tiết...")
    render_3d_thumbnail(s1, os.path.join(THUMB_DIR, "thumb_ct1.png"), color='#64748b', edge_color='#334155')
    render_3d_thumbnail(s2, os.path.join(THUMB_DIR, "thumb_ct2.png"), color='#0284c7', edge_color='#0369a1')
    render_3d_thumbnail(s3, os.path.join(THUMB_DIR, "thumb_ct3.png"), color='#ea580c', edge_color='#c2410c')
    render_3d_thumbnail(s4, os.path.join(THUMB_DIR, "thumb_ct4.png"), color='#10b981', edge_color='#047857')
    render_3d_thumbnail(s5, os.path.join(THUMB_DIR, "thumb_ct5.png"), color='#eab308', edge_color='#ca8a04')
    render_3d_thumbnail(s6, os.path.join(THUMB_DIR, "thumb_ct6.png"), color='#94a3b8', edge_color='#475569')
    print("   -> Đã xuất xong 6 ảnh thumbnail 3D")

    # 3. Xuất file DXF vector 2D
    print("3. Đang xuất file 2D DXF vector cho máy CNC...")
    o1 = doc.addObject('Part::Feature', 'CT01_Chan_Be'); o1.Shape = s1
    o2 = doc.addObject('Part::Feature', 'CT02_Ong_Ren_S125'); o2.Shape = s2
    o3 = doc.addObject('Part::Feature', 'CT03_Long_Den_5mm'); o3.Shape = s3
    o4 = doc.addObject('Part::Feature', 'CT04_Ong_Truot_3mm'); o4.Shape = s4
    o5 = doc.addObject('Part::Feature', 'CT05_Bac_Dan_Phi60'); o5.Shape = s5
    o6 = doc.addObject('Part::Feature', 'CT06_Mat_Bit_Dac_Kin'); o6.Shape = s6

    importDXF.export([o1], os.path.join(DXF_DIR, "CT01_Chan_Be_Ren_Trong_M110_H150.dxf"))
    importDXF.export([o2], os.path.join(DXF_DIR, "CT02_Ong_Ren_Ngoai_Luc_Giac_S125.dxf"))
    importDXF.export([o3], os.path.join(DXF_DIR, "CT03_Long_Den_Mong_5mm_S115.dxf"))
    importDXF.export([o4], os.path.join(DXF_DIR, "CT04_Ong_Truot_Tron_Nhan_Day_3mm.dxf"))
    importDXF.export([o5], os.path.join(DXF_DIR, "CT05_Bac_Dan_Do_Truc_Phi60_6012_2RS.dxf"))
    importDXF.export([o6], os.path.join(DXF_DIR, "CT06_Mat_Bit_Nguyen_Khoi_Dac_Kin.dxf"))
    print("   -> Đã xuất xong 6 file DXF vector cho CNC")

    # 4. Xuất trọn bộ 7 bản vẽ kỹ thuật 2D
    print("4. Đang kết xuất trọn bộ bản vẽ cơ khí 2D với 3 hình chiếu chuẩn...")
    ve_chi_tiet_1()
    ve_chi_tiet_2()
    ve_chi_tiet_3()
    ve_chi_tiet_4()
    ve_chi_tiet_5()
    ve_chi_tiet_6()
    ve_ban_ve_tong_hop()

    print("=== HOÀN TẤT TOÀN BỘ QUY TRÌNH XUẤT HỒ SƠ THIẾT KẾ CƠ KHÍ THÀNH CÔNG ===")

if __name__ == '__main__':
    main()
