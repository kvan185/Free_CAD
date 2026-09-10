# -*- coding: utf-8 -*-
"""
HỆ THỐNG XUẤT 18 BẢN VẼ CƠ KHÍ ĐỘC LẬP (6 CHI TIẾT x 3 HÌNH CHIẾU ĐỨNG - BẰNG - CẠNH)
ĐẠT TIÊU CHUẨN TCVN / ISO:
- Mỗi bản vẽ là 1 tờ riêng biệt (Khổ A3 chuẩn)
- Khung bản vẽ, khung tên chuẩn TCVN
- Hình chiếu đứng (kèm mặt cắt lát cắt A-A), Hình chiếu bằng, Hình chiếu cạnh
- Đường kích thước, dung sai chế tạo, độ nhám bề mặt Ra, ký hiệu ren
- Khung ghi chú yêu cầu kỹ thuật chi tiết
- Nhúng thumbnail 3D Solid Isometric ở góc phải
- Ký hiệu góc chiếu thứ nhất TCVN

Tác giả: Khánh Văn <kvan18052004@gmail.com>
"""

import os
import sys
import math
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass
if hasattr(sys.stderr, 'reconfigure'):
    try: sys.stderr.reconfigure(encoding='utf-8')
    except Exception: pass

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Rectangle, Circle, Wedge, Arc, PathPatch
from matplotlib.path import Path
import matplotlib.image as mpimg
import numpy as np

# Thư mục lưu trữ
WORK_DIR = r"c:\VAN\CAD\ban_ve_18_hinh_chieu"
ARTIFACT_DIR = r"C:\Users\admin\.gemini\antigravity\brain\0b789148-0c1a-433f-9f39-ee380f84bb46"
ARTIFACT_OUT_DIR = os.path.join(ARTIFACT_DIR, "ban_ve_18_hinh_chieu")
THUMB_DIR = os.path.join(ARTIFACT_DIR, "scratch", "thumbs")

os.makedirs(WORK_DIR, exist_ok=True)
os.makedirs(ARTIFACT_OUT_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Segoe UI', 'Tahoma', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# CÁC HÀM TIỆN ÍCH VẼ KHUNG VÀ KÝ HIỆU TIÊU CHUẨN
# ==========================================

def create_base_drawing(part_no_str, part_name, view_title, sheet_code, sheet_no, total_sheets, material, qty, thumb_idx, tech_notes):
    """Tạo phôi bản vẽ A3 tiêu chuẩn với khung bản vẽ, khung tên TCVN, ghi chú và thumbnail 3D."""
    fig = plt.figure(figsize=(16.54, 11.69), dpi=200, facecolor='#ffffff')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 420)
    ax.set_ylim(0, 297)
    ax.set_aspect('equal')
    ax.axis('off')

    # Khung ngoài và khung viền bản vẽ TCVN (Lề trái 25mm đóng gáy, 3 lề còn lại 10mm)
    outer_border = patches.Rectangle((5, 5), 410, 287, fill=False, edgecolor='#94a3b8', linewidth=0.6)
    ax.add_patch(outer_border)
    inner_border = patches.Rectangle((25, 10), 385, 277, fill=False, edgecolor='#0f172a', linewidth=2.0)
    ax.add_patch(inner_border)

    # Khung lưới toạ độ A-B-C-D / 1-2-3-4-5-6
    for i, char in enumerate(['D', 'C', 'B', 'A']):
        y = 10 + (i + 0.5) * (277 / 4)
        ax.text(15, y, char, fontsize=9, fontweight='bold', color='#64748b', va='center', ha='center')
        ax.text(415, y, char, fontsize=9, fontweight='bold', color='#64748b', va='center', ha='center')
    for j in range(6):
        x = 25 + (j + 0.5) * (385 / 6)
        ax.text(x, 7.5, str(j + 1), fontsize=9, fontweight='bold', color='#64748b', va='center', ha='center')
        ax.text(x, 289.5, str(j + 1), fontsize=9, fontweight='bold', color='#64748b', va='center', ha='center')

    # KHUNG TÊN TIÊU CHUẨN TCVN (Góc dưới bên phải)
    tb_x, tb_y = 250, 10
    tb_w, tb_h = 160, 58
    ax.add_patch(patches.Rectangle((tb_x, tb_y), tb_w, tb_h, fill=True, facecolor='#f8fafc', edgecolor='#0f172a', linewidth=1.8))
    
    # Đường kẻ trong khung tên
    ax.plot([tb_x, tb_x + tb_w], [tb_y + 14, tb_y + 14], 'k-', lw=1.2)
    ax.plot([tb_x, tb_x + tb_w], [tb_y + 28, tb_y + 28], 'k-', lw=1.2)
    ax.plot([tb_x, tb_x + tb_w], [tb_y + 44, tb_y + 44], 'k-', lw=1.2)
    
    ax.plot([tb_x + 95, tb_x + 95], [tb_y + 14, tb_y + 58], 'k-', lw=1.2)
    ax.plot([tb_x + 125, tb_x + 125], [tb_y + 14, tb_y + 44], 'k-', lw=1.2)
    ax.plot([tb_x + 70, tb_x + 70], [tb_y, tb_y + 14], 'k-', lw=1.0)
    ax.plot([tb_x + 115, tb_x + 115], [tb_y, tb_y + 14], 'k-', lw=1.0)

    # Nội dung khung tên
    ax.text(tb_x + 47.5, tb_y + 51, "MÁY RANG CỦI CÔNG NGHIỆP", fontsize=9, fontweight='bold', ha='center', va='center', color='#1e293b')
    ax.text(tb_x + 47.5, tb_y + 46, "CỤM CƠ CẤU BỘ CHỈNH VĂN", fontsize=8, fontweight='bold', ha='center', va='center', color='#0369a1')
    
    ax.text(tb_x + 127.5, tb_y + 51, "KÝ HIỆU BẢN VẼ", fontsize=7.5, color='#475569', ha='center', va='center')
    ax.text(tb_x + 127.5, tb_y + 46, sheet_code, fontsize=9.5, fontweight='bold', color='#b91c1c', ha='center', va='center')

    ax.text(tb_x + 47.5, tb_y + 36, f"CHI TIẾT 0{part_no_str}: {part_name.upper()}", fontsize=9, fontweight='bold', ha='center', va='center', color='#0f172a')
    ax.text(tb_x + 47.5, tb_y + 30.5, view_title.upper(), fontsize=8.5, fontweight='bold', ha='center', va='center', color='#047857')

    ax.text(tb_x + 110, tb_y + 36, "TỶ LỆ", fontsize=7.5, color='#475569', ha='center', va='center')
    ax.text(tb_x + 110, tb_y + 29, "1:1", fontsize=9, fontweight='bold', ha='center', va='center')
    
    ax.text(tb_x + 142.5, tb_y + 36, "TỜ / TỔNG", fontsize=7.5, color='#475569', ha='center', va='center')
    ax.text(tb_x + 142.5, tb_y + 29, f"{sheet_no:02d} / {total_sheets:02d}", fontsize=9.5, fontweight='bold', color='#1d4ed8', ha='center', va='center')

    ax.text(tb_x + 47.5, tb_y + 21, f"VẬT LIỆU: {material}", fontsize=8.5, fontweight='bold', ha='center', va='center', color='#334155')
    ax.text(tb_x + 127.5, tb_y + 21, f"SL: {qty}", fontsize=8.5, fontweight='bold', ha='center', va='center', color='#334155')

    ax.text(tb_x + 35, tb_y + 7, "THIẾT KẾ: Khánh Văn", fontsize=8, color='#334155', ha='center', va='center')
    ax.text(tb_x + 92.5, tb_y + 7, "DUYỆT: Q.LÝ", fontsize=8, color='#334155', ha='center', va='center')
    ax.text(tb_x + 137.5, tb_y + 7, "NGÀY: 10/09/26", fontsize=8, color='#334155', ha='center', va='center')

    # KHUNG GHI CHÚ YÊU CẦU KỸ THUẬT (Góc dưới bên trái)
    ax.add_patch(patches.Rectangle((30, 10), 160, 48, fill=True, facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.0))
    ax.text(35, 53, "YÊU CẦU KỸ THUẬT & GIA CÔNG:", fontsize=8.5, fontweight='bold', color='#0f172a')
    for idx, note in enumerate(tech_notes):
        ax.text(35, 46 - idx * 6.8, f"{idx+1}. {note}", fontsize=7.5, color='#334155')

    # NHÚNG ẢNH 3D ISOMETRIC THUMBNAIL (Góc trên bên phải)
    thumb_path = os.path.join(THUMB_DIR, f"thumb_ct{thumb_idx}.png")
    if os.path.exists(thumb_path):
        img = mpimg.imread(thumb_path)
        thumb_ax = fig.add_axes([0.76, 0.72, 0.20, 0.23])
        thumb_ax.imshow(img)
        thumb_ax.axis('off')
        # Viền khung ảnh 3D
        ax.add_patch(patches.Rectangle((315, 210), 90, 72, fill=False, edgecolor='#94a3b8', linewidth=1.2, linestyle='--'))
        ax.text(360, 283.5, f"MÔ HÌNH 3D SOLID (CT{thumb_idx})", fontsize=7.5, fontweight='bold', color='#0284c7', ha='center')

    # BIỂU TƯỢNG GÓC CHIẾU THỨ NHẤT (TCVN)
    # Vẽ hình nón cụt và hai vòng tròn đồng tâm tại góc trên trái
    proj_x, proj_y = 45, 275
    ax.plot([proj_x, proj_x + 12, proj_x + 12, proj_x, proj_x], [proj_y - 3, proj_y - 6, proj_y + 6, proj_y + 3, proj_y - 3], 'k-', lw=1.0)
    ax.plot([proj_x - 4, proj_x + 32], [proj_y, proj_y], 'r-.', lw=0.6)
    c1 = Circle((proj_x + 22, proj_y), 3, fill=False, edgecolor='k', lw=1.0)
    c2 = Circle((proj_x + 22, proj_y), 6, fill=False, edgecolor='k', lw=1.0)
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.text(proj_x + 11, proj_y - 9, "ISO / TCVN (GÓC CHIẾU 1)", fontsize=6.5, color='#64748b', ha='center')

    # TIÊU ĐỀ HÌNH CHIẾU CHÍNH GIỮA TRÊN
    ax.text(210, 275, view_title.upper(), fontsize=14, fontweight='heavy', color='#0f172a', ha='center', va='center')
    ax.plot([140, 280], [270, 270], color='#0284c7', lw=1.8)

    return fig, ax

# ==========================================
# CÁC HÀM VẼ ĐƯỜNG KÍCH THƯỚC VÀ DUNG SAI
# ==========================================

