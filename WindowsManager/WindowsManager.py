from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, QLineEdit,QMainWindow,QListWidget,QListWidgetItem, QPushButton, QScrollArea, QSpinBox,QTreeWidget,QMenu,QTreeWidgetItem, QMessageBox, QVBoxLayout,QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor,QAction,QIcon,QPixmap, QImage
import sys,win32api,win32con,win32gui,os,ctypes
from ctypes import byref, c_int, sizeof, wintypes
#窗口大小定义
w=800
h=500
#-------------------------------窗口工具实现--------------------------------
def show_max(hwnd):
    try:
        win32gui.PostMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_MAXIMIZE, 0)
    except Exception as e:
        win32api.MessageBox(0, f"{str(e)}", "错误", win32con.MB_OK)
def show_min(hwnd):
    try:
        win32gui.PostMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_MINIMIZE, 0)
    except Exception as e:
        win32api.MessageBox(0, f"{str(e)}", "错误", win32con.MB_OK)
def show_normal(hwnd):
    try:
        win32gui.PostMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    except Exception as e:
        win32api.MessageBox(0, f"{str(e)}", "错误", win32con.MB_OK)
def close_window(hwnd):
    try:
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    except Exception as e:
        win32api.MessageBox(0, f"{str(e)}", "错误", win32con.MB_OK)
def toggle_always_on_top(hwnd):
    ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    if ex_style & win32con.WS_EX_TOPMOST:
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    else:
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
def min_button_sh(hwnd):
    try:
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        if style & win32con.WS_MINIMIZEBOX:
            new_style = style & ~win32con.WS_MINIMIZEBOX
        else:
            new_style = style | win32con.WS_MINIMIZEBOX
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)
        win32gui.SetWindowPos(
            hwnd, 0, 0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE |
            win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED
        )
    except Exception as e:
        win32api.MessageBox(0, f"{str(e)}", "错误", win32con.MB_OK)
def window_title_sh(hwnd):
    try:
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        if style & win32con.WS_CAPTION:
            new_style = style & ~win32con.WS_CAPTION
        else:
            new_style = style | win32con.WS_CAPTION
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)
        win32gui.SetWindowPos(
            hwnd, 0, 0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE |
            win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED
        )
    except Exception as e:
        win32api.MessageBox(0, f"{str(e)}", "错误", win32con.MB_OK)
def max_button_sh(hwnd):
    try:
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        if style & win32con.WS_MAXIMIZEBOX:
            new_style = style & ~win32con.WS_MAXIMIZEBOX
        else:
            new_style = style | win32con.WS_MAXIMIZEBOX
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)
        win32gui.SetWindowPos(
            hwnd, 0, 0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE |
            win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED
        )
    except Exception as e:
        win32api.MessageBox(0, f"{str(e)}", "错误", win32con.MB_OK)
def help_button_sh(hwnd):
    try:
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        if style & win32con.WS_EX_CONTEXTHELP:
            new_style = style & ~win32con.WS_EX_CONTEXTHELP
        else:
            new_style = style | win32con.WS_EX_CONTEXTHELP
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, new_style)
        win32gui.SetWindowPos(
            hwnd, 0, 0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE |
            win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED
        )
    except Exception as e:
        win32api.MessageBox(0, f"{str(e)}", "错误", win32con.MB_OK)
def can_change_size(hwnd):
    try:
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        if style & win32con.WS_THICKFRAME:
            new_style = style & ~win32con.WS_THICKFRAME
        else:
            new_style = style | win32con.WS_THICKFRAME
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)
        win32gui.SetWindowPos(
            hwnd, 0, 0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE |
            win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED
        )
    except Exception as e:
        win32api.MessageBox(0, f"{str(e)}", "错误", win32con.MB_OK)
def tool_win(hwnd):
    try:
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        if style & win32con.WS_EX_TOOLWINDOW:
            new_style = style & ~win32con.WS_EX_TOOLWINDOW
        else:
            new_style = style | win32con.WS_EX_TOOLWINDOW
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, new_style)
        win32gui.SetWindowPos(
            hwnd, 0, 0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE |
            win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED
        )
    except Exception as e:
        win32api.MessageBox(0, f"{str(e)}", "错误", win32con.MB_OK)

