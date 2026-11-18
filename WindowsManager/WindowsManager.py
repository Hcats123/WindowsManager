import sys
import warnings
warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, QLineEdit,QMainWindow,QListWidget,QListWidgetItem, QPushButton, QScrollArea, QSpinBox, QToolBar,QTreeWidget,QMenu,QTreeWidgetItem, QMessageBox, QVBoxLayout,QWidget
from PyQt6.QtCore import QSize, QThread, Qt, pyqtSignal
from PyQt6.QtGui import QCloseEvent, QColor,QAction,QIcon,QPixmap, QImage, QResizeEvent, QShowEvent
import sys,win32api,win32con,win32gui,os,ctypes,traceback
from ctypes import byref, c_int, sizeof, wintypes
from pywinauto import Desktop
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

dwmapi.DwmRegisterThumbnail.argtypes = [wintypes.HWND, wintypes.HWND, ctypes.POINTER(wintypes.HANDLE)]
dwmapi.DwmRegisterThumbnail.restype = ctypes.c_long

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
#DWM略缩图
class DWM_THUMBNAIL_PROPERTIES(ctypes.Structure):
    _fields_ = [
        ("dwFlags", wintypes.DWORD),
        ("rcDestination", wintypes.RECT),
        ("rcSource", wintypes.RECT),
        ("opacity", ctypes.c_ubyte),
        ("fVisible", wintypes.BOOL),
        ("fSourceClientAreaOnly", wintypes.BOOL),
    ]

dwmapi.DwmUpdateThumbnailProperties.argtypes = [
    wintypes.HANDLE, ctypes.POINTER(DWM_THUMBNAIL_PROPERTIES)
]
dwmapi.DwmUpdateThumbnailProperties.restype = ctypes.c_long

dwmapi.DwmUnregisterThumbnail.argtypes = [wintypes.HANDLE]
dwmapi.DwmUnregisterThumbnail.restype = ctypes.c_long

DWM_TNP_RECTDESTINATION        = 0x00000001
DWM_TNP_VISIBLE                = 0x00000008
DWM_TNP_OPACITY                = 0x00000004
DWM_TNP_SOURCECLIENTAREAONLY   = 0x00000010


# 宿主窗口
class DWMThumbnailHost(QMainWindow):
    def __init__(self, source_hwnd: int, parent=None):
        super().__init__(parent)
        self.resize(self.parent().width(),self.parent().height())
        self.state_label=QLabel()
        self.state_label.setText("")

        self.is_fscao=False
        self.source_hwnd = source_hwnd
        self.thumbnail_handle = wintypes.HANDLE()
        self._dest_hwnd = 0
        self._registered = False

        self.setWindowTitle("DWM Thumbnail Host")
        self.resize(self.parent().width(),self.parent().height())

        self.toolbar = QToolBar("工具", self)
        self.toolbar.setMovable(False)
        self.toolbar.setFloatable(False)
        self.toolbar.setIconSize(QSize(30, 30))
        self.toolbar.setFixedHeight(30)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)

        self.hwnd_edit=QLineEdit()
        self.hwnd_edit.textChanged.connect(self.changeText)
        self.hwnd_edit.setFixedHeight(25)
        self.hwnd_edit.setPlaceholderText("输入窗口句柄")
        self.hwnd_edit.setText(str(source_hwnd))
        self.toolbar.addWidget(self.hwnd_edit)

        self.fscao=QAction("×：显示窗口非客户区")
        self.fscao.triggered.connect(self.change_fscao)
        self.toolbar.addAction(self.fscao)


        self.statebar = QToolBar("状态", self)
        self.statebar.setMovable(False)
        self.statebar.setFloatable(False)
        self.statebar.setIconSize(QSize(30, 30))
        self.statebar.setFixedHeight(30)
        self.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.statebar)

        self.state_label=QLabel()
        self.state_label.setText("......")
        self.statebar.addWidget(self.state_label)
        self.show()
    def change_fscao(self):
        if self.is_fscao:
            self.is_fscao=False
            self.fscao.setText("×：显示窗口非客户区")
        else:
            self.is_fscao=True
            self.fscao.setText("√：显示窗口非客户区")
        self._update_thumbnail_properties()
    def changeText(self,text):
        try:
            self.source_hwnd=int(text)
            self._register_thumbnail()
            self._update_thumbnail_properties()
        except:
            self.state_label.setText("语法错误")
    #生命周期
    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        # 顶层 QWidget 只有在显示后 winId() 才有效
        if not self._registered:
            if not win32gui.IsWindow(self.source_hwnd):
                self.state_label.setText(f"源窗口句柄无效: {self.source_hwnd}")
            self._dest_hwnd = int(self.winId())
            if self._dest_hwnd == self.source_hwnd:
                self.state_label.setText("源窗口和宿主窗口不能是同一个")
            self._register_thumbnail()
            self._update_thumbnail_properties()
            self._registered = True

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        if self._registered:
            self._update_thumbnail_properties()

    def closeEvent(self, event: QCloseEvent):
        if self._registered and self.thumbnail_handle.value:
            dwmapi.DwmUnregisterThumbnail(self.thumbnail_handle.value)
            self.thumbnail_handle = wintypes.HANDLE()
            self._registered = False
        super().closeEvent(event)

    #DWM 操作
    def _register_thumbnail(self):
        hr = dwmapi.DwmRegisterThumbnail(
            self._dest_hwnd,
            self.source_hwnd,
            ctypes.byref(self.thumbnail_handle),
        )
        if hr != 0:
            self.state_label.setText(str(ctypes.WinError(hr)))
        else:
            self.state_label.setText(f"缩略图注册成功，句柄: {self.thumbnail_handle.value}")

    def _update_thumbnail_properties(self):
        # 客户区尺寸：GetClientRect 返回的是物理像素
        rect = wintypes.RECT()
        ctypes.windll.user32.GetClientRect(self._dest_hwnd, ctypes.byref(rect))

        props = DWM_THUMBNAIL_PROPERTIES()
        props.dwFlags = (
            DWM_TNP_RECTDESTINATION
            | DWM_TNP_VISIBLE
            | DWM_TNP_OPACITY
            | DWM_TNP_SOURCECLIENTAREAONLY
        )

        cw, ch = rect.right, rect.bottom
        props.rcDestination = wintypes.RECT(0,40,cw,ch-40)
        props.opacity = 255
        props.fVisible = True
        props.fSourceClientAreaOnly = not self.is_fscao

        hr = dwmapi.DwmUpdateThumbnailProperties(
            self.thumbnail_handle, ctypes.byref(props)
        )
        if hr != 0:
            self.state_label.setText(str(ctypes.WinError(hr)))

