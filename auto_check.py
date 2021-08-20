<<<<<<< HEAD
# coding=utf-8
# author:whale3070
# time:2021-07-30
# version:v3
import pandas as pd
from lxml import etree
import xlwt
import re
# url和header此处省略
txt = open('cnvd.html','r',encoding='UTF-8')
text = str(txt.readlines())

#req = requests.get(url=url, headers=header)
#text = req.text
# 解析html
res_elements = etree.HTML(text)
# 指定属性的获取方式
# table = res_elements.xpath('//table[@id="table"]')
# 不指定属性获取table
table = res_elements.xpath('//table')
# 将第一个表格转成string格式
table = etree.tostring(table[0], encoding='utf-8').decode()
# pandas读取table
df = pd.read_html(table, encoding='utf-8', header=0)[0]
# 转换成列表嵌套字典的格式
results = list(df.T.to_dict().values())
# 最后能够看到一个包含很多字典的list
#print(results)

id_list = []
vul_title_list = []
time_list = []
status_list = []
for i in results:
	#1
	
	myre = 'CNVD-C-\d+-\d+|CNVD-\d+-\d+'
	id = i['编号']
	find_id = re.findall(myre,id)
	#print(find_id)
	id_list.append(find_id[0])
	
	#2
	
	vul_title = i['漏洞标题']
	v_list = vul_title.split(',')
	v1 = v_list[2].replace("\\t","")
	v2 = v1.replace("\\n\'","")
	v3 = v2.replace("\'","")
	#print(v_list)
	vul_title_list.append(v3.strip())

	#3
	
	time = i['上报时间']
	#print(time)
	time_list.append(time)
	
	#4
	myre_status = '未归档|已作废|驳回|已归档'
	status = i['状态']
	findstatus = re.findall(myre_status,status)
	#print(findstatus)

	status_list.append(findstatus[0])

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

worksheet.write(0, 0,"时间") #第一列
worksheet.write(0, 1,"姓名") #第二列
worksheet.write(0, 2,'事件型') #第三列
worksheet.write(0, 3,'通用型') 
worksheet.write(0, 4,'漏洞编号') 
worksheet.write(0, 5,'是否通过') 
worksheet.write(0, 6,'提交时间') 

#print(vul_title_list)
vul_title_index_list = [] #漏洞标题在列表中的位置
find_each_c_list = []     #我提交的漏洞标题
with open("company.txt","r", encoding='UTF-8') as f:
    for eachCompany in f.readlines():
        eachC = eachCompany.strip()
        for vul_title in vul_title_list:
            #print(vul_title)
            find_each_c = re.findall(eachC,vul_title)
            #print(find_each_c)
            if len(find_each_c)>0:
                #print(find_each_c)
                find_each_c_list.append(find_each_c[0])
                vul_title_index = vul_title_list.index(vul_title) #漏洞标题在列表中的编号
                vul_title_index_list.append(vul_title_index)
num=1
for i in vul_title_index_list: #漏洞标题
	worksheet.write(num, 2,vul_title_list[i]) #第三列
	#print(num)
	num+=1

num_id=1
#for i in id_list :
for j in vul_title_index_list:
    #print(id_list[j])
	worksheet.write(num_id, 4,id_list[j]) #第5列
	#print(num_id)
	num_id+=1

num_status=1
#for i in status_list :
for h in vul_title_index_list:
	worksheet.write(num_status, 5,status_list[h]) #第6列
	#print(num_status)
	num_status+=1
   
num_time=1
#for i in time_list :
for k in vul_title_index_list:
	worksheet.write(num_time, 6,time_list[k]) #第7列
	#print(num_time)
	num_time+=1

worksheet.col(2).width = 6666
worksheet.col(4).width = 5555
worksheet.col(6).width = 3333
workbook.save('20210x山石网科安服东区CNVD汇总表.xls')
txt.close()
=======
# coding=utf-8
# author:whale3070,muyu
# time:2021-08-20
# version:v3
import pandas as pd
from lxml import etree
import xlwt
import re
import time
import locale

