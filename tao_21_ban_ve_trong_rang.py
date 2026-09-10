# -*- coding: utf-8 -*-
"""
HỆ THỐNG XUẤT 21 BẢN VẼ CƠ KHÍ ĐỘC LẬP TRỐNG RANG 2 LỚP ĐỆM KHÍ
(CỤM TỔNG THỂ + 6 CHI TIẾT CỐT LÕI x 3 HÌNH CHIẾU ĐỨNG - BẰNG - CẠNH)
ĐẠT TIÊU CHUẨN TCVN / ISO KHỔ A3 - PHIÊN BẢN TINH CHỈNH HOÀN HẢO (ZERO COLLISION)

Tác giả: Khánh Văn <kvan18052004@gmail.com>
Duyệt: Q.LÝ | Ngày: 10/09/26
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
WORK_DIR = r"c:\VAN\CAD\ban_ve_trong_rang"
ARTIFACT_DIR = r"C:\Users\admin\.gemini\antigravity\brain\0b789148-0c1a-433f-9f39-ee380f84bb46"
ARTIFACT_OUT_DIR = os.path.join(ARTIFACT_DIR, "ban_ve_trong_rang")
THUMB_DIR = os.path.join(ARTIFACT_DIR, "scratch", "thumbs_trong")
if not os.path.exists(THUMB_DIR):
    THUMB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "thumbs_trong")

os.makedirs(WORK_DIR, exist_ok=True)
os.makedirs(ARTIFACT_OUT_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Segoe UI', 'Tahoma', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# CÁC HÀM TIỆN ÍCH VẼ KHUNG VÀ KÝ HIỆU TIÊU CHUẨN
# ==========================================

def create_base_drawing(part_code_str, part_name, view_title, sheet_code, sheet_no, total_sheets, material, qty, scale_str, thumb_file, tech_notes):
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
    
    # Đường kẻ ngang trong khung tên
    ax.plot([tb_x, tb_x + tb_w], [tb_y + 14, tb_y + 14], 'k-', lw=1.2)
    ax.plot([tb_x, tb_x + tb_w], [tb_y + 28, tb_y + 28], 'k-', lw=1.2)
    ax.plot([tb_x, tb_x + tb_w], [tb_y + 44, tb_y + 44], 'k-', lw=1.2)
    
    # Đường kẻ dọc trong khung tên
    ax.plot([tb_x + 95, tb_x + 95], [tb_y + 14, tb_y + 58], 'k-', lw=1.2)
    ax.plot([tb_x + 125, tb_x + 125], [tb_y + 14, tb_y + 44], 'k-', lw=1.2)
    ax.plot([tb_x + 70, tb_x + 70], [tb_y, tb_y + 14], 'k-', lw=1.0)
    ax.plot([tb_x + 115, tb_x + 115], [tb_y, tb_y + 14], 'k-', lw=1.0)

    # Nội dung khung tên
    ax.text(tb_x + 47.5, tb_y + 51, "MÁY RANG CỦI CÔNG NGHIỆP", fontsize=9, fontweight='bold', ha='center', va='center', color='#1e293b')
    ax.text(tb_x + 47.5, tb_y + 46, "CỤM TRỐNG RANG 2 LỚP ĐỆM KHÍ", fontsize=8, fontweight='bold', ha='center', va='center', color='#0369a1')
    
    ax.text(tb_x + 127.5, tb_y + 51, "KÝ HIỆU BẢN VẼ", fontsize=7.5, color='#475569', ha='center', va='center')
    ax.text(tb_x + 127.5, tb_y + 46, sheet_code, fontsize=9.0, fontweight='bold', color='#b91c1c', ha='center', va='center')

    title_part = f"{part_code_str}: {part_name.upper()}" if part_code_str else part_name.upper()
    ax.text(tb_x + 47.5, tb_y + 36, title_part, fontsize=8.5, fontweight='bold', ha='center', va='center', color='#0f172a')
    
    # Rút gọn hoặc điều chỉnh kích cỡ view_title trong khung tên để không tràn
    short_view_title = view_title.split('(')[0].strip() if len(view_title) > 28 else view_title
    ax.text(tb_x + 47.5, tb_y + 30.5, short_view_title.upper(), fontsize=7.5, fontweight='bold', ha='center', va='center', color='#047857')

    ax.text(tb_x + 110, tb_y + 36, "TỶ LỆ", fontsize=7.5, color='#475569', ha='center', va='center')
    ax.text(tb_x + 110, tb_y + 29, scale_str, fontsize=9, fontweight='bold', ha='center', va='center')
    
    ax.text(tb_x + 142.5, tb_y + 36, "TỜ / TỔNG", fontsize=7.5, color='#475569', ha='center', va='center')
    ax.text(tb_x + 142.5, tb_y + 29, f"{sheet_no:02d} / {total_sheets:02d}", fontsize=9.5, fontweight='bold', color='#1d4ed8', ha='center', va='center')

    ax.text(tb_x + 47.5, tb_y + 21, f"VẬT LIỆU: {material}", fontsize=8.0, fontweight='bold', ha='center', va='center', color='#334155')
    ax.text(tb_x + 127.5, tb_y + 21, f"SL: {qty}", fontsize=8.5, fontweight='bold', ha='center', va='center', color='#334155')

    ax.text(tb_x + 35, tb_y + 7, "THIẾT KẾ: Khánh Văn", fontsize=8, color='#334155', ha='center', va='center')
    ax.text(tb_x + 92.5, tb_y + 7, "DUYỆT: Q.LÝ", fontsize=8, color='#334155', ha='center', va='center')
    ax.text(tb_x + 137.5, tb_y + 7, "NGÀY: 10/09/26", fontsize=8, color='#334155', ha='center', va='center')

    # KHUNG GHI CHÚ YÊU CẦU KỸ THUẬT (Góc dưới bên trái)
    ax.add_patch(patches.Rectangle((30, 10), 160, 48, fill=True, facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.0))
    ax.text(35, 53, "YÊU CẦU KỸ THUẬT & GIA CÔNG:", fontsize=8.5, fontweight='bold', color='#0f172a')
    for idx, note in enumerate(tech_notes):
        ax.text(35, 46 - idx * 6.8, f"{idx+1}. {note}", fontsize=7.3, color='#334155')

    # NHÚNG ẢNH 3D ISOMETRIC THUMBNAIL (Góc trên bên phải)
    thumb_path = os.path.join(THUMB_DIR, thumb_file)
    if os.path.exists(thumb_path):
        img = mpimg.imread(thumb_path)
        thumb_ax = fig.add_axes([0.76, 0.72, 0.20, 0.23])
        thumb_ax.imshow(img)
        thumb_ax.axis('off')
        # Viền khung ảnh 3D
        ax.add_patch(patches.Rectangle((315, 210), 90, 72, fill=False, edgecolor='#94a3b8', linewidth=1.2, linestyle='--'))
        lbl = "MÔ HÌNH 3D SOLID (CỤM TỔNG THỂ)" if "tt" in thumb_file else f"MÔ HÌNH 3D SOLID ({part_code_str})"
        ax.text(360, 283.5, lbl, fontsize=7.5, fontweight='bold', color='#0284c7', ha='center')

    # BIỂU TƯỢNG GÓC CHIẾU THỨ NHẤT (TCVN / ISO)
    proj_x, proj_y = 45, 275
    ax.plot([proj_x, proj_x + 12, proj_x + 12, proj_x, proj_x], [proj_y - 3, proj_y - 6, proj_y + 6, proj_y + 3, proj_y - 3], 'k-', lw=1.0)
    ax.plot([proj_x - 4, proj_x + 32], [proj_y, proj_y], 'r-.', lw=0.6)
    c1 = Circle((proj_x + 22, proj_y), 3, fill=False, edgecolor='k', lw=1.0)
    c2 = Circle((proj_x + 22, proj_y), 6, fill=False, edgecolor='k', lw=1.0)
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.text(proj_x + 11, proj_y - 9, "ISO / TCVN (GÓC CHIẾU 1)", fontsize=6.5, color='#64748b', ha='center')

    # TIÊU ĐỀ HÌNH CHIẾU CHÍNH GIỮA TRÊN
    ax.text(210, 275, view_title.upper(), fontsize=13.5, fontweight='heavy', color='#0f172a', ha='center', va='center')
    ax.plot([130, 290], [270, 270], color='#0284c7', lw=1.8)

    return fig, ax

# ==========================================
# CÁC HÀM VẼ ĐƯỜNG KÍCH THƯỚC VÀ DUNG SAI
# ==========================================

def draw_dim_h(ax, x1, x2, y, text, offset=6, color='#0f172a', is_tol=False, tol_text=''):
    """Vẽ đường kích thước nằm ngang với 2 mũi tên và đường gióng."""
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_dim = y + offset
    ax.plot([x_min, x_min], [min(y, y_dim) - 1.5, max(y, y_dim) + 1.5], color='#475569', lw=0.7)
    ax.plot([x_max, x_max], [min(y, y_dim) - 1.5, max(y, y_dim) + 1.5], color='#475569', lw=0.7)
    ax.plot([x_min, x_max], [y_dim, y_dim], color=color, lw=0.9)
    ax.annotate('', xy=(x_min, y_dim), xytext=(x_min + 3.0, y_dim),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=0.9, mutation_scale=8))
    ax.annotate('', xy=(x_max, y_dim), xytext=(x_max - 3.0, y_dim),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=0.9, mutation_scale=8))
    mid_x = (x_min + x_max) / 2.0
    ax.text(mid_x, y_dim + 1.5, text, fontsize=8.0, fontweight='bold', color=color, ha='center', va='bottom',
            bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='none', alpha=0.9))
    if is_tol and tol_text:
        ax.text(mid_x, y_dim - 2.5, tol_text, fontsize=6.5, color='#475569', ha='center', va='top')

def draw_dim_v(ax, y1, y2, x, text, offset=6, color='#0f172a', is_tol=False, tol_text=''):
    """Vẽ đường kích thước thẳng đứng với 2 mũi tên và đường gióng."""
    y_min, y_max = min(y1, y2), max(y1, y2)
    x_dim = x + offset
    ax.plot([min(x, x_dim) - 1.5, max(x, x_dim) + 1.5], [y_min, y_min], color='#475569', lw=0.7)
    ax.plot([min(x, x_dim) - 1.5, max(x, x_dim) + 1.5], [y_max, y_max], color='#475569', lw=0.7)
    ax.plot([x_dim, x_dim], [y_min, y_max], color=color, lw=0.9)
    ax.annotate('', xy=(x_dim, y_min), xytext=(x_dim, y_min + 3.0),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=0.9, mutation_scale=8))
    ax.annotate('', xy=(x_dim, y_max), xytext=(x_dim, y_max - 3.0),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=0.9, mutation_scale=8))
    mid_y = (y_min + y_max) / 2.0
    ax.text(x_dim - 1.8 if offset < 0 else x_dim + 1.8, mid_y, text, fontsize=8.0, fontweight='bold',
            color=color, ha='right' if offset < 0 else 'left', va='center', rotation=90,
            bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='none', alpha=0.9))
    if is_tol and tol_text:
        ax.text(x_dim + 2.5 if offset < 0 else x_dim - 2.5, mid_y, tol_text, fontsize=6.5, color='#475569',
                ha='left' if offset < 0 else 'right', va='center', rotation=90)

def draw_dim_dia(ax, cx, cy, r, angle_deg, text, color='#0f172a'):
    """Vẽ kích thước đường kính xiên có giá đỡ ngang."""
    rad = math.radians(angle_deg)
    px = cx + r * math.cos(rad)
    py = cy + r * math.sin(rad)
    p_lead = (px + 14 * math.cos(rad), py + 14 * math.sin(rad))
    ax.annotate('', xy=(px, py), xytext=p_lead,
                arrowprops=dict(arrowstyle='-|>', color=color, lw=0.9, mutation_scale=8))
    arm_len = 22 if math.cos(rad) >= 0 else -22
    arm_x = p_lead[0] + arm_len
    ax.plot([p_lead[0], arm_x], [p_lead[1], p_lead[1]], color=color, lw=0.9)
    ax.text(arm_x + (2 if math.cos(rad) >= 0 else -2), p_lead[1] + 1.2, text,
            fontsize=8.0, fontweight='bold', color=color,
            ha='left' if math.cos(rad) >= 0 else 'right', va='bottom',
            bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='none', alpha=0.85))

def draw_center_axes(ax, cx, cy, rx, ry, color='#ef4444', lw=0.7):
    """Đường tâm chữ thập chấm gạch đỏ."""
    ax.plot([cx - rx - 8, cx + rx + 8], [cy, cy], color=color, linestyle='-.', lw=lw)
    ax.plot([cx, cx], [cy - ry - 8, cy + ry + 8], color=color, linestyle='-.', lw=lw)

def save_drawing(fig, filename):
    out_p1 = os.path.join(WORK_DIR, filename)
    out_p2 = os.path.join(ARTIFACT_OUT_DIR, filename)
    fig.savefig(out_p1, dpi=200)
    fig.savefig(out_p2, dpi=200)
    plt.close(fig)
    print(f"-> Xuất bản vẽ: {filename}")

# ==============================================================================
# BỘ 21 BẢN VẼ CƠ KHÍ TRỐNG RANG CHI TIẾT
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. CỤM TỔNG THỂ TRỐNG RANG: BV01, BV02, BV03
# ------------------------------------------------------------------------------

def tao_BV01_TT_Dung():
    notes = [
        "Mặt cắt bổ dọc A-A toàn bộ cụm trống rang 2 lớp đệm khí cách nhiệt 10mm.",
        "Trục chính xuyên tâm L=1300mm, 2 đầu nhô ra ngoài mặt máy 82mm.",
        "Đĩa đáy sau Ø784x8mm hàn âm lọt lòng cách đuôi trống 5mm.",
        "10 cây chống Ø20x2mm phân bổ 2 tầng (Y=-400mm và Y=+100mm) lệch pha 36 độ.",
        "5 cánh ngoài uốn xoắn xuôi 216 độ, 5 cánh trong uốn xoắn ngược 216 độ."
    ]
    fig, ax = create_base_drawing('', 'Cụm tổng thể trống rang 2 lớp', 'Hình chiếu đứng / Mặt cắt dọc A-A',
                                  'BV01-TT-DUNG', 1, 21, 'Thép CT3 & Inox 304', '01 Cụm', '1:6', 'thumb_tt.png', notes)
    
    cx, cy = 170, 160
    ax.plot([50, 290], [cy, cy], 'r-.', lw=0.8)

    # 1. Cây láp
    ax.add_patch(Rectangle((82, cy - 5.2), 176, 10.4, facecolor='#e2e8f0', edgecolor='k', lw=1.2))
    ax.add_patch(Rectangle((66, cy - 4.8), 16, 9.6, facecolor='#cbd5e1', edgecolor='k', lw=1.2))
    ax.add_patch(Rectangle((258, cy - 4.8), 16, 9.6, facecolor='#cbd5e1', edgecolor='k', lw=1.2))

    # 2. Vỏ trong (L=160mm, từ x=90 đến x=250)
    ax.add_patch(Rectangle((90, cy + 62.72), 160, 1.28, facecolor='#94a3b8', edgecolor='k', lw=1.1, hatch='///'))
    ax.add_patch(Rectangle((90, cy - 64.0), 160, 1.28, facecolor='#94a3b8', edgecolor='k', lw=1.1, hatch='///'))

    # 3. Vỏ áo ngoài (L=160mm, từ x=90 đến x=250)
    ax.add_patch(Rectangle((90, cy + 65.6), 160, 0.8, facecolor='#64748b', edgecolor='k', lw=1.0, hatch='\\\\\\'))
    ax.add_patch(Rectangle((90, cy - 66.4), 160, 0.8, facecolor='#64748b', edgecolor='k', lw=1.0, hatch='\\\\\\'))

    # Chú thích ĐỆM KHÍ 10MM có đường chỉ mũi tên
    ax.annotate("ĐỆM KHÍ 10MM", xy=(130, cy + 64.8), xytext=(130, cy + 78),
                arrowprops=dict(arrowstyle='->', color='#0284c7', lw=0.8),
                fontsize=7.5, color='#0284c7', ha='center', va='bottom', fontweight='bold',
                bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='#0284c7', lw=0.6))

    # 4. Tấm sắt tròn đáy sau trống
    ax.add_patch(Rectangle((247.92, cy + 5.2), 1.28, 57.52, facecolor='#ea580c', edgecolor='k', lw=1.2, hatch='///'))
    ax.add_patch(Rectangle((247.92, cy - 62.72), 1.28, 57.52, facecolor='#ea580c', edgecolor='k', lw=1.2, hatch='///'))
    ax.plot([250, 250], [cy + 55, cy + 70], 'r--', lw=0.8)
    ax.plot([249.2, 249.2], [cy + 55, cy + 70], 'r--', lw=0.8)
    ax.text(249.6, cy + 72, "Âm 5mm", fontsize=6.5, color='#b91c1c', ha='center', fontweight='bold')

    # 5. Nan hoa cây chống Ø20
    for x_sp in [106, 186]:
        ax.add_patch(Rectangle((x_sp - 1.6, cy + 5.2), 3.2, 57.52, facecolor='#fef08a', edgecolor='k', lw=1.0))
        ax.add_patch(Rectangle((x_sp - 1.6, cy - 62.72), 3.2, 57.52, facecolor='#fef08a', edgecolor='k', lw=1.0))
        ax.plot([x_sp, x_sp], [cy - 68, cy + 68], 'r-.', lw=0.6)

    # 6. Cánh đảo
    ax.plot([93, 140, 200, 247], [cy + 61, cy + 53, cy + 61, cy + 53], color='#ec4899', lw=2.0)
    ax.plot([93, 140, 200, 247], [cy - 61, cy - 53, cy - 61, cy - 53], color='#ec4899', lw=2.0)
    ax.plot([106, 145, 186, 210], [cy + 28, cy + 39, cy + 28, cy + 39], color='#a855f7', lw=2.2, linestyle='--')
    ax.plot([106, 145, 186, 210], [cy - 28, cy - 39, cy - 28, cy - 39], color='#a855f7', lw=2.2, linestyle='--')

    # Kích thước
    draw_dim_h(ax, 66, 274, cy - 70, "L1300 (TỔNG CHIỀU DÀI CÂY LÁP)", offset=-12)
    draw_dim_h(ax, 90, 250, cy + 70, "L1000 (CHIỀU DÀI TRỐNG RANG)", offset=12)
    draw_dim_h(ax, 66, 82, cy - 70, "100", offset=-24)
    draw_dim_h(ax, 258, 274, cy - 70, "100", offset=-24)
    draw_dim_h(ax, 90, 106, cy + 70, "100", offset=22)
    draw_dim_h(ax, 106, 186, cy + 70, "500", offset=22)
    draw_dim_h(ax, 186, 250, cy + 70, "400", offset=22)

    draw_dim_v(ax, cy - 66.4, cy + 66.4, 45, "Ø830 (VỎ ÁO NGOÀI)", offset=-8)
    draw_dim_v(ax, cy - 64.0, cy + 64.0, 55, "Ø800 (VỎ TRỐNG TRONG)", offset=-8)
    draw_dim_v(ax, cy - 62.72, cy + 62.72, 280, "Ø784 (LÒNG TRONG)", offset=8)
    draw_dim_v(ax, cy - 5.2, cy + 5.2, 290, "Ø65 (LÁP GIỮA)", offset=8)
    draw_dim_v(ax, cy - 4.8, cy + 4.8, 66, "Ø60", offset=-8)

    save_drawing(fig, "BV01_TT_Dung_Cat_AA.png")

def tao_BV02_TT_Bang():
    notes = [
        "Hình chiếu bằng nhìn từ trên xuống cụm trống rang 2 lớp đệm khí.",
        "Vỏ áo ngoài hình trụ tròn Ø830mm bao bọc hoàn toàn vỏ trong.",
        "Hai đầu cốt láp Ø60mm thò ra ngoài 82mm gia công rãnh then cavet 18x11x80mm.",
        "Mặt bích và vỏ hàn kín 100% bằng công nghệ hàn giáp mối chìm hồ quang.",
        "Khung định vị lắp bạc đạn gối đỡ UCP212 / UCF212 tiêu chuẩn công nghiệp."
    ]
    fig, ax = create_base_drawing('', 'Cụm tổng thể trống rang 2 lớp', 'Hình chiếu bằng (Top View)',
                                  'BV02-TT-BANG', 2, 21, 'Thép CT3 & Inox 304', '01 Cụm', '1:6', 'thumb_tt.png', notes)
    
    cx, cy = 170, 160
    ax.plot([50, 290], [cy, cy], 'r-.', lw=0.8)

    ax.add_patch(Rectangle((90, cy - 66.4), 160, 132.8, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.8))
    ax.plot([90, 90], [cy - 66.4, cy + 66.4], 'k-', lw=1.8)
    ax.plot([250, 250], [cy - 66.4, cy + 66.4], 'k-', lw=1.8)

    ax.plot([90, 250], [cy + 64.0, cy + 64.0], color='#0284c7', linestyle='--', lw=0.9)
    ax.plot([90, 250], [cy - 64.0, cy - 64.0], color='#0284c7', linestyle='--', lw=0.9)
    ax.plot([90, 250], [cy + 62.72, cy + 62.72], color='#0284c7', linestyle=':', lw=0.8)
    ax.plot([90, 250], [cy - 62.72, cy - 62.72], color='#0284c7', linestyle=':', lw=0.8)

    # Cốt láp
    ax.add_patch(Rectangle((66, cy - 4.8), 24, 9.6, facecolor='#e2e8f0', edgecolor='k', lw=1.2))
    ax.add_patch(Rectangle((69.2, cy - 1.44), 12.8, 2.88, facecolor='#94a3b8', edgecolor='k', lw=0.8))
    ax.add_patch(Rectangle((250, cy - 4.8), 24, 9.6, facecolor='#e2e8f0', edgecolor='k', lw=1.2))
    ax.add_patch(Rectangle((258, cy - 1.44), 12.8, 2.88, facecolor='#94a3b8', edgecolor='k', lw=0.8))

    draw_dim_h(ax, 66, 274, cy - 70, "1300 (CHIỀU DÀI TRỤC)", offset=-10)
    draw_dim_h(ax, 90, 250, cy + 70, "1000 (CHIỀU DÀI VỎ ÁO)", offset=10)
    draw_dim_h(ax, 66, 90, cy - 70, "150 (ĐẦU THÒ)", offset=-22)
    draw_dim_h(ax, 69.2, 82, cy + 10, "Then 18x80", offset=10)

    draw_dim_v(ax, cy - 66.4, cy + 66.4, 55, "Ø830 (VỎ NGOÀI)", offset=-8)
    draw_dim_v(ax, cy - 4.8, cy + 4.8, 66, "Ø60k6", offset=-8)

    save_drawing(fig, "BV02_TT_Bang.png")

def tao_BV03_TT_Canh():
    notes = [
        "Hình chiếu cạnh nhìn từ miệng trước trống rang vào lòng trong.",
        "Thấy rõ 10 cây chống tròn Ø20mm lệch pha 36 độ tạo thành nan hoa đều.",
        "5 cánh đảo ngoài la sắt 70x5mm bám sát vành vỏ trong Ø784mm.",
        "5 cánh đảo trong la sắt 100x8mm đón hạt rơi đối lưu liên tục.",
        "Độ đảo hướng tâm của vỏ trống khi quay trên trục láp <= 0.5mm."
    ]
    fig, ax = create_base_drawing('', 'Cụm tổng thể trống rang 2 lớp', 'Hình chiếu cạnh (Side View - Nhìn từ miệng)',
                                  'BV03-TT-CANH', 3, 21, 'Thép CT3 & Inox 304', '01 Cụm', '1:6', 'thumb_tt.png', notes)
    
    cx, cy = 175, 160
    draw_center_axes(ax, cx, cy, 75, 75)

    ax.add_patch(Circle((cx, cy), 66.4, fill=False, edgecolor='#0f172a', lw=1.8))
    ax.add_patch(Circle((cx, cy), 65.6, fill=False, edgecolor='#64748b', lw=0.9))
    ax.add_patch(Circle((cx, cy), 64.0, fill=False, edgecolor='#0284c7', lw=1.6))
    ax.add_patch(Circle((cx, cy), 62.72, fill=False, edgecolor='#0f172a', lw=1.8))

    ax.add_patch(Circle((cx, cy), 5.2, facecolor='#e2e8f0', edgecolor='k', lw=1.2))
    ax.add_patch(Circle((cx, cy), 4.8, fill=False, edgecolor='#2563eb', linestyle='--', lw=0.8))

    # Tầng 1
    angles_t1 = [-4.5, 67.5, 139.5, 211.5, 283.5]
    for deg in angles_t1:
        rad = math.radians(deg)
        x1, y1 = cx + 5.2 * math.cos(rad), cy + 5.2 * math.sin(rad)
        x2, y2 = cx + 62.72 * math.cos(rad), cy + 62.72 * math.sin(rad)
        ax.plot([x1, x2], [y1, y2], color='#eab308', lw=2.4)

    # Tầng 2
    angles_t2 = [36.0, 108.0, 180.0, 252.0, 324.0]
    for deg in angles_t2:
        rad = math.radians(deg)
        x1, y1 = cx + 5.2 * math.cos(rad), cy + 5.2 * math.sin(rad)
        x2, y2 = cx + 62.72 * math.cos(rad), cy + 62.72 * math.sin(rad)
        ax.plot([x1, x2], [y1, y2], color='#ca8a04', lw=1.8, linestyle='--')

    arc_ang = Arc((cx, cy), 70, 70, angle=0, theta1=-4.5, theta2=36.0, color='#b91c1c', lw=1.2)
    ax.add_patch(arc_ang)
    ax.text(cx + 40, cy + 12, "36°", fontsize=8.0, color='#b91c1c', fontweight='bold')

    draw_dim_dia(ax, cx, cy, 66.4, 45, "Ø830 (VỎ ÁO NGOÀI)")
    draw_dim_dia(ax, cx, cy, 64.0, 135, "Ø800 (VỎ TRỐNG)")
    draw_dim_dia(ax, cx, cy, 62.72, 225, "Ø784 (LÒNG TRỐNG)")
    draw_dim_dia(ax, cx, cy, 5.2, -45, "Ø65 (TRỤC CHÍNH)")

    save_drawing(fig, "BV03_TT_Canh.png")

# ------------------------------------------------------------------------------
# 2. CHI TIẾT 01: VỎ TRỐNG TRONG (Ø800 x 8 x 1000mm) - BV04, BV05, BV06
# ------------------------------------------------------------------------------

def tao_BV04_CT01_Dung():
    notes = [
        "Vỏ trống trong cuộn lốc từ thép tấm dày 8mm chịu nhiệt.",
        "Đường kính ngoài Ø800±0.5mm, đường kính trong lọt lòng Ø784mm.",
        "Đuôi sau tiện gờ lọt lòng sâu 5mm để đặt đĩa đáy sau và hàn âm.",
        "Hai đầu vát mép 1.5x45 độ, làm sạch xỉ hàn và bavia sắc nhọn.",
        "Đường sinh hàn giáp mối dọc thân mài phẳng Ra 3.2, kiểm tra siêu âm mối hàn."
    ]
    fig, ax = create_base_drawing('CT01', 'Vỏ trống trong Ø800x8x1000', 'Hình chiếu đứng / Mặt cắt dọc A-A',
                                  'BV04-CT01-DUNG', 4, 21, 'Thép tấm chịu nhiệt SS400', '01 Cái', '1:6', 'thumb_ct1.png', notes)
    cx, cy = 170, 160
    ax.plot([60, 280], [cy, cy], 'r-.', lw=0.8)

    # Nửa trên: Mặt cắt A-A
    ax.add_patch(Rectangle((90, cy + 62.72), 160, 1.28, facecolor='#f1f5f9', edgecolor='k', lw=1.2, hatch='///'))
    # Nửa dưới: Mặt cắt A-A
    ax.add_patch(Rectangle((90, cy - 64.0), 160, 1.28, facecolor='#f1f5f9', edgecolor='k', lw=1.2, hatch='///'))
    
    # 2 mép đầu
    ax.plot([90, 90], [cy - 64.0, cy + 64.0], 'k-', lw=1.6)
    ax.plot([250, 250], [cy - 64.0, cy + 64.0], 'k-', lw=1.6)

    # Chi tiết gờ âm 5mm ở đuôi
    ax.plot([249.2, 249.2], [cy + 61, cy + 67], 'r--', lw=0.8)
    ax.text(249.2, cy + 69, "Gờ âm 5mm", fontsize=7.0, color='#b91c1c', ha='center', fontweight='bold')

    # Kích thước
    draw_dim_h(ax, 90, 250, cy + 64.0, "1000 ± 0.5 (CHIỀU DÀI PHÔI)", offset=12)
    draw_dim_v(ax, cy - 64.0, cy + 64.0, 75, "Ø800 ± 0.5 (NGOÀI)", offset=-8)
    draw_dim_v(ax, cy - 62.72, cy + 62.72, 85, "Ø784 (TRONG)", offset=-8)
    
    # Chú thích chiều dày thành sắt
    ax.annotate("t = 8.0 mm", xy=(250, cy + 63.36), xytext=(265, cy + 63.36),
                arrowprops=dict(arrowstyle='->', color='#0f172a', lw=0.8),
                fontsize=8.0, fontweight='bold', color='#0f172a', va='center')

    save_drawing(fig, "BV04_CT01_Vo_Trong_Dung.png")

def tao_BV05_CT01_Bang():
    notes = [
        "Hình chiếu bằng vỏ trống trong Ø800mm dài 1000mm.",
        "Thể hiện đường hàn giáp mối dọc thân mài phẳng liền lạc.",
        "Độ cong vênh toàn thân <= 0.8mm dọc theo chiều dài 1m.",
        "Độ trụ và độ tròn đạt trong phạm vi dung sai ±0.5mm.",
        "Bề mặt trong đánh bóng mịn chống bám dính dầu cà phê."
    ]
    fig, ax = create_base_drawing('CT01', 'Vỏ trống trong Ø800x8x1000', 'Hình chiếu bằng (Top View)',
                                  'BV05-CT01-BANG', 5, 21, 'Thép tấm chịu nhiệt SS400', '01 Cái', '1:6', 'thumb_ct1.png', notes)
    cx, cy = 170, 160
    ax.plot([60, 280], [cy, cy], 'r-.', lw=0.8)

    ax.add_patch(Rectangle((90, cy - 64.0), 160, 128.0, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.8))
    ax.plot([90, 250], [cy + 20, cy + 20], color='#2563eb', lw=1.2, linestyle='-')
    ax.text(170, cy + 24, "ĐƯỜNG HÀN CHÌM DỌC THÂN (MÀI PHẲNG Ra 3.2)", fontsize=7.5, color='#2563eb', ha='center', fontweight='bold',
            bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='#2563eb', lw=0.5))

    draw_dim_h(ax, 90, 250, cy + 64.0, "1000 ± 0.5", offset=10)
    draw_dim_v(ax, cy - 64.0, cy + 64.0, 75, "Ø800 ± 0.5", offset=-8)

    save_drawing(fig, "BV05_CT01_Vo_Trong_Bang.png")

def tao_BV06_CT01_Canh():
    notes = [
        "Hình chiếu cạnh vành tròn vỏ trống trong Ø800x8mm.",
        "Độ không tròn (độ ô-van) cho phép <= 0.5mm.",
        "Bề dày thành ống đều đặn 8.0mm ± 0.2mm sau khi lốc tròn.",
        "Vát mép 2 đầu góc 45 độ, bề rộng vát 1.5mm.",
        "Xử lý khử ứng suất nhiệt dư sau nguyên công cuốn ống và hàn."
    ]
    fig, ax = create_base_drawing('CT01', 'Vỏ trống trong Ø800x8x1000', 'Hình chiếu cạnh (Side View)',
                                  'BV06-CT01-CANH', 6, 21, 'Thép tấm chịu nhiệt SS400', '01 Cái', '1:6', 'thumb_ct1.png', notes)
    cx, cy = 175, 160
    draw_center_axes(ax, cx, cy, 75, 75)

    ax.add_patch(Circle((cx, cy), 64.0, fill=True, facecolor='#f1f5f9', edgecolor='#0f172a', lw=1.8))
    ax.add_patch(Circle((cx, cy), 62.72, fill=True, facecolor='#ffffff', edgecolor='#0f172a', lw=1.8))

    draw_dim_dia(ax, cx, cy, 64.0, 45, "Ø800 ± 0.5 (NGOÀI)")
    draw_dim_dia(ax, cx, cy, 62.72, 135, "Ø784 ± 0.5 (TRONG)")
    ax.text(cx, cy - 68, "BỀ DÀY THÀNH SẮT t = 8.0 mm", fontsize=8.0, fontweight='bold', color='#0f172a', ha='center')

    save_drawing(fig, "BV06_CT01_Vo_Trong_Canh.png")

# ------------------------------------------------------------------------------
# 3. CHI TIẾT 02: VỎ ÁO NGOÀI ĐỆM KHÍ (Ø830 x 5 x 1000mm) - BV07, BV08, BV09
# ------------------------------------------------------------------------------

def tao_BV07_CT02_Dung():
    notes = [
        "Vỏ áo ngoài giữ nhiệt cuộn từ thép tấm dày 5mm.",
        "Đường kính ngoài Ø830mm, đường kính trong Ø820mm.",
        "Tạo khoảng hở đệm khí cách nhiệt 10mm so với vỏ trống trong Ø800mm.",
        "Chống táp lửa trực tiếp từ bếp củi vào hạt cà phê.",
        "Sơn chịu nhiệt màu đen mờ (>600 độ C) bề mặt ngoài chống oxy hóa."
    ]
    fig, ax = create_base_drawing('CT02', 'Vỏ áo ngoài đệm khí Ø830x5x1000', 'Hình chiếu đứng / Mặt cắt dọc A-A',
                                  'BV07-CT02-DUNG', 7, 21, 'Thép tấm CT3 / SS400', '01 Cái', '1:6', 'thumb_ct2.png', notes)
    cx, cy = 170, 160
    ax.plot([60, 280], [cy, cy], 'r-.', lw=0.8)

    # Nửa trên cắt A-A
    ax.add_patch(Rectangle((90, cy + 65.6), 160, 0.8, facecolor='#f1f5f9', edgecolor='k', lw=1.1, hatch='///'))
    # Nửa dưới cắt A-A
    ax.add_patch(Rectangle((90, cy - 66.4), 160, 0.8, facecolor='#f1f5f9', edgecolor='k', lw=1.1, hatch='///'))
    
    ax.plot([90, 90], [cy - 66.4, cy + 66.4], 'k-', lw=1.6)
    ax.plot([250, 250], [cy - 66.4, cy + 66.4], 'k-', lw=1.6)

    draw_dim_h(ax, 90, 250, cy + 66.4, "1000 ± 0.8 (CHIỀU DÀI ÁO)", offset=10)
    draw_dim_v(ax, cy - 66.4, cy + 66.4, 75, "Ø830 ± 0.8 (NGOÀI)", offset=-8)
    draw_dim_v(ax, cy - 65.6, cy + 65.6, 85, "Ø820 (TRONG)", offset=-8)
    
    ax.annotate("t = 5.0 mm", xy=(250, cy + 66.0), xytext=(265, cy + 66.0),
                arrowprops=dict(arrowstyle='->', color='#0f172a', lw=0.8),
                fontsize=8.0, fontweight='bold', color='#0f172a', va='center')

    save_drawing(fig, "BV07_CT02_Vo_Ao_Dung.png")

def tao_BV08_CT02_Bang():
    notes = [
        "Hình chiếu bằng vỏ áo ngoài giữ nhiệt Ø830x1000mm.",
        "Mối hàn dọc thân kín khít tuyệt đối, không rò rỉ khí nóng.",
        "Độ đồng trục với vỏ trong đạt sai lệch <= 1.0mm.",
        "Bề mặt làm sạch bằng phun cát trước khi sơn phủ chịu nhiệt.",
        "Kiểm tra ngoại quan không nứt nẻ, biến dạng nhiệt sau hàn."
    ]
    fig, ax = create_base_drawing('CT02', 'Vỏ áo ngoài đệm khí Ø830x5x1000', 'Hình chiếu bằng (Top View)',
                                  'BV08-CT02-BANG', 8, 21, 'Thép tấm CT3 / SS400', '01 Cái', '1:6', 'thumb_ct2.png', notes)
    cx, cy = 170, 160
    ax.plot([60, 280], [cy, cy], 'r-.', lw=0.8)

    ax.add_patch(Rectangle((90, cy - 66.4), 160, 132.8, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.8))
    ax.plot([90, 250], [cy + 15, cy + 15], color='#475569', lw=1.2, linestyle='-')
    ax.text(170, cy + 19, "MỐI HÀN DỌC THÂN KÍN KHÍ", fontsize=7.5, color='#475569', ha='center', fontweight='bold',
            bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='#475569', lw=0.5))

    draw_dim_h(ax, 90, 250, cy + 66.4, "1000 ± 0.8", offset=10)
    draw_dim_v(ax, cy - 66.4, cy + 66.4, 75, "Ø830 ± 0.8", offset=-8)

    save_drawing(fig, "BV08_CT02_Vo_Ao_Bang.png")

def tao_BV09_CT02_Canh():
    notes = [
        "Hình chiếu cạnh vỏ áo ngoài Ø830x5mm.",
        "Độ ô-van cho phép <= 0.8mm.",
        "Tạo đệm không khí tĩnh 10mm bao quanh vành ngoài vỏ trống trong.",
        "Đảm bảo nhiệt lượng phân bổ đều 360 độ quanh thân trống rang.",
        "Vát bavia sắc nhọn 2 đầu ống."
    ]
    fig, ax = create_base_drawing('CT02', 'Vỏ áo ngoài đệm khí Ø830x5x1000', 'Hình chiếu cạnh (Side View)',
                                  'BV09-CT02-CANH', 9, 21, 'Thép tấm CT3 / SS400', '01 Cái', '1:6', 'thumb_ct2.png', notes)
    cx, cy = 175, 160
    draw_center_axes(ax, cx, cy, 75, 75)

    ax.add_patch(Circle((cx, cy), 66.4, fill=True, facecolor='#f1f5f9', edgecolor='#0f172a', lw=1.8))
    ax.add_patch(Circle((cx, cy), 65.6, fill=True, facecolor='#ffffff', edgecolor='#0f172a', lw=1.8))

    draw_dim_dia(ax, cx, cy, 66.4, 45, "Ø830 ± 0.8 (NGOÀI)")
    draw_dim_dia(ax, cx, cy, 65.6, 135, "Ø820 (TRONG)")
    ax.text(cx, cy - 70, "ĐỆM KHÍ CÁCH NHIỆT 10MM", fontsize=8.0, fontweight='bold', color='#0284c7', ha='center')

    save_drawing(fig, "BV09_CT02_Vo_Ao_Canh.png")

# ------------------------------------------------------------------------------
# 4. CHI TIẾT 03: TẤM SẮT TRÒN ĐÁY SAU TRỐNG (Ø784 x 8mm) - BV10, BV11, BV12
# ------------------------------------------------------------------------------

def tao_BV10_CT03_Dung():
    notes = [
        "Đĩa sắt tròn đáy sau cắt CNC Fiber Laser từ thép tấm 8mm.",
        "Đường kính ngoài Ø784-0.5mm lọt khít lòng trống trong.",
        "Lỗ tâm Ø65+0.2mm xỏ khít vừa vặn qua thân cây láp chính.",
        "Vát mép ngoài 3x45 độ tạo rãnh chữ V hàn góc ngấu 4mm.",
        "Hàn vành collar cổ trục láp chịu lực xoắn đảo chiều."
    ]
    fig, ax = create_base_drawing('CT03', 'Tấm sắt tròn đáy sau trống', 'Hình chiếu đứng / Mặt cắt dọc A-A',
                                  'BV10-CT03-DUNG', 10, 21, 'Thép tấm CT3 dày 8mm', '01 Cái', '1:4', 'thumb_ct3.png', notes)
    cx, cy = 170, 160
    ax.plot([100, 240], [cy, cy], 'r-.', lw=0.8)

    # Nửa trên
    ax.add_patch(Rectangle((cx - 8, cy + 13), 16, 65.4, facecolor='#f1f5f9', edgecolor='k', lw=1.4, hatch='///'))
    # Nửa dưới
    ax.add_patch(Rectangle((cx - 8, cy - 78.4), 16, 65.4, facecolor='#f1f5f9', edgecolor='k', lw=1.4, hatch='///'))

    # Mối hàn collar cổ trục
    ax.add_patch(Polygon([[cx + 8, cy + 13], [cx + 16, cy + 13], [cx + 8, cy + 21]], closed=True, facecolor='#ea580c', edgecolor='k', lw=1.0))
    ax.add_patch(Polygon([[cx + 8, cy - 13], [cx + 16, cy - 13], [cx + 8, cy - 21]], closed=True, facecolor='#ea580c', edgecolor='k', lw=1.0))
    
    # Leader arrow cho mối hàn góc
    ax.annotate("HÀN GÓC a=4mm", xy=(cx + 12, cy + 17), xytext=(cx + 32, cy + 30),
                arrowprops=dict(arrowstyle='->', color='#ea580c', lw=0.9),
                fontsize=7.5, color='#ea580c', fontweight='bold',
                bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='#ea580c', lw=0.6))

    # Đường tâm lỗ cốt
    ax.plot([cx - 15, cx + 25], [cy + 13, cy + 13], 'k--', lw=0.9)
    ax.plot([cx - 15, cx + 25], [cy - 13, cy - 13], 'k--', lw=0.9)

    draw_dim_h(ax, cx - 8, cx + 8, cy + 82, "8.0 mm (DÀY)", offset=8)
    draw_dim_v(ax, cy - 78.4, cy + 78.4, cx - 18, "Ø784 -0.5", offset=-8)
    draw_dim_v(ax, cy - 13, cy + 13, cx + 18, "Ø65 +0.2 (LỖ CỐT LÁP)", offset=6)

    save_drawing(fig, "BV10_CT03_Day_Sau_Dung.png")

def tao_BV11_CT03_Bang():
    notes = [
        "Hình chiếu bằng tấm sắt tròn đáy sau trống rang dày 8mm.",
        "Độ phẳng bề mặt đĩa đạt sai lệch <= 0.5mm sau khi cắt laser.",
        "Lỗ tâm xỏ cốt khoan/doa tinh đạt độ vuông góc 0.05mm so với mặt đĩa.",
        "Không cong vênh, ba via được mài sạch hoàn toàn.",
        "Vị trí lắp đặt: Thụt lọt lòng âm 5mm so với mép đuôi trống."
    ]
    fig, ax = create_base_drawing('CT03', 'Tấm sắt tròn đáy sau trống', 'Hình chiếu bằng (Top View)',
                                  'BV11-CT03-BANG', 11, 21, 'Thép tấm CT3 dày 8mm', '01 Cái', '1:4', 'thumb_ct3.png', notes)
    cx, cy = 170, 160
    ax.plot([100, 240], [cy, cy], 'r-.', lw=0.8)

    ax.add_patch(Rectangle((cx - 8, cy - 78.4), 16, 156.8, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.6))
    ax.plot([cx - 8, cx + 8], [cy + 13, cy + 13], color='#0284c7', linestyle='--', lw=1.0)
    ax.plot([cx - 8, cx + 8], [cy - 13, cy - 13], color='#0284c7', linestyle='--', lw=1.0)

    draw_dim_h(ax, cx - 8, cx + 8, cy + 82, "8.0 mm", offset=8)
    draw_dim_v(ax, cy - 78.4, cy + 78.4, cx - 18, "Ø784 -0.5", offset=-8)
    draw_dim_v(ax, cy - 13, cy + 13, cx + 18, "Ø65", offset=8)

    save_drawing(fig, "BV11_CT03_Day_Sau_Bang.png")

def tao_BV12_CT03_Canh():
    notes = [
        "Hình chiếu cạnh mặt tròn đĩa đáy sau Ø784mm.",
        "Cắt CNC Laser lỗ tâm Ø65mm đồng tâm với đường kính ngoài.",
        "Độ đảo mặt đầu khi quay cùng trục láp <= 0.3mm.",
        "Mép ngoài vát nghiêng 45 độ chuẩn bị mối hàn góc với lòng trống.",
        "Sau khi hàn hoàn thiện tiến hành mài phẳng mặt trong chống kẹt hạt."
    ]
    fig, ax = create_base_drawing('CT03', 'Tấm sắt tròn đáy sau trống', 'Hình chiếu cạnh (Side View)',
                                  'BV12-CT03-CANH', 12, 21, 'Thép tấm CT3 dày 8mm', '01 Cái', '1:6', 'thumb_ct3.png', notes)
    cx, cy = 175, 160
    draw_center_axes(ax, cx, cy, 75, 75)

    ax.add_patch(Circle((cx, cy), 65.4, fill=True, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.8))
    ax.add_patch(Circle((cx, cy), 5.4, fill=True, facecolor='#ffffff', edgecolor='#0f172a', lw=1.4))

    draw_dim_dia(ax, cx, cy, 65.4, 45, "Ø784 -0.5 (ĐƯỜNG KÍNH ĐĨA)")
    draw_dim_dia(ax, cx, cy, 5.4, 135, "Ø65 +0.2 (LỖ CỐT LÁP)")

    save_drawing(fig, "BV12_CT03_Day_Sau_Canh.png")

# ------------------------------------------------------------------------------
# 5. CHI TIẾT 04: CÂY LÁP TRỤC CHÍNH XUYÊN TÂM (L=1300mm) - BV13, BV14, BV15
# ------------------------------------------------------------------------------

def tao_BV13_CT04_Dung():
    notes = [
        "Trục bậc gia công từ thép tròn đặc C45 tôi ram cải thiện độ bền.",
        "Tổng chiều dài 1300±0.5mm. Thân giữa Ø65h8 dài 1100mm.",
        "2 đầu tiện bậc Ø60k6 dài 100mm, nhô ra ngoài mặt máy 82mm.",
        "Hai đầu phay rãnh then bằng cavet 18x11x80mm đạt cấp dung sai P9.",
        "Độ đảo hướng tâm toàn phần của cổ trục <= 0.03mm. Mài tinh Ra 0.8."
    ]
    fig, ax = create_base_drawing('CT04', 'Cây láp trục chính xuyên tâm', 'Hình chiếu đứng (Trục bậc L=1300)',
                                  'BV13-CT04-DUNG', 13, 21, 'Thép C45 tôi ram', '01 Cây', '1:8', 'thumb_ct4.png', notes)
    cx, cy = 170, 160
    ax.plot([45, 295], [cy, cy], 'r-.', lw=0.8)

    ax.add_patch(Rectangle((82, cy - 5.2), 176, 10.4, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.6))
    ax.add_patch(Rectangle((66, cy - 4.8), 16, 9.6, facecolor='#f1f5f9', edgecolor='#0f172a', lw=1.4))
    ax.add_patch(Rectangle((258, cy - 4.8), 16, 9.6, facecolor='#f1f5f9', edgecolor='#0f172a', lw=1.4))

    # Vát mép 2 đầu 2x45 độ
    ax.plot([66, 68], [cy - 4.8, cy - 2.8], 'k-', lw=1.0)
    ax.plot([66, 68], [cy + 4.8, cy + 2.8], 'k-', lw=1.0)
    ax.plot([274, 272], [cy - 4.8, cy - 2.8], 'k-', lw=1.0)
    ax.plot([274, 272], [cy + 4.8, cy + 2.8], 'k-', lw=1.0)

    # Rãnh then 2 đầu
    ax.plot([68, 80.8], [cy + 3.68, cy + 3.68], 'b--', lw=0.9)
    ax.plot([259.2, 272], [cy + 3.68, cy + 3.68], 'b--', lw=0.9)

    draw_dim_h(ax, 66, 274, cy - 15, "1300 ± 0.5 (TỔNG DÀI)", offset=-12)
    draw_dim_h(ax, 82, 258, cy + 15, "1100 (THÂN TRỤC GIỮA 2 MẶT MÁY)", offset=12)
    draw_dim_h(ax, 66, 82, cy - 15, "100", offset=-24)
    draw_dim_h(ax, 258, 274, cy - 15, "100", offset=-24)

    # Dimension đường kính thân trục Ø65
    draw_dim_v(ax, cy - 5.2, cy + 5.2, 170, "Ø65 h8", offset=25)
    draw_dim_v(ax, cy - 4.8, cy + 4.8, 66, "Ø60 k6", offset=-8)
    draw_dim_v(ax, cy - 4.8, cy + 4.8, 274, "Ø60 k6", offset=8)

    save_drawing(fig, "BV13_CT04_Cay_Lap_Dung.png")

def tao_BV14_CT04_Bang():
    notes = [
        "Hình chiếu bằng thể hiện chính xác 2 rãnh then cavet ở 2 đầu cốt láp.",
        "Quy cách rãnh then: Bề rộng b=18mm (P9), Chiều dài L=80mm, Độ sâu t1=7.0mm.",
        "Gia công bằng dao phay ngón Ø18mm, bo tròn 2 đầu bán kính R=9mm.",
        "Khoảng cách từ mép đầu cốt đến rãnh then là 10mm.",
        "Lắp ráp then bằng tiêu chuẩn TCVN 4216-86 / DIN 6885."
    ]
    fig, ax = create_base_drawing('CT04', 'Cây láp trục chính xuyên tâm', 'Hình chiếu bằng (Rãnh then cavet 18x80)',
                                  'BV14-CT04-BANG', 14, 21, 'Thép C45 tôi ram', '01 Cây', '1:8', 'thumb_ct4.png', notes)
    cx, cy = 170, 160
    ax.plot([45, 295], [cy, cy], 'r-.', lw=0.8)

    ax.add_patch(Rectangle((82, cy - 5.2), 176, 10.4, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.6))
    ax.add_patch(Rectangle((66, cy - 4.8), 16, 9.6, facecolor='#f1f5f9', edgecolor='#0f172a', lw=1.4))
    ax.add_patch(Rectangle((258, cy - 4.8), 16, 9.6, facecolor='#f1f5f9', edgecolor='#0f172a', lw=1.4))

    ax.add_patch(Rectangle((67.6, cy - 1.44), 12.8, 2.88, facecolor='#cbd5e1', edgecolor='#0f172a', lw=1.0))
    ax.add_patch(Rectangle((259.6, cy - 1.44), 12.8, 2.88, facecolor='#cbd5e1', edgecolor='#0f172a', lw=1.0))

    draw_dim_h(ax, 67.6, 80.4, cy + 10, "80 (DÀI THEN)", offset=8)
    draw_dim_v(ax, cy - 1.44, cy + 1.44, 67.6, "18 P9", offset=-10)
    draw_dim_h(ax, 66, 67.6, cy - 10, "10", offset=-8)

    save_drawing(fig, "BV14_CT04_Cay_Lap_Bang.png")

def tao_BV15_CT04_Canh():
    notes = [
        "Hình chiếu cạnh và Mặt cắt phóng to B-B qua rãnh then cavet đầu trục.",
        "Tiết diện thân trục Ø65mm và cổ trục Ø60mm.",
        "Mặt cắt B-B tỷ lệ 1:1 làm rõ kích thước rãnh then: b=18mm, h=11mm, t1=7mm.",
        "Độ nhám rãnh then Ra 1.6, vát góc rãnh r=0.4mm.",
        "Khử ba via hoàn toàn mép rãnh then trước khi nghiệm thu."
    ]
    fig, ax = create_base_drawing('CT04', 'Cây láp trục chính xuyên tâm', 'Hình chiếu cạnh & Mặt cắt B-B rãnh then',
                                  'BV15-CT04-CANH', 15, 21, 'Thép C45 tôi ram', '01 Cây', '1:2 & 1:1', 'thumb_ct4.png', notes)
    # Bên trái: Chiếu cạnh trục Ø65 và Ø60
    cx1, cy1 = 110, 160
    draw_center_axes(ax, cx1, cy1, 45, 45)
    ax.add_patch(Circle((cx1, cy1), 32.5, fill=True, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.8))
    ax.add_patch(Circle((cx1, cy1), 30.0, fill=False, edgecolor='#2563eb', linestyle='--', lw=1.2))
    draw_dim_dia(ax, cx1, cy1, 32.5, 45, "Ø65 h8")
    draw_dim_dia(ax, cx1, cy1, 30.0, 135, "Ø60 k6")

    # Bên phải: Mặt cắt phóng to B-B tỷ lệ 1:1
    cx2, cy2 = 230, 155
    draw_center_axes(ax, cx2, cy2, 40, 40)
    ax.add_patch(Circle((cx2, cy2), 30.0, fill=True, facecolor='#f1f5f9', edgecolor='#0f172a', lw=1.8, hatch='///'))
    ax.add_patch(Rectangle((cx2 - 9, cy2 + 23), 18, 8, facecolor='#ffffff', edgecolor='#ffffff', lw=0.1))
    ax.plot([cx2 - 9, cx2 - 9], [cy2 + 23, cy2 + 29.5], 'k-', lw=1.4)
    ax.plot([cx2 + 9, cx2 + 9], [cy2 + 23, cy2 + 29.5], 'k-', lw=1.4)
    ax.plot([cx2 - 9, cx2 + 9], [cy2 + 23, cy2 + 23], 'k-', lw=1.4)

    # Tiêu đề mặt cắt nâng cao để không đè chữ kích thước
    ax.text(cx2, cy2 + 52, "MẶT CẮT B-B (TỶ LỆ 1:1)", fontsize=9.5, fontweight='bold', color='#0369a1', ha='center')
    draw_dim_h(ax, cx2 - 9, cx2 + 9, cy2 + 30, "b = 18 P9", offset=8)
    draw_dim_v(ax, cy2 + 23, cy2 + 30, cx2 + 9, "t1 = 7.0", offset=12)

    save_drawing(fig, "BV15_CT04_Cay_Lap_Canh.png")

# ------------------------------------------------------------------------------
# 6. CHI TIẾT 05: CỤM 10 CÂY CHỐNG TRÒN Ø20mm - BV16, BV17, BV18
# ------------------------------------------------------------------------------

def tao_BV16_CT05_Dung():
    notes = [
        "Chi tiết gia công 1 cây chống đơn lẻ (Tổng cộng 10 cây giống hệt nhau).",
        "Vật liệu: Ống thép đúc Ø20mm, bề dày thành ống 2.0mm (Ø trong 16mm).",
        "Chiều dài tổng thể L=359.5mm (khoảng cách từ mặt láp Ø65 đến lòng trống Ø784).",
        "Đầu trong cắt lõm bán nguyệt R=32.5mm ôm khít cốt láp để hàn liền ngấu.",
        "Đầu ngoài cắt vát bán nguyệt R=392mm ôm khít lòng vỏ trống trong."
    ]
    fig, ax = create_base_drawing('CT05', 'Cụm 10 cây chống tròn Ø20mm', 'Hình chiếu đứng (Chi tiết 1 nan hoa L=359.5)',
                                  'BV16-CT05-DUNG', 16, 21, 'Ống thép đúc Ø20x2', '10 Cây', '1:2', 'thumb_ct5.png', notes)
    cx, cy = 170, 160
    ax.plot([60, 280], [cy, cy], 'r-.', lw=0.8)

    ax.add_patch(Rectangle((80, cy + 4), 179.75, 1.0, facecolor='#f1f5f9', edgecolor='k', lw=1.2, hatch='///'))
    ax.plot([80, 259.75], [cy - 5, cy - 5], 'k-', lw=1.6)
    ax.plot([80, 259.75], [cy - 4, cy - 4], color='#0284c7', linestyle='--', lw=0.8)

    arc_in = Arc((80, cy), 12, 10, angle=0, theta1=-90, theta2=90, color='k', lw=1.4)
    ax.add_patch(arc_in)
    arc_out = Arc((259.75, cy), 6, 10, angle=0, theta1=90, theta2=270, color='k', lw=1.4)
    ax.add_patch(arc_out)

    draw_dim_h(ax, 80, 259.75, cy + 12, "359.5 ± 0.5 (CHIỀU DÀI GIA CÔNG)", offset=8)
    draw_dim_v(ax, cy - 5, cy + 5, 70, "Ø20 (NGOÀI)", offset=-8)
    draw_dim_v(ax, cy - 4, cy + 4, 270, "Ø16 (TRONG)", offset=8)
    ax.text(80, cy - 14, "Mép lượn R32.5 ôm cốt láp", fontsize=7.0, color='#0284c7', ha='center')
    ax.text(260, cy - 14, "Mép lượn R392 ôm vỏ trống", fontsize=7.0, color='#0284c7', ha='center')

    save_drawing(fig, "BV16_CT05_Cay_Chong_Dung.png")

def tao_BV17_CT05_Bang():
    notes = [
        "Sơ đồ phân bổ dọc trục của 10 cây chống tròn Ø20mm.",
        "Tầng 1 (5 cây gần miệng trước): Đặt tại Y = -400mm (cách miệng trước 100mm).",
        "Tầng 2 (5 cây ở giữa thân trống): Đặt tại Y = +100mm (cách miệng sau 400mm).",
        "Khoảng cách giữa 2 tầng cây chống: 500mm.",
        "Hai tầng lệch pha nhau đúng 36 độ quanh chu vi, triệt tiêu biến dạng xoắn."
    ]
    fig, ax = create_base_drawing('CT05', 'Cụm 10 cây chống tròn Ø20mm', 'Hình chiếu bằng (Sơ đồ phân bổ 2 tầng Y=-400 & Y=+100)',
                                  'BV17-CT05-BANG', 17, 21, 'Ống thép đúc Ø20x2', '10 Cây', '1:6', 'thumb_ct5.png', notes)
    cx, cy = 170, 160
    ax.plot([60, 280], [cy, cy], 'r-.', lw=0.8)

    ax.add_patch(Rectangle((90, cy - 62.72), 160, 125.44, fill=False, edgecolor='#94a3b8', linestyle='--', lw=1.2))
    ax.add_patch(Rectangle((66, cy - 5.2), 208, 10.4, fill=False, edgecolor='#64748b', lw=1.0))

    ax.plot([106, 106], [cy - 62.72, cy + 62.72], color='#eab308', lw=3.0)
    ax.text(106, cy + 68, "TẦNG 1 (Y = -400)\n5 CÂY (GÓC -4.5° + k.72°)", fontsize=7.5, color='#a16207', ha='center', fontweight='bold',
            bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='#eab308', lw=0.6))

    ax.plot([186, 186], [cy - 62.72, cy + 62.72], color='#ca8a04', lw=3.0, linestyle='-')
    ax.text(186, cy + 68, "TẦNG 2 (Y = +100)\n5 CÂY (GÓC 36° + k.72°)", fontsize=7.5, color='#a16207', ha='center', fontweight='bold',
            bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='#ca8a04', lw=0.6))

    draw_dim_h(ax, 90, 106, cy - 70, "100", offset=-8)
    draw_dim_h(ax, 106, 186, cy - 70, "500 (KHOẢNG CÁCH 2 TẦNG)", offset=-8)
    draw_dim_h(ax, 186, 250, cy - 70, "400", offset=-8)

    save_drawing(fig, "BV17_CT05_Cay_Chong_Bang.png")

def tao_BV18_CT05_Canh():
    notes = [
        "Hình chiếu cạnh cụm nan hoa 10 cây chống nhìn dọc theo trục máy.",
        "5 cây Tầng 1 (nét liền): Các góc -4.5°, 67.5°, 139.5°, 211.5°, 283.5°.",
        "5 cây Tầng 2 (nét đứt): Các góc 36°, 108°, 180°, 252°, 324°.",
        "Tạo thành mạng nan hoa chữ thập đối xứng lệch pha 36 độ quanh chu vi.",
        "Mối hàn tiếp tuyến ngấu chắc chắn với 5 cánh đảo ngoài dọc theo thân."
    ]
    fig, ax = create_base_drawing('CT05', 'Cụm 10 cây chống tròn Ø20mm', 'Hình chiếu cạnh (Mặt bích nan hoa 10 cánh lệch 36°)',
                                  'BV18-CT05-CANH', 18, 21, 'Ống thép đúc Ø20x2', '10 Cây', '1:6', 'thumb_ct5.png', notes)
    cx, cy = 175, 160
    draw_center_axes(ax, cx, cy, 75, 75)

    ax.add_patch(Circle((cx, cy), 62.72, fill=False, edgecolor='#94a3b8', linestyle='--', lw=1.2))
    ax.add_patch(Circle((cx, cy), 5.2, fill=True, facecolor='#cbd5e1', edgecolor='k', lw=1.2))

    angles_t1 = [-4.5, 67.5, 139.5, 211.5, 283.5]
    for deg in angles_t1:
        rad = math.radians(deg)
        x1, y1 = cx + 5.2 * math.cos(rad), cy + 5.2 * math.sin(rad)
        x2, y2 = cx + 62.72 * math.cos(rad), cy + 62.72 * math.sin(rad)
        ax.plot([x1, x2], [y1, y2], color='#eab308', lw=2.6)

    angles_t2 = [36.0, 108.0, 180.0, 252.0, 324.0]
    for deg in angles_t2:
        rad = math.radians(deg)
        x1, y1 = cx + 5.2 * math.cos(rad), cy + 5.2 * math.sin(rad)
        x2, y2 = cx + 62.72 * math.cos(rad), cy + 62.72 * math.sin(rad)
        ax.plot([x1, x2], [y1, y2], color='#ca8a04', lw=2.0, linestyle='--')

    # Góc lệch 36 độ
    arc_ang = Arc((cx, cy), 80, 80, angle=0, theta1=-4.5, theta2=36.0, color='#b91c1c', lw=1.4)
    ax.add_patch(arc_ang)
    ax.text(cx + 46, cy + 14, "36°", fontsize=8.5, color='#b91c1c', fontweight='bold')

    draw_dim_dia(ax, cx, cy, 62.72, 135, "Ø784 (LÒNG TRỐNG TRONG)")
    draw_dim_dia(ax, cx, cy, 5.2, -45, "Ø65 (CÂY LÁP)")

    ax.text(cx, cy - 72, "LỆCH PHA ĐỀU 36 ĐỘ QUANH CHU VI (10 CÁNH ĐỐI XỨNG)", fontsize=8.0, fontweight='bold', color='#0f172a', ha='center')

    save_drawing(fig, "BV18_CT05_Cay_Chong_Canh.png")

# ------------------------------------------------------------------------------
# 7. CHI TIẾT 06: HỆ THỐNG CÁNH ĐẢO CUỘN HẠT - BV19, BV20, BV21
# ------------------------------------------------------------------------------

def tao_BV19_CT06_Dung():
    notes = [
        "Hệ thống gồm 10 cánh đảo uốn xoắn 3D (5 cánh ngoài + 5 cánh trong).",
        "5 Cánh ngoài: La thép 70x5mm, dài 960mm, bước xoắn P=1600mm, xoắn xuôi 216 độ.",
        "5 Cánh trong: La thép 100x8mm, dài 650mm, bước xoắn P=1083.3mm, xoắn ngược 216 độ.",
        "Bề mặt cánh tiếp xúc hạt được mài nhẵn Ra 1.6 chống cấn xước hạt rang.",
        "Tạo luồng đối lưu hạt 3D: Cánh ngoài cào đẩy hạt xuôi, cánh trong hắt ngược."
    ]
    fig, ax = create_base_drawing('CT06', 'Hệ thống cánh đảo cuộn hạt', 'Hình chiếu đứng (Biên dạng dải xoắn ốc 3D)',
                                  'BV19-CT06-DUNG', 19, 21, 'Thép SS400 / Inox 304', '05 Cặp', '1:6', 'thumb_ct6.png', notes)
    cx, cy = 170, 160
    ax.plot([60, 280], [cy, cy], 'r-.', lw=0.8)

    ax.add_patch(Rectangle((90, cy - 62.72), 160, 125.44, fill=False, edgecolor='#cbd5e1', linestyle='--', lw=1.0))
    ax.add_patch(Rectangle((66, cy - 5.2), 208, 10.4, fill=False, edgecolor='#cbd5e1', lw=0.8))

    xs = np.linspace(93, 247, 100)
    for i in range(3):
        phase = i * (2 * np.pi / 5)
        ys_out = cy + 57.0 * np.sin((xs - 93) / 154.0 * (1.2 * np.pi) + phase)
        ax.plot(xs, ys_out, color='#ec4899', lw=2.2)

    xs_in = np.linspace(106, 210, 80)
    for i in range(2):
        phase = i * (2 * np.pi / 5) + np.pi / 4
        ys_in = cy + 34.0 * np.sin(-(xs_in - 106) / 104.0 * (1.2 * np.pi) + phase)
        ax.plot(xs_in, ys_in, color='#a855f7', lw=2.4, linestyle='--')

    draw_dim_h(ax, 93, 247, cy + 65, "960 (CHIỀU DÀI CÁNH NGOÀI)", offset=8)
    draw_dim_h(ax, 106, 210, cy - 65, "650 (CHIỀU DÀI CÁNH TRONG)", offset=-8)
    
    # Ghi nhãn có khung trắng chống đè vạch sóng
    ax.text(140, cy + 42, "5 CÁNH NGOÀI LA 70x5 (XOẮN XUÔI 216°)", fontsize=7.5, color='#ec4899', ha='center', fontweight='bold',
            bbox=dict(boxstyle='square,pad=0.2', facecolor='#ffffff', edgecolor='#ec4899', lw=0.8))
    ax.text(140, cy - 42, "5 CÁNH TRONG LA 100x8 (XOẮN NGƯỢC 216°)", fontsize=7.5, color='#a855f7', ha='center', fontweight='bold',
            bbox=dict(boxstyle='square,pad=0.2', facecolor='#ffffff', edgecolor='#a855f7', lw=0.8))

    save_drawing(fig, "BV19_CT06_Canh_Dao_Dung.png")

def tao_BV20_CT06_Bang():
    notes = [
        "Hình chiếu bằng biểu diễn bước xoắn P và góc uốn xoắn 216 độ (6/10 vòng).",
        "Cánh ngoài: Bước xoắn P=1600mm. Xoắn đúng 216 độ dọc theo chiều dài 960mm.",
        "Cánh trong: Bước xoắn P=1083.3mm. Xoắn ngược 216 độ dọc theo chiều dài 650mm.",
        "Gia công uốn lốc trên bộ dưỡng uốn xoắn ốc chuyên dụng.",
        "Hàn gá tiếp xúc trực tiếp vào thân 10 cây chống và thành trống."
    ]
    fig, ax = create_base_drawing('CT06', 'Hệ thống cánh đảo cuộn hạt', 'Hình chiếu bằng (Bước xoắn P & Góc xoắn 216°)',
                                  'BV20-CT06-BANG', 20, 21, 'Thép SS400 / Inox 304', '05 Cặp', '1:6', 'thumb_ct6.png', notes)
    cx, cy = 170, 160
    ax.plot([60, 280], [cy, cy], 'r-.', lw=0.8)

    ax.add_patch(Rectangle((90, cy - 62.72), 160, 125.44, fill=False, edgecolor='#cbd5e1', linestyle='--', lw=1.0))
    ax.add_patch(Rectangle((66, cy - 5.2), 208, 10.4, fill=False, edgecolor='#cbd5e1', lw=0.8))

    xs = np.linspace(93, 247, 100)
    for i in range(2):
        phase = i * (2 * np.pi / 5) + np.pi / 2
        ys_out = cy + 57.0 * np.cos((xs - 93) / 154.0 * (1.2 * np.pi) + phase)
        ax.plot(xs, ys_out, color='#ec4899', lw=2.2)

    draw_dim_h(ax, 90, 250, cy + 65, "BƯỚC XOẮN NGOÀI P = 1600 mm", offset=8)
    draw_dim_h(ax, 106, 210, cy - 65, "BƯỚC XOẮN TRONG P = 1083.3 mm", offset=-8)
    ax.text(170, cy, "GÓC XOẮN UỐN 216° (6/10 VÒNG TRÒN)", fontsize=8.0, color='#b91c1c', ha='center', fontweight='bold',
            bbox=dict(boxstyle='square,pad=0.2', facecolor='#ffffff', edgecolor='#b91c1c', lw=0.8))

    save_drawing(fig, "BV20_CT06_Canh_Dao_Bang.png")

def tao_BV21_CT06_Canh():
    notes = [
        "Hình chiếu cạnh và tiết diện làm việc bán kính của 2 hệ thống cánh đảo.",
        "Cánh ngoài: Bán kính làm việc R = 322mm -> 392mm (bản rộng 70mm, dày 5mm).",
        "Cánh trong: Bán kính làm việc R = 162mm -> 262mm (bản rộng 100mm, dày 8mm).",
        "Khoảng cách thông thủy từ cánh trong đến trục láp: 129.5mm (không kẹt hạt).",
        "Khoảng cách thông thủy giữa 2 tầng cánh: 60mm tạo khe hở đối lưu tối ưu."
    ]
    fig, ax = create_base_drawing('CT06', 'Hệ thống cánh đảo cuộn hạt', 'Hình chiếu cạnh (Biên dạng bán kính & Khe hở đối lưu)',
                                  'BV21-CT06-CANH', 21, 21, 'Thép SS400 / Inox 304', '05 Cặp', '1:6', 'thumb_ct6.png', notes)
    cx, cy = 175, 160
    draw_center_axes(ax, cx, cy, 75, 75)

    ax.add_patch(Circle((cx, cy), 62.72, fill=False, edgecolor='#94a3b8', linestyle='--', lw=1.2))
    ax.add_patch(Circle((cx, cy), 5.2, fill=True, facecolor='#cbd5e1', edgecolor='k', lw=1.2))

    # 5 Cánh ngoài
    for i in range(5):
        ang = math.radians(i * 72 + 18)
        x1, y1 = cx + 51.52 * math.cos(ang), cy + 51.52 * math.sin(ang)
        x2, y2 = cx + 62.72 * math.cos(rad if (rad := ang) else ang), cy + 62.72 * math.sin(ang)
        ax.plot([x1, x2], [y1, y2], color='#ec4899', lw=4.0)

    # 5 Cánh trong
    for i in range(5):
        ang = math.radians(i * 72 + 54)
        x1, y1 = cx + 25.92 * math.cos(ang), cy + 25.92 * math.sin(ang)
        x2, y2 = cx + 41.92 * math.cos(ang), cy + 41.92 * math.sin(ang)
        ax.plot([x1, x2], [y1, y2], color='#a855f7', lw=5.0)

    # Leader labels phân tán góc so le để tuyệt đối không đè nhau
    draw_dim_dia(ax, cx, cy, 62.72, 35, "R392 (ÁP SÁT THÀNH TRỐNG)")
    draw_dim_dia(ax, cx, cy, 51.52, 70, "R322 (CHÂN CÁNH NGOÀI)")
    draw_dim_dia(ax, cx, cy, 41.92, 115, "R262 (ĐỈNH CÁNH TRONG)")
    draw_dim_dia(ax, cx, cy, 25.92, 155, "R162 (CHÂN CÁNH TRONG)")

    save_drawing(fig, "BV21_CT06_Canh_Dao_Canh.png")

# ==============================================================================
# HÀM MAIN THỰC THI TOÀN BỘ 21 BẢN VẼ
# ==============================================================================

def main():
    print("=== BẮT ĐẦU XUẤT 21 BẢN VẼ CƠ KHÍ TRỐNG RANG (TCVN/ISO A3 - REFINED) ===")
    
    tao_BV01_TT_Dung()
    tao_BV02_TT_Bang()
    tao_BV03_TT_Canh()
    
    tao_BV04_CT01_Dung()
    tao_BV05_CT01_Bang()
    tao_BV06_CT01_Canh()
    
    tao_BV07_CT02_Dung()
    tao_BV08_CT02_Bang()
    tao_BV09_CT02_Canh()
    
    tao_BV10_CT03_Dung()
    tao_BV11_CT03_Bang()
    tao_BV12_CT03_Canh()
    
    tao_BV13_CT04_Dung()
    tao_BV14_CT04_Bang()
    tao_BV15_CT04_Canh()
    
    tao_BV16_CT05_Dung()
    tao_BV17_CT05_Bang()
    tao_BV18_CT05_Canh()
    
    tao_BV19_CT06_Dung()
    tao_BV20_CT06_Bang()
    tao_BV21_CT06_Canh()

    print("=== HOÀN TẤT XUẤT 21 BẢN VẼ CƠ KHÍ ĐẠT CHUẨN TCVN / ISO! ===")

if __name__ == '__main__':
    main()
