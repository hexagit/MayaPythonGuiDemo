# -*- coding: utf-8 -*-
# =========================== Author and Copyright. ===========================
# Author: Hiroki TAKAGAHARA(Hexadrive Inc.)
# Licence: MIT License (https://opensource.org/licenses/mit-license.php)
# =============================================================================
import xml.etree.ElementTree as ET

# Maya2016まで(PySide)と2017以降(PySide2)の互換性確保
try:
    from PySide2.QtWidgets import QVBoxLayout
    from PySide2.QtGui import QPixmap
    from PySide2.QtUiTools import QUiLoader
    from PySide2.QtCore import Qt
except ImportError:
    from PySide.QtGui import QPixmap, QVBoxLayout
    from PySide.QtUiTools import QUiLoader
    from PySide.QtCore import Qt


# =============================================================================
def set_imagefile(label, image_file):
    # 画像をGUIに組み込む

    w = label.width()
    h = label.height()

    image = QPixmap(image_file)
    image = image.scaled(w, h, aspectMode=Qt.KeepAspectRatio,
                         transformMode=Qt.SmoothTransformation)
    label.setPixmap(image)


# =============================================================================
def get_ui_size(ui_file):
    # uiファイルからウィンドウサイズを取得

    tree = ET.parse(ui_file)
    elem = tree.getroot()
    width  = elem.findtext(".//width")
    height = elem.findtext(".//height")
    return [int(width), int(height)]


# =============================================================================
def gui(qt, ui_file, title):
    # uiファイルのロード

    loader = QUiLoader()
    ui = loader.load(ui_file)
    size = get_ui_size(ui_file)

    try:
        qt.setCentralWidget(ui)
    except AttributeError:
        layout = QVBoxLayout()
        layout.addWidget(ui)
        qt.setLayout(layout)
        size[0] += 20
        size[1] += 20

    # ウィンドウのタイトルとサイズを設定
    qt.setWindowTitle(title)
    qt.setFixedSize(size[0], size[1])

    return ui


# =============================================================================
# EOF
# =============================================================================
