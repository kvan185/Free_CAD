# -*- coding: utf-8 -*-
"""
HỆ THỐNG XUẤT 3 BẢN VẼ CƠ KHÍ KHỔ A3 TIÊU CHUẨN TCVN / ISO:
CHI TIẾT: 4 CÂY LÁP GIẰNG M16 CỐ ĐỊNH 2 MẶT MÁY (CT07)
MÁY RANG CÀ PHÊ CỦI 2 LỚP ĐỆM KHÍ

CƠ CẤU GIA CÔNG & LẮP RÁP CẢI TIẾN HOÀN CHỈNH:
1. Bản vẽ 1: Hình chiếu đứng & Mặt cắt bổ dọc A-A toàn phần cây láp Ø16 dài 1155mm, ren ngoài 2 đầu M16.
2. Bản vẽ 2: Hình chiếu bằng & Sơ đồ cụm liên kết 2 mặt máy:
   - Mặt Máy Trước (18mm): Không khoan lỗ ra mặt tiền, 4 đai ốc M16 áp sát mặt trong và HÀN CHẾT.
   - Mặt Máy Sau (18mm): Khoan 4 lỗ Ø17.5mm xỏ cây láp qua, dùng 2 con ốc (tán kép M16) + long đền siết khóa.
3. Bản vẽ 3: Chiếu cạnh, Chi tiết B-B (hàn ốc trước), Chi tiết C-C (2 tán sau) & Sơ đồ tọa độ 4 vị trí giằng:
   - 2 Cây trên: X = ±315.0mm, Z = +315.0mm (R = 445.5mm, 45° và 135°).
   - 2 Cây dưới: X = ±345.0mm, Z = -290.0mm (Ngay chỗ cuối của đường tròn R480, góc thắt eo -40°).

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


def create_base_drawing(part_code_str, part_name, view_title, sheet_code, sheet_no, total_sheets, material, qty, scale_str, thumb_file, tech_notes, notes_box=(30, 15, 180, 52)):
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
    ax.text(tb_x + 57, tb_y + 32, part_name.upper(), fontsize=9.5, fontweight='heavy', ha='center', color='#0f172a')
    ax.text(tb_x + 57, tb_y + 23, view_title.upper(), fontsize=8.5, fontweight='bold', ha='center', color='#b91c1c')

    ax.text(tb_x + 147, tb_y + 53, 'KÝ HIỆU BẢN VẼ', fontsize=7, ha='center', color='#64748b')
    ax.text(tb_x + 147, tb_y + 43, sheet_code, fontsize=10, fontweight='heavy', ha='center', color='#0f172a')
    ax.text(tb_x + 132, tb_y + 34, 'TỶ LỆ', fontsize=7, ha='center', color='#64748b')
    ax.text(tb_x + 132, tb_y + 24, scale_str, fontsize=9.0, fontweight='bold', ha='center', color='#0f172a')
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
    nt_x, nt_y, nt_w, nt_h = notes_box
    ax.add_patch(patches.Rectangle((nt_x, nt_y), nt_w, nt_h, fill=True, facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.0, linestyle='--'))
    ax.text(nt_x + 8, nt_y + nt_h - 7.5, 'YÊU CẦU KỸ THUẬT & QUY TRÌNH LẮP RÁP:', fontsize=8.0, fontweight='bold', color='#0f172a')
    step_y = (nt_h - 13.0) / max(len(tech_notes), 1)
    for idx, note in enumerate(tech_notes):
        ax.text(nt_x + 8, nt_y + nt_h - 13.5 - idx * step_y, f'{idx+1}. {note}', fontsize=6.8, color='#334155')

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
        "Vật liệu: Thép tròn đặc C45 kéo nguội, tôi cải thiện 24-28 HRC, chống cong võng nhịp 1.15m.",
        "Tiện 2 đầu ren ngoài M16x2.0-6g: Đầu trước ren dài 30mm, đầu sau ren dài 60mm; Vát mép C1.5x45°.",
        "Độ thẳng toàn thân trục <= 0.3mm/m; Độ đồng tâm giữa đường kính ren và thân trục <= 0.05mm.",
        "Độ nhám gia công: Thân trục tiện láng đạt Ra 1.6 um; Mặt ren ngoài đạt Ra 1.6 um; Vát mép Ra 0.8 um.",
        "Xử lý bề mặt: Mạ kẽm điện phân nhúng sáng hoặc mạ crom chống ăn mòn bởi hơi nhiệt máy rang.",
        "Kiểm tra 100% bằng dưỡng vòng ren tiêu chuẩn M16x2.0 6g GO/NO-GO trước khi xuất xưởng giao lắp."
    ]

    fig, ax = create_base_drawing(
        "CT07", "Cây Láp Giằng Tiện Ren 2 Đầu",
        "Hình Chiếu Đứng / Mặt Cắt A-A Toàn Phần",
        "BV01_CT07", 1, 3, "Thép C45", "4 Cây", "Tỷ lệ 1:4 (Chi tiết 1:1)",
        "thumb_lap_giang.png", tech_notes
    )

    y_center = 160.0
    r_body = 8.0     # Phi 16mm -> r = 8mm
    r_core = 6.91    # Chân ren M16x2.0 (d3 = 13.83mm -> r = 6.91mm)
    x_left = 65.0
    x_right = 345.0

    # 1. Trục tâm đối xứng
    ax.plot([x_left - 15, x_right + 15], [y_center, y_center], color='#0284c7', lw=0.8, ls='-.')

    # Đoạn ren đầu trước (Trái: dài 30mm biểu diễn tương đương 28mm)
    w_th_f = 28.0
    # Thân ren trái
    ax.add_patch(Rectangle((x_left, y_center - r_body), w_th_f, 2 * r_body, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))
    # Đường chân ren hở (nét mảnh)
    ax.plot([x_left, x_left + w_th_f], [y_center + r_core, y_center + r_core], color='#0f172a', lw=0.7)
    ax.plot([x_left, x_left + w_th_f], [y_center - r_core, y_center - r_core], color='#0f172a', lw=0.7)
    # Đường ranh giới ren
    ax.plot([x_left + w_th_f, x_left + w_th_f], [y_center - r_body, y_center + r_body], color='#0f172a', lw=1.4)
    # Vát mép đầu trái
    ax.plot([x_left, x_left + 2.0], [y_center + r_body - 1.5, y_center + r_body], color='#0f172a', lw=1.2)
    ax.plot([x_left, x_left + 2.0], [y_center - r_body + 1.5, y_center - r_body], color='#0f172a', lw=1.2)

    # Đoạn thân trơn bên trái
    ax.add_patch(Rectangle((x_left + w_th_f, y_center - r_body), 55, 2 * r_body, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))

    # Đoạn thân trơn bên phải
    w_th_r = 50.0
    ax.add_patch(Rectangle((x_right - w_th_r - 55, y_center - r_body), 55, 2 * r_body, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))

    # Đoạn ren đầu sau (Phải: dài 60mm biểu diễn tương đương 50mm)
    ax.add_patch(Rectangle((x_right - w_th_r, y_center - r_body), w_th_r, 2 * r_body, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))
    ax.plot([x_right - w_th_r, x_right], [y_center + r_core, y_center + r_core], color='#0f172a', lw=0.7)
    ax.plot([x_right - w_th_r, x_right], [y_center - r_core, y_center - r_core], color='#0f172a', lw=0.7)
    ax.plot([x_right - w_th_r, x_right - w_th_r], [y_center - r_body, y_center + r_body], color='#0f172a', lw=1.4)
    # Vát mép đầu phải
    ax.plot([x_right, x_right - 2.0], [y_center + r_body - 1.5, y_center + r_body], color='#0f172a', lw=1.2)
    ax.plot([x_right, x_right - 2.0], [y_center - r_body + 1.5, y_center - r_body], color='#0f172a', lw=1.2)

    # Ký hiệu gãy thu gọn đoạn giữa
    for x_b in [155, 235]:
        z_pts = [
            [x_b - 2, y_center - r_body - 3],
            [x_b + 2, y_center - 3],
            [x_b - 3, y_center],
            [x_b + 3, y_center + 3],
            [x_b - 2, y_center + r_body + 3]
        ]
        ax.plot([p[0] for p in z_pts], [p[1] for p in z_pts], color='#0f172a', lw=1.2)

    ax.add_patch(Rectangle((165, y_center - r_body), 60, 2 * r_body, facecolor='#f8fafc', hatch='///', edgecolor='#0f172a', lw=1.2))

    # Kích thước chính
    draw_dim_h(ax, x_left, x_right, y_center + r_body, '1155.0 ±0.5 (TỔNG CHIỀU DÀI CÂY LÁP GIẰNG)', offset=28, fontsize=9.5)
    draw_dim_h(ax, x_left, x_right - 37, y_center + r_body, '1118.0 (ĐẦU TRƯỚC ĐẾN MẶT NGOÀI MẶT SAU)', offset=16, fontsize=8.0)
    draw_dim_h(ax, x_left, x_left + w_th_f, y_center - r_body, '30 (Ren trước)', offset=-16, fontsize=8.0)
    draw_dim_h(ax, x_right - w_th_r, x_right, y_center - r_body, '60 (Ren sau)', offset=-16, fontsize=8.0)

    ax.annotate('Ren ngoài M16x2.0 - 6g\nDài 30mm (Vặn ốc hàn)\nVát mép C1.5x45°', xy=(x_left + 14, y_center + r_body),
                xytext=(x_left - 15, y_center + 42),
                arrowprops=dict(arrowstyle='->', color='#b91c1c', lw=1.0),
                fontsize=8.0, fontweight='bold', color='#b91c1c',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef2f2', edgecolor='#f87171'))

    ax.annotate('Ren ngoài M16x2.0 - 6g\nDài 60mm (Xỏ mặt sau & 2 tán)\nVát mép C1.5x45°', xy=(x_right - 25, y_center + r_body),
                xytext=(x_right - 60, y_center + 42),
                arrowprops=dict(arrowstyle='->', color='#b91c1c', lw=1.0),
                fontsize=8.0, fontweight='bold', color='#b91c1c',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef2f2', edgecolor='#f87171'))

    draw_dim_v(ax, y_center - r_body, y_center + r_body, x_right, 'Ø16 h9 (-0.043)', offset=18, fontsize=9.0)

    ax.text(x_left + 5, y_center - r_body - 28, 'Ra 1.6', fontsize=7.5, color='#047857', fontweight='bold')
    ax.text(x_right - 25, y_center - r_body - 28, 'Ra 1.6', fontsize=7.5, color='#047857', fontweight='bold')
    ax.text(195, y_center + r_body + 4, 'Ra 1.6', fontsize=7.5, color='#047857', fontweight='bold')

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
        "Sơ đồ mô tả quy trình lắp ráp: Đút cây láp Ø16 từ lỗ Ø17.5mm ở Mặt Máy Sau tiến vào lòng máy.",
        "Tại đầu trước: Vặn 1 con đai ốc M16 vào cây láp, áp sát mặt trong Mặt Máy Trước và HÀN DÍNH CHẾT.",
        "Mặt Máy Trước (18mm) tuyệt đối KHÔNG KHOAN LỖ ra mặt tiền, giữ bề mặt phẳng đặc nguyên khối thẩm mỹ.",
        "Tại Mặt Máy Sau: Lỗ khoan thông Ø17.5mm (+0.3/0), lắp 1 long đền phẳng Ø32x3mm mạ kẽm.",
        "Phía sau dùng 2 CON ỐC M16 (TÁN KÉP / Double Jam Nuts) siết chặt kéo căng và khóa ren chống rung.",
        "Đai ốc 1 siết mô-men 90 N.m; Đai ốc 2 vặn siết hãm khóa chặt ngược chiều triệt tiêu độ rơ lỏng."
    ]

    fig, ax = create_base_drawing(
        "CT07", "Cây Láp Giằng Tiện Ren 2 Đầu",
        "Hình Chiếu Bằng & Sơ Đồ Cụm Liên Kết 2 Mặt Máy",
        "BV02_CT07", 2, 3, "Thép C45 / Sắt 18mm", "4 Bộ", "Tỷ lệ 1:4 (Chi tiết 1:1)",
        "thumb_lap_giang_cum.png", tech_notes
    )

    y_c = 158.0
    r_body = 8.0
    x_L = 95.0      # Mặt trong Mặt Máy Trước
    x_R = 305.0     # Mặt trong Mặt Máy Sau
    t_mat = 18.0    # Chiều dày tấm sắt 18mm
    h_mat = 75.0    # Chiều cao thể hiện mặt máy

    ax.plot([x_L - 35, x_R + 65], [y_c, y_c], color='#0284c7', lw=0.8, ls='-.')

    # 1. Thân cây láp ở giữa (từ x_L đến x_R, có thu gọn)
    ax.add_patch(Rectangle((x_L, y_c - r_body), 55, 2 * r_body, facecolor='#e2e8f0', edgecolor='#0f172a', lw=1.4))
    ax.add_patch(Rectangle((x_R - 55, y_c - r_body), 55, 2 * r_body, facecolor='#e2e8f0', edgecolor='#0f172a', lw=1.4))
    ax.add_patch(Rectangle((160, y_c - r_body), 80, 2 * r_body, facecolor='#e2e8f0', edgecolor='#0f172a', lw=1.4))

    for x_b in [150, 245]:
        z_pts = [[x_b - 2, y_c - r_body - 3], [x_b + 2, y_c - 3], [x_b - 3, y_c], [x_b + 3, y_c + 3], [x_b - 2, y_c + r_body + 3]]
        ax.plot([p[0] for p in z_pts], [p[1] for p in z_pts], color='#0f172a', lw=1.2)

    # 2. MẶT MÁY TRƯỚC (18mm, KHÔNG KHOÉT LỖ)
    ax.add_patch(Rectangle((x_L - t_mat, y_c - h_mat/2), t_mat, h_mat, facecolor='#cbd5e1', hatch='\\\\\\', edgecolor='#0f172a', lw=1.4))
    ax.text(x_L - t_mat/2, y_c + h_mat/2 + 5, 'MẶT MÁY TRƯỚC (18MM)\n(Phẳng đặc - Không khoét lỗ)', fontsize=8.0, fontweight='bold', ha='center', color='#1e293b')

    # Đai ốc M16 hàn áp sát mặt trong tại x_L (dày 13mm, cao 24mm)
    h_nut_draw = 13.0
    s_nut_draw = 24.0
    ax.add_patch(Rectangle((x_L, y_c - s_nut_draw/2), h_nut_draw, s_nut_draw, facecolor='#f59e0b', edgecolor='#78350f', lw=1.2))
    # Đường ren cắm vào đai ốc
    ax.plot([x_L, x_L + h_nut_draw], [y_c + r_body, y_c + r_body], color='#0f172a', lw=1.0)
    ax.plot([x_L, x_L + h_nut_draw], [y_c - r_body, y_c - r_body], color='#0f172a', lw=1.0)

    # Mối hàn góc chu vi đai ốc vào tấm sắt mặt trước
    poly_weld_top = Polygon([[x_L, y_c + s_nut_draw/2], [x_L + 3.5, y_c + s_nut_draw/2], [x_L, y_c + s_nut_draw/2 + 3.5]], closed=True, facecolor='#0284c7', edgecolor='#0f172a', lw=0.8)
    poly_weld_bot = Polygon([[x_L, y_c - s_nut_draw/2], [x_L + 3.5, y_c - s_nut_draw/2], [x_L, y_c - s_nut_draw/2 - 3.5]], closed=True, facecolor='#0284c7', edgecolor='#0f172a', lw=0.8)
    ax.add_patch(poly_weld_top); ax.add_patch(poly_weld_bot)

    # Ký hiệu mối hàn góc chu vi TCVN
    ax.annotate('Mối hàn chu vi\nđai ốc vào mặt máy\n(Góc a = 3mm)', xy=(x_L + 1.5, y_c + s_nut_draw/2 + 1.5),
                xytext=(x_L - 50, y_c + 32),
                arrowprops=dict(arrowstyle='->', color='#0284c7', lw=1.0),
                fontsize=7.8, fontweight='bold', color='#0369a1',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f9ff', edgecolor='#7dd3fc'))

    # 3. MẶT MÁY SAU (18mm, CÓ LỖ KHOAN THÔNG Ø17.5mm)
    ax.add_patch(Rectangle((x_R, y_c - h_mat/2), t_mat, h_mat, facecolor='#cbd5e1', hatch='\\\\\\', edgecolor='#0f172a', lw=1.4))
    # Lỗ khoan Ø17.5 (khe hở trên dưới đối với thân Ø16)
    r_hole = 8.75
    ax.plot([x_R, x_R + t_mat], [y_c + r_hole, y_c + r_hole], color='#ef4444', lw=1.0, ls='--')
    ax.plot([x_R, x_R + t_mat], [y_c - r_hole, y_c - r_hole], color='#ef4444', lw=1.0, ls='--')
    # Thân cây láp chạy xuyên qua lỗ
    ax.plot([x_R, x_R + t_mat], [y_c + r_body, y_c + r_body], color='#0f172a', lw=1.2)
    ax.plot([x_R, x_R + t_mat], [y_c - r_body, y_c - r_body], color='#0f172a', lw=1.2)
    ax.text(x_R + t_mat/2, y_c + h_mat/2 + 5, 'MẶT MÁY SAU (18MM)\n(Khoan lỗ thông Ø17.5)', fontsize=8.0, fontweight='bold', ha='center', color='#1e293b')

    # 4. CỤM BẮT ỐC PHÍA NGOÀI MẶT MÁY SAU (x_R + t_mat trở ra)
    x_out = x_R + t_mat  # 323.0
    # Long đền phẳng Ø32x3mm
    t_washer = 3.5
    d_washer = 32.0
    ax.add_patch(Rectangle((x_out, y_c - d_washer/2), t_washer, d_washer, facecolor='#94a3b8', edgecolor='#334155', lw=1.0))

    # Tán chính M16 (dày 13mm)
    ax.add_patch(Rectangle((x_out + t_washer, y_c - s_nut_draw/2), h_nut_draw, s_nut_draw, facecolor='#f59e0b', edgecolor='#78350f', lw=1.2))
    # Tán hãm M16 (dày 13mm)
    ax.add_patch(Rectangle((x_out + t_washer + h_nut_draw, y_c - s_nut_draw/2), h_nut_draw, s_nut_draw, facecolor='#d97706', edgecolor='#78350f', lw=1.2))

    # Đuôi cây láp thò ra ngoài 8mm vát mép
    x_tail = x_out + t_washer + 2 * h_nut_draw
    ax.add_patch(Rectangle((x_tail, y_c - r_body), 8.0, 2 * r_body, facecolor='#e2e8f0', edgecolor='#0f172a', lw=1.2))
    ax.plot([x_tail + 8.0, x_tail + 6.5], [y_c + r_body - 1.5, y_c + r_body], color='#0f172a', lw=1.0)
    ax.plot([x_tail + 8.0, x_tail + 6.5], [y_c - r_body + 1.5, y_c - r_body], color='#0f172a', lw=1.0)

    # Kích thước
    draw_dim_h(ax, x_L, x_R, y_c + r_body, '1100.0 ±0.2 (KHOẢNG CÁCH LỌT LÒNG 2 MẶT MÁY)', offset=26, fontsize=9.5)
    draw_dim_h(ax, x_L - t_mat, x_L, y_c - h_mat/2, '18', offset=-12, fontsize=8.0)
    draw_dim_h(ax, x_R, x_R + t_mat, y_c - h_mat/2, '18', offset=-12, fontsize=8.0)
    draw_dim_h(ax, x_L - t_mat, x_R + t_mat, y_c - h_mat/2, '1136.0 (PHỦ BÌ 2 MẶT MÁY)', offset=-26, fontsize=9.0)
    draw_dim_h(ax, x_L, x_tail + 8.0, y_c - h_mat/2, '1155.0 (CHIỀU DÀI LÁP)', offset=-40, fontsize=9.0)

    # Chú thích tán kép đặt ở GÓC TRÊN BÊN PHẢI (không đè kích thước 18 ở dưới)
    ax.annotate('2 CON ỐC M16 (TÁN KÉP CHỐNG RUNG)\n+ 1 Long đền phẳng Ø32x3mm\nSiết kéo căng và khóa chặt Mặt Máy Sau',
                xy=(x_out + t_washer + h_nut_draw, y_c + s_nut_draw/2), xytext=(x_out + 12, y_c + 38),
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
# BẢN VẼ 03: HÌNH CHIẾU CẠNH, CHI TIẾT B-B, C-C & SƠ ĐỒ TỌA ĐỘ 4 CÂY (BV03_CT07)
# ==============================================================================
def ve_bv03_canh_va_so_do_toa_do():
    tech_notes = [
        "Sơ đồ tọa độ bố trí 4 Cây Láp Giằng phân bổ lực kéo/nén đều, chống vặn xoắn khung máy.",
        "2 Cây phía trên: Tọa độ X = ±315.0mm, Z = +315.0mm (Bán kính R = 445.5mm, góc 45° và 135°).",
        "2 Cây phía dưới: Tọa độ X = ±345.0mm, Z = -290.0mm (Đúng ngay chỗ cuối của đường tròn R480).",
        "Khoảng hở an toàn cây dưới: Cách vỏ trống (R=415) là 27.7mm; Cách mép ngoài tấm sắt: 29.3mm.",
        "Mặt Máy Trước: Giữ phẳng đặc, hàn 4 đai ốc M16 áp sát mặt trong tại 4 tọa độ trên.",
        "Mặt Máy Sau: Khoan 4 lỗ thông xuyên tâm Ø17.5mm (+0.3/0) tại 4 tọa độ tương ứng."
    ]

    fig, ax = create_base_drawing(
        "CT07", "Cây Láp Giằng Tiện Ren 2 Đầu",
        "Chiếu Cạnh, Chi Tiết Hàn & Sơ Đồ Tọa Độ 4 Cây",
        "BV03_CT07", 3, 3, "Thép C45 / Sắt 18mm", "4 Bộ", "Tỷ lệ 1:1 & 1:10 (Sơ đồ)",
        "thumb_lap_giang_cum.png", tech_notes,
        notes_box=(30, 12, 175, 46)
    )

    # 1. HÌNH CHIẾU CẠNH (TỶ LỆ 1:1)
    xc1, yc1 = 70.0, 238.0
    r_outer = 8.0    # Ø16
    r_thread = 8.0   # Đường kính đỉnh ren
    r_core = 6.91    # Đường kính chân ren

    ax.plot([xc1 - 18, xc1 + 18], [yc1, yc1], color='#0284c7', lw=0.7, ls='-.')
    ax.plot([xc1, xc1], [yc1 - 18, yc1 + 18], color='#0284c7', lw=0.7, ls='-.')

    ax.add_patch(Circle((xc1, yc1), r_outer, fill=True, facecolor='#f8fafc', edgecolor='#0f172a', lw=1.6))
    arc_thread = Arc((xc1, yc1), 2*r_core, 2*r_core, angle=0, theta1=45, theta2=315, color='#0f172a', lw=0.9)
    ax.add_patch(arc_thread)

    draw_dim_v(ax, yc1 - r_outer, yc1 + r_outer, xc1, 'Ø16 h9', offset=16, fontsize=8.0)
    ax.annotate('Ren ngoài M16x2.0-6g\n(Vòng chân ren hở 1/4)', xy=(xc1 + r_core*0.7, yc1 + r_core*0.7),
                xytext=(xc1 + 18, yc1 + 18),
                arrowprops=dict(arrowstyle='->', color='#b91c1c', lw=0.8),
                fontsize=7.2, fontweight='bold', color='#b91c1c')

    ax.text(xc1, yc1 - 18, 'HÌNH CHIẾU CẠNH (TỶ LỆ 1:1)', fontsize=8.0, fontweight='bold', ha='center', color='#0f172a')

    # 2. CHI TIẾT B-B (PHÓNG TO 2:1): MỐI GHÉP HÀN ĐAI ỐC MẶT MÁY TRƯỚC
    xb2, yb2 = 70.0, 166.0
    t_mat_b = 16.0
    h_mat_b = 36.0
    
    # Mặt máy trước không lỗ
    ax.add_patch(Rectangle((xb2 - t_mat_b, yb2 - h_mat_b/2), t_mat_b, h_mat_b, facecolor='#cbd5e1', hatch='\\\\\\', edgecolor='#0f172a', lw=1.2))
    # Đai ốc M16 (phóng to)
    w_nut_b = 15.0
    h_nut_b = 26.0
    ax.add_patch(Rectangle((xb2, yb2 - h_nut_b/2), w_nut_b, h_nut_b, facecolor='#f59e0b', edgecolor='#78350f', lw=1.2))
    # Mối hàn góc
    ax.add_patch(Polygon([[xb2, yb2 + h_nut_b/2], [xb2 + 4, yb2 + h_nut_b/2], [xb2, yb2 + h_nut_b/2 + 4]], closed=True, facecolor='#0284c7', edgecolor='#0f172a', lw=0.8))
    ax.add_patch(Polygon([[xb2, yb2 - h_nut_b/2], [xb2 + 4, yb2 - h_nut_b/2], [xb2, yb2 - h_nut_b/2 - 4]], closed=True, facecolor='#0284c7', edgecolor='#0f172a', lw=0.8))
    # Cây láp vặn vào
    ax.add_patch(Rectangle((xb2, yb2 - 8), 30, 16, facecolor='#e2e8f0', edgecolor='#0f172a', lw=1.1))

    ax.annotate('Mặt trước phẳng đặc\nKhông khoét lỗ', xy=(xb2 - t_mat_b/2, yb2 + h_mat_b/2),
                xytext=(xb2 - 42, yb2 + h_mat_b/2 + 6),
                arrowprops=dict(arrowstyle='->', color='#1e293b', lw=0.8),
                fontsize=6.8, fontweight='bold', color='#1e293b')

    ax.annotate('Mối hàn góc a=3\nĐai ốc M16 hàn chết', xy=(xb2 + 2, yb2 + h_nut_b/2 + 2),
                xytext=(xb2 + 12, yb2 + h_nut_b/2 + 8),
                arrowprops=dict(arrowstyle='->', color='#0284c7', lw=0.8),
                fontsize=6.8, fontweight='bold', color='#0369a1')

    ax.text(xb2 + 6, yb2 - h_mat_b/2 - 4, 'CHI TIẾT B-B (PHÓNG TO 2:1)\nMỐI GHÉP HÀN ĐAI ỐC MẶT TRƯỚC', fontsize=7.5, fontweight='bold', ha='center', va='top', color='#0f172a')

    # 3. CHI TIẾT C-C (PHÓNG TO 2:1): MỐI GHÉP 2 TÁN KÉP MẶT MÁY SAU
    xb3, yb3 = 70.0, 98.0
    ax.add_patch(Rectangle((xb3 - t_mat_b, yb3 - h_mat_b/2), t_mat_b, h_mat_b, facecolor='#cbd5e1', hatch='\\\\\\', edgecolor='#0f172a', lw=1.2))
    # Lỗ khoan Ø17.5
    ax.plot([xb3 - t_mat_b, xb3], [yb3 + 9, yb3 + 9], color='#ef4444', lw=0.8, ls='--')
    ax.plot([xb3 - t_mat_b, xb3], [yb3 - 9, yb3 - 9], color='#ef4444', lw=0.8, ls='--')
    # Cây láp chạy qua
    ax.add_patch(Rectangle((xb3 - t_mat_b - 10, yb3 - 8), t_mat_b + 42, 16, facecolor='#e2e8f0', edgecolor='#0f172a', lw=1.1))
    # Long đền
    ax.add_patch(Rectangle((xb3, yb3 - 15), 3.5, 30, facecolor='#94a3b8', edgecolor='#334155', lw=0.9))
    # Tán 1
    ax.add_patch(Rectangle((xb3 + 3.5, yb3 - h_nut_b/2), 12, h_nut_b, facecolor='#f59e0b', edgecolor='#78350f', lw=1.1))
    # Tán 2
    ax.add_patch(Rectangle((xb3 + 15.5, yb3 - h_nut_b/2), 12, h_nut_b, facecolor='#d97706', edgecolor='#78350f', lw=1.1))

    ax.annotate('Lỗ thông Ø17.5mm\nCây láp xỏ qua', xy=(xb3 - t_mat_b/2, yb3 + 9),
                xytext=(xb3 - 42, yb3 + 16),
                arrowprops=dict(arrowstyle='->', color='#ef4444', lw=0.8),
                fontsize=6.8, fontweight='bold', color='#b91c1c')

    ax.annotate('2 Đai ốc M16 siết khóa\n(Tán kép chống rung)', xy=(xb3 + 21, yb3 + h_nut_b/2),
                xytext=(xb3 + 12, yb3 + h_nut_b/2 + 6),
                arrowprops=dict(arrowstyle='->', color='#78350f', lw=0.8),
                fontsize=6.8, fontweight='bold', color='#78350f')

    ax.text(xb3 + 6, yb3 - h_mat_b/2 - 4, 'CHI TIẾT C-C (PHÓNG TO 2:1)\nMỐI GHÉP 2 TÁN KÉP MẶT SAU', fontsize=7.5, fontweight='bold', ha='center', va='top', color='#0f172a')

    # 4. SƠ ĐỒ TỌA ĐỘ 4 CÂY LÁP GIẰNG TRÊN MẶT MÁY (TỶ LỆ 1:10)
    xs, ys = 265.0, 168.0
    scale_m = 0.090

    ax.plot([xs - 65, xs + 65], [ys, ys], color='#94a3b8', lw=0.6, ls='-.')
    ax.plot([xs, xs], [ys - 85, ys + 55], color='#94a3b8', lw=0.6, ls='-.')
    ax.text(xs + 65, ys - 4.0, 'X', fontsize=8, color='#64748b', va='center')
    ax.text(xs + 2.5, ys + 52, 'Z', fontsize=8, color='#64748b', ha='center')

    # Vòm và chân mặt máy: Vòm tròn R=480mm từ theta = -40° đến 220°
    th = np.linspace(-math.pi*0.222, math.pi*1.222, 60)
    x_arc_m = xs + 480.0 * scale_m * np.cos(th)
    y_arc_m = ys + 480.0 * scale_m * np.sin(th)
    ax.plot(x_arc_m, y_arc_m, color='#0f172a', lw=1.4)

    # Chân vát từ eo thắt (X = ±367.7, Z = -308.5)
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

    # 4 Vị trí cây láp M16 MỚI:
    # 2 cây trên: (±315, +315)
    # 2 cây dưới: (±345, -290) - NGAY CHỖ CUỐI ĐƯỜNG TRÒN
    pts_rods = [
        ('1 (Trên-Phải)', +315.0, +315.0),
        ('2 (Trên-Trái)', -315.0, +315.0),
        ('3 (Dưới-Phải)', +345.0, -290.0),
        ('4 (Dưới-Trái)', -345.0, -290.0)
    ]

    for name, xr, zr in pts_rods:
        xp = xs + xr * scale_m
        yp = ys + zr * scale_m
        ax.add_patch(Circle((xp, yp), 12.0 * scale_m, fill=True, facecolor='#ef4444', edgecolor='#b91c1c', lw=1.0, zorder=5))
        ax.plot([xp - 2.5, xp + 2.5], [yp, yp], color='#ffffff', lw=0.8, zorder=6)
        ax.plot([xp, xp], [yp - 2.5, yp + 2.5], color='#ffffff', lw=0.8, zorder=6)

    # Kích thước
    x_tL = xs - 315.0 * scale_m
    x_tR = xs + 315.0 * scale_m
    y_top = ys + 315.0 * scale_m
    draw_dim_h(ax, x_tL, x_tR, y_top, '630 (X = ±315)', offset=14, fontsize=7.5)

    x_bL = xs - 345.0 * scale_m
    x_bR = xs + 345.0 * scale_m
    y_bot = ys - 290.0 * scale_m
    draw_dim_h(ax, x_bL, x_bR, y_bot, '690 (X = ±345)', offset=-12, text_above=False, fontsize=7.5)

    draw_dim_v(ax, y_bot, y_top, x_bR, '605 (ΔZ)', offset=18, fontsize=7.5)

    ax.annotate('R 445.5 (45°)', xy=(x_tR, y_top), xytext=(x_tR + 10, y_top + 12),
                arrowprops=dict(arrowstyle='->', color='#b91c1c', lw=0.8),
                fontsize=7.2, fontweight='bold', color='#b91c1c')

    ax.annotate('CUỐI ĐƯỜNG TRÒN\n(Góc thắt eo -40°)', xy=(x_bR, y_bot), xytext=(x_bR + 10, y_bot - 12),
                arrowprops=dict(arrowstyle='->', color='#b91c1c', lw=0.8),
                fontsize=7.2, fontweight='bold', color='#b91c1c')

    # Bảng tọa độ nhỏ gọn đặt cao thoáng ở ys - 64
    ax.text(xs, ys - 65,
            'TỌA ĐỘ 4 CÂY LÁP GIẰNG M16:\n'
            '• Cây 1: X = +315, Z = +315 (R=445.5, 45°)\n'
            '• Cây 2: X = -315, Z = +315 (R=445.5, 135°)\n'
            '• Cây 3: X = +345, Z = -290 (Cuối đường tròn -40°)\n'
            '• Cây 4: X = -345, Z = -290 (Cuối đường tròn -40°)',
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
    print("BẮT ĐẦU XUẤT 3 BẢN VẼ CƠ KHÍ KHỔ A3: 4 CÂY LÁP GIẰNG M16 CẢI TIẾN")
    print("=" * 70)
    ve_bv01_dung_cat_aa()
    ve_bv02_bang_va_lap_rap()
    ve_bv03_canh_va_so_do_toa_do()
    print("=" * 70)
    print("HOÀN TẤT XUẤT 3 BẢN VẼ A3 VÀ LƯU VÀO CẢ 2 THƯ MỤC!")
    print(f"1. Workspace: {WORK_DIR}")
    print(f"2. Artifacts: {ARTIFACT_OUT_DIR}")
    print("=" * 70)