#---------------DWM----------
dwmapi = ctypes.windll.dwmapi
# 定义函数签名
DwmSetWindowAttribute = dwmapi.DwmSetWindowAttribute
DwmSetWindowAttribute.argtypes = [wintypes.HWND, wintypes.DWORD, ctypes.c_void_p, wintypes.DWORD]
DwmSetWindowAttribute.restype = wintypes.LONG

DwmGetWindowAttribute = dwmapi.DwmGetWindowAttribute
DwmGetWindowAttribute.argtypes = [wintypes.HWND, wintypes.DWORD, ctypes.c_void_p, wintypes.DWORD]
DwmGetWindowAttribute.restype = wintypes.LONG

# --- 属性常量定义 ---
DWMWA_TRANSITIONS_FORCEDISABLED = 3
DWMWA_USE_IMMERSIVE_DARK_MODE = 20
DWMWA_WINDOW_CORNER_PREFERENCE = 33
DWMWA_CAPTION_COLOR = 35
DWMWA_TEXT_COLOR = 36

# --- 圆角偏好值 (DWM_WINDOW_CORNER_PREFERENCE) ---
DWMWCP_DEFAULT = 0          # 系统决定
DWMWCP_DONOTROUND = 1       # 直角
DWMWCP_ROUND = 2            # 标准圆角
DWMWCP_ROUNDSMALL = 3       # 小圆角

DWMNCRP_USEWINDOWSTYLE = 0  #系统决定
DWMWA_NCRENDERING_POLICY = 2
DWMNCRP_ENABLED = 2         #启用
DWMNCRP_DISABLED = 1        #关闭
def dwm_ncrp(hwnd,enab):
    if enab=="enable":
        value = c_int(DWMNCRP_ENABLED)
    elif enab=="disable":
        value = c_int(DWMNCRP_DISABLED)
    else:
        value = c_int(DWMNCRP_USEWINDOWSTYLE)
    result = DwmSetWindowAttribute(
            hwnd, DWMWA_NCRENDERING_POLICY, byref(value), sizeof(value)
        )
def dwm_round(hwnd,r):
    if r=="system":
        pref = ctypes.c_int(DWMWCP_DEFAULT)
    elif r=="noround":
        pref = ctypes.c_int(DWMWCP_DONOTROUND)
    elif r=="round":
        pref = ctypes.c_int(DWMWCP_ROUND)
    else:
        pref = ctypes.c_int(DWMWCP_ROUNDSMALL)

    result = DwmSetWindowAttribute(
        hwnd, 
        DWMWA_WINDOW_CORNER_PREFERENCE, 
        ctypes.byref(pref), 
        ctypes.sizeof(pref)
    )
    if result!=0:
        win32api.MessageBox(0, f"出现一个错误，代码：{result}", "错误", win32con.MB_OK)
def set_animations_disabled(hwnd, disable):
    value = wintypes.BOOL(disable)
    result = DwmSetWindowAttribute(
        hwnd, 
        DWMWA_TRANSITIONS_FORCEDISABLED, 
        ctypes.byref(value), 
        ctypes.sizeof(value)
    )
    if result!=0:
        win32api.MessageBox(0, f"出现一个错误，代码：{result}", "错误", win32con.MB_OK)
#-------------------------------GUI界面实现--------------------------------

