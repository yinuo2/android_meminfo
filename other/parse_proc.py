#encoding:utf-8
import os, csv
app_list = [] #app list
mem_dict = {} #pidname:{top:1,Imp:0}进程各个状态信息

def get_applist():
    global app_list
    with open('applist.txt',encoding='utf-8', mode='r') as f:
        lines = f.readlines()
        for line in lines:
            app_list.append(line.strip())
        print(app_list)
        print(len(app_list))

def parse_procstats():
    global filename, app_list, mem_dict
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for app in app_list:
            if app == 'system':
                app = 'system_server'
            for line in lines:
                mem_dict[app] = -1
                if app in line:
                    pidname = line.split()[-1].strip()
                    if pidname == app:
                        mem_value = round((float(line.split()[3].replace('K', ''))/1024), 2)
                        mem_dict[pidname] = mem_value
                        print(line.strip())
                        print(pidname, mem_value)
                        break
    return mem_dict

def write_report():
    global mem_dict
    headers = ['pid_name', 'init_mem']
    print(mem_dict)
    with open('proc.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for key in mem_dict:
            writer.writerow({'pid_name':key, 'init_mem':mem_dict[key]})

get_applist()
filename = str(input("请输入文件名："))
parse_procstats()
write_report()