def draw_dim_h(ax, x1, x2, y, text, offset=6, color='#0f172a', is_tol=False, tol_text=''):
    """Vẽ đường kích thước nằm ngang với 2 mũi tên và đường gióng."""
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_dim = y + offset if offset >= 0 else y + offset
    # Đường gióng
    ax.plot([x_min, x_min], [min(y, y_dim) - 1.5, max(y, y_dim) + 1.5], color='#475569', lw=0.7)
    ax.plot([x_max, x_max], [min(y, y_dim) - 1.5, max(y, y_dim) + 1.5], color='#475569', lw=0.7)
    # Đường kích thước
    ax.plot([x_min, x_max], [y_dim, y_dim], color=color, lw=0.9)
    # Mũi tên 2 đầu
    ax.annotate('', xy=(x_min, y_dim), xytext=(x_min + 3.0, y_dim),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=0.9, mutation_scale=9))
    ax.annotate('', xy=(x_max, y_dim), xytext=(x_max - 3.0, y_dim),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=0.9, mutation_scale=9))
    # Text kích thước
    mid_x = (x_min + x_max) / 2.0
    ax.text(mid_x, y_dim + 1.8, text, fontsize=8.5, fontweight='bold', color=color, ha='center', va='bottom',
            bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='none', alpha=0.9))
    if is_tol and tol_text:
        ax.text(mid_x, y_dim - 2.8, tol_text, fontsize=6.5, color='#475569', ha='center', va='top')

def draw_dim_v(ax, y1, y2, x, text, offset=6, color='#0f172a', is_tol=False, tol_text=''):
    """Vẽ đường kích thước thẳng đứng với 2 mũi tên và đường gióng."""
    y_min, y_max = min(y1, y2), max(y1, y2)
    x_dim = x + offset if offset >= 0 else x + offset
    # Đường gióng
    ax.plot([min(x, x_dim) - 1.5, max(x, x_dim) + 1.5], [y_min, y_min], color='#475569', lw=0.7)
    ax.plot([min(x, x_dim) - 1.5, max(x, x_dim) + 1.5], [y_max, y_max], color='#475569', lw=0.7)
    # Đường kích thước
    ax.plot([x_dim, x_dim], [y_min, y_max], color=color, lw=0.9)
    # Mũi tên 2 đầu
    ax.annotate('', xy=(x_dim, y_min), xytext=(x_dim, y_min + 3.0),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=0.9, mutation_scale=9))
    ax.annotate('', xy=(x_dim, y_max), xytext=(x_dim, y_max - 3.0),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=0.9, mutation_scale=9))
    # Text kích thước (xoay 90 độ)
    mid_y = (y_min + y_max) / 2.0
    ax.text(x_dim - 1.8 if offset < 0 else x_dim + 1.8, mid_y, text, fontsize=8.5, fontweight='bold',
            color=color, ha='right' if offset < 0 else 'left', va='center', rotation=90,
            bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='none', alpha=0.9))
    if is_tol and tol_text:
        ax.text(x_dim + 2.8 if offset < 0 else x_dim - 2.8, mid_y, tol_text, fontsize=6.5, color='#475569',
                ha='left' if offset < 0 else 'right', va='center', rotation=90)

def draw_dim_dia(ax, cx, cy, r, angle_deg, text, color='#0f172a'):
    """Vẽ đường kích thước đường kính có mũi tên chỉ xiên và giá đỡ ngang."""
    rad = math.radians(angle_deg)
    px = cx + r * math.cos(rad)
    py = cy + r * math.sin(rad)
    p_lead = (px + 12 * math.cos(rad), py + 12 * math.sin(rad))
    ax.annotate('', xy=(px, py), xytext=p_lead,
                arrowprops=dict(arrowstyle='-|>', color=color, lw=0.9, mutation_scale=9))
    arm_x = p_lead[0] + (16 if math.cos(rad) >= 0 else -16)
    ax.plot([p_lead[0], arm_x], [p_lead[1], p_lead[1]], color=color, lw=0.9)
    ax.text(arm_x + (2 if math.cos(rad) >= 0 else -2), p_lead[1] + 1.2, text,
            fontsize=8.5, fontweight='bold', color=color,
            ha='left' if math.cos(rad) >= 0 else 'right', va='bottom')

def draw_center_axes(ax, cx, cy, rx, ry, color='#ef4444', lw=0.7):
    """Vẽ đường tâm chữ thập nét chấm gạch màu đỏ."""
    ax.plot([cx - rx - 8, cx + rx + 8], [cy, cy], color=color, linestyle='-.', lw=lw)
    ax.plot([cx, cx], [cy - ry - 8, cy + ry + 8], color=color, linestyle='-.', lw=lw)

# ==========================================
# 18 BẢN VẼ CHI TIẾT ĐỘC LẬP
# ==========================================

# ----------------------------------------------------
# CHI TIẾT 1: CHÂN BỆ TRỤ REN TRONG M110 CAO 15CM
# ----------------------------------------------------

