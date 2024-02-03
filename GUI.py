# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import TTP
import openfile
import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 531,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel2 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_button7 = wx.Button( self.m_panel2, wx.ID_ANY, u"OpenExcel", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"這裡是路徑", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		wSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer2, 0, 0, 5 )


		gSizer5.Add( bSizer1, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_button8 = wx.Button( self.m_panel2, wx.ID_ANY, u"DestinationPath", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.m_button8, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"目標路徑", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		wSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer2, 0, 0, 5 )


		gSizer5.Add( bSizer2, 0, wx.EXPAND, 5 )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Pic_length = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.Pic_length, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"圖片長度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gbSizer3.Add( self.m_staticText5, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		gSizer5.Add( gbSizer3, 1, wx.EXPAND, 5 )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Pic_width = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.Pic_width, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"圖片寬度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer4.Add( self.m_staticText6, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		gSizer5.Add( gbSizer4, 1, wx.EXPAND, 5 )

		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button5 = wx.Button( self.m_panel2, wx.ID_ANY, u"StartTTP", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.m_button5, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.informTxt = wx.StaticText( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.informTxt.Wrap( -1 )

		gbSizer6.Add( self.informTxt, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		gSizer5.Add( gbSizer6, 1, wx.EXPAND, 5 )

		self.m_button6 = wx.Button( self.m_panel2, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button6, 0, wx.ALL, 5 )


		bSizer3.Add( gSizer5, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		self.m_notebook2.AddPage( self.m_panel2, u"TTP", True )
		self.m_panel21 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.SheetNumber = wx.TextCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.SheetNumber, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"指定第X張試算表\n或填入試算表名稱", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		gbSizer1.Add( self.m_staticText31, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		gSizer2.Add( gbSizer1, 1, wx.EXPAND, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.column = wx.TextCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.column, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"指定第幾欄的索引值\n或是輸入欄位名稱\n或是標題", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gbSizer2.Add( self.m_staticText4, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		gSizer2.Add( gbSizer2, 1, wx.EXPAND, 5 )

		self.m_checkBox1 = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"是否跳過空白文字\n預設未跳過", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.FontSize = wx.TextCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.FontSize, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"字體大小設置", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer5.Add( self.m_staticText7, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		gSizer2.Add( gbSizer5, 1, wx.EXPAND, 5 )


		self.m_panel21.SetSizer( gSizer2 )
		self.m_panel21.Layout()
		gSizer2.Fit( self.m_panel21 )
		self.m_notebook2.AddPage( self.m_panel21, u"ExcelSetting", False )

		bSizer4.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.OpenFile )
		self.m_button8.Bind( wx.EVT_BUTTON, self.GetDestination )
		self.m_button5.Bind( wx.EVT_BUTTON, self.StartTTP )
		self.m_button6.Bind( wx.EVT_BUTTON, self.Exit )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.SkipSpace )
		self.excel_path=""
		self.destinationPath=""
		self.SkipTxtSpace=False

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OpenFile( self, event ):
		self.excel_path=openfile.FileOpen()
		k=self.excel_path.split('/')
		self.m_staticText2.Label=k[-1]

	def GetDestination( self, event ):
		self.destinationPath=openfile.FolderOpen()
		k=self.destinationPath.split('/')
		self.m_staticText3.Label=k[-1]

	def StartTTP( self, event ):
		self.informTxt.Label=""
		if self.SheetNumber.Value.isdigit():
			Sheet_num=int(self.SheetNumber.Value)
			if self.column.Value.isdigit():
				cols_number=int(self.column.Value)
				df=TTP.OE(self.excel_path, Sheet_num, cols_number)
			else:
				df=TTP.OE(self.excel_path, Sheet_num, self.column.Value)
		else:
			if self.column.Value.isdigit():
				cols_number=int(self.column.Value)
				df=TTP.OE(self.excel_path, self.SheetNumber.Value, cols_number)
			else:
				df=TTP.OE(self.excel_path, self.SheetNumber.Value, self.column.Value)
		#print(df)
		count=0
		for txts in df:
			for txt in txts:
				if (txt!=txt) & (self.SkipTxtSpace):
					continue
				try:
					TTP.TTP(txt, self.destinationPath+f"\\{count}.png", int(self.Pic_length.Value), int(self.Pic_width.Value),int(self.FontSize.Value))
				except:
					TTP.TTP(txt, self.destinationPath+f"\\{count}.png")
				count=count+1
		self.informTxt.Label="圖片轉換完成"

	def Exit( self, event ):
		wx.Exit()

	def SkipSpace( self, event ):
		if self.SkipTxtSpace:
			self.SkipTxtSpace=False
			self.m_checkBox1.Label="是否跳過空白文字\n設定未跳過"
		else:
			self.SkipTxtSpace=True
			self.m_checkBox1.Label="是否跳過空白文字\n設定已跳過"