#信息修改器
class Info_changer(QWidget):
    def __init__(self, parent =None, hwnd=None):
        super().__init__(parent)
        if not hwnd:
            self.destroy()
            return
        self.setWindowTitle(win32gui.GetWindowText(hwnd)+" - 信息修改")
        self.resize(w,h)
        self.setWindowFlags(Qt.WindowType.Window|Qt.WindowType.WindowCloseButtonHint)
        self.hwnd=hwnd
        #主布局
        self.mainLayout=QVBoxLayout(self)
        self.scroll = QScrollArea()
        self.tool_widget=QWidget()
        self.tool_layout = QVBoxLayout(self.tool_widget)
        self.scroll.setWidget(self.tool_widget)
        self.scroll.setWidgetResizable(True)
        self.mainLayout.addWidget(self.scroll)

        #窗口标题修改
        self.tool_layout.addWidget(QLabel("窗口标题："))
        self.win_title_cha=QLineEdit()
        self.win_title_cha.setText(win32gui.GetWindowText(hwnd))
        self.tool_layout.addWidget(self.win_title_cha)

        #窗口x,y,h,w
        rect = win32gui.GetWindowRect(hwnd)
        self.tool_layout.addWidget(QLabel("X坐标："))
        self.x_edit=QSpinBox()
        self.x_edit.setRange(0,win32api.GetSystemMetrics(win32con.SM_CXSCREEN))
        self.x_edit.setValue(rect[0])
        self.tool_layout.addWidget(self.x_edit)
        self.tool_layout.addWidget(QLabel("Y坐标："))
        self.y_edit=QSpinBox()
        self.y_edit.setRange(0,win32api.GetSystemMetrics(win32con.SM_CYSCREEN))
        self.y_edit.setValue(rect[1])
        self.tool_layout.addWidget(self.y_edit)

        self.tool_layout.addWidget(QLabel("宽度："))
        self.w_edit=QSpinBox()
        self.w_edit.setRange(0,win32api.GetSystemMetrics(win32con.SM_CXSCREEN))
        self.w_edit.setValue(rect[2]-rect[0])
        self.tool_layout.addWidget(self.w_edit)
        self.tool_layout.addWidget(QLabel("高度："))
        self.h_edit=QSpinBox()
        self.h_edit.setRange(0,win32api.GetSystemMetrics(win32con.SM_CYSCREEN))
        self.h_edit.setValue(rect[3]-rect[1])
        self.tool_layout.addWidget(self.h_edit)


        #确定 取消 应用
        self.buttonFrame=QFrame()
        self.buttonFrame.setFixedHeight(50)
        self.buttonLayout=QHBoxLayout(self.buttonFrame)
        self.ok_button=QPushButton("确定")
        self.cancel_button=QPushButton("取消")
        self.apply_button=QPushButton("应用")
        self.ok_button.clicked.connect(lambda:[self.apply_setting(),self.destroy()])
        self.cancel_button.clicked.connect(self.destroy)
        self.apply_button.clicked.connect(self.apply_setting)
        self.buttonLayout.addWidget(self.ok_button)
        self.buttonLayout.addWidget(self.cancel_button)
        self.buttonLayout.addWidget(self.apply_button)
        self.mainLayout.addWidget(self.buttonFrame)


    def apply_setting(self):
        try:
            win32gui.SetWindowText(self.hwnd, self.win_title_cha.text())
            win32gui.MoveWindow(self.hwnd, self.x_edit.value(), self.y_edit.value(), 
                            self.w_edit.value(), self.h_edit.value(), True)
        except Exception as e:
            QMessageBox.information(self,"错误",f"{str(e)}")
#子控件列举器
def enum_direct_children(hwnd):
    children = []
    child = win32gui.FindWindowEx(hwnd, 0, None, None)
    while child:
        children.append(child)
        try:
            child = win32gui.FindWindowEx(hwnd, child, None, None)
        except Exception:
            break  # 窗口可能在枚举过程中被销毁
    return children


def safe_get_class(hwnd):
    try:
        return win32gui.GetClassName(hwnd)
    except Exception:
        return "<已失效>"


def safe_get_text(hwnd):
    try:
        return win32gui.GetWindowText(hwnd)
    except Exception:
        return ""

#子控件列举器
class WindowInspector(QTreeWidget):
    def __init__(self, hwnd: int, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.Window|Qt.WindowType.WindowCloseButtonHint)
        self.target_hwnd = hwnd
        self.hwnd_map = {}  # HWND -> QTreeWidgetItem

        self.setWindowTitle(f"窗口子控件 - {win32gui.GetWindowText(hwnd)}")
        self.resize(w,h)

        self.setHeaderLabels(["HWND", "类名 (ClassName)", "文本 (Text)"])

        self._populate()

    #构建根节点
    def _make_item(self, parent_item, hwnd):
        item = QTreeWidgetItem(parent_item)
        item.setText(0, str(hwnd))
        item.setText(1, safe_get_class(hwnd))
        item.setText(2, safe_get_text(hwnd))
        item.setData(0, Qt.ItemDataRole.UserRole, hwnd)
        return item

    #把 item 作为下一层的 parent
    def _build_children(self, parent_item, hwnd, depth=0):
        if depth > 100:
            return
        for child in enum_direct_children(hwnd):
            if child in self.hwnd_map:
                continue
            item = self._make_item(parent_item, child)
            self.hwnd_map[child] = item
            self._build_children(item, child, depth + 1)

    def _populate(self):
        self.setUpdatesEnabled(False)
        self.clear()
        self.hwnd_map.clear()
        try:
            root = self._make_item(self, self.target_hwnd)
            self.hwnd_map[self.target_hwnd] = root
            self._build_children(root, self.target_hwnd)
            self.expandToDepth(2)
        finally:
            self.setUpdatesEnabled(True)
