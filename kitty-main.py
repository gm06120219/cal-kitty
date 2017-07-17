from PyQt5 import QtWidgets, QtGui
import sys

from Calculator import Ui_Calculator    # 导入生成form.py里生成的类

class mywindow(QtWidgets.QWidget,Ui_Calculator):
    def __init__(self):    
        super(mywindow,self).__init__()    
        self.setupUi(self)
        self.clear_flag = True                # 初始化清空标志位

    #定义槽函数
    def but_1(self):
        if self.clear_flag == True:
            temp = "1"                          # 初始化输入时，原先的0不保留
            self.clear_flag = False
        else :
            temp = self.textEdit.toPlainText()    # 获取原先的输入框
            temp = temp + "1"                     # 将原先的值在末尾添加字符1
        self.textEdit.setText(temp)           # 将输入框值设置为添加1之后的字符串

    def but_2(self):
        if self.clear_flag == True:
            temp = "2"                          
            self.clear_flag = False
        else :
            temp = self.textEdit.toPlainText()    
            temp = temp + "2"                    
        self.textEdit.setText(temp)           
    def but_3(self):
        if self.clear_flag == True:
            temp = "3"                          
            self.clear_flag = False
        else :
            temp = self.textEdit.toPlainText()    
            temp = temp + "3"                    
        self.textEdit.setText(temp)          

    def but_4(self):
        if self.clear_flag == True:
            temp = "4"                          
            self.clear_flag = False
        else :
            temp = self.textEdit.toPlainText()    
            temp = temp + "4"                     
        self.textEdit.setText(temp)           

    def but_5(self):
        if self.clear_flag == True:
            temp = "5"                         
            self.clear_flag = False
        else :
            temp = self.textEdit.toPlainText()    
            temp = temp + "5"                    
        self.textEdit.setText(temp)          

    def but_6(self):
        if self.clear_flag == True:
            temp = "6"                          
            self.clear_flag = False
        else :
            temp = self.textEdit.toPlainText()    
            temp = temp + "6"                     
        self.textEdit.setText(temp)           

    def but_7(self):
        if self.clear_flag == True:
            temp = "7"                          
            self.clear_flag = False
        else :
            temp = self.textEdit.toPlainText()   
            temp = temp + "7"                    
        self.textEdit.setText(temp)           

    def but_8(self):
        if self.clear_flag == True:
            temp = "8"                          
            self.clear_flag = False
        else :
            temp = self.textEdit.toPlainText()    
            temp = temp + "8"                     
        self.textEdit.setText(temp)          

    def but_9(self):
        if self.clear_flag == True:
            temp = "9"                         
            self.clear_flag = False
        else :
            temp = self.textEdit.toPlainText()   
            temp = temp + "9"                    
        self.textEdit.setText(temp)          

    def but_add(self):
        temp = self.textEdit.toPlainText()    # 获取原先的输入框值
        if temp.find("+") == -1:              # 如果原先的输入中没有 +
            temp = temp + "+"                 # 将原先的值在末尾添加 +
            self.textEdit.setText(temp)

    def but_sub(self):
        temp = self.textEdit.toPlainText()    
        if temp.find("-") == -1:              
            temp = temp + "-"                
            self.textEdit.setText(temp)

    def but_mu(self):
        temp = self.textEdit.toPlainText()    
        if temp.find("*") == -1:              
            temp = temp + "*"                
            self.textEdit.setText(temp)

    def but_div(self):
        temp = self.textEdit.toPlainText()    
        if temp.find("/") == -1:              
            temp = temp + "/"                 
            self.textEdit.setText(temp)

    def but_equ(self):
        temp = self.textEdit.toPlainText()    # 获取原先的输入框值
        result = str(eval(temp))             # 取出输入的字符串，用eval函数计算结果
        self.textEdit.setText(result)


app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())


