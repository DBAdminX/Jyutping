import wx
import jyutping


class PinyinEditor(wx.Frame):
    def __init__(self):
        super().__init__(None, title="粤拼编辑器", size=(800, 600))
        panel = wx.Panel(self)

        # 多行文本框
        self.text_input = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        self.pinyin_display = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)

        # 统一字体
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.text_input.SetFont(font)
        self.pinyin_display.SetFont(font)

        # 布局
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.pinyin_display, proportion=1, flag=wx.EXPAND)
        sizer.Add(self.text_input, proportion=1, flag=wx.EXPAND)
        panel.SetSizer(sizer)

        # 绑定事件
        self.text_input.Bind(wx.EVT_TEXT, self.update_pinyin)

    def update_pinyin(self, event):
        current_pos = self.text_input.GetInsertionPoint()
        text = self.text_input.GetValue()
        pinyin_lines = []
        
        for line in text.split('\n'):
            pinyin_chars = []
            for char in line:
                try:
                    pinyin_list = jyutping.get(char)
                    
                    # 双重校验：1. 列表存在且非空 2. 第一个元素是字符串
                    if pinyin_list and len(pinyin_list) > 0 and isinstance(pinyin_list[0], str):
                        pinyin_chars.append(pinyin_list[0])
                    else:
                        pinyin_chars.append(char)
                except Exception as e:
                    pinyin_chars.append(char)
            
            # 确保所有元素都是字符串
            safe_pinyin = [str(item) for item in pinyin_chars]
            pinyin_lines.append(' '.join(safe_pinyin))
        
        self.pinyin_display.SetValue('\n'.join(pinyin_lines))
        self.text_input.SetInsertionPoint(current_pos)


if __name__ == "__main__":
    app = wx.App()
    frame = PinyinEditor()
    frame.Show()
    app.MainLoop()