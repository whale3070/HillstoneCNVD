#author:whale3070
#version:v1
#time:2021-07-21
import configparser
import os
import re
from docx import Document
from docx.shared import Inches


def Use_template(Select_Num):
    #获取当前目录下的所有文件
    path = os.listdir(os.getcwd())
    company_list = company()
    # print(company_list)
    '''
    ['重庆赣江实业有限公司', '新希望六和股份有限公司', '白馬窯業']
    '''
    # 漏洞地址名称
    vul_address_list = vul_address()
    # 使用默认模板时
    if Select_Num == 1:
        # 读取当前目录下文件

        if "CNVD.ini" in path:
            # 读取配置文件
            config = configparser.ConfigParser()
            config.read("CNVD.ini", encoding="utf-8")
            # 获取所有的选项
            secs = config.sections()
            # print(secs)
            i = 0
            # 遍历所有的模板名称并可选择
            for section in secs:
                print("编号" + str(i) + ":" + section)
                i += 1
            # 锁定模板文件
            sec_num = int(input("请输入对应模板文件的编号:"))
            #漏洞名称
            title_texts = config.get(secs[sec_num], "title_texts")
            #漏洞发现
            Vuln_discovery = config.get(secs[sec_num], "Vuln_discovery")
            #漏洞地址
            Vuln_address = config.get(secs[sec_num], "Vuln_address")
            #漏洞验证
            Vuln_check = config.get(secs[sec_num], "Vuln_check")
            new_docx(company_list, vul_address_list, Vuln_discovery, Vuln_address, Vuln_check, title_texts)
        else:
            print("读取配置文件失败，请检查CNVD.ini文件是否存在，是否生成新的自定义配置选项,使用请按1，退出请按0:")
            flag = int(input())
            if flag:
                Create_New_temp()
            else:
                exit(0)
    # 创建新的模板文件
    else:

        Create_New_temp()

def Create_New_temp():
    # 自定义信息，并询问是否需要生成到模板中
    title_texts = input("请输入漏洞名称:")
    Vuln_discovery = input("请输入漏洞发现内容:")
    Vuln_address = input("请输入漏洞地址:")
    Vuln_check = input("请输入漏洞证明:")

    template_name = input("请输入配置名称(请勿输入已存在配置名称):")
    conf = configparser.ConfigParser()
    conf.add_section(template_name)
    conf.set(template_name, "title_texts", title_texts)
    conf.set(template_name, "Vuln_discovery", Vuln_discovery)
    conf.set(template_name, "Vuln_address", Vuln_address)
    conf.set(template_name, "Vuln_check", Vuln_check)

    conf.write(open("CNVD.ini", 'a', encoding="utf-8"))
    print("是否生成docx文档,生成请输入1，退出请按0")
    num = int(input())
    if num ==1:
        Use_template(1)
    else:
        exit(0)

# 获取公司名称
def company():
    list = []
    company_file = open("company.txt", "r", encoding='utf-8')
    for eachCompany in company_file.readlines():
        list.append(eachCompany.strip("\n"))
    company_file.close()
    return list
 #获取漏洞地址
def vul_address():
    list = []
    vul_add = open("pwned.txt", "r", encoding='utf-8')
    for each in vul_add.readlines():
        mysplit = each.strip("\n").split(",")
        #print(mysplit)
        list.append(mysplit)
    vul_add.close()
    return list

# def get_file_path_by_name(file_dir):
#     '''
#     获取指定路径下所有文件的绝对路径
#     :param file_dir:
#     :return:
#     '''
#     L = []
#     for root,dirs,files in os.walk(file_dir):  # 获取所有文件
#         for file in files:  # 遍历所有文件名
#             if os.path.splitext(file)[1] == '.bmp':
#                 L.append(os.path.join(root, file))  # 拼接处绝对路径并放入列表
#     print('总文件数目：', len(L))
#     return L

    
def mk_docx(num,company_name,vul_address_list, Vuln_discovery, Vuln_address, Vuln_check, title_texts):
    #print(num)
    picnum=0
    for vul_address_name in vul_address_list:
        #trueIp =re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',vul_address_name)
        # trueIp = re.findall( r'[0-9]+(?:\.[0-9]+){3}',vul_address_name)
        # print(trueIp)
        print(vul_address_name)
        '''
        pic_path = ''
        for i in img_path_list:
            #print(i)
            img_path = re.findall(trueIp[0],i)
            if len(img_path)>0:
                #print(i)
                
                pic_path = i
        print(pic_path)
        '''
        document = Document()
        document.add_heading(company_name+'存在'+title_texts, 0)
        #document.add_picture(pic_path,width=Inches(6.0) )

        document.add_heading('漏洞发现', level=1)
        p = document.add_paragraph(Vuln_discovery)
        document.add_heading('漏洞地址', level=1)
        Vuln_address = vul_address_name+Vuln_address
        p1 = document.add_paragraph(Vuln_address)

        document.add_heading('漏洞证明', level=1)
        p2 = document.add_paragraph(Vuln_check)
        documentName = company_name+'.docx'
        
        
        #print('title: '+company_name.strip('\n')+'存在蓝凌OA custom.jsp 任意文件读取漏洞')
        picnum+=1
        print(str(num)+'-'+str(picnum)+": "+'vul_address: '+vul_address_name.strip('\n'))
        document.save(str(num)+'-'+str(picnum)+documentName)
        
        

        
def new_docx(company_list,vul_address_list, Vuln_discovery, Vuln_address, Vuln_check, title_texts):
    num=0

    for j in range(len(vul_address_list)):
        num+=1
        mk_docx(num,company_list[j],vul_address_list[j], Vuln_discovery, Vuln_address, Vuln_check, title_texts)

def auto_docx():
    #图片读取写入,暂时不写.
    # img_path_list = get_file_path_by_name('C:\\Users\\Local\\Desktop\\new\\images')
    print("欢迎使用CNVD模板生成工具，是否使用系统默认模板文件,使用请按1，否则请按0:")
    Select_Num = int(input())
    # 启动生成模板文件
    Use_template(Select_Num)








    # company_list = company()
    # #print(company_list)
    # '''
    # ['重庆赣江实业有限公司', '新希望六和股份有限公司', '白馬窯業']
    # '''
    # #漏洞地址名称
    # vul_address_list = vul_address()
    # #print(vul_address_list[1])
    # '''
    # ['http://61.163.234.38:8090/sys/ui/extend/varkind/custom.jsp', 'http://119.249.96.46:8090/sys/ui/extend/varkind/custom.jsp', 'http://116.177.226.119:8090/sys/ui/extend/varkind/custom.jsp', 'http://221.193.246.90:8090/sys/ui/extend/varkind/custom.jsp', 'http://117.157.243.34:8090/sys/ui/extend/varkind/custom.jsp', 'http://116.211.78.155:8090/sys/ui/extend/varkind/custom.jsp', 'http://112.90.245.13:8090/sys/ui/extend/varkind/custom.jsp', 'http://117.187.245.56:8090/sys/ui/extend/varkind/custom.jsp', 'http://111.206.10.146:8090/sys/ui/extend/varkind/custom.jsp', 'http://14.205.40.192:8090/sys/ui/extend/varkind/custom.jsp', 'http://111.43.179.221:8090/sys/ui/extend/varkind/custom.jsp', 'http://113.201.107.205:8090/sys/ui/extend/varkind/custom.jsp']
    # '''

if __name__ == '__main__':
    auto_docx()