locale.setlocale(locale.LC_CTYPE, 'Chinese')
locale.setlocale(locale.LC_ALL,'en')

def auto_check():
    # url和header此处省略
    txt = open('cnvd.html', 'r', encoding='UTF-8')
    text = str(txt.readlines())

    # req = requests.get(url=url, headers=header)
    # text = req.text
    # 解析html
    res_elements = etree.HTML(text)
    # 指定属性的获取方式
    # table = res_elements.xpath('//table[@id="table"]')
    # 不指定属性获取table
    table = res_elements.xpath('//table')
    # 将第一个表格转成string格式
    table = etree.tostring(table[0], encoding='utf-8').decode()
    # pandas读取table
    df = pd.read_html(table, encoding='utf-8', header=0)[0]
    # 转换成列表嵌套字典的格式
    results = list(df.T.to_dict().values())
    # 最后能够看到一个包含很多字典的list
    # print(results)

    id_list = []
    vul_title_list = []
    time_list = []
    status_list = []
    for i in results:
        # 1

        myre = 'CNVD-C-\d+-\d+|CNVD-\d+-\d+'
        id = i['编号']
        find_id = re.findall(myre, id)
        #print(find_id)
        id_list.append(find_id[0])

        # 2

        vul_title = i['漏洞标题']
        v_list = vul_title.split(',')
        v1 = v_list[2].replace("\\t", "")
        v2 = v1.replace("\\n\'", "")
        v3 = v2.replace("\'", "")
        # print(v_list)
        vul_title_list.append(v3.strip())

        # 3

        times = i['上报时间']
        # print(time)
        time_list.append(times)

        # 4
        myre_status = '未归档|已作废|驳回|已归档'
        status = i['状态']
        findstatus = re.findall(myre_status, status)


        status_list.append(findstatus[0])
    # print(vul_title_list)
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('My Sheet')

    worksheet.write(0, 0, "时间")  # 第一列
    worksheet.write(0, 1, "姓名")  # 第二列
    worksheet.write(0, 2, '事件型')  # 第三列
    worksheet.write(0, 3, '通用型')
    worksheet.write(0, 4, '漏洞编号')
    worksheet.write(0, 5, '是否通过')
    worksheet.write(0, 6, '提交时间')

    # print(vul_title_list)
    vul_title_index_list = []  # 漏洞标题在列表中的位置
    find_each_c_list = []  # 我提交的漏洞标题

    with open("company.txt", "r", encoding='UTF-8') as f:
        for eachCompany in f.readlines():
            eachC = eachCompany.strip()
            # print(eachC)

            for vul_title in vul_title_list:
                res = eachC+".*"

                find_each_c = re.findall(res, vul_title)


                if len(find_each_c) > 0:
                    # print(find_each_c)
                    find_each_c_list.append(find_each_c[0])
                    vul_title_index = vul_title_list.index(find_each_c[0])  # 漏洞标题在列表中的编号
                    # print(vul_title_index)
                    vul_title_index_list.append(vul_title_index)
    num = 1
    for i in find_each_c_list:  # 漏洞标题
        worksheet.write(num, 2, i)  # 第三列
        # print(num)
        num += 1

    num_id = 1
    # for i in id_list :
    for j in vul_title_index_list:
        # print(id_list[j])
        worksheet.write(num_id, 4, id_list[j])  # 第5列
        # print(num_id)
        num_id += 1

    num_status = 1
    # for i in status_list :
    for h in vul_title_index_list:
        worksheet.write(num_status, 5, status_list[h])  # 第6列
        # print(num_status)
        num_status += 1

    num_time = 1
    # for i in time_list :
    for k in vul_title_index_list:
        worksheet.write(num_time, 6, time_list[k])  # 第7列
        # print(num_time)
        num_time += 1

    worksheet.col(2).width = 6666
    worksheet.col(4).width = 5555
    worksheet.col(6).width = 3333
    save_time = time.strftime("%Y%m", time.localtime())
    workbook.save(save_time+'山石网科安服东区CNVD汇总表.xls')
    txt.close()
if __name__ == '__main__':
    auto_check()
>>>>>>> 8ebfeca (V3.0)
