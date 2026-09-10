# -*- coding: utf-8 -*-
"""
HỆ THỐNG XUẤT 3 BẢN VẼ CƠ KHÍ KHỔ A3 TIÊU CHUẨN TCVN / ISO:
CHI TIẾT: 4 CÂY LÁP GIẰNG KHOÉT REN 2 ĐẦU CỐ ĐỊNH 2 MẶT MÁY (CT07)
MÁY RANG CÀ PHÊ CỦI 2 LỚP ĐỆM KHÍ

Bản vẽ 1: Hình chiếu đứng & Mặt cắt bổ dọc A-A toàn phần (L=1100mm, Ø30, ren trong M14x40mm)
Bản vẽ 2: Hình chiếu bằng & Sơ đồ lắp ráp liên kết 2 mặt máy (8 Bu-lông M14x40 + Long đền)
Bản vẽ 3: Hình chiếu cạnh, Chi tiết phóng to B-B lỗ ren M14 & Sơ đồ tọa độ 4 vị trí giằng

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

WORK_DIR = r"c:\VAN\CAD\ban_ve_cay_lap_giang"
ARTIFACT_DIR = r"C:\Users\admin\.gemini\antigravity\brain\0b789148-0c1a-433f-9f39-ee380f84bb46"
ARTIFACT_OUT_DIR = os.path.join(ARTIFACT_DIR, "ban_ve_cay_lap_giang")
THUMB_DIR = r"c:\VAN\CAD\thumbs_lap_giang"

os.makedirs(WORK_DIR, exist_ok=True)
os.makedirs(ARTIFACT_OUT_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Segoe UI', 'Tahoma', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False


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

    # Lưới tọa độ mép A-B-C-D / 1-6
    for i, ch in enumerate(['A', 'B', 'C', 'D']):
        y = 287 - i * (277 / 4) - (277 / 8)
        ax.text(20, y, ch, fontsize=9, fontweight='bold', color='#64748b', va='center', ha='center')
        ax.text(415, y, ch, fontsize=9, fontweight='bold', color='#64748b', va='center', ha='center')
    for j in range(6):
        x = 25 + j * (385 / 6) + (385 / 12)
        ax.text(x, 292, str(j + 1), fontsize=9, fontweight='bold', color='#64748b', va='center', ha='center')
        ax.text(x, 5, str(j + 1), fontsize=9, fontweight='bold', color='#64748b', va='center', ha='center')

    # Ký hiệu phương pháp chiếu góc thứ nhất (1st Angle Projection)
    px, py = 45, 272
    ax.plot([px - 14, px + 14], [py, py], color='#0284c7', lw=0.7, ls='-.')
    ax.plot([px, px], [py - 8, py + 8], color='#0284c7', lw=0.7, ls='-.')
    cone = Polygon([[px - 10, py - 4], [px - 10, py + 4], [px - 2, py + 7], [px - 2, py - 7]], closed=True, fill=False, edgecolor='#0f172a', lw=1.2)
    ax.add_patch(cone)
    c1 = patches.Circle((px + 7, py), 4, fill=False, edgecolor='#0f172a', lw=1.2)
    c2 = patches.Circle((px + 7, py), 7, fill=False, edgecolor='#0f172a', lw=1.2)
    ax.add_patch(c1); ax.add_patch(c2)
    ax.text(px, py - 11, 'TCVN / ISO (GÓC CHIẾU 1)', fontsize=7.5, fontweight='bold', ha='center', color='#334155')

    # Khung tên tiêu chuẩn TCVN ở góc dưới bên phải (180 x 60 mm)
    tb_w, tb_h = 180, 60
    tb_x, tb_y = 410 - tb_w, 10
    ax.add_patch(patches.Rectangle((tb_x, tb_y), tb_w, tb_h, fill=True, facecolor='#ffffff', edgecolor='#0f172a', linewidth=1.8))

    ax.plot([tb_x, tb_x + tb_w], [tb_y + 40, tb_y + 40], color='#0f172a', lw=1.2)
    ax.plot([tb_x, tb_x + tb_w], [tb_y + 20, tb_y + 20], color='#0f172a', lw=1.2)
    ax.plot([tb_x + 115, tb_x + 115], [tb_y + 20, tb_y + tb_h], color='#0f172a', lw=1.2)
    ax.plot([tb_x + 115, tb_x + tb_w], [tb_y + 50, tb_y + 50], color='#0f172a', lw=0.8)
    ax.plot([tb_x + 115, tb_x + tb_w], [tb_y + 30, tb_y + 30], color='#0f172a', lw=0.8)
    ax.plot([tb_x + 150, tb_x + 150], [tb_y + 20, tb_y + 50], color='#0f172a', lw=0.8)

    ax.plot([tb_x + 35, tb_x + 35], [tb_y, tb_y + 20], color='#0f172a', lw=0.8)
    ax.plot([tb_x + 75, tb_x + 75], [tb_y, tb_y + 20], color='#0f172a', lw=0.8)
    ax.plot([tb_x + 115, tb_x + 115], [tb_y, tb_y + 20], color='#0f172a', lw=0.8)
    ax.plot([tb_x + 150, tb_x + 150], [tb_y, tb_y + 20], color='#0f172a', lw=0.8)
    ax.plot([tb_x, tb_x + tb_w], [tb_y + 10, tb_y + 10], color='#0f172a', lw=0.8)

    # Chữ trong khung tên
    ax.text(tb_x + 57, tb_y + 53, 'MÁY RANG CÀ PHÊ CỦI 2 LỚP - 60KG', fontsize=8.5, fontweight='bold', ha='center', color='#0f172a')
    ax.text(tb_x + 57, tb_y + 44, 'CỤM KHUNG GÁ & HAI MẶT MÁY', fontsize=8.0, fontweight='bold', ha='center', color='#0369a1')
    ax.text(tb_x + 57, tb_y + 32, part_name.upper(), fontsize=10.0, fontweight='heavy', ha='center', color='#0f172a')
    ax.text(tb_x + 57, tb_y + 23, view_title.upper(), fontsize=9.0, fontweight='bold', ha='center', color='#b91c1c')

    ax.text(tb_x + 147, tb_y + 53, 'KÝ HIỆU BẢN VẼ', fontsize=7, ha='center', color='#64748b')
    ax.text(tb_x + 147, tb_y + 43, sheet_code, fontsize=10, fontweight='heavy', ha='center', color='#0f172a')
    ax.text(tb_x + 132, tb_y + 34, 'TỶ LỆ', fontsize=7, ha='center', color='#64748b')
    ax.text(tb_x + 132, tb_y + 24, scale_str, fontsize=9.5, fontweight='bold', ha='center', color='#0f172a')
    ax.text(tb_x + 165, tb_y + 34, 'TỜ SỐ', fontsize=7, ha='center', color='#64748b')
    ax.text(tb_x + 165, tb_y + 24, f'{sheet_no} / {total_sheets}', fontsize=9.5, fontweight='bold', ha='center', color='#0f172a')

    ax.text(tb_x + 17, tb_y + 13, 'THIẾT KẾ', fontsize=6.5, ha='center', color='#64748b')
    ax.text(tb_x + 17, tb_y + 4, 'Khánh Văn', fontsize=8.0, fontweight='bold', ha='center', color='#0f172a')
    ax.text(tb_x + 55, tb_y + 13, 'KIỂM DUYỆT', fontsize=6.5, ha='center', color='#64748b')
    ax.text(tb_x + 55, tb_y + 4, 'Q.LÝ', fontsize=8.0, fontweight='bold', ha='center', color='#0f172a')
    ax.text(tb_x + 95, tb_y + 13, 'VẬT LIỆU', fontsize=6.5, ha='center', color='#64748b')
    ax.text(tb_x + 95, tb_y + 4, material, fontsize=8.0, fontweight='bold', ha='center', color='#0f172a')
    ax.text(tb_x + 132, tb_y + 13, 'SỐ LƯỢNG', fontsize=6.5, ha='center', color='#64748b')
    ax.text(tb_x + 132, tb_y + 4, qty, fontsize=8.5, fontweight='bold', ha='center', color='#b91c1c')
    ax.text(tb_x + 165, tb_y + 13, 'NGÀY VẼ', fontsize=6.5, ha='center', color='#64748b')
    ax.text(tb_x + 165, tb_y + 4, '10/09/26', fontsize=8.0, fontweight='bold', ha='center', color='#0f172a')

    # Khung yêu cầu kỹ thuật bên trái khung tên
    nt_w, nt_h = 180, 52
    nt_x, nt_y = 30, 15
    ax.add_patch(patches.Rectangle((nt_x, nt_y), nt_w, nt_h, fill=True, facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.0, linestyle='--'))
    ax.text(nt_x + 8, nt_y + nt_h - 9, 'YÊU CẦU KỸ THUẬT & HƯỚNG DẪN CHẾ TẠO:', fontsize=8.5, fontweight='bold', color='#0f172a')
    for idx, note in enumerate(tech_notes):
        ax.text(nt_x + 8, nt_y + nt_h - 19 - idx * 7.5, f'{idx+1}. {note}', fontsize=7.2, color='#334155')

    # Nhúng hình ảnh 3D Isometric góc trên bên phải
    thumb_path = os.path.join(THUMB_DIR, thumb_file)
    if os.path.exists(thumb_path):
        try:
            img = mpimg.imread(thumb_path)
            im_w, im_h = 75, 55
            im_x, im_y = 330, 225
            ax.imshow(img, extent=[im_x, im_x + im_w, im_y, im_y + im_h], aspect='auto', zorder=10)
            ax.add_patch(patches.Rectangle((im_x, im_y), im_w, im_h, fill=False, edgecolor='#94a3b8', linewidth=0.8, zorder=11))
            ax.text(im_x + im_w / 2, im_y - 4, 'MÔ HÌNH PHỐI CẢNH 3D SOLID', fontsize=7.0, fontweight='bold', ha='center', color='#475569')
        except Exception:
            pass

    return fig, ax


def draw_dim_h(ax, x1, x2, y, text, offset=12, text_above=True, color='#0f172a', fontsize=8.5):
    """Vẽ đường gióng và kích thước nằm ngang."""
    y_dim = y + offset
    ax.plot([x1, x1], [y, y_dim + 3 * np.sign(offset)], color='#94a3b8', lw=0.6)
    ax.plot([x2, x2], [y, y_dim + 3 * np.sign(offset)], color='#94a3b8', lw=0.6)
    ax.annotate('', xy=(x1, y_dim), xytext=(x2, y_dim),
                arrowprops=dict(arrowstyle='<->', color=color, lw=0.9, shrinkA=0, shrinkB=0))
    ty = y_dim + (2.5 if text_above else -4.5)
    ax.text((x1 + x2)/2, ty, text, fontsize=fontsize, fontweight='bold', ha='center', va='center', color=color,
            bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='none', alpha=0.9))


def draw_dim_v(ax, y1, y2, x, text, offset=14, text_right=True, color='#0f172a', fontsize=8.5):
    """Vẽ đường gióng và kích thước thẳng đứng."""
    x_dim = x + offset
    ax.plot([x, x_dim + 3 * np.sign(offset)], [y1, y1], color='#94a3b8', lw=0.6)
    ax.plot([x, x_dim + 3 * np.sign(offset)], [y2, y2], color='#94a3b8', lw=0.6)
    ax.annotate('', xy=(x_dim, y1), xytext=(x_dim, y2),
                arrowprops=dict(arrowstyle='<->', color=color, lw=0.9, shrinkA=0, shrinkB=0))
    tx = x_dim + (3.0 if text_right else -3.0)
    ax.text(tx, (y1 + y2)/2, text, fontsize=fontsize, fontweight='bold', ha='left' if text_right else 'right',
            va='center', color=color, bbox=dict(boxstyle='square,pad=0.15', facecolor='#ffffff', edgecolor='none', alpha=0.9))


# ==============================================================================
# BẢN VẼ 01: HÌNH CHIẾU ĐỨNG / MẶT CẮT BỔ DỌC A-A TOÀN PHẦN (BV01_CT07)
# ==============================================================================
def ve_bv01_dung_cat_aa():
    tech_notes = [
        "Vật liệu: Thép tròn đặc C45 tôi cải thiện, độ cứng 24-28 HRC, chống cong võng nhịp 1.1m.",
        "Tiện khỏa 2 mặt đầu đạt phẳng vuông góc tâm trục <= 0.02mm, làm mặt tì cữ cự ly 1100.0mm (+-0.2).",
        "Khoan lỗ tâm phi 12.0mm sâu 40mm, taro ren trong M14x2.0-6H sâu hữu dụng 30mm, vát mép C1.5x45°.",
        "Độ nhám gia công: Thân trục đạt Ra 1.6 um; 2 mặt phẳng đầu tì cữ mài bóng đạt Ra 0.8 um.",
        "Xử lý bề mặt: Mạ kẽm điện phân nhúng sáng hoặc mạ crom chống ăn mòn bởi hơi nhiệt máy rang.",
        "Kiểm tra 100% bằng dưỡng ren tiêu chuẩn M14 GO/NO-GO trước khi xuất xưởng giao lắp."
    ]

    fig, ax = create_base_drawing(
        "CT07", "Cây Láp Giằng Khét Ren 2 Đầu",
        "Hình Chiếu Đứng / Mặt Cắt A-A Toàn Phần",
        "BV01_CT07", 1, 3, "Thép C45", "4 Bộ", "Tỷ lệ 1:4 (Chi tiết 1:1)",
        "thumb_lap_giang.png", tech_notes
    )

    y_center = 155.0
    r_body = 12.0
    x_left = 60.0
    x_right = 350.0

    # 1. Trục tâm đối xứng
    ax.plot([x_left - 15, x_right + 15], [y_center, y_center], color='#0284c7', lw=0.8, ls='-.')
    ax.text(x_right + 18, y_center, 'CL', fontsize=8, color='#0284c7', va='center')

    # 2. Vùng kim loại đặc được gạch mặt cắt hatching A-A
    ax.add_patch(Rectangle((x_left, y_center + 5.5), 80, r_body - 5.5, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))
    ax.add_patch(Rectangle((x_left, y_center - r_body), 80, r_body - 5.5, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))
    ax.add_patch(Rectangle((x_left + 40, y_center - r_body), 40, 2 * r_body, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))

    # Lỗ ren M14 đầu trái
    ax.plot([x_left, x_left + 2], [y_center + 7.0, y_center + 5.5], color='#0f172a', lw=1.2)
    ax.plot([x_left, x_left + 2], [y_center - 7.0, y_center - 5.5], color='#0f172a', lw=1.2)
    ax.plot([x_left + 2, x_left + 30], [y_center + 5.5, y_center + 5.5], color='#0f172a', lw=1.4)
    ax.plot([x_left + 2, x_left + 30], [y_center - 5.5, y_center - 5.5], color='#0f172a', lw=1.4)
    ax.plot([x_left, x_left + 30], [y_center + 7.0, y_center + 7.0], color='#0f172a', lw=0.7)
    ax.plot([x_left, x_left + 30], [y_center - 7.0, y_center - 7.0], color='#0f172a', lw=0.7)
    ax.plot([x_left + 30, x_left + 30], [y_center - 7.0, y_center + 7.0], color='#0f172a', lw=1.2)
    ax.plot([x_left + 30, x_left + 37], [y_center + 5.5, y_center + 5.5], color='#0f172a', lw=1.2)
    ax.plot([x_left + 30, x_left + 37], [y_center - 5.5, y_center - 5.5], color='#0f172a', lw=1.2)
    ax.plot([x_left + 37, x_left + 40], [y_center + 5.5, y_center], color='#0f172a', lw=1.2)
    ax.plot([x_left + 37, x_left + 40], [y_center - 5.5, y_center], color='#0f172a', lw=1.2)

    # Đoạn phải
    ax.add_patch(Rectangle((x_right - 80, y_center + 5.5), 80, r_body - 5.5, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))
    ax.add_patch(Rectangle((x_right - 80, y_center - r_body), 80, r_body - 5.5, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))
    ax.add_patch(Rectangle((x_right - 80, y_center - r_body), 40, 2 * r_body, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))

    # Lỗ ren M14 đầu phải
    ax.plot([x_right, x_right - 2], [y_center + 7.0, y_center + 5.5], color='#0f172a', lw=1.2)
    ax.plot([x_right, x_right - 2], [y_center - 7.0, y_center - 5.5], color='#0f172a', lw=1.2)
    ax.plot([x_right - 2, x_right - 30], [y_center + 5.5, y_center + 5.5], color='#0f172a', lw=1.4)
    ax.plot([x_right - 2, x_right - 30], [y_center - 5.5, y_center - 5.5], color='#0f172a', lw=1.4)
    ax.plot([x_right, x_right - 30], [y_center + 7.0, y_center + 7.0], color='#0f172a', lw=0.7)
    ax.plot([x_right, x_right - 30], [y_center - 7.0, y_center - 7.0], color='#0f172a', lw=0.7)
    ax.plot([x_right - 30, x_right - 30], [y_center - 7.0, y_center + 7.0], color='#0f172a', lw=1.2)
    ax.plot([x_right - 30, x_right - 37], [y_center + 5.5, y_center + 5.5], color='#0f172a', lw=1.2)
    ax.plot([x_right - 30, x_right - 37], [y_center - 5.5, y_center - 5.5], color='#0f172a', lw=1.2)
    ax.plot([x_right - 37, x_right - 40], [y_center + 5.5, y_center], color='#0f172a', lw=1.2)
    ax.plot([x_right - 37, x_right - 40], [y_center - 5.5, y_center], color='#0f172a', lw=1.2)

    # Ký hiệu gãy thu gọn đoạn giữa
    for x_b in [150, 260]:
        z_pts = [
            [x_b - 2, y_center - r_body - 3],
            [x_b + 2, y_center - 4],
            [x_b - 4, y_center],
            [x_b + 4, y_center + 4],
            [x_b - 2, y_center + r_body + 3]
        ]
        ax.plot([p[0] for p in z_pts], [p[1] for p in z_pts], color='#0f172a', lw=1.2)

    ax.add_patch(Rectangle((160, y_center - r_body), 90, 2 * r_body, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))

    # Kích thước chính
    draw_dim_h(ax, x_left, x_right, y_center + r_body, '1100.0 ±0.2 (CHIỀU DÀI CHUẨN CỮ)', offset=26, fontsize=9.5)
    draw_dim_h(ax, x_left, x_left + 30, y_center - r_body, '30 (Ren)', offset=-16, fontsize=8.0)
    draw_dim_h(ax, x_left, x_left + 40, y_center - r_body, '40 (Lỗ khoan)', offset=-28, fontsize=8.0)

    ax.annotate('M14x2.0 - 6H\nsâu 30mm\n(Lỗ khoan Ø12 sâu 40)', xy=(x_left + 15, y_center + 7.0),
                xytext=(x_left - 10, y_center + 35),
                arrowprops=dict(arrowstyle='->', color='#b91c1c', lw=1.0),
                fontsize=8.0, fontweight='bold', color='#b91c1c',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef2f2', edgecolor='#f87171'))

    ax.annotate('M14x2.0 - 6H\nsâu 30mm\nVát C1.5x45°', xy=(x_right - 15, y_center + 7.0),
                xytext=(x_right - 35, y_center + 35),
                arrowprops=dict(arrowstyle='->', color='#b91c1c', lw=1.0),
                fontsize=8.0, fontweight='bold', color='#b91c1c',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef2f2', edgecolor='#f87171'))

    draw_dim_v(ax, y_center - r_body, y_center + r_body, x_right, 'Ø30 h9 (-0.052)', offset=18, fontsize=9.0)

    ax.text(x_left - 6, y_center + 16, 'Ra 0.8', fontsize=7.5, color='#047857', fontweight='bold')
    ax.text(x_right + 4, y_center + 16, 'Ra 0.8', fontsize=7.5, color='#047857', fontweight='bold')
    ax.text(205, y_center + r_body + 4, 'Ra 1.6', fontsize=7.5, color='#047857', fontweight='bold')

    ax.text((x_left + x_right)/2, y_center + 58, 'MẶT CẮT BỔ DỌC A-A (TỶ LỆ 1:1 ĐẦU REN - THU GỌN THÂN)',
            fontsize=10.5, fontweight='heavy', ha='center', color='#0f172a',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#f1f5f9', edgecolor='#64748b'))

    out_file = os.path.join(WORK_DIR, 'BV01_CT07_Lap_Giang_Dung_Cat_AA.png')
    plt.savefig(out_file, dpi=200)
    shutil.copy(out_file, os.path.join(ARTIFACT_OUT_DIR, 'BV01_CT07_Lap_Giang_Dung_Cat_AA.png'))
    plt.close()
    print(">> Đã xuất: BV01_CT07_Lap_Giang_Dung_Cat_AA.png")


# ==============================================================================
# BẢN VẼ 02: HÌNH CHIẾU BẰNG & SƠ ĐỒ LẮP GHÉP CỤM GIẰNG (BV02_CT07)
# ==============================================================================
def ve_bv02_bang_va_lap_rap():
    tech_notes = [
        "Sơ đồ lắp ráp thể hiện 1 Cây Láp Giằng được kẹp chặt giữa Mặt Máy Trước (18mm) và Mặt Máy Sau (18mm).",
        "Hai mặt đầu của cây láp tì phẳng khít 100% vào mặt trong của 2 tấm sắt máy, tạo thành cữ cự ly 1100.0mm.",
        "8 Bu-lông lục giác M14x40mm (thép 8.8) kèm long đền vênh chống lỏng và long đền phẳng chống trầy xước.",
        "Bu-lông xuyên qua lỗ phi 15mm trên tấm sắt 18mm, cắm sâu 22mm vào ren M14 của cây láp.",
        "Lực siết bu-lông tiêu chuẩn: 95 - 105 N.m, siết đều chéo 4 góc đảm bảo 2 mặt máy song song tuyệt đối.",
        "Dung sai độ không song song giữa 2 mặt máy sau khi siết chặt không vượt quá 0.5mm trên toàn diện tích."
    ]

    fig, ax = create_base_drawing(
        "CT07", "Cây Láp Giằng Khét Ren 2 Đầu",
        "Hình Chiếu Bằng & Sơ Đồ Lắp Ráp Cụm Giằng 2 Mặt Máy",
        "BV02_CT07", 2, 3, "Thép C45 / Bu-lông 8.8", "4 Bộ", "Tỷ lệ 1:4 (Chi tiết 1:1)",
        "thumb_lap_giang_cum.png", tech_notes
    )

    y_c = 155.0
    r_body = 12.0
    x_L = 80.0
    x_R = 330.0

    ax.plot([x_L - 45, x_R + 45], [y_c, y_c], color='#0284c7', lw=0.8, ls='-.')

    # Thân cây láp ở giữa
    ax.add_patch(Rectangle((x_L, y_c - r_body), 60, 2 * r_body, facecolor='#e2e8f0', edgecolor='#0f172a', lw=1.4))
    ax.plot([x_L, x_L + 30], [y_c + 7.0, y_c + 7.0], color='#ef4444', lw=0.9, ls='--')
    ax.plot([x_L, x_L + 30], [y_c - 7.0, y_c - 7.0], color='#ef4444', lw=0.9, ls='--')
    ax.plot([x_L + 30, x_L + 30], [y_c - 7.0, y_c + 7.0], color='#ef4444', lw=0.9, ls='--')
    ax.plot([x_L, x_L + 40], [y_c + 5.5, y_c + 5.5], color='#b91c1c', lw=0.9, ls='--')
    ax.plot([x_L, x_L + 40], [y_c - 5.5, y_c - 5.5], color='#b91c1c', lw=0.9, ls='--')

    ax.add_patch(Rectangle((x_R - 60, y_c - r_body), 60, 2 * r_body, facecolor='#e2e8f0', edgecolor='#0f172a', lw=1.4))
    ax.plot([x_R, x_R - 30], [y_c + 7.0, y_c + 7.0], color='#ef4444', lw=0.9, ls='--')
    ax.plot([x_R, x_R - 30], [y_c - 7.0, y_c - 7.0], color='#ef4444', lw=0.9, ls='--')
    ax.plot([x_R - 30, x_R - 30], [y_c - 7.0, y_c + 7.0], color='#ef4444', lw=0.9, ls='--')
    ax.plot([x_R, x_R - 40], [y_c + 5.5, y_c + 5.5], color='#b91c1c', lw=0.9, ls='--')
    ax.plot([x_R, x_R - 40], [y_c - 5.5, y_c - 5.5], color='#b91c1c', lw=0.9, ls='--')

    ax.add_patch(Rectangle((160, y_c - r_body), 90, 2 * r_body, facecolor='#e2e8f0', edgecolor='#0f172a', lw=1.4))
    for x_b in [145, 265]:
        z_pts = [[x_b - 2, y_c - r_body - 3], [x_b + 2, y_c - 4], [x_b - 4, y_c], [x_b + 4, y_c + 4], [x_b - 2, y_c + r_body + 3]]
        ax.plot([p[0] for p in z_pts], [p[1] for p in z_pts], color='#0f172a', lw=1.2)

    # Mặt Máy Trước
    t_mat = 14.0
    h_mat = 65.0
    ax.add_patch(Rectangle((x_L - t_mat, y_c - h_mat/2), t_mat, h_mat, facecolor='#cbd5e1', hatch='\\\\\\', edgecolor='#0f172a', lw=1.4))
    ax.plot([x_L - t_mat, x_L], [y_c + 6.0, y_c + 6.0], color='#0f172a', lw=1.2)
    ax.plot([x_L - t_mat, x_L], [y_c - 6.0, y_c - 6.0], color='#0f172a', lw=1.2)
    ax.text(x_L - t_mat/2, y_c + h_mat/2 + 5, 'MẶT MÁY TRƯỚC\n(SẮT 18MM)', fontsize=8.0, fontweight='bold', ha='center', color='#1e293b')

    # Mặt Máy Sau
    ax.add_patch(Rectangle((x_R, y_c - h_mat/2), t_mat, h_mat, facecolor='#cbd5e1', hatch='\\\\\\', edgecolor='#0f172a', lw=1.4))
    ax.plot([x_R, x_R + t_mat], [y_c + 6.0, y_c + 6.0], color='#0f172a', lw=1.2)
    ax.plot([x_R, x_R + t_mat], [y_c - 6.0, y_c - 6.0], color='#0f172a', lw=1.2)
    ax.text(x_R + t_mat/2, y_c + h_mat/2 + 5, 'MẶT MÁY SAU\n(SẮT 18MM)', fontsize=8.0, fontweight='bold', ha='center', color='#1e293b')

    # Bu-lông đầu trái
    ax.add_patch(Rectangle((x_L - t_mat - 4.5, y_c - 11.0), 4.5, 22.0, facecolor='#f59e0b', edgecolor='#78350f', lw=1.0))
    ax.add_patch(Rectangle((x_L - t_mat - 4.5 - 9.0, y_c - 9.5), 9.0, 19.0, facecolor='#d97706', edgecolor='#78350f', lw=1.2))
    ax.plot([x_L - t_mat - 4.5, x_L + 22.0], [y_c + 5.5, y_c + 5.5], color='#78350f', lw=1.0, ls=':')
    ax.plot([x_L - t_mat - 4.5, x_L + 22.0], [y_c - 5.5, y_c - 5.5], color='#78350f', lw=1.0, ls=':')

    # Bu-lông đầu phải
    ax.add_patch(Rectangle((x_R + t_mat, y_c - 11.0), 4.5, 22.0, facecolor='#f59e0b', edgecolor='#78350f', lw=1.0))
    ax.add_patch(Rectangle((x_R + t_mat + 4.5, y_c - 9.5), 9.0, 19.0, facecolor='#d97706', edgecolor='#78350f', lw=1.2))
    ax.plot([x_R + t_mat + 4.5, x_R - 22.0], [y_c + 5.5, y_c + 5.5], color='#78350f', lw=1.0, ls=':')
    ax.plot([x_R + t_mat + 4.5, x_R - 22.0], [y_c - 5.5, y_c - 5.5], color='#78350f', lw=1.0, ls=':')

    # Kích thước
    draw_dim_h(ax, x_L, x_R, y_c + r_body, '1100.0 ±0.2 (KHOẢNG CÁCH LỌT LÒNG 2 MẶT MÁY)', offset=24, fontsize=9.5)
    draw_dim_h(ax, x_L - t_mat, x_L, y_c - h_mat/2, '18', offset=-12, fontsize=8.0)
    draw_dim_h(ax, x_R, x_R + t_mat, y_c - h_mat/2, '18', offset=-12, fontsize=8.0)
    draw_dim_h(ax, x_L - t_mat, x_R + t_mat, y_c - h_mat/2, '1136.0 (PHỦ BÌ 2 MẶT MÁY)', offset=-26, fontsize=9.0)

    # Chú thích bu-lông đặt ở góc dưới bên trái (không đè nhãn MẶT MÁY TRƯỚC ở trên)
    ax.annotate('Bu-lông lục giác M14x40mm (Cấp bền 8.8)\n+ Long đền phẳng Ø28x3 + Long đền vênh\nSiết cữ ép phẳng khít mặt đầu cây láp',
                xy=(x_L - t_mat - 4.5, y_c - 9.5), xytext=(x_L - 55, y_c - 42),
                arrowprops=dict(arrowstyle='->', color='#b45309', lw=1.0),
                fontsize=8.0, fontweight='bold', color='#78350f',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#fffbeb', edgecolor='#fcd34d'))

    ax.text((x_L + x_R)/2, y_c + 58, 'HÌNH CHIẾU BẰNG & SƠ ĐỒ LẮP GHÉP CỤM GIẰNG 2 MẶT MÁY (TỶ LỆ 1:4)',
            fontsize=10.5, fontweight='heavy', ha='center', color='#0f172a',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#f1f5f9', edgecolor='#64748b'))

    out_file = os.path.join(WORK_DIR, 'BV02_CT07_Lap_Giang_Bang.png')
    plt.savefig(out_file, dpi=200)
    shutil.copy(out_file, os.path.join(ARTIFACT_OUT_DIR, 'BV02_CT07_Lap_Giang_Bang.png'))
    plt.close()
    print(">> Đã xuất: BV02_CT07_Lap_Giang_Bang.png")


# ==============================================================================
# BẢN VẼ 03: HÌNH CHIẾU CẠNH, CHI TIẾT B-B & SƠ ĐỒ TỌA ĐỘ 4 CÂY (BV03_CT07)
# ==============================================================================
def ve_bv03_canh_va_so_do_toa_do():
    tech_notes = [
        "Sơ đồ tọa độ bố trí 4 Cây Láp Giằng trên Mặt Máy phân bố lực kéo/nén đều, chống vặn xoắn khung.",
        "2 Cây phía trên: Tọa độ X = +-315.0mm, Z = +315.0mm (Bán kính R = 445.5mm, góc nghiêng 45°).",
        "  -> Cách vỏ áo ngoài (R=415) là 30.5mm; Cách mép ngoài vòm máy (R=480) là 34.5mm; Cách phễu nạp 165mm.",
        "2 Cây phía dưới: Tọa độ X = +-400.0mm, Z = -350.0mm (Nằm trên vai chân vát dày 18mm).",
        "  -> Cách cụm gối UCP206 và máng xả 90mm; Nằm ngoài buồng đốt gạch sa mốt 50mm, vững như kiềng ba chân.",
        "4 Lỗ khoan trên Mặt Máy Trước & Sau: Khoan lỗ xuyên tâm phi 15.0mm (+0.2/0), vát mép miệng lỗ C1.0."
    ]

    fig, ax = create_base_drawing(
        "CT07", "Cây Láp Giằng Khét Ren 2 Đầu",
        "Chiếu Cạnh, Chi Tiết B-B & Sơ Đồ Tọa Độ 4 Cây",
        "BV03_CT07", 3, 3, "Thép C45 / Sắt 18mm", "4 Bộ", "Tỷ lệ 1:1 & 1:10 (Sơ đồ)",
        "thumb_lap_giang.png", tech_notes
    )

    # 1. HÌNH CHIẾU CẠNH (TỶ LỆ 1:1)
    xc1, yc1 = 80.0, 195.0
    r_outer = 15.0
    r_thread = 7.0
    r_core = 5.91

    ax.plot([xc1 - 25, xc1 + 25], [yc1, yc1], color='#0284c7', lw=0.7, ls='-.')
    ax.plot([xc1, xc1], [yc1 - 25, yc1 + 25], color='#0284c7', lw=0.7, ls='-.')

    ax.add_patch(Circle((xc1, yc1), r_outer, fill=True, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.6))
    ax.add_patch(Circle((xc1, yc1), r_thread, fill=False, edgecolor='#0f172a', lw=1.2))
    arc_thread = Arc((xc1, yc1), 2*r_core, 2*r_core, angle=0, theta1=45, theta2=315, color='#0f172a', lw=0.8)
    ax.add_patch(arc_thread)

    draw_dim_v(ax, yc1 - r_outer, yc1 + r_outer, xc1, 'Ø30 h9', offset=22, fontsize=8.5)
    ax.annotate('Ren trong M14x2.0-6H\n(Vòng chân ren hở 3/4)', xy=(xc1 + r_thread*0.7, yc1 + r_thread*0.7),
                xytext=(xc1 + 25, yc1 + 30),
                arrowprops=dict(arrowstyle='->', color='#b91c1c', lw=0.9),
                fontsize=7.8, fontweight='bold', color='#b91c1c')

    ax.text(xc1, yc1 - 28, 'HÌNH CHIẾU CẠNH\n(TỶ LỆ 1:1)', fontsize=8.5, fontweight='bold', ha='center', color='#0f172a')

    # 2. CHI TIẾT B-B PHÓNG TO 2:1
    xb2, yb2 = 80.0, 105.0
    scale_b = 1.6
    rb_body = r_outer * scale_b
    rb_th = r_thread * scale_b
    rb_core = 5.91 * scale_b
    
    ax.plot([xb2 - 15, xb2 + 45], [yb2, yb2], color='#0284c7', lw=0.7, ls='-.')
    ax.add_patch(Rectangle((xb2, yb2 + rb_th), 35, rb_body - rb_th, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))
    ax.add_patch(Rectangle((xb2, yb2 - rb_body), 35, rb_body - rb_th, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))
    ax.plot([xb2, xb2], [yb2 - rb_body, yb2 + rb_body], color='#0f172a', lw=1.6)
    ax.plot([xb2, xb2 + 3], [yb2 + rb_th + 2.4, yb2 + rb_core], color='#0f172a', lw=1.2)
    ax.plot([xb2, xb2 + 3], [yb2 - rb_th - 2.4, yb2 - rb_core], color='#0f172a', lw=1.2)
    ax.plot([xb2 + 3, xb2 + 30], [yb2 + rb_core, yb2 + rb_core], color='#0f172a', lw=1.4)
    ax.plot([xb2 + 3, xb2 + 30], [yb2 - rb_core, yb2 - rb_core], color='#0f172a', lw=1.4)
    ax.plot([xb2, xb2 + 30], [yb2 + rb_th, yb2 + rb_th], color='#0f172a', lw=0.7)
    ax.plot([xb2, xb2 + 30], [yb2 - rb_th, yb2 - rb_th], color='#0f172a', lw=0.7)
    ax.plot([xb2 + 30, xb2 + 30], [yb2 - rb_th, yb2 + rb_th], color='#0f172a', lw=1.2)
    ax.plot([xb2 + 30, xb2 + 38], [yb2 + rb_core, yb2 + rb_core], color='#0f172a', lw=1.2)
    ax.plot([xb2 + 30, xb2 + 38], [yb2 - rb_core, yb2 - rb_core], color='#0f172a', lw=1.2)
    ax.plot([xb2 + 38, xb2 + 42], [yb2 + rb_core, yb2], color='#0f172a', lw=1.2)
    ax.plot([xb2 + 38, xb2 + 42], [yb2 - rb_core, yb2], color='#0f172a', lw=1.2)

    ax.annotate('C1.5 x 45°', xy=(xb2 + 1.5, yb2 + rb_core + 2), xytext=(xb2 - 18, yb2 + rb_body + 4),
                arrowprops=dict(arrowstyle='->', color='#475569', lw=0.8), fontsize=7.5, color='#334155')
    ax.text(xb2 + 18, yb2 - rb_body - 9, 'CHI TIẾT B-B (PHÓNG TO 2:1)\nKẾT CẤU LỖ REN M14', fontsize=8.0, fontweight='bold', ha='center', color='#0f172a')

    # 3. SƠ ĐỒ TỌA ĐỘ 4 CÂY LÁP GIẰNG TRÊN MẶT MÁY (TỶ LỆ 1:10)
    xs, ys = 265.0, 162.0  # Nâng lên Y=162 để bảng tọa độ dưới cách xa khung tên
    scale_m = 0.090

    ax.plot([xs - 65, xs + 65], [ys, ys], color='#94a3b8', lw=0.6, ls='-.')
    ax.plot([xs, xs], [ys - 85, ys + 55], color='#94a3b8', lw=0.6, ls='-.')
    ax.text(xs + 58, ys - 3.5, 'X', fontsize=8, color='#64748b', va='center')
    ax.text(xs + 2.5, ys + 52, 'Z', fontsize=8, color='#64748b', ha='center')

    # Vòm và chân mặt máy
    th = np.linspace(-math.pi*0.22, math.pi*1.22, 50)
    x_arc_m = xs + 480.0 * scale_m * np.cos(th)
    y_arc_m = ys + 480.0 * scale_m * np.sin(th)
    ax.plot(x_arc_m, y_arc_m, color='#0f172a', lw=1.4)

    pts_leg = [
        [xs + 367.7 * scale_m, ys - 308.5 * scale_m],
        [xs + 550.0 * scale_m, ys - 795.0 * scale_m],
        [xs + 550.0 * scale_m, ys - 850.0 * scale_m],
        [xs - 550.0 * scale_m, ys - 850.0 * scale_m],
        [xs - 550.0 * scale_m, ys - 795.0 * scale_m],
        [xs - 367.7 * scale_m, ys - 308.5 * scale_m]
    ]
    ax.plot([p[0] for p in pts_leg], [p[1] for p in pts_leg], color='#0f172a', lw=1.4)

    # Vòng tròn vỏ áo ngoài trống Ø830mm
    c_drum = Circle((xs, ys), 415.0 * scale_m, fill=False, edgecolor='#64748b', lw=0.9, ls=':')
    ax.add_patch(c_drum)
    ax.text(xs, ys + 15.0, 'VỎ ÁO TRỐNG Ø830', fontsize=6.8, color='#64748b', ha='center',
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#ffffff', edgecolor='none', alpha=0.8))

    # 4 Vị trí cây láp
    pts_rods = [
        ('1 (Trên-Phải)', +315.0, +315.0),
        ('2 (Trên-Trái)', -315.0, +315.0),
        ('3 (Dưới-Phải)', +400.0, -350.0),
        ('4 (Dưới-Trái)', -400.0, -350.0)
    ]

    for name, xr, zr in pts_rods:
        xp = xs + xr * scale_m
        yp = ys + zr * scale_m
        ax.add_patch(Circle((xp, yp), 15.0 * scale_m, fill=True, facecolor='#ef4444', edgecolor='#b91c1c', lw=1.0, zorder=5))
        ax.plot([xp - 3, xp + 3], [yp, yp], color='#ffffff', lw=0.8, zorder=6)
        ax.plot([xp, xp], [yp - 3, yp + 3], color='#ffffff', lw=0.8, zorder=6)

    # Kích thước
    x_tL = xs - 315.0 * scale_m
    x_tR = xs + 315.0 * scale_m
    y_top = ys + 315.0 * scale_m
    draw_dim_h(ax, x_tL, x_tR, y_top, '630 (X = ±315)', offset=14, fontsize=7.5)

    x_bL = xs - 400.0 * scale_m
    x_bR = xs + 400.0 * scale_m
    y_bot = ys - 350.0 * scale_m
    draw_dim_h(ax, x_bL, x_bR, y_bot, '800 (X = ±400)', offset=-12, text_above=False, fontsize=7.5)

    draw_dim_v(ax, y_bot, y_top, x_bR, '665 (ΔZ)', offset=12, fontsize=7.5)

    ax.annotate('R 445.5\n(Góc 45°)', xy=(x_tR, y_top), xytext=(x_tR + 10, y_top + 14),
                arrowprops=dict(arrowstyle='->', color='#b91c1c', lw=0.8),
                fontsize=7.2, fontweight='bold', color='#b91c1c')

    # Bảng tọa độ nhỏ gọn đặt cao thoáng ở ys - 65
    ax.text(xs, ys - 66,
            'TỌA ĐỘ 4 CÂY LÁP GIẰNG:\n'
            '• Cây 1: X = +315, Z = +315 (R=445.5, 45°)\n'
            '• Cây 2: X = -315, Z = +315 (R=445.5, 135°)\n'
            '• Cây 3: X = +400, Z = -350 (Vai chân vát)\n'
            '• Cây 4: X = -400, Z = -350 (Vai chân vát)',
            fontsize=6.8, color='#1e293b', ha='center',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#f8fafc', edgecolor='#cbd5e1'))

    ax.text(xs, ys + 50, 'SƠ ĐỒ BỐ TRÍ TỌA ĐỘ 4 CÂY LÁP TRÊN MẶT MÁY (TỶ LỆ 1:10)',
            fontsize=9.5, fontweight='heavy', ha='center', color='#0f172a',
            bbox=dict(boxstyle='square,pad=0.25', facecolor='#f1f5f9', edgecolor='#64748b'))

    out_file = os.path.join(WORK_DIR, 'BV03_CT07_Lap_Giang_Canh.png')
    plt.savefig(out_file, dpi=200)
    shutil.copy(out_file, os.path.join(ARTIFACT_OUT_DIR, 'BV03_CT07_Lap_Giang_Canh.png'))
    plt.close()
    print(">> Đã xuất: BV03_CT07_Lap_Giang_Canh.png")


if __name__ == '__main__':
    print("=" * 70)
    print("BẮT ĐẦU XUẤT 3 BẢN VẼ CƠ KHÍ KHỔ A3: 4 CÂY LÁP GIẰNG KHOÉT REN 2 ĐẦU")
    print("=" * 70)
    ve_bv01_dung_cat_aa()
    ve_bv02_bang_va_lap_rap()
    ve_bv03_canh_va_so_do_toa_do()
    print("=" * 70)
    print("HOÀN TẤT XUẤT 3 BẢN VẼ A3 VÀ LƯU VÀO CẢ 2 THƯ MỤC!")
    print(f"1. Workspace: {WORK_DIR}")
    print(f"2. Artifacts: {ARTIFACT_OUT_DIR}")
    print("=" * 70)