#获取图标工具
def get_window_icon(hwnd: int) -> QIcon:
    hicon = 0

    # 1. 尝试通过 WM_GETICON 获取窗口大图标
    try:
        _, hicon = win32gui.SendMessageTimeout(
            hwnd, win32con.WM_GETICON, win32con.ICON_BIG, 0,
            win32con.SMTO_ABORTIFHUNG, 100
        )
    except Exception:
        pass

    # 2. 若失败，回退到窗口类图标
    if not hicon:
        try:
            hicon = win32gui.GetClassLongPtr(hwnd, win32con.GCLP_HICON)
        except Exception:
            pass

    # 3. 若仍失败，使用系统默认应用程序图标
    if not hicon:
        hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)

    # 4. 转换为 QIcon
    try:
        pixmap = QPixmap.fromImage(QImage.fromHICON(int(hicon)))
        if not pixmap.isNull():
            return QIcon(pixmap)
    except Exception:
        pass

    # 5. 失败则返回默认图标
    try:
        hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
        return QIcon(QPixmap.fromImage(QImage.fromHICON(int(hicon))))
    except Exception:
        return QIcon.fromTheme("application-x-executable")
#实现属性编辑器
class attribute_item(QListWidgetItem):
    def __init__(self, hwnd,style_name):
        super().__init__()
        self.hwnd = hwnd
        
        if style_name[:6]=="WS_EX_":
            self.gwl=win32con.GWL_EXSTYLE
        else:
            self.gwl=win32con.GWL_STYLE
        try:
            self.style = getattr(win32con, style_name)
        except:
            pass
        self.style_name=style_name
        self.setText(f"{"√" if self.get() else "×"}  {self.style_name}")
    #获取当前属性是否启用
    def get(self):
        try:
            style = win32gui.GetWindowLong(self.hwnd, self.gwl)
            return (style & self.style) != 0
        except Exception as e:
            QMessageBox.information(None,"错误",f"{str(e)}")
    #切换属性的状态
    def set(self):
        try:
            style = win32gui.GetWindowLong(self.hwnd, self.gwl)
            if self.get():
                new_style = style & ~self.style
            else:
                new_style = style | self.style
            win32gui.SetWindowLong(self.hwnd, self.gwl, new_style)
            win32gui.SetWindowPos(self.hwnd, 0, 0, 0, 0, 0,
                win32con.SWP_NOMOVE | win32con.SWP_NOSIZE |
                win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED
            )
        except Exception as e:
            QMessageBox.information(None,"错误",f"{str(e)}")
        self.setText(f"{"√" if self.get() else "×"}  {self.style_name}")
class attribute_editor(QListWidget):
    def __init__(self, parent, hwnd):
        super().__init__(parent)
        if not hwnd:
            return
        self.setWindowTitle(win32gui.GetWindowText(hwnd)+" - Attributes Editor - 双击选项更改")
        self.setWindowFlags(Qt.WindowType.Window|Qt.WindowType.WindowCloseButtonHint)
        self.resize(w,h)

        all_ws = [name for name in dir(win32con) if name.isupper() and name[:3]=="WS_"]
        for i in all_ws:
            self.addItem(attribute_item(hwnd,i))

    def mouseDoubleClickEvent(self, e):
        try:
            self.currentItem().set()
            return super().mouseDoubleClickEvent(e)
        except:
            pass

#以管理员身份重启实现
def restart_to_admin():
    exe_path=sys.executable
    if getattr(sys, 'frozen', False):
        argv=None
    else:
        argv=f'"{os.path.abspath(sys.argv[0])}"'
    result = ctypes.windll.shell32.ShellExecuteW(
        None,"runas",exe_path,argv,None,1
    )
    if result <= 32:
        QMessageBox.information(None,"警告","管理员提权失败。")
    else:
        sys.exit()
