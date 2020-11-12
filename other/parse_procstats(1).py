# coding:utf-8
import os, csv
app_list = [] #app list
mem_dict = {} #pidname:{top:1,Imp:0}进程各个状态信息
def get_applist():
    global app_list
    with open('/Users/ruitao.su/Desktop/applist.txt',encoding='utf-8', mode='r') as f:
        lines = f.readlines()
        for line in lines:
            app_list.append(line.strip())
        print(app_list)

def _parse_procstats():
    global filename
    t = 0
    mem_dict = {}
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for app in app_list:
            start_flag = False
            for line in lines:
                if start_flag and "*" not in line and t > 0:
                    mem_dict[pidname].append(line.strip())
                    t += 1
                if start_flag and "*" in line:
                    start_flag = False
                if app in line:
                    start_flag = True
                    pidname = line.split()[1].strip()
                    print(f"进程号：{pidname}")
                    mem_dict[pidname] = []
                    mem_dict[pidname].append(line.strip())
    return mem_dict

def get_mem():
    global mem_dict
    pidname_dict = _parse_procstats()
    print(f"pid序列：{pidname_dict}")
    for key in pidname_dict:
        item = {'Persistent': 0, 'Top': 0, 'Imp Fg': 0, 'Imp Bg': 0, 'Service': 0, 'Service Rs': 0, 'Receiver': 0,
                'Heavy': 0, 'Home': 0, 'Last Act': 0, 'Cached': 0}
        #top	impfg	impbg	backup	service	service-rs	receiver	heavy	home	lastact	Cache
        mem_dict[key] = item
        value = pidname_dict[key]
        for line in value:
            if "TOTAL" in line:
                continue
            else:
                mem_type = line.split(":")[0].replace('(', '').replace(')', '')
                # print(f"mem_type:{mem_type}")
                if 'MB' in line:
                    v = line.split(':')[-1].split()[1].split('/')[0].split('-')[-1].replace('MB', '')
                    if mem_type in item.keys():
                        mem_dict[key][mem_type] = float(v)
                    else:
                        print(mem_type, "new memory type")
                else:
                    mem_dict[key][mem_type] = 0

def write_report():
    global mem_dict
    headers = ['pid_name', 'Persistent', 'Top', 'Imp Fg', 'Imp Bg', 'Service', 'Service Rs', 'Receiver', 'Heavy',
               'Home', 'Last Act', 'Cached']
    with open('procstats.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for key in mem_dict:
            print(key)
            print(mem_dict[key])
            dict1 = {'pid_name': key}
            dict1.update(mem_dict[key])
            writer.writerow(dict1)

filename = str(input("请输入文件名："))
get_applist()
get_mem()
write_report()