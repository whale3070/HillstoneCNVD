<<<<<<< HEAD
import auto_docx
import auto_check

if __name__ == '__main__':
    print("欢迎来到山石网科CNVD报告生成以及验证系统")
    print("生成报告请按1，验证漏洞信息请按2")
    Input_Num = int(input())
    if Input_Num == 1:

        auto_docx.auto_docx()
    elif Input_Num ==2:
        auto_check.auto_check()


=======
import auto_docx
import auto_check




if __name__ == '__main__':
    print("欢迎来到山石网科CNVD报告生成以及验证系统")
    print("生成报告请按1，验证漏洞信息请按2")
    Input_Num = int(input())
    if Input_Num == 1:

        auto_docx.auto_docx()
    elif Input_Num ==2:
        auto_check.auto_check()


>>>>>>> 8ebfeca (V3.0)