#菜单类
class WMenu(QMenu):
    def __init__(self, title, /, parent = ...,hwnd=None):
        super().__init__(title, parent)
        self.hwnd=hwnd
        self.atw=None
        self.lis=None

        self.pu_tong=QMenu("普通操作")
        self.addMenu(self.pu_tong)

        self.shu_xing=QMenu("简单属性")
        self.addMenu(self.shu_xing)

        self.dwm_menu=QMenu("DWM特效")
        self.addMenu(self.dwm_menu)

        self.dwm_round_menu=QMenu("窗口圆角")
        self.dwm_menu.addMenu(self.dwm_round_menu)
        self.dwmrou_system=QAction("系统")
        self.dwmrou_noround=QAction("直角")
        self.dwmrou_round=QAction("中圆角")
        self.dwmrou_smallround=QAction("小圆角")
        self.dwm_round_menu.addActions([self.dwmrou_system,self.dwmrou_noround,
                                        self.dwmrou_round,self.dwmrou_smallround])
        self.dwmrou_system.triggered.connect(lambda checked=False:dwm_round(self.hwnd,"system"))
        self.dwmrou_noround.triggered.connect(lambda checked=False:dwm_round(self.hwnd,"noround"))
        self.dwmrou_round.triggered.connect(lambda checked=False:dwm_round(self.hwnd,"round"))
        self.dwmrou_smallround.triggered.connect(lambda checked=False:dwm_round(self.hwnd,"smallrou"))


        self.dwm_animations=QMenu("窗口过渡动画")
        self.dwm_menu.addMenu(self.dwm_animations)

        self.no_anim=QAction("关闭")
        self.ok_anim=QAction("启用")
        self.no_anim.triggered.connect(lambda checked=False:set_animations_disabled(self.hwnd,True))
        self.ok_anim.triggered.connect(lambda checked=False:set_animations_disabled(self.hwnd,False))
        self.dwm_animations.addActions([self.no_anim,self.ok_anim])


        self.dwm_ncrp=QMenu("渲染非客户区")
        self.dwm_ncrp_system=QAction("系统")
        self.dwm_ncrp_enable=QAction("启用")
        self.dwm_ncrp_disable=QAction("禁用")
        self.dwm_ncrp.addActions([self.dwm_ncrp_system,self.dwm_ncrp_enable,self.dwm_ncrp_disable])
        self.dwm_menu.addMenu(self.dwm_ncrp)
        self.dwm_ncrp_system.triggered.connect(lambda checked=False:dwm_ncrp(hwnd=self.hwnd,enab=""))
        self.dwm_ncrp_enable.triggered.connect(lambda checked=False:dwm_ncrp(hwnd=self.hwnd,enab="enable"))
        self.dwm_ncrp_disable.triggered.connect(lambda checked=False:dwm_ncrp(hwnd=self.hwnd,enab="disable"))


        self.max_action=QAction("最大化")
        self.min_action=QAction("最小化")
        self.nor_action=QAction("还原")
        self.clo_action=QAction("关闭")
        self.aot_action=QAction("置顶")
        self.has_titlea=QAction("有标题栏")
        self.min_sh_act=QAction("可最小化")
        self.max_sh_act=QAction("可最大化")
        self.hel_sh_act=QAction("有“帮助”")
        self.can_cg_act=QAction("可调整大小")
        self.toolwin_ac=QAction("工具窗口")
        self.attribu_set=QAction("所有属性")
        self.show_lis=QAction("查看子控件")
        self.cha_info=QAction("信息更改")

        self.addActions([self.attribu_set,self.show_lis,self.cha_info])
        self.pu_tong.addActions([self.max_action,self.min_action,self.nor_action,self.clo_action])
        self.shu_xing.addActions([self.aot_action,self.has_titlea,self.min_sh_act,self.max_sh_act,self.hel_sh_act,self.can_cg_act,self.toolwin_ac])
        self.max_action.triggered.connect(lambda checked=False:show_max(self.hwnd))
        self.min_action.triggered.connect(lambda checked=False:show_min(self.hwnd))
        self.nor_action.triggered.connect(lambda checked=False:show_normal(self.hwnd))
        self.clo_action.triggered.connect(lambda checked=False:close_window(self.hwnd))
        self.aot_action.triggered.connect(lambda checked=False:toggle_always_on_top(self.hwnd))
        self.has_titlea.triggered.connect(lambda checked=False:window_title_sh(self.hwnd))
        self.min_sh_act.triggered.connect(lambda checked=False:min_button_sh(self.hwnd))
        self.max_sh_act.triggered.connect(lambda checked=False:max_button_sh(self.hwnd))
        self.hel_sh_act.triggered.connect(lambda checked=False:help_button_sh(self.hwnd))
        self.can_cg_act.triggered.connect(lambda checked=False:can_change_size(self.hwnd))
        self.toolwin_ac.triggered.connect(lambda checked=False:tool_win(self.hwnd))
        self.attribu_set.triggered.connect(self.att)
        self.show_lis.triggered.connect(self.show_lis_a)
        self.cha_info.triggered.connect(self.show_info_c)
    def att(self):
        if self.hwnd:
            self.atw=attribute_editor(parent=self.parent(),hwnd=self.hwnd)
            self.atw.show()
    def show_lis_a(self):
        if self.hwnd:
            self.lis=WindowInspector(parent=self.parent(),hwnd=self.hwnd)
            self.lis.show()
    def show_info_c(self):
        if self.hwnd:
            self.lis=Info_changer(parent=self.parent(),hwnd=self.hwnd)
            self.lis.show()
    def setHwnd(self,hwnd):
        self.hwnd=hwnd
    
