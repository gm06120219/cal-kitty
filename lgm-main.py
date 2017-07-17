from PyQt5 import QtWidgets, QtGui
import sys

from Calculator import Ui_Calculator  # 导入生成form.py里生成的类

class mywindow(QtWidgets.QWidget,Ui_Calculator):
	list_one = []
	list_two = []
	list_save_flat = 0
	operation = ''

    def __init__(self):
    	super(mywindow,self).__init__()    
    	self.setupUi(self)

    #定义槽函数
    def butt_1_1(self):
        self.textEdit.setText("")

    # 定义数字按钮处理方法
    def btn_number(self):
    	# 检查……
    	# 如果已经有point在list中，忽略此次按钮处理
    	# 如果当前list只有一位0，并且按下的按钮也是0，忽略此次处理

    	# 把数字按钮的值保存到list变量中，并且需要同步显示到text-edit当中
    	
    	# 如果当前标志位是1，则将数字按钮的值保存到list-one中
    	# 如果当前标志位是2，则将数组按钮的值保存到list-two中
    	#pass

    # 定义加减乘除按钮处理方法
    def btn_operation(self):
    	# 把list_one变量 转换成float类型
    	# 记录运算方法
    	# 将list标志位置为2
    	# 将text-edit当中内容清为0
    	#pass

    # 定义小数点按钮处理方法
    # TODO
    def btn_point(self):
    	#pass

    # 定义清空按钮处理方法
    #def btn_clear(self):
    	#pass

    # 定义等于按钮处理方法	
    #def btn_equal(self):
    	# 将list-one数组中拿出来，转为int型
    	# 将list-two数组中拿出来，转为int型

    	#将上面的两个数字与operation做运算

    	pass


QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())