#信息修改器
class Info_changer(QWidget):
    def __init__(self, parent =None, hwnd=None):
        super().__init__(parent)
        if not hwnd:
            self.destroy()
            return
        self.setWindowTitle(win32gui.GetWindowText(hwnd)+" - 信息修改")
        self.resize(self.parent().width(),self.parent().height())
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
class EnumWorker(QThread):
    done = pyqtSignal(dict)
    failed = pyqtSignal(str)

    def __init__(self, hwnd, max_depth=30):
        super().__init__()
        self.hwnd = hwnd
        self.max_depth = max_depth

    def run(self):
        try:
            root = Desktop(backend="uia").window(handle=self.hwnd)
            self.done.emit(self._walk(root, 0))
        except Exception as e:
            self.failed.emit(f"{e}\n{traceback.format_exc()}")

    def _walk(self, ctrl, depth):
        node = self._info(ctrl)
        if depth < self.max_depth:
            try:
                children = ctrl.children()
            except Exception:
                children = []
            node["children"] = [self._walk(c, depth + 1) for c in children]
        return node
    @staticmethod
    def _info(ctrl):
        try:
            ei = ctrl.element_info
            r = ei.rectangle
            return {"text": ei.name or "",
                    "type": ei.control_type or "",
                    "class": ei.class_name or "",
                    "auto_id": ei.automation_id or "",
                    "handle": ei.handle,
                    "rect": (r.left, r.top, r.right, r.bottom),
                    "children": []}
        except Exception:
            return {"text": "<error>", "type": "", "class": "", "auto_id": "",
                    "handle": 0, "rect": (0, 0, 0, 0), "children": []}
class WindowInspector(QMainWindow):
    HEADERS = ["Text", "ControlType", "Class Name", "AutomationId", "HWND"]

    def __init__(self,parent,hwnd):
        super().__init__(parent)
        self.setWindowTitle(f"{win32gui.GetWindowText(hwnd)} - 窗口子控件")
        self.resize(self.parent().width(),self.parent().height())

        self.edit = QLineEdit(placeholderText="输入窗口句柄")
        self.edit.setText(str(hwnd))
        btn = QPushButton("刷新")
        btn.clicked.connect(self.on_enum)
        self.status = QLabel("就绪")

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(self.HEADERS)
        self.tree.setColumnWidth(0, 320)

        top = QHBoxLayout()
        top.addWidget(self.edit, 1)
        top.addWidget(btn)
        lay = QVBoxLayout()
        lay.addLayout(top)
        lay.addWidget(self.tree, 1)
        lay.addWidget(self.status)
        w = QWidget(); w.setLayout(lay)
        self.setCentralWidget(w)
        self.worker = None
        self.on_enum()
        self.show()

    def on_enum(self):
        try:
            hwnd = int(self.edit.text().strip(), 0)
        except ValueError:
            self.status.setText("HWND 格式错误")
            return
        if self.worker and self.worker.isRunning():
            return
        self.status.setText("枚举中…")
        self.worker = EnumWorker(hwnd)
        self.worker.done.connect(self.fill_tree)
        self.worker.failed.connect(lambda m: self.status.setText("失败：" + m.splitlines()[0]))
        self.worker.start()

    def fill_tree(self, data: dict):
        self.tree.clear()
        root_item = QTreeWidgetItem([data["text"], data["type"],
                                     data["class"], data["auto_id"], str(data["handle"])])
        self.tree.addTopLevelItem(root_item)

        def add(node, parent):
            for ch in node["children"]:
                it = QTreeWidgetItem([
                    ch["text"], 
                    ch["type"],
                    ch["class"], 
                    ch["auto_id"], 
                    str(ch["handle"]),
                ])
                parent.addChild(it)
                add(ch, it)

        add(data, root_item)
        self.tree.expandToDepth(1)
        self.status.setText(f"共 {self.tree.topLevelItemCount()} 个顶层根节点")
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
        self.resize(self.parent().width(),self.parent().height())

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
        self.dws=None

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
        self.dwm_show=QAction("DWM略缩图")

        self.addActions([self.attribu_set,self.show_lis,self.cha_info,self.dwm_show])
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
        self.dwm_show.triggered.connect(self.ds)
    def att(self):
        if self.hwnd:
            self.atw=attribute_editor(parent=self.parent(),hwnd=self.hwnd)
            self.atw.show()
    def ds(self):
        if self.hwnd:
            self.dws=DWMThumbnailHost(self.hwnd,self.parent())
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