#列表项类
class Item(QListWidgetItem):
    def __init__(self,text,parent,hwnd):
        super().__init__()
        icon=get_window_icon(hwnd)
        self.setIcon(icon)
        self.hwnd=hwnd
        try:
            title = win32gui.GetWindowText(hwnd)
            class_name = win32gui.GetClassName(hwnd)
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            width = right - left
            height = bottom - top
            is_min=win32gui.IsIconic(hwnd)
        except:
            title="无法获取消息"
            class_name="无法获取消息"
            left,top,right,bottom=0,0,0,0
            width=0
            height=0
            is_min="?"
        self.setText(title)
        self.setToolTip(f"窗口句柄：{hwnd}\n窗口标题：{title}\n窗口类名：{class_name}\n窗口rect：{str((left, top, right, bottom))}\n窗口大小：{str((width,height))}\n是否最小化：{"是" if is_min else "否"}")
    def getHwnd(self):
        return self.hwnd
#主窗口类
class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_all=False
        self.setWindowTitle("WindowsManager - HCT")
        self.resize(w,h)
        #菜单项
        menubar = self.menuBar() 
        menubar.setStyleSheet("background:white;")
        #文件菜单
        self.fileMenu=QMenu("文件")
        self.restart_as_admin=QAction("以管理员身份重启")
        self.about_action=QAction("关于")
        self.exit_program=QAction("退出")
        self.restart_as_admin.triggered.connect(lambda:restart_to_admin())
        self.about_action.triggered.connect(lambda:QMessageBox.information(self,"关于","窗口管理工具\nHCT制作\n1.0.0"))
        self.exit_program.triggered.connect(QApplication.instance().quit)
        self.fileMenu.addActions([self.restart_as_admin,self.exit_program,self.about_action])
        menubar.addMenu(self.fileMenu)

        #显示菜单
        self.show_menu=QMenu("显示")
        self.show_all_action=QAction("显示隐藏的窗口")
        self.flush_action=QAction("刷新列表")
        self.always_on_top_action=QAction("置顶显示此窗口")
        self.show_all_action.triggered.connect(self.show_hide)
        self.flush_action.triggered.connect(self.flush_list)
        self.always_on_top_action.triggered.connect(self.always_on_top)
        self.show_menu.addActions([self.show_all_action,self.flush_action,self.always_on_top_action])
        menubar.addMenu(self.show_menu)

        #操作菜单
        self.com_menu=WMenu("操作",self)
        menubar.addMenu(self.com_menu)
        
        #主要布局
        self.mainWidget=QListWidget()
        self.mainWidget.currentItemChanged.connect(self.change_win_hwnd)
        self.mainWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.mainWidget.customContextMenuRequested.connect(lambda pos:self.com_menu.exec(self.mainWidget.mapToGlobal(pos)))
        self.setCentralWidget(self.mainWidget)
        self.flush_list()
    def change_win_hwnd(self, current, previous):
        self.com_menu.setHwnd(current.getHwnd() if current else None)
    def always_on_top(self):
        toggle_always_on_top(int(self.winId()))
    def show_hide(self):
        if self.is_all:
            self.is_all=False
            self.flush_list()
        else:
            self.is_all=True
            self.flush_list()
    def flush_list(self):
        self.mainWidget.clear()
        windows=[]
        win32gui.EnumWindows(lambda hwnd, resultList: resultList.append(hwnd), windows)
        for i in windows:
            if win32gui.IsWindowVisible(i) or self.is_all:
                if i!=int(self.winId()):
                    self.mainWidget.addItem(Item('',self.mainWidget,i))

        

if __name__=="__main__":
    a=QApplication(sys.argv)
    wi=Win()
    wi.show()
    sys.exit(a.exec())