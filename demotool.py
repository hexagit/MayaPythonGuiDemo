# -*- coding: utf-8 -*-
# =========================== Author and Copyright. ===========================
# Author: Hiroki TAKAGAHARA(Hexadrive Inc.)
# Licence: MIT License (https://opensource.org/licenses/mit-license.php)
# =============================================================================
from __future__ import unicode_literals
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

import os
import demowindow

try:
    from PySide2.QtWidgets import QMainWindow, QApplication, QDialog
except ImportError:
    from PySide.QtGui import QMainWindow, QApplication, QDialog

# =============================================================================
CURRENT_PATH = os.path.dirname(__file__)
MAIN_UI_TITLE = 'テスト：メインウィンドウ'
MAIN_UI_FILE = os.path.join(CURRENT_PATH, 'demotool_main.ui')
SETTING_UI_TITLE = 'テスト：設定ウィンドウ'
SETTING_UI_FILE = os.path.join(CURRENT_PATH, 'demotool_setting.ui')
IMAGE_FILE = 'testimage.png'
IMAGE_PATH = os.path.join(CURRENT_PATH, IMAGE_FILE)


# =============================================================================
class TestToolMainWindow(MayaQWidgetBaseMixin, QMainWindow):

    def __init__(self, parent=None):
        super(TestToolMainWindow, self).__init__(parent)
        self.ui = demowindow.gui(self, MAIN_UI_FILE, MAIN_UI_TITLE)
        demowindow.set_imagefile(self.ui.label_image, IMAGE_PATH)
        self.set_signals()

    # =====================================
    def set_signals(self):
        # シグナルの登録
        self.ui.button.clicked.connect(self.open_sub_window)

    # =====================================
    def open_sub_window(self):
        # 設定ウィンドウを開く
        sub_gui = TestToolSettingWindow(self)
        sub_gui.show()

    # =====================================
    def apply_value(self, value):
        # 設定を適用する
        self.ui.label_result.setText(str(value))


# =============================================================================
class TestToolSettingWindow(MayaQWidgetBaseMixin, QMainWindow):
    # サブウィンドウのクラス（設定画面）

    def __init__(self, parent=None):
        super(TestToolSettingWindow, self).__init__(parent)
        self.sub_window = QDialog(parent)
        self.parent = parent
        self.ui = demowindow.gui(self.sub_window, SETTING_UI_FILE, SETTING_UI_TITLE)
        demowindow.set_imagefile(self.ui.label_image, IMAGE_PATH)
        self.set_signals()

    # =====================================
    def set_signals(self):
        # シグナルの登録
        self.ui.button.clicked.connect(self.send_value)

    # =====================================
    def send_value(self):
        # 設定を反映
        value = self.ui.lineEdit.text()
        self.parent.apply_value(value)

    # =====================================
    def show(self):
        # ウィンドウ表示
        self.sub_window.exec_()


# =============================================================================
def main():
    # メインウィンドウを起動

    QApplication.instance()
    gui = TestToolMainWindow()
    gui.show()


if __name__ == '__main__':
    main()
# =============================================================================
# EOF
# =============================================================================