def tao_BV01_CT01_Dung():
    notes = [
        "Tiện ren trong M110x3 bước 3, độ chính xác cấp 6H, chiều sâu 110mm.",
        "Độ vuông góc giữa mặt bích và đường tâm trụ đạt 0.05mm.",
        "Bề mặt ren Ra 1.6, bề mặt bích Ra 3.2. Không sơn bề mặt ren.",
        "Đã bỏ hoàn toàn 4 bu lông màu dưới chân bệ theo đúng yêu cầu.",
        "Vát mép miệng ren 2x45 độ, làm sạch bavia sắc cạnh."
    ]
    fig, ax = create_base_drawing('1', 'Chân bệ trụ ren M110', 'Hình chiếu đứng / Mặt cắt dọc A-A',
                                  'BV01_CT01', 1, 18, 'Thép CT3 / SS400', '02 Cái', 1, notes)
    
    # Gốc toạ độ tâm bệ: (170, 95)
    cx, cy = 170, 95
    # Bích 165 x 16 (y từ cy đến cy+16)
    # Trụ Phi 130 cao đến cy+150 (gờ loe phi 150 tại chân)
    # Lỗ ren M110 sâu 110 (từ cy+150 xuống cy+40)
    # Lỗ đáy phi 104 xuyên từ cy+40 xuống cy
    # Lỗ bu-lông chân phi 14.5 tại x = cx - 65, cx + 65

    # Đường tâm chính
    ax.plot([cx, cx], [cy - 12, cy + 165], 'r-.', lw=0.8)

    # Nửa trái: Hình chiếu ngoài
    pts_left = [
        [cx, cy + 150], [cx - 65, cy + 150], [cx - 65, cy + 41],
        [cx - 75, cy + 16], [cx - 82.5, cy + 16], [cx - 82.5, cy],
        [cx, cy]
    ]
    ax.plot([p[0] for p in pts_left], [p[1] for p in pts_left], 'k-', lw=1.6)

    # Nửa phải: Mặt cắt hatching A-A
    # Kim loại cắt:
    # 1. Bích và thân đặc bao quanh lỗ ren & khoang đáy
    poly_cut = [
        [cx, cy + 40], [cx + 52, cy + 40], [cx + 52, cy], [cx + 82.5, cy],
        [cx + 82.5, cy + 16], [cx + 75, cy + 16], [cx + 65, cy + 41],
        [cx + 65, cy + 150], [cx + 55, cy + 150], [cx + 55, cy + 40], [cx, cy + 40]
    ]
    # Khoét lỗ bu-lông chân Ø14.5 tại x = cx+65 (từ x=57.75 đến 72.25)
    p_hatch = patches.Polygon([
        [cx + 55, cy + 40], [cx + 65, cy + 40], [cx + 65, cy + 150], [cx + 55, cy + 150]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.4)
    ax.add_patch(p_hatch)

    p_hatch_mid = patches.Polygon([
        [cx + 52, cy + 16], [cx + 75, cy + 16], [cx + 65, cy + 41], [cx + 55, cy + 41], [cx + 55, cy + 40], [cx + 52, cy + 40]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.4)
    ax.add_patch(p_hatch_mid)

    p_hatch_base1 = patches.Polygon([
        [cx + 52, cy], [cx + 57.75, cy], [cx + 57.75, cy + 16], [cx + 52, cy + 16]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.4)
    ax.add_patch(p_hatch_base1)

    p_hatch_base2 = patches.Polygon([
        [cx + 72.25, cy], [cx + 82.5, cy], [cx + 82.5, cy + 16], [cx + 72.25, cy + 16]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.4)
    ax.add_patch(p_hatch_base2)

    # Lỗ bu-lông bên phải và bên trái
    for sign in [-1, 1]:
        bx = cx + sign * 65
        ax.plot([bx - 7.25, bx - 7.25], [cy, cy + 16], 'k-', lw=1.1)
        ax.plot([bx + 7.25, bx + 7.25], [cy, cy + 16], 'k-', lw=1.1)
        ax.plot([bx, bx], [cy - 5, cy + 21], 'r-.', lw=0.6)

    # Đường ren M110 bên phải (đỉnh ren phi 110 x=cx+55 nét đậm, chân ren phi 106.7 x=cx+53.35 nét mảnh)
    ax.plot([cx + 55, cx + 55], [cy + 40, cy + 150], 'k-', lw=1.4)
    ax.plot([cx + 53.35, cx + 53.35], [cy + 40, cy + 150], color='#2563eb', lw=0.9)
    # Đáy ren vát mép
    ax.plot([cx + 52, cx + 55], [cy + 40, cy + 40], 'k-', lw=1.2)

    # Đường phân cách nửa cắt / nửa chiếu
    ax.plot([cx, cx], [cy, cy + 150], 'r-.', lw=1.0)
    # Đường đáy
    ax.plot([cx - 82.5, cx + 82.5], [cy, cy], 'k-', lw=1.6)
    # Đỉnh bệ
    ax.plot([cx - 65, cx], [cy + 150, cy + 150], 'k-', lw=1.6)

    # KÍCH THƯỚC CHI TIẾT
    # Chiều cao tổng 150
    draw_dim_v(ax, cy, cy + 150, cx - 82.5, "150 ±0.2", offset=-18)
    # Chiều cao bích 16
    draw_dim_v(ax, cy, cy + 16, cx - 82.5, "16", offset=-8)
    # Chiều sâu ren 110
    draw_dim_v(ax, cy + 40, cy + 150, cx + 55, "Sâu 110", offset=-16, color='#047857')
    # Bề rộng bích 165
    draw_dim_h(ax, cx - 82.5, cx + 82.5, cy, "□ 165", offset=-14)
    # Khoảng cách 2 lỗ bu-lông chân 130
    draw_dim_h(ax, cx - 65, cx + 65, cy, "130 ±0.15", offset=-26)
    # Đường kính trụ phi 130
    draw_dim_h(ax, cx - 65, cx + 65, cy + 150, "Ø 130", offset=14)
    # Đường kính gờ loe phi 150
    draw_dim_h(ax, cx - 75, cx + 75, cy + 16, "Ø 150", offset=8)
    # Ren M110x3
    ax.annotate('Ren trong M110x3 - 6H', xy=(cx + 54, cy + 95), xytext=(cx + 85, cy + 115),
                arrowprops=dict(arrowstyle='-|>', color='#2563eb', lw=1.0),
                fontsize=9, fontweight='bold', color='#2563eb')
    # Lỗ bu-lông chân
    ax.annotate('4 Lỗ Ø14.5 xuyên suốt\n(ĐÃ BỎ 4 ỐC MÀU)', xy=(cx + 65, cy + 8), xytext=(cx + 95, cy + 25),
                arrowprops=dict(arrowstyle='-|>', color='#b91c1c', lw=1.0),
                fontsize=8, fontweight='bold', color='#b91c1c')

    fig.savefig(os.path.join(WORK_DIR, "BV01_CT01_Chan_Be_Hinh_Chieu_Dung.png"))
    plt.close(fig)

def tao_BV02_CT01_Bang():
    notes = [
        "Hình chiếu bằng nhìn từ trên xuống mặt bích 165x165.",
        "4 góc bích bo tròn bán kính R15 đồng đều.",
        "4 lỗ bắt bu-lông Ø14.5 cách đều tâm 130x130mm (không gắn ốc chân).",
        "Vòng tròn đỉnh ren nét liền, chân ren vẽ bằng nét đứt 3/4 cung tròn chuẩn ISO."
    ]
    fig, ax = create_base_drawing('1', 'Chân bệ trụ ren M110', 'Hình chiếu bằng (Top View)',
                                  'BV02_CT01', 2, 18, 'Thép CT3 / SS400', '02 Cái', 1, notes)
    
    cx, cy = 175, 145
    draw_center_axes(ax, cx, cy, 95, 95)

    # Khung bích vuông 165x165 có bo góc R15
    rect_poly = patches.FancyBboxPatch((cx - 82.5, cy - 82.5), 165, 165,
                                       boxstyle="round,pad=0,rounding_size=15",
                                       facecolor='#f8fafc', edgecolor='#0f172a', lw=1.6)
    ax.add_patch(rect_poly)

    # Gờ loe chân Ø150
    c_loe = Circle((cx, cy), 75, fill=False, edgecolor='#64748b', lw=1.0, linestyle='--')
    ax.add_patch(c_loe)

    # Thân trụ Ø130
    c_tru = Circle((cx, cy), 65, fill=False, edgecolor='#0f172a', lw=1.4)
    ax.add_patch(c_tru)

    # Lỗ ren M110 (đỉnh ren phi 106.7 nét liền, chân ren phi 110 là nét mảnh hở 1/4 cung)
    c_ren_dinh = Circle((cx, cy), 53.35, fill=False, edgecolor='#0f172a', lw=1.3)
    ax.add_patch(c_ren_dinh)
    arc_ren_day = Arc((cx, cy), 110, 110, angle=0, theta1=20, theta2=290, edgecolor='#2563eb', lw=1.1)
    ax.add_patch(arc_ren_day)

    # Lỗ thông phoi đáy Ø104
    c_day = Circle((cx, cy), 52, fill=False, edgecolor='#94a3b8', lw=0.8, linestyle=':')
    ax.add_patch(c_day)

    # 4 lỗ bu lông Ø14.5 tại (-65, -65), (-65, 65), (65, -65), (65, 65)
    for xb in [-65, 65]:
        for yb in [-65, 65]:
            hx, hy = cx + xb, cy + yb
            draw_center_axes(ax, hx, hy, 10, 10, lw=0.5)
            ch = Circle((hx, hy), 7.25, fill=True, facecolor='#ffffff', edgecolor='#0f172a', lw=1.2)
            ax.add_patch(ch)

    # KÍCH THƯỚC
    # Kích thước ngoài 165x165
    draw_dim_h(ax, cx - 82.5, cx + 82.5, cy + 82.5, "165", offset=14)
    draw_dim_v(ax, cy - 82.5, cy + 82.5, cx - 82.5, "165", offset=-14)
    # Khoảng cách tâm lỗ 130x130
    draw_dim_h(ax, cx - 65, cx + 65, cy - 65, "130 ±0.15", offset=-14)
    draw_dim_v(ax, cy - 65, cy + 65, cx + 65, "130 ±0.15", offset=14)
    # Đường kính trụ Ø130 & Gờ loe Ø150
    draw_dim_dia(ax, cx, cy, 65, 45, "Ø 130")
    draw_dim_dia(ax, cx, cy, 75, 135, "Gờ loe Ø 150")
    draw_dim_dia(ax, cx, cy, 55, -45, "Ren M110x3")
    # Ghi chú 4 lỗ Ø14.5
    ax.annotate('4 Lỗ Ø14.5 xuyên suốt\n(KHÔNG CÓ 4 ỐC CHÂN)', xy=(cx + 65, cy + 65), xytext=(cx + 85, cy + 95),
                arrowprops=dict(arrowstyle='-|>', color='#b91c1c', lw=1.0),
                fontsize=8.5, fontweight='bold', color='#b91c1c')
    # Bo góc R15
    ax.annotate('4x R15', xy=(cx - 82.5 + 4, cy + 82.5 - 4), xytext=(cx - 105, cy + 95),
                arrowprops=dict(arrowstyle='-|>', color='#0f172a', lw=0.8),
                fontsize=8, fontweight='bold')

    fig.savefig(os.path.join(WORK_DIR, "BV02_CT01_Chan_Be_Hinh_Chieu_Bang.png"))
    plt.close(fig)

def tao_BV03_CT01_Canh():
    notes = [
        "Hình chiếu cạnh nhìn từ trái sang vuông góc mặt bích.",
        "Thể hiện đường bao ngoài đối xứng, các nét khuất ren trong M110 và lỗ bu lông.",
        "Độ nhám bề mặt ngoài thân trụ Ra 6.3."
    ]
    fig, ax = create_base_drawing('1', 'Chân bệ trụ ren M110', 'Hình chiếu cạnh (Side View)',
                                  'BV03_CT01', 3, 18, 'Thép CT3 / SS400', '02 Cái', 1, notes)
    
    cx, cy = 175, 95
    ax.plot([cx, cx], [cy - 12, cy + 165], 'r-.', lw=0.8)

    # Đường bao ngoài bệ
    poly_outer = [
        [cx - 82.5, cy], [cx + 82.5, cy], [cx + 82.5, cy + 16],
        [cx + 75, cy + 16], [cx + 65, cy + 41], [cx + 65, cy + 150],
        [cx - 65, cy + 150], [cx - 65, cy + 41], [cx - 75, cy + 16],
        [cx - 82.5, cy + 16], [cx - 82.5, cy]
    ]
    ax.plot([p[0] for p in poly_outer], [p[1] for p in poly_outer], 'k-', lw=1.6)

    # Nét khuất lòng ren M110 (phi 110 từ cy+40 đến cy+150)
    ax.plot([cx - 55, cx - 55], [cy + 40, cy + 150], 'k--', lw=0.9)
    ax.plot([cx + 55, cx + 55], [cy + 40, cy + 150], 'k--', lw=0.9)
    ax.plot([cx - 52, cx + 52], [cy + 40, cy + 40], 'k--', lw=0.9)
    # Lỗ thông phoi đáy phi 104
    ax.plot([cx - 52, cx - 52], [cy, cy + 40], 'k--', lw=0.9)
    ax.plot([cx + 52, cx + 52], [cy, cy + 40], 'k--', lw=0.9)

    # Nét khuất 2 lỗ bu lông chân phi 14.5
    for sign in [-1, 1]:
        bx = cx + sign * 65
        ax.plot([bx - 7.25, bx - 7.25], [cy, cy + 16], 'k--', lw=0.8)
        ax.plot([bx + 7.25, bx + 7.25], [cy, cy + 16], 'k--', lw=0.8)
        ax.plot([bx, bx], [cy - 4, cy + 20], 'r-.', lw=0.5)

    # KÍCH THƯỚC
    draw_dim_v(ax, cy, cy + 150, cx - 82.5, "150", offset=-16)
    draw_dim_v(ax, cy, cy + 16, cx + 82.5, "16", offset=14)
    draw_dim_h(ax, cx - 82.5, cx + 82.5, cy, "165", offset=-14)
    draw_dim_h(ax, cx - 65, cx + 65, cy + 150, "Ø 130", offset=12)
    draw_dim_h(ax, cx - 55, cx + 55, cy + 70, "Ren M110 (Nét khuất)", offset=0, color='#2563eb')

    fig.savefig(os.path.join(WORK_DIR, "BV03_CT01_Chan_Be_Hinh_Chieu_Canh.png"))
    plt.close(fig)

# ----------------------------------------------------
# CHI TIẾT 2: ỐNG CỐ ĐỊNH REN NGOÀI ĐẦU LỤC GIÁC TO S125
# ----------------------------------------------------

def tao_BV04_CT02_Dung():
    notes = [
        "Ren ngoài M110x3 tiện suốt chiều dài 115mm, cấp chính xác 6g.",
        "Đầu lục giác to S=125mm dày 18mm vặn siết trực tiếp bằng cờ-lê/khẩu.",
        "Lòng trong Ø86 H7 mài bóng đạt độ nhám Ra 0.8 để dẫn hướng ống trượt.",
        "4 lỗ ren M6 sâu 12mm bố trí đều trên PCD Ø94mm mặt đầu.",
        "Vát mép đỉnh ren 2.5x45 độ, vát mép miệng lỗ trong 1.5x45 độ."
    ]
    fig, ax = create_base_drawing('2', 'Ống ren ngoài đầu lục giác to S125', 'Hình chiếu đứng / Mặt cắt dọc toàn phần',
                                  'BV04_CT02', 4, 18, 'Thép C45 / S45C', '02 Cái', 2, notes)
    
    cx, cy = 175, 95
    # cy là đáy ren ngoài (y=0)
    # Chiều dài ren 115mm (đến cy+115)
    # Đầu lục giác to S125 dày 18mm (từ cy+115 đến cy+133)
    # Lòng trong Ø86 (r=43) suốt chiều dài
    # 4 lỗ ren M6 tại x = cx - 47, cx + 47 sâu 12mm từ cy+133 xuống cy+121

    ax.plot([cx, cx], [cy - 12, cy + 148], 'r-.', lw=0.8)

    # Mặt cắt kim loại bên trái
    # Ngoài: ren phi 110 (x=cx-55), lục giác S125 (x=cx-62.5)
    # Trong: lỗ phi 86 (x=cx-43)
    p_hatch_left = patches.Polygon([
        [cx - 43, cy], [cx - 55, cy], [cx - 55, cy + 115], [cx - 62.5, cy + 115],
        [cx - 62.5, cy + 133], [cx - 48.5, cy + 133], [cx - 48.5, cy + 121],
        [cx - 45.5, cy + 121], [cx - 45.5, cy + 133], [cx - 43, cy + 133], [cx - 43, cy]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.3)
    ax.add_patch(p_hatch_left)

    # Mặt cắt kim loại bên phải
    p_hatch_right = patches.Polygon([
        [cx + 43, cy], [cx + 55, cy], [cx + 55, cy + 115], [cx + 62.5, cy + 115],
        [cx + 62.5, cy + 133], [cx + 48.5, cy + 133], [cx + 48.5, cy + 121],
        [cx + 45.5, cy + 121], [cx + 45.5, cy + 133], [cx + 43, cy + 133], [cx + 43, cy]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.3)
    ax.add_patch(p_hatch_right)

    # Lỗ ren M6 2 bên (x = cx - 47, cx + 47)
    for sign in [-1, 1]:
        mx = cx + sign * 47
        ax.plot([mx, mx], [cy + 118, cy + 136], 'r-.', lw=0.6)
        ax.plot([mx - 1.5, mx - 1.5], [cy + 121, cy + 133], 'k-', lw=1.0)
        ax.plot([mx + 1.5, mx + 1.5], [cy + 121, cy + 133], 'k-', lw=1.0)
        ax.plot([mx - 1.5, mx + 1.5], [cy + 121, cy + 121], 'k-', lw=1.0)
        # Đáy mũi khoan nhọn 118 độ
        ax.plot([mx - 1.5, mx, mx + 1.5], [cy + 121, cy + 118.5, cy + 121], 'k-', lw=0.8)

    # Ren ngoài M110: đỉnh ren phi 110 nét liền đậm, chân ren phi 106.7 nét mảnh
    for sign in [-1, 1]:
        ax.plot([cx + sign * 55, cx + sign * 55], [cy, cy + 115], 'k-', lw=1.5)
        ax.plot([cx + sign * 53.35, cx + sign * 53.35], [cy, cy + 115], color='#2563eb', lw=0.9)

    # Đầu lục giác S125
    ax.plot([cx - 62.5, cx + 62.5], [cy + 133, cy + 133], 'k-', lw=1.6)
    ax.plot([cx - 62.5, cx - 55], [cy + 115, cy + 115], 'k-', lw=1.3)
    ax.plot([cx + 55, cx + 62.5], [cy + 115, cy + 115], 'k-', lw=1.3)
    ax.plot([cx - 62.5, cx - 62.5], [cy + 115, cy + 133], 'k-', lw=1.6)
    ax.plot([cx + 62.5, cx + 62.5], [cy + 115, cy + 133], 'k-', lw=1.6)

    # Đáy ống
    ax.plot([cx - 55, cx - 43], [cy, cy], 'k-', lw=1.4)
    ax.plot([cx + 43, cx + 55], [cy, cy], 'k-', lw=1.4)

    # KÍCH THƯỚC
    # Tổng chiều dài 133
    draw_dim_v(ax, cy, cy + 133, cx + 62.5, "133 ±0.2", offset=18)
    # Chiều dài ren 115
    draw_dim_v(ax, cy, cy + 115, cx - 62.5, "115", offset=-14)
    # Bề dày đầu lục giác 18
    draw_dim_v(ax, cy + 115, cy + 133, cx - 62.5, "18", offset=-8)
    # Lòng trong Ø86 H7
    draw_dim_h(ax, cx - 43, cx + 43, cy + 60, "Ø 86 H7 (+0.035/0)", offset=0, color='#047857')
    # Bề rộng lục giác S=125
    draw_dim_h(ax, cx - 62.5, cx + 62.5, cy + 133, "S = 125", offset=14)
    # Ren ngoài M110x3
    draw_dim_h(ax, cx - 55, cx + 55, cy, "Ren ngoài M110x3 - 6g", offset=-14, color='#2563eb')
    # Kích thước 4 lỗ M6 sâu 12 trên PCD 94
    ax.annotate('4 Lỗ ren M6 sâu 12mm\ntrên PCD Ø94', xy=(cx + 47, cy + 127), xytext=(cx + 78, cy + 142),
                arrowprops=dict(arrowstyle='-|>', color='#0f172a', lw=0.9),
                fontsize=8.5, fontweight='bold')
    # Độ nhám mài bóng
    ax.annotate('Mài bóng Ra 0.8', xy=(cx - 43, cy + 85), xytext=(cx - 85, cy + 95),
                arrowprops=dict(arrowstyle='-|>', color='#047857', lw=0.9),
                fontsize=8.5, fontweight='bold', color='#047857')

    fig.savefig(os.path.join(WORK_DIR, "BV04_CT02_Ong_Ren_Hinh_Chieu_Dung.png"))
    plt.close(fig)

def tao_BV05_CT02_Bang():
    notes = [
        "Hình chiếu bằng nhìn từ phía mặt đầu lục giác to S125.",
        "Lục giác ngoài kích thước 2 mặt song song S = 125mm.",
        "Lòng trong Ø86 H7 đồng tâm tuyệt đối với vòng lục giác và vòng ren.",
        "4 lỗ ren M6 phân bố đều góc 90 độ trên đường tròn PCD Ø94mm."
    ]
    fig, ax = create_base_drawing('2', 'Ống ren ngoài đầu lục giác to S125', 'Hình chiếu bằng (Top View)',
                                  'BV05_CT02', 5, 18, 'Thép C45 / S45C', '02 Cái', 2, notes)
    
    cx, cy = 175, 145
    draw_center_axes(ax, cx, cy, 85, 85)

    # Lục giác đều S=125mm (R = 125 / sqrt(3) = 72.17mm)
    R_hex = 125.0 / math.sqrt(3.0)
    hex_pts = []
    for i in range(6):
        ang = math.radians(i * 60.0 + 30.0)
        hex_pts.append([cx + R_hex * math.cos(ang), cy + R_hex * math.sin(ang)])
    p_hex = patches.Polygon(hex_pts, closed=True, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.8)
    ax.add_patch(p_hex)

    # Đường tròn PCD Ø94
    c_pcd = Circle((cx, cy), 47, fill=False, edgecolor='#ef4444', lw=0.8, linestyle='-.')
    ax.add_patch(c_pcd)

    # Lỗ trong Ø86 H7
    c_in = Circle((cx, cy), 43, fill=True, facecolor='#ffffff', edgecolor='#0f172a', lw=1.5)
    ax.add_patch(c_in)

    # Vòng đỉnh ren ngoài M110 bên dưới (nét khuất)
    c_ren = Circle((cx, cy), 55, fill=False, edgecolor='#64748b', lw=0.9, linestyle='--')
    ax.add_patch(c_ren)

    # 4 lỗ ren M6 trên PCD 94 góc 45, 135, 225, 315 độ
    for i in range(4):
        ang = math.radians(i * 90.0 + 45.0)
        hx = cx + 47.0 * math.cos(ang)
        hy = cy + 47.0 * math.sin(ang)
        draw_center_axes(ax, hx, hy, 6, 6, lw=0.5)
        ch_in = Circle((hx, hy), 2.5, fill=True, facecolor='#ffffff', edgecolor='#0f172a', lw=1.0)
        ax.add_patch(ch_in)
        # Nét ren M6 hở 3/4 vòng
        arc_m6 = Arc((hx, hy), 6.0, 6.0, angle=0, theta1=30, theta2=300, edgecolor='#2563eb', lw=0.8)
        ax.add_patch(arc_m6)

    # KÍCH THƯỚC
    # Kích thước S=125mm
    ax.plot([cx - 62.5, cx - 62.5], [cy - 36.08, cy + 36.08], 'k-', lw=1.0)
    ax.plot([cx + 62.5, cx + 62.5], [cy - 36.08, cy + 36.08], 'k-', lw=1.0)
    draw_dim_h(ax, cx - 62.5, cx + 62.5, cy + 36.08, "S = 125", offset=20)
    # Lỗ trong Ø86 H7
    draw_dim_dia(ax, cx, cy, 43, 135, "Ø 86 H7")
    # PCD Ø94
    draw_dim_dia(ax, cx, cy, 47, -35, "PCD Ø 94")
    # 4 lỗ ren M6
    hx45 = cx + 47.0 * math.cos(math.radians(45.0))
    hy45 = cy + 47.0 * math.sin(math.radians(45.0))
    ax.annotate('4 Lỗ ren M6 sâu 12\n(Góc 90°)', xy=(hx45, hy45), xytext=(cx + 70, cy + 70),
                arrowprops=dict(arrowstyle='-|>', color='#0f172a', lw=0.9),
                fontsize=8.5, fontweight='bold')

    fig.savefig(os.path.join(WORK_DIR, "BV05_CT02_Ong_Ren_Hinh_Chieu_Bang.png"))
    plt.close(fig)

def tao_BV06_CT02_Canh():
    notes = [
        "Hình chiếu cạnh thể hiện đầu lục giác 18mm và thân ren M110 dài 115mm.",
        "Các đường nét khuất thể hiện lỗ trụ trong Ø86 và 2 lỗ ren M6.",
        "Vát mép đuôi ren 2.5x45 độ."
    ]
    fig, ax = create_base_drawing('2', 'Ống ren ngoài đầu lục giác to S125', 'Hình chiếu cạnh (Side View)',
                                  'BV06_CT02', 6, 18, 'Thép C45 / S45C', '02 Cái', 2, notes)
    
    cx, cy = 175, 95
    ax.plot([cx, cx], [cy - 12, cy + 148], 'r-.', lw=0.8)

    # Thân ren M110
    ax.plot([cx - 55, cx + 55, cx + 55, cx - 55, cx - 55], [cy, cy, cy + 115, cy + 115, cy], 'k-', lw=1.5)
    # Đường chân ren
    ax.plot([cx - 53.35, cx - 53.35], [cy, cy + 115], color='#2563eb', lw=0.9)
    ax.plot([cx + 53.35, cx + 53.35], [cy, cy + 115], color='#2563eb', lw=0.9)

    # Đầu lục giác S125 (nhìn cạnh bề rộng 125mm)
    ax.plot([cx - 62.5, cx + 62.5, cx + 62.5, cx - 62.5, cx - 62.5],
            [cy + 115, cy + 115, cy + 133, cy + 133, cy + 115], 'k-', lw=1.6)

    # Nét đứt lỗ trong Ø86
    ax.plot([cx - 43, cx - 43], [cy, cy + 133], 'k--', lw=0.9)
    ax.plot([cx + 43, cx + 43], [cy, cy + 133], 'k--', lw=0.9)

    # Nét đứt 2 lỗ M6
    for sign in [-1, 1]:
        mx = cx + sign * 47
        ax.plot([mx - 1.5, mx - 1.5], [cy + 121, cy + 133], 'k--', lw=0.7)
        ax.plot([mx + 1.5, mx + 1.5], [cy + 121, cy + 133], 'k--', lw=0.7)

    # KÍCH THƯỚC
    draw_dim_v(ax, cy, cy + 133, cx + 62.5, "133", offset=16)
    draw_dim_v(ax, cy, cy + 115, cx - 62.5, "115", offset=-14)
    draw_dim_v(ax, cy + 115, cy + 133, cx - 62.5, "18", offset=-8)
    draw_dim_h(ax, cx - 55, cx + 55, cy, "M110", offset=-14, color='#2563eb')
    draw_dim_h(ax, cx - 62.5, cx + 62.5, cy + 133, "S = 125", offset=12)

    fig.savefig(os.path.join(WORK_DIR, "BV06_CT02_Ong_Ren_Hinh_Chieu_Canh.png"))
    plt.close(fig)

# ----------------------------------------------------
# CHI TIẾT 3: LONG ĐỀN / TÁN KHÓA LỤC GIÁC MỎNG 5MM
# ----------------------------------------------------

def tao_BV07_CT03_Dung():
    notes = [
        "Độ dày long đền đúng 5.0mm (-0.1/0), tuyệt đối không làm dày.",
        "ĐÃ XÓA HOÀN TOÀN CÂY CÙI TRÒN / TAY CẦM THEO YÊU CẦU.",
        "Hình dạng lục giác S=115mm siết chặt bằng cờ-lê hoặc mỏ-lết.",
        "Ren trong M110x3 bước 3, vát mép 2 mặt đầu 0.5x45 độ.",
        "Xử lý bề mặt: Nhiệt luyện tôi ram nhẹ, mạ kẽm chống gỉ."
    ]
    fig, ax = create_base_drawing('3', 'Long đền tán khóa mỏng 5mm', 'Hình chiếu đứng / Mặt cắt A-A',
                                  'BV07_CT03', 7, 18, 'Thép C45 tôi cứng', '02 Cái', 3, notes)
    
    # Do chi tiết mỏng 5mm nên vẽ phóng to tỷ lệ 2:1 trên bản vẽ nhưng ghi đúng kích thước
    cx, cy = 180, 140
    ax.plot([cx, cx], [cy - 20, cy + 30], 'r-.', lw=0.8)

    # Chiều dày 5mm, bán kính ren r=55, lục giác r=57.5 (S=115)
    # Tỷ lệ hiển thị trục Y giãn 3x để nhìn rất rõ nét mặt cắt dày 5mm
    scale_y = 3.0
    h_vis = 5.0 * scale_y  # 15mm trực quan

    # Mặt cắt kim loại bên trái
    p_cut_l = patches.Polygon([
        [cx - 57.5, cy], [cx - 53.35, cy], [cx - 53.35, cy + h_vis], [cx - 57.5, cy + h_vis]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.4)
    ax.add_patch(p_cut_l)

    # Mặt cắt kim loại bên phải
    p_cut_r = patches.Polygon([
        [cx + 53.35, cy], [cx + 57.5, cy], [cx + 57.5, cy + h_vis], [cx + 53.35, cy + h_vis]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.4)
    ax.add_patch(p_cut_r)

    # Đường đỉnh ren phi 106.7 và chân ren phi 110
    ax.plot([cx - 53.35, cx - 53.35], [cy, cy + h_vis], 'k-', lw=1.4)
    ax.plot([cx + 53.35, cx + 53.35], [cy, cy + h_vis], 'k-', lw=1.4)
    ax.plot([cx - 55, cx - 55], [cy, cy + h_vis], color='#2563eb', lw=0.9)
    ax.plot([cx + 55, cx + 55], [cy, cy + h_vis], color='#2563eb', lw=0.9)

    # Đường mép ngoài lục giác
    ax.plot([cx - 57.5, cx - 57.5], [cy, cy + h_vis], 'k-', lw=1.5)
    ax.plot([cx + 57.5, cx + 57.5], [cy, cy + h_vis], 'k-', lw=1.5)
    ax.plot([cx - 57.5, cx - 53.35], [cy, cy], 'k-', lw=1.4)
    ax.plot([cx + 53.35, cx + 57.5], [cy, cy], 'k-', lw=1.4)
    ax.plot([cx - 57.5, cx - 53.35], [cy + h_vis, cy + h_vis], 'k-', lw=1.4)
    ax.plot([cx + 53.35, cx + 57.5], [cy + h_vis, cy + h_vis], 'k-', lw=1.4)

    # KÍCH THƯỚC
    draw_dim_v(ax, cy, cy + h_vis, cx + 57.5, "5.0 -0.1", offset=16, is_tol=True, tol_text="ĐỘ DÀY MỎNG 5MM")
    draw_dim_h(ax, cx - 57.5, cx + 57.5, cy + h_vis, "S = 115", offset=18)
    draw_dim_h(ax, cx - 55, cx + 55, cy, "Ren M110x3", offset=-18, color='#2563eb')
    
    # Ghi chú xóa cùi tròn
    ax.annotate('XÓA HOÀN TOÀN CÂY CÙI TRÒN\n(Khóa ren bằng cờ-lê/mỏ-lết 115mm)', xy=(cx + 57.5, cy + h_vis/2),
                xytext=(cx + 80, cy + 30),
                arrowprops=dict(arrowstyle='-|>', color='#b91c1c', lw=1.2),
                fontsize=9, fontweight='bold', color='#b91c1c')

    fig.savefig(os.path.join(WORK_DIR, "BV07_CT03_Long_Den_Hinh_Chieu_Dung.png"))
    plt.close(fig)

def tao_BV08_CT03_Bang():
    notes = [
        "Hình chiếu bằng thể hiện hình dạng lục giác đều S = 115mm.",
        "Ren trong M110x3 bước 3 đạt cấp chính xác 6H.",
        "Tuyệt đối không có bất kỳ tay quay hay cây cùi tròn nào nhô ra ngoài.",
        "Bề mặt phẳng hai bên mài phẳng đạt độ nhám Ra 1.6."
    ]
    fig, ax = create_base_drawing('3', 'Long đền tán khóa mỏng 5mm', 'Hình chiếu bằng (Top View)',
                                  'BV08_CT03', 8, 18, 'Thép C45 tôi cứng', '02 Cái', 3, notes)
    
    cx, cy = 175, 145
    draw_center_axes(ax, cx, cy, 80, 80)

    # Lục giác S=115 (R = 115 / sqrt(3) = 66.39mm)
    R_hex = 115.0 / math.sqrt(3.0)
    pts = []
    for i in range(6):
        ang = math.radians(i * 60.0 + 30.0)
        pts.append([cx + R_hex * math.cos(ang), cy + R_hex * math.sin(ang)])
    p_hex = patches.Polygon(pts, closed=True, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.8)
    ax.add_patch(p_hex)

    # Lỗ ren trong M110: đỉnh ren phi 106.7 nét liền, chân ren phi 110 nét mảnh hở 1/4
    c_dinh = Circle((cx, cy), 53.35, fill=True, facecolor='#ffffff', edgecolor='#0f172a', lw=1.4)
    ax.add_patch(c_dinh)
    arc_day = Arc((cx, cy), 110, 110, angle=0, theta1=20, theta2=290, edgecolor='#2563eb', lw=1.1)
    ax.add_patch(arc_day)

    # KÍCH THƯỚC
    draw_dim_h(ax, cx - 57.5, cx + 57.5, cy + 33.2, "S = 115 -0.2", offset=18)
    draw_dim_dia(ax, cx, cy, 55, 45, "Ren trong M110x3 - 6H")
    ax.annotate('KHÔNG CÓ CÂY CÙI TRÒN\n(Hình phẳng lục giác gọn gàng)', xy=(cx - 40, cy + 50), xytext=(cx - 95, cy + 75),
                arrowprops=dict(arrowstyle='-|>', color='#b91c1c', lw=1.0),
                fontsize=8.5, fontweight='bold', color='#b91c1c')

    fig.savefig(os.path.join(WORK_DIR, "BV08_CT03_Long_Den_Hinh_Chieu_Bang.png"))
    plt.close(fig)

def tao_BV09_CT03_Canh():
    notes = [
        "Hình chiếu cạnh của long đền mỏng 5mm.",
        "Thể hiện chiều dày chuẩn xác 5.0mm và bề rộng lục giác nhìn cạnh.",
        "Đường nét đứt thể hiện lỗ ren trong M110."
    ]
    fig, ax = create_base_drawing('3', 'Long đền tán khóa mỏng 5mm', 'Hình chiếu cạnh (Side View)',
                                  'BV09_CT03', 9, 18, 'Thép C45 tôi cứng', '02 Cái', 3, notes)
    
    cx, cy = 180, 140
    ax.plot([cx, cx], [cy - 20, cy + 30], 'r-.', lw=0.8)

    scale_y = 3.0
    h_vis = 5.0 * scale_y

    # Thân lục giác ngoài
    ax.plot([cx - 57.5, cx + 57.5, cx + 57.5, cx - 57.5, cx - 57.5],
            [cy, cy, cy + h_vis, cy + h_vis, cy], 'k-', lw=1.6)

    # Nét đứt ren trong M110
    ax.plot([cx - 55, cx - 55], [cy, cy + h_vis], 'k--', lw=0.9)
    ax.plot([cx + 55, cx + 55], [cy, cy + h_vis], 'k--', lw=0.9)

    draw_dim_v(ax, cy, cy + h_vis, cx + 57.5, "5.0 mm", offset=16)
    draw_dim_h(ax, cx - 57.5, cx + 57.5, cy + h_vis, "S = 115", offset=16)
    draw_dim_h(ax, cx - 55, cx + 55, cy, "M110", offset=-16, color='#2563eb')

    fig.savefig(os.path.join(WORK_DIR, "BV09_CT03_Long_Den_Hinh_Chieu_Canh.png"))
    plt.close(fig)

# ----------------------------------------------------
# CHI TIẾT 4: ỐNG TRỤ TRÒN NHẴN THÀNH 3MM DÙNG ĐỂ CỐ ĐỊNH
# ----------------------------------------------------

def tao_BV10_CT04_Dung():
    notes = [
        "Đường kính ngoài Ø86 f7 mài bóng Ra 0.8 để lắp trượt dẫn hướng chính xác.",
        "Đường kính trong Ø80 H8 chứa vừa thân ngoài bạc đạn 6012 (Ø80mm).",
        "Bề dày thành ống chuẩn đúng 3.0mm: (86 - 80) / 2 = 3.0mm.",
        "Gờ chặn dày 5.0mm ở đáy với lỗ thông trục Ø62mm để tì mặt bên bạc đạn.",
        "Độ đồng tâm giữa đường kính ngoài Ø86 và đường kính trong Ø80 đạt 0.02mm."
    ]
    fig, ax = create_base_drawing('4', 'Ống trụ tròn nhẵn thành 3mm', 'Hình chiếu đứng / Mặt cắt dọc toàn phần',
                                  'BV10_CT04', 10, 18, 'Thép C45 / S45C mài nhẵn', '02 Cái', 4, notes)
    
    cx, cy = 175, 110
    # Dài 65mm (từ cy đến cy+65)
    # Ngoài phi 86 (r=43)
    # Trong phi 80 (r=40) -> thành dày 3mm
    # Gờ chặn đáy dày 5mm (từ cy đến cy+5) lỗ phi 62 (r=31)
    ax.plot([cx, cx], [cy - 12, cy + 78], 'r-.', lw=0.8)

    # Mặt cắt kim loại bên trái
    p_left = patches.Polygon([
        [cx - 31, cy], [cx - 43, cy], [cx - 43, cy + 65], [cx - 40, cy + 65],
        [cx - 40, cy + 5], [cx - 31, cy + 5]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.4)
    ax.add_patch(p_left)

    # Mặt cắt kim loại bên phải
    p_right = patches.Polygon([
        [cx + 31, cy], [cx + 43, cy], [cx + 43, cy + 65], [cx + 40, cy + 65],
        [cx + 40, cy + 5], [cx + 31, cy + 5]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.4)
    ax.add_patch(p_right)

    # Đáy gờ chặn
    ax.plot([cx - 43, cx - 31], [cy, cy], 'k-', lw=1.5)
    ax.plot([cx + 31, cx + 43], [cy, cy], 'k-', lw=1.5)
    # Đỉnh miệng ống
    ax.plot([cx - 43, cx - 40], [cy + 65, cy + 65], 'k-', lw=1.4)
    ax.plot([cx + 40, cx + 43], [cy + 65, cy + 65], 'k-', lw=1.4)

    # KÍCH THƯỚC
    draw_dim_v(ax, cy, cy + 65, cx + 43, "65 ±0.15", offset=18)
    draw_dim_v(ax, cy, cy + 5, cx - 43, "5.0", offset=-10)
    draw_dim_h(ax, cx - 43, cx + 43, cy + 65, "Ø 86 f7 (-0.03/-0.06)", offset=14, color='#047857')
    draw_dim_h(ax, cx - 40, cx + 40, cy + 40, "Ø 80 H8 (+0.046/0)", offset=0, color='#1d4ed8')
    draw_dim_h(ax, cx - 31, cx + 31, cy, "Ø 62", offset=-16)
    
    # Chỉ rõ thành dày 3mm
    ax.annotate('THÀNH ỐNG DÀY ĐÚNG 3.0mm\n(Ø86 - Ø80)/2 = 3.0mm', xy=(cx - 41.5, cy + 50),
                xytext=(cx - 95, cy + 55),
                arrowprops=dict(arrowstyle='-|>', color='#b91c1c', lw=1.1),
                fontsize=8.5, fontweight='bold', color='#b91c1c')

    fig.savefig(os.path.join(WORK_DIR, "BV10_CT04_Ong_Truot_Hinh_Chieu_Dung.png"))
    plt.close(fig)

def tao_BV11_CT04_Bang():
    notes = [
        "Hình chiếu bằng nhìn từ miệng ống trượt.",
        "Vòng ngoài Ø86 và vòng trong Ø80 thể hiện rõ độ dày thành 3.0mm.",
        "Vòng trong cùng Ø62 là gờ chặn giữ bạc đạn.",
        "Độ nhám mài bóng lòng trong và ngoài Ra 0.8."
    ]
    fig, ax = create_base_drawing('4', 'Ống trụ tròn nhẵn thành 3mm', 'Hình chiếu bằng (Top View)',
                                  'BV11_CT04', 11, 18, 'Thép C45 / S45C mài nhẵn', '02 Cái', 4, notes)
    
    cx, cy = 175, 145
    draw_center_axes(ax, cx, cy, 60, 60)

    # Vòng ngoài Ø86
    c_out = Circle((cx, cy), 43, fill=True, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.6)
    ax.add_patch(c_out)

    # Vòng trong Ø80
    c_in = Circle((cx, cy), 40, fill=True, facecolor='#ffffff', edgecolor='#0f172a', lw=1.4)
    ax.add_patch(c_in)

    # Gờ chặn Ø62
    c_lip = Circle((cx, cy), 31, fill=True, facecolor='#f1f5f9', edgecolor='#64748b', lw=1.2, linestyle='--')
    ax.add_patch(c_lip)

    # Lỗ xuyên tâm Ø62
    c_hole = Circle((cx, cy), 31, fill=True, facecolor='#ffffff', edgecolor='#0f172a', lw=1.2)
    ax.add_patch(c_hole)

    # KÍCH THƯỚC
    draw_dim_dia(ax, cx, cy, 43, 45, "Ø 86 ngoài")
    draw_dim_dia(ax, cx, cy, 40, 135, "Ø 80 trong")
    draw_dim_dia(ax, cx, cy, 31, -45, "Lỗ gờ Ø 62")
    ax.annotate('BỀ DÀY THÀNH = 3.0 mm', xy=(cx + 41.5, cy), xytext=(cx + 65, cy + 20),
                arrowprops=dict(arrowstyle='-|>', color='#b91c1c', lw=1.0),
                fontsize=9, fontweight='bold', color='#b91c1c')

    fig.savefig(os.path.join(WORK_DIR, "BV11_CT04_Ong_Truot_Hinh_Chieu_Bang.png"))
    plt.close(fig)

def tao_BV12_CT04_Canh():
    notes = [
        "Hình chiếu cạnh ống trụ nhẵn dài 65mm.",
        "Các đường nét đứt thể hiện lòng trong Ø80 và gờ chặn Ø62.",
        "Bề mặt nhẵn bóng không có ren."
    ]
    fig, ax = create_base_drawing('4', 'Ống trụ tròn nhẵn thành 3mm', 'Hình chiếu cạnh (Side View)',
                                  'BV12_CT04', 12, 18, 'Thép C45 / S45C mài nhẵn', '02 Cái', 4, notes)
    
    cx, cy = 175, 110
    ax.plot([cx, cx], [cy - 12, cy + 78], 'r-.', lw=0.8)

    # Bao ngoài Ø86 dài 65
    ax.plot([cx - 43, cx + 43, cx + 43, cx - 43, cx - 43], [cy, cy, cy + 65, cy + 65, cy], 'k-', lw=1.6)

    # Nét đứt lòng trong Ø80
    ax.plot([cx - 40, cx - 40], [cy + 5, cy + 65], 'k--', lw=1.0)
    ax.plot([cx + 40, cx + 40], [cy + 5, cy + 65], 'k--', lw=1.0)

    # Nét đứt gờ đáy Ø62
    ax.plot([cx - 31, cx - 31], [cy, cy + 5], 'k--', lw=1.0)
    ax.plot([cx + 31, cx + 31], [cy, cy + 5], 'k--', lw=1.0)
    ax.plot([cx - 40, cx - 31], [cy + 5, cy + 5], 'k--', lw=1.0)
    ax.plot([cx + 31, cx + 40], [cy + 5, cy + 5], 'k--', lw=1.0)

    # KÍCH THƯỚC
    draw_dim_v(ax, cy, cy + 65, cx + 43, "65", offset=16)
    draw_dim_v(ax, cy, cy + 5, cx - 43, "5.0", offset=-12)
    draw_dim_h(ax, cx - 43, cx + 43, cy + 65, "Ø 86", offset=14)
    draw_dim_h(ax, cx - 40, cx + 40, cy + 30, "Ø 80 (Nét khuất)", offset=0, color='#1d4ed8')

    fig.savefig(os.path.join(WORK_DIR, "BV12_CT04_Ong_Truot_Hinh_Chieu_Canh.png"))
    plt.close(fig)

# ----------------------------------------------------
# CHI TIẾT 5: BẠC ĐẠN ĐỠ TRỤC PHI 60 (TIÊU CHUẨN 6012-2RS)
# ----------------------------------------------------

def tao_BV13_CT05_Dung():
    notes = [
        "Vòng bi đỡ chặn tiêu chuẩn quốc tế ISO 6012-2RS.",
        "Kích thước chuẩn: d = Ø60mm, D = Ø80mm, bề rộng B = 22mm.",
        "Trang bị 2 phớt cao su làm kín 2RS chống bụi bẩn và rò rỉ mỡ bôi trơn.",
        "10 viên bi thép chịu tải cao trên đường kính PCD Ø70mm.",
        "Lắp vừa khít vào lòng ống trượt Chi tiết 4 (Ø80 H8)."
    ]
    fig, ax = create_base_drawing('5', 'Bạc đạn đỡ trục phi 60 (6012-2RS)', 'Hình chiếu đứng / Mặt cắt bán diện',
                                  'BV13_CT05', 13, 18, 'Thép vòng bi GCr15 / 100Cr6', '02 Bộ', 5, notes)
    
    # Do bạc đạn dày 22mm nên vẽ phóng đại tỷ lệ trực quan
    cx, cy = 175, 125
    # Bề rộng B=22mm (từ cy đến cy+22)
    # Đường kính trong d=60 (r=30), ngoài D=80 (r=40)
    # Tâm bi tại r=35 (PCD 70), đường kính bi d_bi=8 (r_bi=4)
    # Scale trục Y 2.5x để hiển thị rõ chi tiết cấu tạo
    sc_y = 2.5
    b_vis = 22.0 * sc_y # 55mm

    ax.plot([cx, cx], [cy - 16, cy + b_vis + 24], 'r-.', lw=0.8)

    # Cắt bên trái: Vòng ngoài, vòng trong, viên bi, phớt cao su
    # Vòng ngoài (r từ 36 đến 40)
    p_out_l = patches.Polygon([
        [cx - 40, cy], [cx - 36, cy], [cx - 36, cy + b_vis], [cx - 40, cy + b_vis]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.3)
    ax.add_patch(p_out_l)

    # Vòng trong (r từ 30 đến 34)
    p_in_l = patches.Polygon([
        [cx - 34, cy], [cx - 30, cy], [cx - 30, cy + b_vis], [cx - 34, cy + b_vis]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.3)
    ax.add_patch(p_in_l)

    # Bi cầu bên trái
    c_ball_l = Circle((cx - 35, cy + b_vis/2), 4 * sc_y * 0.5, fill=True, facecolor='#e2e8f0', edgecolor='k', lw=1.2)
    ax.add_patch(c_ball_l)

    # Phớt cao su 2RS hai bên (màu cam)
    rect_seal_b = patches.Rectangle((cx - 36, cy + 1), 2, 3, fill=True, facecolor='#f97316', edgecolor='k', lw=0.6)
    rect_seal_t = patches.Rectangle((cx - 36, cy + b_vis - 4), 2, 3, fill=True, facecolor='#f97316', edgecolor='k', lw=0.6)
    ax.add_patch(rect_seal_b)
    ax.add_patch(rect_seal_t)

    # Chiếu bên phải: Thể hiện bề mặt ngoài
    ax.plot([cx + 30, cx + 40, cx + 40, cx + 30, cx + 30],
            [cy, cy, cy + b_vis, cy + b_vis, cy], 'k-', lw=1.5)
    # Đường rãnh phớt 2 bên
    ax.plot([cx + 31, cx + 39], [cy + 3, cy + 3], color='#f97316', lw=1.2)
    ax.plot([cx + 31, cx + 39], [cy + b_vis - 3, cy + b_vis - 3], color='#f97316', lw=1.2)

    # KÍCH THƯỚC
    draw_dim_v(ax, cy, cy + b_vis, cx + 40, "B = 22.0", offset=16)
    draw_dim_h(ax, cx - 40, cx + 40, cy + b_vis, "D = Ø 80 -0.013", offset=14)
    draw_dim_h(ax, cx - 30, cx + 30, cy, "d = Ø 60 +0.015", offset=-14, color='#1d4ed8')
    ax.annotate('Phớt cao su làm kín 2RS', xy=(cx - 36, cy + b_vis - 2.5),
                xytext=(cx - 95, cy + b_vis + 12),
                arrowprops=dict(arrowstyle='-|>', color='#ea580c', lw=0.9),
                fontsize=8.5, fontweight='bold', color='#ea580c')
    ax.annotate('Viên bi thép Ø8.0\n(10 viên trên PCD Ø70)', xy=(cx - 35, cy + b_vis/2),
                xytext=(cx - 95, cy + b_vis/2 - 14),
                arrowprops=dict(arrowstyle='-|>', color='#0f172a', lw=0.9),
                fontsize=8.5, fontweight='bold')

    fig.savefig(os.path.join(WORK_DIR, "BV13_CT05_Bac_Dan_Hinh_Chieu_Dung.png"))
    plt.close(fig)

def tao_BV14_CT05_Bang():
    notes = [
        "Hình chiếu bằng thể hiện vòng trong Ø60, vòng ngoài Ø80 và 10 viên bi.",
        "Phớt cao su chắn bụi màu cam/đen bao bọc rãnh bi.",
        "Đường chia tâm bi PCD Ø70mm phân bố góc 36 độ.",
        "Vận hành êm ái, bôi trơn sẵn mỡ chịu nhiệt cao cấp."
    ]
    fig, ax = create_base_drawing('5', 'Bạc đạn đỡ trục phi 60 (6012-2RS)', 'Hình chiếu bằng (Top View)',
                                  'BV14_CT05', 14, 18, 'Thép vòng bi GCr15 / 100Cr6', '02 Bộ', 5, notes)
    
    cx, cy = 175, 145
    draw_center_axes(ax, cx, cy, 55, 55)

    # Vòng ngoài Ø80
    c_out = Circle((cx, cy), 40, fill=True, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.6)
    ax.add_patch(c_out)

    # Vành phớt cao su 2RS (màu cam nhạt)
    c_seal = Circle((cx, cy), 38, fill=True, facecolor='#ffedd5', edgecolor='#f97316', lw=1.0)
    ax.add_patch(c_seal)

    # PCD Ø70
    c_pcd = Circle((cx, cy), 35, fill=False, edgecolor='#ef4444', lw=0.8, linestyle='-.')
    ax.add_patch(c_pcd)

    # 10 viên bi trên PCD Ø70
    for i in range(10):
        ang = math.radians(i * 36.0)
        bx = cx + 35.0 * math.cos(ang)
        by = cy + 35.0 * math.sin(ang)
        cb = Circle((bx, by), 4.0, fill=True, facecolor='#ffffff', edgecolor='#0f172a', lw=0.9)
        ax.add_patch(cb)

    # Vòng trong Ø60
    c_in_rim = Circle((cx, cy), 32, fill=True, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.2)
    ax.add_patch(c_in_rim)
    c_in_hole = Circle((cx, cy), 30, fill=True, facecolor='#ffffff', edgecolor='#0f172a', lw=1.5)
    ax.add_patch(c_in_hole)

    # KÍCH THƯỚC
    draw_dim_dia(ax, cx, cy, 40, 45, "D = Ø 80")
    draw_dim_dia(ax, cx, cy, 30, 135, "d = Ø 60")
    draw_dim_dia(ax, cx, cy, 35, -45, "PCD Ø 70")
    ax.annotate('10 Viên bi Ø8.0\n(Góc chia 36°)', xy=(cx + 35, cy), xytext=(cx + 55, cy + 25),
                arrowprops=dict(arrowstyle='-|>', color='#0f172a', lw=0.9),
                fontsize=8.5, fontweight='bold')

    fig.savefig(os.path.join(WORK_DIR, "BV14_CT05_Bac_Dan_Hinh_Chieu_Bang.png"))
    plt.close(fig)

def tao_BV15_CT05_Canh():
    notes = [
        "Hình chiếu cạnh bạc đạn 6012-2RS.",
        "Kích thước bao chữ nhật 22 x 80mm.",
        "Đường nét đứt thể hiện rãnh bi và lỗ tâm Ø60."
    ]
    fig, ax = create_base_drawing('5', 'Bạc đạn đỡ trục phi 60 (6012-2RS)', 'Hình chiếu cạnh (Side View)',
                                  'BV15_CT05', 15, 18, 'Thép vòng bi GCr15 / 100Cr6', '02 Bộ', 5, notes)
    
    cx, cy = 175, 125
    sc_y = 2.5
    b_vis = 22.0 * sc_y

    ax.plot([cx, cx], [cy - 16, cy + b_vis + 24], 'r-.', lw=0.8)

    # Bao ngoài
    ax.plot([cx - 40, cx + 40, cx + 40, cx - 40, cx - 40],
            [cy, cy, cy + b_vis, cy + b_vis, cy], 'k-', lw=1.6)

    # Nét đứt lỗ trong Ø60
    ax.plot([cx - 30, cx - 30], [cy, cy + b_vis], 'k--', lw=1.0)
    ax.plot([cx + 30, cx + 30], [cy, cy + b_vis], 'k--', lw=1.0)

    # KÍCH THƯỚC
    draw_dim_v(ax, cy, cy + b_vis, cx + 40, "B = 22", offset=16)
    draw_dim_h(ax, cx - 40, cx + 40, cy + b_vis, "Ø 80", offset=14)
    draw_dim_h(ax, cx - 30, cx + 30, cy, "Ø 60 (Nét khuất)", offset=-14, color='#1d4ed8')

    fig.savefig(os.path.join(WORK_DIR, "BV15_CT05_Bac_Dan_Hinh_Chieu_Canh.png"))
    plt.close(fig)

# ----------------------------------------------------
# CHI TIẾT 6: MẶT BÍT NGUYÊN KHỐI ĐẶC KÍN 100%
# ----------------------------------------------------

def tao_BV16_CT06_Dung():
    notes = [
        "MẶT BÍT NGUYÊN KHỐI ĐẶC KÍN 100% (TUYỆT ĐỐI KHÔNG KHOÉT LỖ TÂM).",
        "Vành ngoài Ø104 dày 8mm, gờ định vị Ø85.5 (-0.05/-0.1) dày 6mm.",
        "Tổng chiều dày mặt bít 14.0mm, mặt cắt hatching liền mạch qua tâm.",
        "4 lỗ bu-lông chìm M6 (khoét bậc Ø11 sâu 3.5mm, lỗ suốt Ø6.5) trên PCD Ø94.",
        "Vát mép gờ định vị 1.0x45 độ để lắp êm vào ống trượt."
    ]
    fig, ax = create_base_drawing('6', 'Mặt bít nguyên khối đặc kín', 'Hình chiếu đứng / Mặt cắt A-A',
                                  'BV16_CT06', 16, 18, 'Thép C45 / S45C nguyên khối', '02 Cái', 6, notes)
    
    cx, cy = 175, 120
    # Gờ định vị Ø85.5 (r=42.75) dày 6mm (từ cy đến cy+6)
    # Vành Ø104 (r=52) dày 8mm (từ cy+6 đến cy+14)
    # Tổng dày 14mm
    # Scale Y 2.5x để đường kích thước và bậc khoét chìm rõ nét
    sc_y = 2.5
    h_spigot = 6.0 * sc_y   # 15mm
    h_flange = 8.0 * sc_y   # 20mm
    h_tot = h_spigot + h_flange # 35mm
    h_cbore = 3.5 * sc_y   # 8.75mm

    ax.plot([cx, cx], [cy - 12, cy + h_tot + 20], 'r-.', lw=0.8)

    # ĐẶC KÍN NGUYÊN KHỐI TẠI TÂM!
    # Lỗ vít chìm M6 tại x = cx - 47 và cx + 47
    # Lỗ bậc: r_cb = 5.5, r_th = 3.25
    # Mặt cắt kim loại gồm 3 phần: Trái ngoài lỗ, Giữa tâm (liền mạch), Phải ngoài lỗ

    # 1. Phần tâm ở giữa: Xuyên suốt từ x = cx - 41.5 đến cx + 41.5 (ĐẶC KÍN 100%!)
    p_mid = patches.Polygon([
        [cx - 41.5, cy], [cx + 41.5, cy], [cx + 41.5, cy + h_tot], [cx - 41.5, cy + h_tot]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.3)
    ax.add_patch(p_mid)

    # 2. Phần bên trái
    p_left_out = patches.Polygon([
        [cx - 52, cy + h_spigot], [cx - 42.75, cy + h_spigot], [cx - 42.75, cy],
        [cx - 50.25, cy], [cx - 50.25, cy + h_tot - h_cbore], [cx - 52.5, cy + h_tot - h_cbore],
        [cx - 52.5, cy + h_tot], [cx - 52, cy + h_tot]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.3)
    ax.add_patch(p_left_out)

    # 3. Phần bên phải
    p_right_out = patches.Polygon([
        [cx + 52, cy + h_spigot], [cx + 42.75, cy + h_spigot], [cx + 42.75, cy],
        [cx + 50.25, cy], [cx + 50.25, cy + h_tot - h_cbore], [cx + 52.5, cy + h_tot - h_cbore],
        [cx + 52.5, cy + h_tot], [cx + 52, cy + h_tot]
    ], closed=True, facecolor='#f1f5f9', edgecolor='k', hatch='///', lw=1.3)
    ax.add_patch(p_right_out)

    # Lỗ vít chìm 2 bên
    for sign in [-1, 1]:
        vx = cx + sign * 47.0
        ax.plot([vx, vx], [cy - 6, cy + h_tot + 6], 'r-.', lw=0.6)
        # Bậc khoét chìm Ø11
        ax.plot([vx - 5.5, vx - 5.5], [cy + h_tot - h_cbore, cy + h_tot], 'k-', lw=1.1)
        ax.plot([vx + 5.5, vx + 5.5], [cy + h_tot - h_cbore, cy + h_tot], 'k-', lw=1.1)
        ax.plot([vx - 5.5, vx - 3.25], [cy + h_tot - h_cbore, cy + h_tot - h_cbore], 'k-', lw=1.1)
        ax.plot([vx + 3.25, vx + 5.5], [cy + h_tot - h_cbore, cy + h_tot - h_cbore], 'k-', lw=1.1)
        # Lỗ suốt Ø6.5
        ax.plot([vx - 3.25, vx - 3.25], [cy, cy + h_tot - h_cbore], 'k-', lw=1.1)
        ax.plot([vx + 3.25, vx + 3.25], [cy, cy + h_tot - h_cbore], 'k-', lw=1.1)

    # Đường biên bao ngoài
    ax.plot([cx - 42.75, cx + 42.75], [cy, cy], 'k-', lw=1.6)
    ax.plot([cx - 52, cx - 42.75], [cy + h_spigot, cy + h_spigot], 'k-', lw=1.3)
    ax.plot([cx + 42.75, cx + 52], [cy + h_spigot, cy + h_spigot], 'k-', lw=1.3)
    ax.plot([cx - 52, cx - 52], [cy + h_spigot, cy + h_tot], 'k-', lw=1.6)
    ax.plot([cx + 52, cx + 52], [cy + h_spigot, cy + h_tot], 'k-', lw=1.6)
    ax.plot([cx - 52, cx + 52], [cy + h_tot, cy + h_tot], 'k-', lw=1.6)

    # KÍCH THƯỚC
    draw_dim_v(ax, cy, cy + h_tot, cx + 52, "14.0 ±0.1", offset=18)
    draw_dim_v(ax, cy, cy + h_spigot, cx - 52, "6.0", offset=-10)
    draw_dim_v(ax, cy + h_spigot, cy + h_tot, cx - 52, "8.0", offset=-18)
    draw_dim_h(ax, cx - 52, cx + 52, cy + h_tot, "Ø 104", offset=14)
    draw_dim_h(ax, cx - 42.75, cx + 42.75, cy, "Gờ Ø 85.5 (-0.05/-0.1)", offset=-14, color='#047857')
    
    # Ghi chú tâm đặc kín 100%
    ax.annotate('TÂM ĐẶC KÍN NGUYÊN KHỐI 100%\n(TUYỆT ĐỐI KHÔNG KHOÉT LỖ TÂM)', xy=(cx, cy + h_tot/2),
                xytext=(cx - 65, cy + h_tot + 25),
                arrowprops=dict(arrowstyle='-|>', color='#b91c1c', lw=1.2),
                fontsize=9, fontweight='bold', color='#b91c1c')
    # Ghi chú lỗ vít chìm M6
    ax.annotate('4 Lỗ khoét bậc bu-lông chìm M6\n(Lỗ suốt Ø6.5, khoét Ø11 sâu 3.5mm)',
                xy=(cx + 47, cy + h_tot - h_cbore/2), xytext=(cx + 65, cy + h_tot + 15),
                arrowprops=dict(arrowstyle='-|>', color='#0f172a', lw=1.0),
                fontsize=8.5, fontweight='bold')

    fig.savefig(os.path.join(WORK_DIR, "BV16_CT06_Mat_Bit_Hinh_Chieu_Dung.png"))
    plt.close(fig)

def tao_BV17_CT06_Bang():
    notes = [
        "Hình chiếu bằng nhìn từ mặt ngoài vành Ø104.",
        "TÂM MẶT BÍT PHẲNG ĐẶC KÍN NGUYÊN KHỐI 100% (không có lỗ thủng tâm).",
        "4 lỗ bu-lông chìm M6 bố trí đều góc 90 độ trên PCD Ø94mm.",
        "Vát mép cạnh ngoài vành và mép các lỗ khoét 0.5x45 độ."
    ]
    fig, ax = create_base_drawing('6', 'Mặt bít nguyên khối đặc kín', 'Hình chiếu bằng (Top View)',
                                  'BV17_CT06', 17, 18, 'Thép C45 / S45C nguyên khối', '02 Cái', 6, notes)
    
    cx, cy = 175, 145
    draw_center_axes(ax, cx, cy, 65, 65)

    # Vành ngoài Ø104
    c_out = Circle((cx, cy), 52, fill=True, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.8)
    ax.add_patch(c_out)

    # Đường tròn gờ định vị Ø85.5 bên dưới (nét đứt)
    c_spigot = Circle((cx, cy), 42.75, fill=False, edgecolor='#64748b', lw=0.9, linestyle='--')
    ax.add_patch(c_spigot)

    # Đường chia tâm PCD Ø94
    c_pcd = Circle((cx, cy), 47, fill=False, edgecolor='#ef4444', lw=0.8, linestyle='-.')
    ax.add_patch(c_pcd)

    # 4 lỗ bu-lông chìm M6 góc 45, 135, 225, 315 độ
    for i in range(4):
        ang = math.radians(i * 90.0 + 45.0)
        hx = cx + 47.0 * math.cos(ang)
        hy = cy + 47.0 * math.sin(ang)
        draw_center_axes(ax, hx, hy, 8, 8, lw=0.5)
        # Bậc khoét Ø11
        cb_out = Circle((hx, hy), 5.5, fill=True, facecolor='#e2e8f0', edgecolor='#0f172a', lw=1.1)
        ax.add_patch(cb_out)
        # Lỗ suốt Ø6.5
        cb_in = Circle((hx, hy), 3.25, fill=True, facecolor='#ffffff', edgecolor='#0f172a', lw=1.0)
        ax.add_patch(cb_in)

    # KÍCH THƯỚC
    draw_dim_dia(ax, cx, cy, 52, 35, "Vành ngoài Ø 104")
    draw_dim_dia(ax, cx, cy, 47, -35, "PCD Ø 94")
    draw_dim_dia(ax, cx, cy, 42.75, 145, "Gờ Ø 85.5 (Nét khuất)")

    # Ghi chú tâm đặc kín
    ax.text(cx, cy, "TÂM ĐẶC KÍN 100%\nNGUYÊN KHỐI", fontsize=9, fontweight='heavy',
            color='#b91c1c', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fee2e2', edgecolor='#ef4444', lw=1.0))
    # Ghi chú 4 lỗ vít chìm M6
    hx45 = cx + 47.0 * math.cos(math.radians(45.0))
    hy45 = cy + 47.0 * math.sin(math.radians(45.0))
    ax.annotate('4 Lỗ bu-lông chìm M6\n(Lỗ Ø6.5 khoét Ø11 sâu 3.5mm)', xy=(hx45, hy45), xytext=(cx + 70, cy + 70),
                arrowprops=dict(arrowstyle='-|>', color='#0f172a', lw=1.0),
                fontsize=8.5, fontweight='bold')

    fig.savefig(os.path.join(WORK_DIR, "BV17_CT06_Mat_Bit_Hinh_Chieu_Bang.png"))
    plt.close(fig)

def tao_BV18_CT06_Canh():
    notes = [
        "Hình chiếu cạnh mặt bít nguyên khối.",
        "Thể hiện gờ định vị 6mm x Ø85.5mm và vành 8mm x Ø104mm.",
        "Các đường nét đứt thể hiện lỗ bu-lông chìm M6.",
        "Tâm đặc kín nguyên khối không có lỗ trục xuyên qua."
    ]
    fig, ax = create_base_drawing('6', 'Mặt bít nguyên khối đặc kín', 'Hình chiếu cạnh (Side View)',
                                  'BV18_CT06', 18, 18, 'Thép C45 / S45C nguyên khối', '02 Cái', 6, notes)
    
    cx, cy = 175, 120
    sc_y = 2.5
    h_spigot = 6.0 * sc_y
    h_flange = 8.0 * sc_y
    h_tot = h_spigot + h_flange
    h_cbore = 3.5 * sc_y

    ax.plot([cx, cx], [cy - 12, cy + h_tot + 20], 'r-.', lw=0.8)

    # Biên dạng ngoài nhìn cạnh
    pts_edge = [
        [cx - 42.75, cy], [cx + 42.75, cy], [cx + 42.75, cy + h_spigot],
        [cx + 52, cy + h_spigot], [cx + 52, cy + h_tot], [cx - 52, cy + h_tot],
        [cx - 52, cy + h_spigot], [cx - 42.75, cy + h_spigot], [cx - 42.75, cy]
    ]
    ax.plot([p[0] for p in pts_edge], [p[1] for p in pts_edge], 'k-', lw=1.6)

    # Nét đứt lỗ vít chìm M6
    for sign in [-1, 1]:
        vx = cx + sign * 47.0
        ax.plot([vx - 5.5, vx - 5.5], [cy + h_tot - h_cbore, cy + h_tot], 'k--', lw=0.8)
        ax.plot([vx + 5.5, vx + 5.5], [cy + h_tot - h_cbore, cy + h_tot], 'k--', lw=0.8)
        ax.plot([vx - 3.25, vx - 3.25], [cy, cy + h_tot - h_cbore], 'k--', lw=0.8)
        ax.plot([vx + 3.25, vx + 3.25], [cy, cy + h_tot - h_cbore], 'k--', lw=0.8)

    # KÍCH THƯỚC
    draw_dim_v(ax, cy, cy + h_tot, cx + 52, "14", offset=16)
    draw_dim_v(ax, cy, cy + h_spigot, cx - 52, "6", offset=-10)
    draw_dim_v(ax, cy + h_spigot, cy + h_tot, cx - 52, "8", offset=-18)
    draw_dim_h(ax, cx - 52, cx + 52, cy + h_tot, "Ø 104", offset=14)
    draw_dim_h(ax, cx - 42.75, cx + 42.75, cy, "Ø 85.5", offset=-14)

    fig.savefig(os.path.join(WORK_DIR, "BV18_CT06_Mat_Bit_Hinh_Chieu_Canh.png"))
    plt.close(fig)

# ==========================================
# HÀM ĐIỀU PHỐI CHẠY TẤT CẢ 18 BẢN VẼ
# ==========================================

def run_all():
    print("=" * 65)
    print("BẮT ĐẦU SINH BỘ 18 BẢN VẼ CƠ KHÍ ĐỘC LẬP THEO TIÊU CHUẨN TCVN / ISO")
    print("=" * 65)

    drawing_funcs = [
        ("BV01_CT01", tao_BV01_CT01_Dung),
        ("BV02_CT01", tao_BV02_CT01_Bang),
        ("BV03_CT01", tao_BV03_CT01_Canh),
        ("BV04_CT02", tao_BV04_CT02_Dung),
        ("BV05_CT02", tao_BV05_CT02_Bang),
        ("BV06_CT02", tao_BV06_CT02_Canh),
        ("BV07_CT03", tao_BV07_CT03_Dung),
        ("BV08_CT03", tao_BV08_CT03_Bang),
        ("BV09_CT03", tao_BV09_CT03_Canh),
        ("BV10_CT04", tao_BV10_CT04_Dung),
        ("BV11_CT04", tao_BV11_CT04_Bang),
        ("BV12_CT04", tao_BV12_CT04_Canh),
        ("BV13_CT05", tao_BV13_CT05_Dung),
        ("BV14_CT05", tao_BV14_CT05_Bang),
        ("BV15_CT05", tao_BV15_CT05_Canh),
        ("BV16_CT06", tao_BV16_CT06_Dung),
        ("BV17_CT06", tao_BV17_CT06_Bang),
        ("BV18_CT06", tao_BV18_CT06_Canh),
    ]

    for idx, (code, func) in enumerate(drawing_funcs):
        print(f"[{idx+1:02d}/18] Đang vẽ {code}...")
        func()
        print(f"       -> Hoàn thành {code}")

    # Đồng bộ toàn bộ sang ARTIFACT_OUT_DIR và ARTIFACT_DIR
    print("\nĐang sao chép các bản vẽ vào thư mục Artifact...")
    for filename in os.listdir(WORK_DIR):
        if filename.endswith(".png"):
            src = os.path.join(WORK_DIR, filename)
            dst1 = os.path.join(ARTIFACT_OUT_DIR, filename)
            dst2 = os.path.join(ARTIFACT_DIR, filename)
            shutil.copy2(src, dst1)
            shutil.copy2(src, dst2)

    print("=" * 65)
    print("HOÀN THÀNH TOÀN BỘ 18 BẢN VẼ CƠ KHÍ ĐỘC LẬP!")
    print(f"Thư mục làm việc: {WORK_DIR}")
    print(f"Thư mục Artifact: {ARTIFACT_OUT_DIR}")
    print("=" * 65)

if __name__ == "__main__":
    run_all()
